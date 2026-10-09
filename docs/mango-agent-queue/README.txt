Mango SEO Agent: commercial / buy-intent blog queue (64 items, same format as your current queue file)

1) Put these 3 files anywhere on your PC (for example E:\Claude SEO tool\mango-seo-agent-v4.0\).
2) Open a terminal in that folder and run (use the real path of your queue file):
     node merge-queue.js "E:\Claude SEO tool\mango-seo-agent-v4.0\<your-queue-file>.json" new-items.json
   This adds the 64 items to the end of your queue, skips any id that already exists, and saves a backup copy of your queue file first.
   (No Node? Open new-items.json, copy everything inside "items": [ ... ] and paste it at the end of the "items" array in your queue file, adding a comma after your last item.)
3) The new items have status "queued", action "new", pinned true, and score 899 down to 836, so the agent takes them in order after your pinned items. If your agent uses a different word for "waiting to run" than "queued", replace "queued" with it (search and replace in the queue file).
4) The "angle" of each item already contains the rules: live price tokens, no pre-orders, 48 coastal villages, the exact delivery sentence, and the phone numbers. Extra fields suggestedTitle and slug are only hints; the agent can ignore them.
