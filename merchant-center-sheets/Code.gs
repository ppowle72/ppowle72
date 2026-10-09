/**
 * AlphonsoMango.in: free Merchant Center reporting in Google Sheets (Merchant API v1).
 * Replaces the paid Supermetrics connector. Untested draft: run it once and check the
 * field names against https://developers.google.com/merchant/api/reference/rest if a call fails.
 *
 * Sheets created: Products, Issues, Performance, Summary.
 */
var CONFIG = {
  MERCHANT_ID: '719656549',                 // Merchant Center ID (from the Supermetrics account list)
  DEVELOPER_EMAIL: 'ppowle1@gmail.com',     // used once for Merchant API developer registration
  PERFORMANCE_DAYS: 90,
  // Optional: send a daily summary event to your AdPulse collector Worker (POST /e). Leave blank to skip.
  ADPULSE_URL: '',                          // e.g. 'https://adpulse-collector.<your-subdomain>.workers.dev/e'
  ADPULSE_WS: 'alphonsomango'               // workspace tag stored in the events table
};

var API = 'https://merchantapi.googleapis.com';

function onOpen() {
  SpreadsheetApp.getUi().createMenu('Merchant Center')
    .addItem('1. Register (run once)', 'registerOnce')
    .addItem('2. Pull everything now', 'pullAll')
    .addItem('3. Create daily trigger', 'createDailyTrigger')
    .addToUi();
}

function call_(method, path, body) {
  var opts = {
    method: method,
    headers: { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() },
    muteHttpExceptions: true
  };
  if (body) { opts.contentType = 'application/json'; opts.payload = JSON.stringify(body); }
  var res = UrlFetchApp.fetch(API + path, opts);
  var code = res.getResponseCode();
  var text = res.getContentText();
  if (code >= 300) throw new Error(method + ' ' + path + ' -> ' + code + ': ' + text.slice(0, 600));
  return text ? JSON.parse(text) : {};
}

/** One-time: link this script's Google Cloud project to your Merchant Center account. */
function registerOnce() {
  var r = call_('POST', '/accounts/v1/accounts/' + CONFIG.MERCHANT_ID + '/developerRegistration:registerGcp',
                { developerEmail: CONFIG.DEVELOPER_EMAIL });
  Logger.log(JSON.stringify(r));
  SpreadsheetApp.getUi().alert('Registered: ' + JSON.stringify(r).slice(0, 300));
}

function sheet_(name, header) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(name) || ss.insertSheet(name);
  sh.clear();
  sh.getRange(1, 1, 1, header.length).setValues([header]).setFontWeight('bold');
  sh.setFrozenRows(1);
  return sh;
}

function write_(sh, rows) {
  if (!rows.length) return;
  sh.getRange(2, 1, rows.length, rows[0].length).setValues(rows);
}

function listProducts_() {
  var out = [], token = '';
  do {
    var path = '/products/v1/accounts/' + CONFIG.MERCHANT_ID + '/products?pageSize=250' + (token ? '&pageToken=' + encodeURIComponent(token) : '');
    var r = call_('GET', path);
    (r.products || []).forEach(function (p) { out.push(p); });
    token = r.nextPageToken || '';
  } while (token);
  return out;
}

function pullProducts() {
  var products = listProducts_();
  var sh = sheet_('Products', ['offerId', 'title', 'feedLabel', 'language', 'dataSource', 'availability', 'price', 'currency',
                               'brand', 'gtin', 'mpn', 'link', 'approved countries', 'disapproved countries', 'issue count']);
  var issues = sheet_('Issues', ['offerId', 'title', 'code', 'severity', 'attribute', 'description', 'detail', 'resolution', 'countries', 'documentation']);
  var rows = [], irows = [];
  products.forEach(function (p) {
    var a = p.attributes || {};
    var st = p.productStatus || {};
    var approved = [], disapproved = [];
    (st.destinationStatuses || []).forEach(function (d) {
      (d.approvedCountries || []).forEach(function (c) { if (approved.indexOf(c) < 0) approved.push(c); });
      (d.disapprovedCountries || []).forEach(function (c) { if (disapproved.indexOf(c) < 0) disapproved.push(c); });
    });
    var iss = st.itemLevelIssues || [];
    var price = a.price ? (Number(a.price.amountMicros) / 1e6) : '';
    rows.push([p.offerId, a.title || '', p.feedLabel || '', p.contentLanguage || '', p.dataSource || '',
               a.availability || '', price, a.price ? a.price.currencyCode : '', a.brand || '',
               (a.gtins || []).join(','), a.mpn || '', a.link || '', approved.join(','), disapproved.join(','), iss.length]);
    iss.forEach(function (i) {
      irows.push([p.offerId, a.title || '', i.code || '', i.severity || '', i.attribute || '', i.description || '', i.detail || '',
                  i.resolution || '', (i.applicableCountries || []).join(','), i.documentation || '']);
    });
  });
  write_(sh, rows);
  write_(issues, irows);
  return { products: rows.length, issues: irows.length,
           disapproved: rows.filter(function (r) { return r[13]; }).length };
}

function pullPerformance() {
  var end = new Date(), start = new Date(end.getTime() - CONFIG.PERFORMANCE_DAYS * 86400000);
  function d(x) { return Utilities.formatDate(x, 'Asia/Kolkata', 'yyyy-MM-dd'); }
  var query = "SELECT date, offer_id, title, clicks, impressions, click_through_rate " +
              "FROM product_performance_view WHERE date BETWEEN '" + d(start) + "' AND '" + d(end) + "' ORDER BY clicks DESC";
  var rows = [], token = '';
  do {
    var body = { query: query, pageSize: 1000 };
    if (token) body.pageToken = token;
    var r = call_('POST', '/reports/v1/accounts/' + CONFIG.MERCHANT_ID + '/reports:search', body);
    (r.results || []).forEach(function (x) {
      var v = x.productPerformanceView || {};
      var dt = v.date ? (v.date.year + '-' + v.date.month + '-' + v.date.day) : '';
      rows.push([dt, v.offerId || '', v.title || '', Number(v.clicks || 0), Number(v.impressions || 0), Number(v.clickThroughRate || 0)]);
    });
    token = r.nextPageToken || '';
  } while (token);
  var sh = sheet_('Performance', ['date', 'offerId', 'title', 'clicks', 'impressions', 'ctr']);
  write_(sh, rows);
  return rows.length;
}

function pullAll() {
  var s = pullProducts();
  var perfRows = 0;
  try { perfRows = pullPerformance(); } catch (e) { Logger.log('Performance report failed: ' + e); }
  var sum = sheet_('Summary', ['metric', 'value']);
  write_(sum, [['updated', new Date()], ['products', s.products], ['products with disapproved countries', s.disapproved],
               ['item-level issues', s.issues], ['performance rows', perfRows]]);
  if (CONFIG.ADPULSE_URL) {
    UrlFetchApp.fetch(CONFIG.ADPULSE_URL, {
      method: 'post', contentType: 'application/json', muteHttpExceptions: true,
      payload: JSON.stringify({ ws: CONFIG.ADPULSE_WS, events: [{
        event: 'merchant_center_snapshot', url: 'merchant-center',
        props: { products: s.products, disapproved: s.disapproved, issues: s.issues, performance_rows: perfRows }
      }] })
    });
  }
}

function createDailyTrigger() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'pullAll') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('pullAll').timeBased().everyDays(1).atHour(7).create();
}
