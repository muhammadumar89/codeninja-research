"""The Contact page: one short form for anyone who wants to talk to CodeNinja (Umar, 14 Oct 2026).
Praxis signup stays the door for engineers who want to design; this page is the door for everyone else.
The form posts to brand.CONTACT_API, which emails hello@codeninjaconsulting.com with Reply-To set to the sender.
    python tools/contact_page.py
"""
import html, json, datetime
from pathlib import Path
import brand
ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)

CSS = """
.contact{max-width:var(--max);margin:0 auto;padding:168px var(--gutter) 120px;display:grid;grid-template-columns:5fr 6fr;gap:72px;align-items:start}
.contact h1{font-weight:300;font-size:clamp(44px,6vw,88px);line-height:1;letter-spacing:-.035em;margin:.2em 0 .35em}
.contact .lede{font-family:var(--serif);font-weight:300;font-size:clamp(20px,2vw,26px);line-height:1.4;color:var(--on-dark);margin:0 0 40px;max-width:30ch}
.contact .aside{border-top:1px solid var(--rule-d);padding-top:20px;font-size:15px;line-height:1.6;color:var(--muted-d);max-width:40ch}
.contact .aside a{color:var(--on-dark)}
@media (max-width:860px){.contact{grid-template-columns:1fr;gap:40px;padding:120px var(--gutter) 80px}}
"""


def form():
    return """<form class="access" id="contact-form">
<label>Name<input name="fullname" required autocomplete="name"></label>
<label>Work email<input name="email" type="email" required autocomplete="email"></label>
<label>Company<input name="org" required autocomplete="organization"></label>
<label>Your role<input name="role" autocomplete="organization-title" placeholder="For example: CIO, VP operations"></label>
<label class="full">What would you like to talk about?<textarea name="message" required placeholder="One operation and what you want from it. For example: years of maintenance and sensor data across three plants, and we would rather not fine tune a model on it."></textarea></label>
<input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<p class="status" role="status" aria-live="polite"></p>
<button type="submit" data-label="Send">Send</button>
<p class="note">Goes straight to the CodeNinja team. Nothing is published, and we only use your details to reply.</p>
</form>
""" + brand.post_script("contact-form", "{name:f.fullname.value,email:f.email.value,company:f.org.value,role:f.role.value,message:f.message.value}")


def main():
    desc = "Talk to CodeNinja about physical AI, industrial AI and knowledge work: one short form, read by a person, answered by email."
    ld = {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact CodeNinja Atoms", "url": f"{BASE}/contact/", "description": desc,
          "about": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms", "url": f"{BASE}/"}}
    out = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Contact CodeNinja Atoms</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/contact/">
<meta property="og:type" content="website"><meta property="og:title" content="Contact CodeNinja Atoms"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/contact/">
<meta property="og:image" content="{BASE}/assets/video/port-night.jpg">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}</style></head>
<body>{brand.header(BASE + "/", brand.nav(BASE + "/"))}
<main><div class="contact">
<div><p class="eyebrow">Contact</p><h1>Talk to us</h1>
<p class="lede">Tell us about one operation and what you want from it. A person on the CodeNinja team reads every request and replies by email.</p>
<p class="aside" style="border-top:0;padding-top:0;margin-bottom:24px">Sitting on years of operational data and would rather not fine tune a model on it? That is exactly the conversation we want: your expertise as a living system of context, inside your own boundary.</p>
<p class="aside">Engineers who want to design on Praxis can <a href="{brand.SIGNUP}">unlock free access</a> directly.</p></div>
<div>{form()}</div>
</div></main>
<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}{brand.footer_links(BASE + "/")}<span>CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a> · Updated {datetime.date.today().isoformat()}</span></div></footer>
{brand.SCRIPT}</body></html>"""
    (ROOT / "contact").mkdir(exist_ok=True)
    (ROOT / "contact" / "index.html").write_text(out, encoding="utf-8")
    print("contact/index.html", len(out))


if __name__ == "__main__":
    main()
