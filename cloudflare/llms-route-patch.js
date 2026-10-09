// Patch for the existing Worker "am-agent-readiness" (v11).
// Paste this block in the router, directly BEFORE the line:  switch (path) {
// It serves /llms.txt and /llms-full.txt as text/plain, using the text printed by the
// Shopify templates page.llms.liquid (/pages/llms) and page.llms-full.liquid (/pages/llms-full).

      // ---- llms.txt / llms-full.txt: text/plain at the root, no redirect ----
      if (path === "/llms.txt" || path === "/llms-full.txt") {
        const target = path === "/llms.txt" ? "/pages/llms" : "/pages/llms-full";
        const r = await fetch(APEX + target, {
          headers: { "user-agent": "am-agent-readiness-worker" },
          cf: { cacheTtl: 300, cacheEverything: true },
        });
        if (!r.ok) return fetch(request);                  // fail open: let Shopify handle it
        const text = await r.text();
        if (!text.trim().startsWith("#")) return fetch(request); // only serve if it looks like our markdown
        return new Response(request.method === "HEAD" ? null : text.trim() + "\n", {
          headers: {
            "content-type": "text/plain; charset=utf-8",
            "cache-control": "public, max-age=300",
            "x-served-by": "am-agent-readiness-worker",
          },
        });
      }
