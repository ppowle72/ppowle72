// Usage:  node merge-queue.js "<path to your current blog queue .json>" new-items.json
// Appends the new items (skips ids that already exist), keeps a backup copy of your file next to it.
const fs = require('fs');
const [,, queuePath, newPath] = process.argv;
if (!queuePath || !newPath) { console.log('Usage: node merge-queue.js <current-queue.json> new-items.json'); process.exit(1); }
const q = JSON.parse(fs.readFileSync(queuePath, 'utf8'));
const n = JSON.parse(fs.readFileSync(newPath, 'utf8'));
fs.copyFileSync(queuePath, queuePath + '.backup-' + Date.now());
const have = new Set(q.items.map(i => i.id));
let added = 0;
for (const it of n.items) { if (!have.has(it.id)) { q.items.push(it); added++; } }
q.builtAt = new Date().toISOString();
fs.writeFileSync(queuePath, JSON.stringify(q, null, 1));
console.log('Added ' + added + ' items, total now ' + q.items.length + '. Backup saved next to the queue file.');
