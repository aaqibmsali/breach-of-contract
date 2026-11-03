"""Build the deployable site into _site/.

Fills the double-underscore placeholders in index.html from environment
variables, so the real names and phone number live only in the repo's
GitHub Actions secrets, never in the repository itself.

    HER_NAME         required
    MY_NAME          required
    WHATSAPP_NUMBER  optional, international format (e.g. +91-98765-43210);
                     if empty, the WhatsApp button opens the contact picker
    SITE_URL         optional, set by the deploy workflow (used for link previews)

Local preview:  HER_NAME=... MY_NAME=... python3 build.py   ->  open _site/index.html
"""
import html
import json
import os
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "_site"


def fail(msg):
    print(f"::error::{msg}", file=sys.stderr)
    sys.exit(1)


her = os.environ.get("HER_NAME", "").strip()
me = os.environ.get("MY_NAME", "").strip()
number = re.sub(r"\D", "", os.environ.get("WHATSAPP_NUMBER", ""))
site_url = os.environ.get("SITE_URL", "").strip().rstrip("/")

missing = [k for k, v in (("HER_NAME", her), ("MY_NAME", me)) if not v]
if missing:
    fail("Missing repository secret(s): " + ", ".join(missing)
         + ". Add them under Settings > Secrets and variables > Actions.")
if number and not 8 <= len(number) <= 15:
    fail("WHATSAPP_NUMBER should be a full international number, e.g. +91-98765-43210.")

page = (ROOT / "index.html").read_text(encoding="utf-8")
values = {
    "__HER_NAME__": her,
    "__MY_NAME__": me,
    "__WHATSAPP_NUMBER__": number,
    "__SITE_URL__": site_url,
}
for placeholder, value in values.items():
    # Inside <script>: replace the quoted string with a safe JS string literal.
    js_literal = json.dumps(value, ensure_ascii=False).replace("<", "\\u003c")
    page = page.replace(f'"{placeholder}"', js_literal)
    # Everywhere else (HTML text and attributes): HTML-escape.
    page = page.replace(placeholder, html.escape(value, quote=True))

leftover = sorted(set(re.findall(r"__[A-Z][A-Z_]*__", page)))
if leftover:
    fail("Unfilled placeholder(s) in index.html: " + ", ".join(leftover))

shutil.rmtree(OUT, ignore_errors=True)
OUT.mkdir()
(OUT / "index.html").write_text(page, encoding="utf-8")
shutil.copy2(ROOT / "preview.jpg", OUT / "preview.jpg")
print("Built _site/ " + ("with" if number else "without") + " a WhatsApp number.")
