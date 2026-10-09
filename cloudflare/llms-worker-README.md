# Serve /llms.txt and /llms-full.txt as text/plain (Cloudflare Worker)

Shopify cannot serve a file at the site root. Your existing Worker `am-agent-readiness` already serves the other agent files (`/.well-known/*`, `/auth.md`, `/sitemap_policies.xml`), so add two paths to it instead of creating a new Worker. It was not deployed from here.

## Order matters
1. Publish the "HOME SEO v1" theme first. The Worker reads `/pages/llms` and `/pages/llms-full`, which print the rewritten text only after the theme is live. Before that they still print the old Proveda text.
2. Then add the patch and routes below.

## Steps (Cloudflare dashboard)
1. Workers & Pages, open `am-agent-readiness`, Edit code.
2. Paste the block from `llms-route-patch.js` directly above `switch (path) {` in the router. Save and Deploy.
3. Open the Worker's Settings, Triggers (Routes) and add:
   - `alphonsomango.in/llms.txt`
   - `www.alphonsomango.in/llms.txt`
   - `alphonsomango.in/llms-full.txt`
   - `www.alphonsomango.in/llms-full.txt`
   (If you deploy with your `deploy.mjs`, add the same four routes to its route list.)
4. Test (Windows PowerShell):
   ```powershell
   Invoke-WebRequest https://alphonsomango.in/llms.txt -UseBasicParsing | Select-Object StatusCode, @{n='Type';e={$_.Headers['Content-Type']}}, @{n='By';e={$_.Headers['x-served-by']}}
   (Invoke-WebRequest https://alphonsomango.in/llms-full.txt -UseBasicParsing).Content.Substring(0,200)
   ```
   Expect 200, `text/plain; charset=utf-8`, `am-agent-readiness-worker`, and a body starting with `# AlphonsoMango.in`.
5. After it works, delete the two Shopify redirects `/llms.txt` and `/llms-full.txt` (Online Store, Navigation, URL Redirects). They point to pages that do not exist.

## Safety
- If the page fetch fails or the text does not start with `#`, the Worker passes the request to Shopify unchanged.
- Cache lifetime is 5 minutes, matching the Worker's other agent files.
- To roll back: remove the four routes (the rest of the Worker is unchanged).
