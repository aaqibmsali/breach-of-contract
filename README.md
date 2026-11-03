# breach-of-contract

A mobile-first site for asking someone out, under the Totally Non‑Binding, Completely Unsigned No‑Contact Agreement:
if the sender breaks no contact, he donates ₹2,000 of clothes to an orphanage. If she breaks it, she owes ₹5,000
("premium party, premium penalty"). The sender broke it, so the sender pays.

**No names or phone numbers are stored in this repo.** `index.html` holds placeholders (`__HER_NAME__`, `__MY_NAME__`,
`__WHATSAPP_NUMBER__`). On every push to `main`, a GitHub Action (`.github/workflows/deploy.yml`) runs `build.py`, which fills them in
from repository **secrets** and publishes the result to GitHub Pages.

> The *live page* still contains the names and number, because her browser needs them to show her name and open
> WhatsApp. Anyone with the link can see them with "view source". The repo itself only has placeholders.

## The flow

1. **Identity check**: "Is your name ___?" No → asks once more → "Please identify yourself" → asks them to exit calmly.
   If they then type her name in the box, it calls them out.
2. **Verification** (fake scan) → **Official Notice**: the sender confesses to the breach, with a scoreboard
   (him: 1 breach; her: 0 breaches, ₹5,000 untouched 🏆) → **The plan**: chai (black tea, milk not invited),
   online ribbon‑cutting right after chai, buying clothes, the orphanage donation, a fun activity of her choice,
   and a bonus choco lava cake ("diplomatic immunity").
3. **The question**. Each "No" escalates, and Yes grows while No shrinks every time:
   plain ask → "black tea, zero milk, I've done research" → No button runs away → a reserved lava cake that will go uneaten,
   then *Error 418: I'm a teapot (we're out of milk, on purpose)* → No needs a 2.5s press‑and‑hold.
   After the 5th No it accepts gracefully, with a small "I changed my mind" link.
4. **Yes** → confetti, emoji rain, fanfare and vibration, with the chai cup and a choco lava cake dancing.
   She then **signs the Date Agreement with her finger** (the original contract was famously unsigned), and a
   choco lava cake drops from the sky as the official **seal**. If she skips signing, it signs her name in handwriting for her.
5. **Booking form**:
   - An **availability calendar** offering only *this weekend and the next one*, a rolling window counted from
     the day she opens it. Weekends are free all day (✨), weekdays are nights only (🌙), and taken dates (📚)
     can't be picked. Picking a weekday locks the time to Night. Anything later is an icy 🥶 "too late" day:
     tapping it shows a rotating, wildly dramatic denial ("the kids will have no clothes, and they will not survive").
   - Then the fun activity, a black‑tea chai order (with a "Department of Dairy Regulation" for regular milk),
     dessert (every option is choco lava cake) and notes.
   - Submitting shows a **ticket** with a countdown and a **Send on WhatsApp** button with the message already filled in.

   To change availability, edit `TAKEN`, `WEEKDAY_TIMES`, `WEEKENDS_AHEAD` and the `DENIALS` lines in the
   "Availability calendar" block of `index.html`.

## Setup

These settings aren't in the GitHub mobile app. Use github.com in your phone's browser; if a menu is missing, switch to "Desktop site".

1. **Add secrets:** repo **Settings → Secrets and variables → Actions → New repository secret**

   | Name | Value |
   |---|---|
   | `HER_NAME` | her name, as it should appear on the page |
   | `MY_NAME` | your name |
   | `WHATSAPP_NUMBER` | your number with country code, e.g. `+91-98765-43210` (optional; without it, WhatsApp asks her to pick the chat) |

2. **Name the repo `breach-of-contract`** so the link is `https://<your-username>.github.io/breach-of-contract/`:
   **Settings → General → Repository name**. A Pages link always ends in the repo name, so this is how you choose it.
   The link-preview tags pick up the new address automatically on the next deploy.
3. **Turn on Pages:** **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. **Make the repo public** (Pages on a private repo needs a paid plan): **Settings → General → Danger Zone → Change visibility**.
5. **Deploy:** push to `main`, or **Actions → Deploy to GitHub Pages → Run workflow**.
   If a secret is missing, the run fails with a message saying which one, and nothing half‑filled gets published.
   Changing a secret, or renaming the repo, doesn't redeploy automatically; re-run the workflow.

**Local preview:** `HER_NAME=... MY_NAME=... python3 build.py`, then open `_site/index.html`. `_site/` is git‑ignored.
Opening `index.html` directly shows "Her Name" / "Your Name" stand‑ins.

Test it on your own phone before sending it. WhatsApp caches link previews, so send yourself the link first.
