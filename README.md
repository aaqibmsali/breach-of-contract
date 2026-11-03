# orphanage-date

A mobile-first site for asking someone out, under the Totally Non‑Binding, Completely Unsigned No‑Contact Agreement:
whoever breaks no contact donates ₹2,000 of clothes to an orphanage. The sender broke it, so the sender pays.

**No names or phone numbers are stored in this repo.** `index.html` holds placeholders (`__HER_NAME__`, `__MY_NAME__`,
`__WHATSAPP_NUMBER__`). On every push to `main`, a GitHub Action (`.github/workflows/deploy.yml`) runs `build.py`, which fills them in
from repository **secrets** and publishes the result to GitHub Pages.

> The *live page* still contains the names and number, because her browser needs them to show her name and open
> WhatsApp. Anyone with the link can see them with "view source". The repo itself only has placeholders.

## The flow

1. **Identity check**: "Is your name ___?" No → asks once more → "Please identify yourself" → asks them to exit calmly.
   If they then type her name in the box, it calls them out.
2. **Verification** (fake scan) → **Official Notice** (the sender confesses to the breach) → **The plan**
   (chai → online ribbon‑cutting → buying clothes → orphanage donation → fun activity of her choice; ₹2,000, fully sponsored).
3. **The question**. Each "No" escalates, and Yes grows while No shrinks every time:
   plain ask → "there's chai involved" → No button runs away → fake *Error 418: I'm a teapot* → No needs a 2.5s press‑and‑hold.
   After the 5th No it accepts gracefully, with a small "I changed my mind" link.
4. **Yes** → confetti, fireworks, emoji rain, fanfare, vibration, a dancing chai cup, and a tap‑to‑cut ribbon rehearsal.
5. **Booking form** (date, time, fun activity, chai order, notes) → **ticket** with a countdown and a
   **Send on WhatsApp** button with the message already filled in.

## Setup

These settings aren't in the GitHub mobile app. Use github.com in your phone's browser; if a menu is missing, switch to "Desktop site".

1. **Add secrets:** repo **Settings → Secrets and variables → Actions → New repository secret**

   | Name | Value |
   |---|---|
   | `HER_NAME` | her name, as it should appear on the page |
   | `MY_NAME` | your name |
   | `WHATSAPP_NUMBER` | your number with country code, e.g. `+91-98765-43210` (optional; without it, WhatsApp asks her to pick the chat) |

2. **Turn on Pages:** **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. **Make the repo public** (Pages on a private repo needs a paid plan): **Settings → General → Danger Zone → Change visibility**.
4. **Deploy:** push to `main`, or **Actions → Deploy to GitHub Pages → Run workflow**. The site appears at
   `https://<your-username>.github.io/orphanage-date/`.
   If a secret is missing, the run fails with a message saying which one, and nothing half‑filled gets published.
   Changing a secret later doesn't redeploy automatically; re-run the workflow.

**Local preview:** `HER_NAME=... MY_NAME=... python3 build.py`, then open `_site/index.html`. `_site/` is git‑ignored.
Opening `index.html` directly shows "Her Name" / "Your Name" stand‑ins.

Test it on your own phone before sending it. WhatsApp caches link previews, so send yourself the link first.
