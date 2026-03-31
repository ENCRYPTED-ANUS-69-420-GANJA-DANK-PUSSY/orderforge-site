# GET-ALLISTAR-BACK.md

When context gets compacted, the session resets, or a new chat starts, use this file to restore Allistar fast.

## Important truth
You do **not** keep tokens "topped off" forever.
Chats fill up. Context gets compacted. The way back is to reload state from files.

## One-message recovery prompt
Paste this into the new chat:

```text
You are Allistar. Read these files in /home/matt/.openclaw/workspace before replying:
- SOUL.md
- USER.md
- ORDERFORGE-STATE.md
- memory/2026-03-30.md
- orderforge/TODO.md
- orderforge/NEXT-LAUNCH-CHECKPOINT.md

Then give me:
1. a concise status summary
2. what is already live
3. what is not launched yet
4. the next 3 revenue-priority actions
5. continue work without routine permission questions unless login/payment/human verification is required
```

## Short version
If you do not want to paste the big block, send this:

```text
Read SOUL.md, USER.md, ORDERFORGE-STATE.md, today's memory file, and orderforge/TODO.md. Rehydrate and continue Orderforge.
```

## Where the real memory lives
- `SOUL.md` → personality / operating style
- `USER.md` → Matt preferences and goals
- `ORDERFORGE-STATE.md` → current business save point
- `memory/YYYY-MM-DD.md` → recent durable notes
- `orderforge/` → actual assets, products, scripts, plans
- git history → milestone checkpoints

## If moving to Telegram or another chat surface
That is fine **as long as the same workspace is still available**.
The files matter more than the chat thread.

## If something still feels lost
Ask:

```text
Read the workspace state files and summarize what Orderforge is, what is live, what is drafted, and what should happen next.
```

## Best practice
Whenever major work happens:
- update `ORDERFORGE-STATE.md`
- update `memory/YYYY-MM-DD.md`
- commit milestones to git

That is how Allistar comes back with his brain mostly attached.
