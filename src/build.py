"""Генератор статического сайта Waypoint (RU в корне, DE в /de/).
Запуск из корня репозитория:  python3 src/build.py
Пишет готовые HTML-страницы прямо в репозиторий (index.html, consulting/index.html, de/..., sitemap.xml).
"""
import os, sys, html, json
from datetime import date

sys.path.insert(0, os.path.dirname(__file__))
from content import SITE_URL, CONTACTS, FORMSPREE, POSTS, SERVICES, UI
from legal import LEGAL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["ru", "de"]
PREFIX = {"ru": "/", "de": "/de/"}
SERVICE_ORDER = ["consulting", "marketing", "video-ads"]
PAGES = []  # (path_without_prefix) for sitemap

e = html.escape
CUR = ' aria-current="page"'
CURT = ' aria-current="true"'


def url(lang, path=""):
    return PREFIX[lang] + path


LOGO = '<svg viewBox="0 0 44 24" aria-hidden="true"><circle cx="8" cy="14" r="5" fill="none" stroke="#111" stroke-width="2.4"/><circle cx="36" cy="10" r="5" fill="#e0352b"/><path d="M13 12.5 L31 10.8" stroke="#111" stroke-width="2.4" stroke-linecap="round"/><circle cx="22" cy="11.7" r="2.4" fill="#111"/></svg>'

ICONS = {
    "mail": '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 6 9-6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a1 1 0 01-1 1A16 16 0 014 5a1 1 0 011-1z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-12a7 7 0 0114 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
    "tg": '<svg viewBox="0 0 24 24"><path d="M21 4L3 11l6 2 2 6 3-4 5 4 2-15z"/><path d="M9 13l8-6"/></svg>',
    "wa": '<svg viewBox="0 0 24 24"><path d="M4 20l1.4-4A8 8 0 1112 20a8 8 0 01-4-1z"/></svg>',
}


def head(lang, path, title, desc):
    alt = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE_URL}{url(l, path)}">' for l in LANGS
    ) + f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}{url("ru", path)}">'
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE_URL}{url(lang, path)}">
{alt}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Waypoint">
<meta property="og:locale" content="{UI[lang]['locale']}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE_URL}{url(lang, path)}">
<meta name="theme-color" content="#f3f3f1">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/inter-{'cyrillic' if lang == 'ru' else 'latin'}-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#main">{UI[lang]['skip']}</a>
"""


def header(lang, path):
    u = UI[lang]
    active = path.split("/")[0] + "/" if path else ""
    links = "".join(
        f'<a href="{url(lang, p)}"{CUR if p == active else ""}>{e(label)}</a>'
        for p, label in u["nav"]
    )
    langs = "".join(
        f'<a href="{url(l, path)}" hreflang="{l}" lang="{l}"{CURT if l == lang else ""}>{l.upper()}</a>'
        for l in LANGS
    )
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{url(lang)}" aria-label="Waypoint">{LOGO}<span>Waypoint</span></a>
    <nav class="nav" id="nav" aria-label="Menu">{links}</nav>
    <div style="display:flex;align-items:center;gap:8px">
      <div class="lang" aria-label="Language">{langs}</div>
      <button class="menu-btn" type="button" aria-controls="nav" aria-expanded="false" aria-label="{u['menu']}"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main id="main">
"""


def footer(lang):
    u = UI[lang]
    c = CONTACTS
    navl = "".join(f'<li><a href="{url(lang, p)}">{e(l)}</a></li>' for p, l in u["nav"])
    legal = "".join(f'<li><a href="{url(lang, p)}">{e(l)}</a></li>' for p, l in u["legal"])
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="logo" href="{url(lang)}">{LOGO}<span>Waypoint</span></a>
        <p>{e(u['footer_about'])}<br>{e(u['footer_tag'])}</p>
      </div>
      <div>
        <ul class="footer-contacts">
          <li>{ICONS['mail']}<a href="mailto:{c['email']}">{c['email']}</a></li>
          <li>{ICONS['phone']}<a href="tel:{c['phone_href']}">{c['phone']}</a></li>
          <li>{ICONS['pin']}<span>{e(c['city'][lang])}</span></li>
          <li>{ICONS['tg']}<a href="{c['telegram']}" target="_blank" rel="noopener">Telegram</a></li>
          <li>{ICONS['wa']}<a href="{c['whatsapp']}" target="_blank" rel="noopener">WhatsApp</a></li>
        </ul>
      </div>
      <div><ul class="footer-links">{navl}</ul></div>
      <div><ul>{legal}</ul></div>
    </div>
    <div class="copy"><span>© {date.today().year} Waypoint. {e(u['rights'])}</span><a href="https://clickbari.it" target="_blank" rel="noopener">Website by ClickBari</a></div>
  </div>
</footer>
<script>
(function(){{var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)}})}})();
</script>
</body>
</html>
"""


def card(lang, p, link=True):
    u = UI[lang]
    t = p[lang]
    foot = u["read_case"] if p["kind"] == "case" else f'{p["min"]} {u["min_read"]}'
    desc = f'<p>{e(t["d"])}</p>' if t.get("d") else ""
    href = url(lang, f'blog/{p["cat"]}/') + f'#{p["id"]}'
    return f"""<a class="card {p['kind']}" id="{p['id']}" href="{href}">
  <span class="kind">{u['kind'][p['kind']]}</span>
  <h3>{e(t['t'])}</h3>{desc}
  <span class="foot"><i></i>{e(foot)}</span>
</a>"""


def posts(cat=None):
    return [p for p in POSTS if cat is None or p["cat"] == cat]


def write(lang, path, body):
    rel = (url(lang, path)).lstrip("/")
    out = os.path.join(ROOT, rel, "index.html") if rel else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(body)
    if lang == "ru":
        PAGES.append(path)


# ---------- pages ----------

def page_home(lang):
    u = UI[lang]
    hero_post = POSTS[0]
    body = head(lang, "", u["home_title"], u["home_desc"]) + header(lang, "")
    tags = "".join(f"<li>{e(t)}</li>" for t in u["tags"])
    body += f"""<section class="row hero split-grid">
  <div class="wrap">
    <div class="row-copy">
      <p class="eyebrow">{u['hero_eyebrow']}</p>
      <h1>{u['hero_h']}</h1>
      <p class="lead">{e(u['hero_lead'])}</p>
      <a class="arrow-link" href="#consulting"><i></i>{e(u['hero_cta'])}</a>
    </div>
    <div class="row-side">
      <div class="hero-side">
        <div class="hero-art">
          <img src="/assets/img/route.svg" alt="" width="440" height="440">
          {card(lang, hero_post)}
        </div>
        <ul class="tags">{tags}</ul>
      </div>
    </div>
  </div>
</section>
"""
    for i, key in enumerate(SERVICE_ORDER, 1):
        s = SERVICES[key][lang]
        steps = "".join(f"<li>{e(h)}</li>" for h, _ in s["steps"])
        ps = posts(key)
        case = next(p for p in ps if p["kind"] == "case")
        others = [p for p in ps if p["kind"] != "case" and p is not hero_post]
        body += f"""<section class="row service split-grid" id="{key}">
  <div class="wrap">
    <div class="row-copy">
      <div class="num"><b>0{i}</b><span class="eyebrow">{e(s['label'])}</span></div>
      <div class="body">
        <h2>{e(s['h'])}</h2>
        <p class="lead">{e(s['lead'])}</p>
        <ol class="steps">{steps}</ol>
        <a class="arrow-link" href="{url(lang, key + '/')}"><i></i>{e(s['more'])}</a>
      </div>
    </div>
    <div class="row-side">
      <div class="cards">
        <div class="tile"><img src="/assets/img/{SERVICES[key]['img']}" alt="" width="440" height="340" loading="lazy"></div>
        {card(lang, case)}
        {''.join(card(lang, p) for p in others[:2])}
      </div>
    </div>
  </div>
</section>
"""
    body += footer(lang)
    write(lang, "", body)


def page_service(lang, key):
    u = UI[lang]
    s = SERVICES[key][lang]
    path = key + "/"
    body = head(lang, path, f"{s['title']} | Waypoint", s["desc"]) + header(lang, path)
    detail = "".join(
        f"<li><b>0{n}</b><h3>{e(h)}</h3><p>{e(t)}</p></li>" for n, (h, t) in enumerate(s["steps"], 1)
    )
    cards = "".join(card(lang, p) for p in posts(key))
    body += f"""<section class="page-head gridpaper">
  <div class="wrap">
    <p class="eyebrow">{e(s['label'])}</p>
    <h1>{e(s['h'])}</h1>
    <p class="lead">{e(s['lead'])}</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>{e(u['how'])}</h2>
    <ol class="detail">{detail}</ol>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>{e(u['related'])}</h2>
    <div class="cards-3">{cards}</div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="cta"><h2>{e(u['cta_h'])}</h2><a class="arrow-link" href="{url(lang, 'contact/')}"><i></i>{e(u['cta_btn'])}</a></div>
  </div>
</section>
"""
    body += footer(lang)
    write(lang, path, body)


def blog_filters(lang, current):
    u = UI[lang]
    items = [("blog/", u["all"])] + [(f"blog/{k}/", SERVICES[k][lang]["label"]) for k in SERVICE_ORDER]
    return '<nav class="filters" aria-label="Blog">' + "".join(
        f'<a href="{url(lang, p)}"{CUR if p == current else ""}>{e(l)}</a>' for p, l in items
    ) + "</nav>"


def page_blog(lang, cat=None):
    u = UI[lang]
    path = f"blog/{cat}/" if cat else "blog/"
    title = f"{SERVICES[cat][lang]['label']} — Blog | Waypoint" if cat else f"{u['blog_title']} | Waypoint"
    body = head(lang, path, title, u["blog_lead"]) + header(lang, path)
    h = f"Blog: {SERVICES[cat][lang]['label']}" if cat else u["blog_h"]
    body += f"""<section class="page-head gridpaper">
  <div class="wrap">
    <p class="eyebrow">Blog</p>
    <h1>{e(h)}</h1>
    <p class="lead">{e(u['blog_lead'])}</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    {blog_filters(lang, path)}
"""
    groups = [cat] if cat else SERVICE_ORDER
    for g in groups:
        more = "" if cat else f' <a href="{url(lang, f"blog/{g}/")}">{e(u["all_posts"])} →</a>'
        body += f"""    <div class="blog-group">
      <h2>{e(SERVICES[g][lang]['label'])}{more}</h2>
      <div class="cards-3">{''.join(card(lang, p) for p in posts(g))}</div>
    </div>
"""
    body += f'    <p class="note">{e(u["blog_note"])}</p>\n  </div>\n</section>\n'
    body += footer(lang)
    write(lang, path, body)


def page_contact(lang):
    u = UI[lang]
    c = CONTACTS
    path = "contact/"
    body = head(lang, path, f"{u['contact_title']} | Waypoint", u["contact_lead"]) + header(lang, path)
    opts = "".join(f"<option>{e(SERVICES[k][lang]['label'])}</option>" for k in SERVICE_ORDER)
    body += f"""<section class="page-head gridpaper">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>{e(u['contact_h'])}</h1>
    <p class="lead">{e(u['contact_lead'])}</p>
  </div>
</section>
<section class="section">
  <div class="wrap contact-grid">
    <ul class="contact-list">
      <li><span>{u['c_email']}</span><a href="mailto:{c['email']}">{c['email']}</a></li>
      <li><span>{u['c_phone']}</span><a href="tel:{c['phone_href']}">{c['phone']}</a></li>
      <li><span>WhatsApp</span><a href="{c['whatsapp']}" target="_blank" rel="noopener">{c['phone']}</a></li>
      <li><span>Telegram</span><a href="{c['telegram']}" target="_blank" rel="noopener">@VentarSlavich</a></li>
      <li><span>{u['c_city']}</span>{e(c['city'][lang])}</li>
    </ul>
    <form class="contact" id="form" action="{FORMSPREE}" method="POST">
      <input type="hidden" name="_subject" value="Waypoint — new request ({lang.upper()})">
      <label class="hp" aria-hidden="true">_gotcha<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label>
      <label>{u['f_name']}<input name="name" required autocomplete="name"></label>
      <label>{u['f_contact']}<input name="contact" required></label>
      <label>{u['f_topic']}<select name="topic">{opts}</select></label>
      <label>{u['f_msg']}<textarea name="message" rows="5" placeholder="{e(u['f_msg_ph'])}"></textarea></label>
      <p class="note" style="margin:0">{u['f_legal']} <a href="{url(lang, 'privacy/')}" style="text-decoration:underline">{e(dict(u['legal'])['privacy/'])}</a>.</p>
      <button type="submit">{u['f_send']}</button>
      <p class="form-status" id="status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
<script>
document.getElementById('form').addEventListener('submit',async function(ev){{
  ev.preventDefault();var f=ev.target,s=document.getElementById('status'),b=f.querySelector('button');b.disabled=true;
  try{{var r=await fetch(f.action,{{method:'POST',body:new FormData(f),headers:{{Accept:'application/json'}}}});
    if(!r.ok)throw 0;f.reset();s.textContent={json.dumps(u['f_ok'], ensure_ascii=False)};}}
  catch(_){{s.textContent={json.dumps(u['f_err'], ensure_ascii=False)};}}finally{{b.disabled=false;}}
}});
</script>
"""
    body += footer(lang)
    write(lang, path, body)


def page_legal(lang, key):
    u = UI[lang]
    path = key + "/"
    doc = LEGAL[key]
    note = f'<p class="note" style="margin-bottom:24px">{e(u["legal_note"])}</p>' if u["legal_note"] else ""
    body = head(lang, path, f"{doc['title']} | Waypoint", doc["title"]) + header(lang, path)
    body += f"""<section class="page-head">
  <div class="wrap"><h1>{e(doc['title'])}</h1></div>
</section>
<section class="section">
  <div class="wrap prose" lang="de">{note}{doc['html']}</div>
</section>
"""
    body += footer(lang)
    write(lang, path, body)


def page_sitemap(lang):
    u = UI[lang]
    path = "sitemap/"
    items = []
    for p, l in u["nav"]:
        items.append((p, l))
        if p.rstrip("/") in SERVICE_ORDER:
            pass
        if p == "blog/":
            for k in SERVICE_ORDER:
                items.append((f"blog/{k}/", f"Blog — {SERVICES[k][lang]['label']}"))
    items += u["legal"][:-1]
    lis = "".join(f'<li><a href="{url(lang, p)}">{e(l)}</a></li>' for p, l in items)
    body = head(lang, path, f"{u['sitemap_h']} | Waypoint", u["sitemap_h"]) + header(lang, path)
    body += f"""<section class="page-head"><div class="wrap"><h1>{e(u['sitemap_h'])}</h1></div></section>
<section class="section"><div class="wrap"><ul class="sitemap-list">{lis}</ul></div></section>
"""
    body += footer(lang)
    write(lang, path, body)


def sitemap_xml():
    today = date.today().isoformat()
    rows = []
    for path in PAGES:
        alts = "".join(
            f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE_URL}{url(l, path)}"/>' for l in LANGS
        )
        for l in LANGS:
            rows.append(f"  <url><loc>{SITE_URL}{url(l, path)}</loc><lastmod>{today}</lastmod>{alts}</url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(xml)
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")


if __name__ == "__main__":
    for lang in LANGS:
        page_home(lang)
        for k in SERVICE_ORDER:
            page_service(lang, k)
        page_blog(lang)
        for k in SERVICE_ORDER:
            page_blog(lang, k)
        page_contact(lang)
        for k in ["impressum", "privacy", "terms"]:
            page_legal(lang, k)
        page_sitemap(lang)
    sitemap_xml()
    print(f"{len(PAGES)} pages x {len(LANGS)} languages")
