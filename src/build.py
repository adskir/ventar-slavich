#!/usr/bin/env python3
"""Генератор сайта GETNEUROB2B. Запуск: python3 src/build.py — пересобирает все страницы в корне репозитория."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = 'https://getneurob2b.com'  # поменять на адрес Netlify, пока сайт в черновике
AR = '<span class="ar" aria-hidden="true">→</span>'

# порядок страниц = порядок уголка «Далее»
PAGES = [
    ('', '00', 'Главная'),
    ('sobstvennikam/', '01', 'Собственникам'),
    ('diagnostika/', '02', 'Диагностика'),
    ('apgreid/', '03', 'Апгрейд'),
    ('videoreklama/', '04', 'Видеореклама'),
    ('saity/', '05', 'Сайты'),
    ('blog/', '06', 'Блог'),
    ('kontakty/', '07', 'Контакты'),
]
NAV = PAGES[1:]


def head(slug, title, desc):
    url = SITE_URL + '/' + slug
    return f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#F3EFE7">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ru_RU">
<meta property="og:site_name" content="GETNEUROB2B">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/fonts/fonts.css">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#main">К содержанию</a>
<div class="margin-line" aria-hidden="true"></div>
'''


def header(slug):
    num, name = next((n, t) for s, n, t in PAGES if s == slug)
    links = ''.join(f'<a href="/{s}"{" aria-current=\"page\"" if s == slug else ""}>{t}</a>' for s, n, t in NAV)
    mlinks = ''.join(f'<li><a href="/{s}"><span>{n}</span>{t}</a></li>' for s, n, t in PAGES)
    return f'''<header class="hdr wrap">
  <div class="inner">
    <a class="brand" href="/" aria-label="GETNEUROB2B, главная"><span class="logo">GETNEURO<b>B2B</b></span><span class="doc-id">ПРОТОКОЛ № 00{num} · {name.upper()}</span></a>
    <nav class="nav" aria-label="Основное">{links}</nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav">Меню</button>
  </div>
</header>
<div class="mnav" id="mnav" role="dialog" aria-modal="true" aria-label="Меню">
  <button class="close" type="button">Закрыть</button>
  <p>СОДЕРЖАНИЕ ПРОТОКОЛА</p>
  <ol>{mlinks}</ol>
</div>
'''


def next_corner(slug):
    i = [p[0] for p in PAGES].index(slug)
    if i + 1 >= len(PAGES):
        return ''
    s, n, t = PAGES[i + 1]
    return f'<a class="next" href="/{s}" aria-label="Далее: {t}"><b>{n}</b><small>Далее:<br>{t}</small></a>\n'


def sec_top(left, right=''):
    return f'<div class="sec-top rv"><span><b>{left.split(" / ")[0]}</b> / {left.split(" / ")[1]}</span><span>{right}</span></div>' if ' / ' in left else f'<div class="sec-top rv"><span>{left}</span><span>{right}</span></div>'


def cta(title='Пришлите сайт — сделаю бесплатную базовую диагностику',
        text='Найду ошибки, выберу одну главную и объясню, как её исправить. Дальше объём, цену и сроки согласуем заранее, до начала работ.',
        btn='Прислать сайт'):
    return f'''<section class="cta wrap" aria-labelledby="cta-t">
  <div class="inner">
    <div><p class="kicker">Следующий шаг</p><h2 class="h2" id="cta-t" style="margin-top:14px">{title}</h2><p>{text}</p></div>
    <div><a class="btn" href="/kontakty/">{btn} {AR}</a></div>
  </div>
</section>
'''


def footer(slug):
    links = ''.join(f'<li><a href="/{s}">{t}</a></li>' for s, n, t in NAV)
    return f'''<footer class="ftr wrap">
  <div class="inner">
    <div class="ftr-grid">
      <div>
        <span class="logo">GETNEURO<b>B2B</b></span>
        <p style="margin:12px 0 0;color:var(--ink-2);max-width:26em">Маркетинговый консалтинг на стороне предпринимателя. Андрей Потехин — 25 лет в бизнесе, 15 в маркетинге.</p>
        <p class="langs">Работаю с проектами на рынках: английский, немецкий, итальянский и все славянские языки.</p>
      </div>
      <div><h4>Разделы</h4><ul>{links}</ul></div>
      <div><h4>Связь</h4><ul><li><a href="/kontakty/">Форма заявки</a></li><li>[email]</li><li>[Telegram / WhatsApp]</li></ul></div>
    </div>
    <div class="ftr-bottom"><span>© <span data-year>2026</span> GETNEUROB2B · Андрей Потехин · [реквизиты]</span><span><a href="#">Политика конфиденциальности</a></span></div>
  </div>
</footer>
{next_corner(slug)}<script src="/assets/main.js" defer></script>
</body>
</html>
'''


def page(slug, title, desc, body):
    html = head(slug, title, desc) + header(slug) + '<main id="main">\n' + body + '</main>\n' + footer(slug)
    path = os.path.join(ROOT, slug, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(html)


def cards(items, cls='g2', more=False):
    out = ''
    for i, it in enumerate(items):
        n, h, p = it[:3]
        href = it[3] if len(it) > 3 else None
        tag = 'a' if href else 'div'
        attr = f' href="{href}"' if href else ''
        m = '<span class="more">Подробнее →</span>' if href else ''
        out += f'<{tag} class="card rv" style="transition-delay:{i*0.08:.2f}s"{attr}><div class="n">{n}</div><h3>{h}</h3><p>{p}</p>{m}</{tag}>'
    return f'<div class="grid {cls}">{out}</div>'


def alerts():
    items = ['Доступы к рекламным кабинетам и аналитике есть только у исполнителя, а не у вас.',
             '«Подождите ещё пару месяцев» без понятных цифровых критериев и KPI.',
             'Гарантии результата без глубокого погружения в вашу юнит-экономику и маржинальность.',
             'Маркетолог никогда не спрашивает про вашу чистую маржу и реальные финансовые цели бизнеса.']
    return '<ul class="alerts">' + ''.join(f'<li style="--i:{i}">{t}</li>' for i, t in enumerate(items)) + '</ul>'


def about_block():
    return '''<div class="about">
  <div class="rv"><p class="big">Ошибок я наделал много. Вам делать их не придётся.</p>
    <div class="facts"><div><b data-to="25">25</b><span>лет в бизнесе</span></div><div><b data-to="15">15</b><span>в маркетинге</span></div></div></div>
  <div class="rv"><p>25 лет я совладелец бизнеса, и 15 из них управляю его маркетологами. Ошибки — лучший учитель, и у меня их набралось внушительное количество.</p>
    <p>Теперь этот опыт работает на вас: подскажу, как не повторить мои промахи. Вы работаете лично со мной, <span class="mark">без посредников и юниоров</span>.</p></div>
</div>
'''


# ---------------- ГЛАВНАЯ ----------------
home = f'''<section class="hero wrap" aria-labelledby="h1">
  <div class="inner">
    <div>
      <p class="kicker">Маркетинговый консалтинг на стороне предпринимателя</p>
      <h1 class="h1" id="h1">Найду, куда <span class="pen">утекают<svg aria-hidden="true" viewBox="0 0 300 30" preserveAspectRatio="none"><path d="M4 18 C 60 6, 140 26, 200 12 S 280 10, 296 16"></path></svg></span> ваши деньги.</h1>
      <p class="lead">Проверю сайт, рекламу и работу подрядчиков. Покажу, за что вы переплачиваете, и как это исправить — по шагам.</p>
      <form class="urlform" action="/kontakty/" method="get">
        <label class="sr" for="site">Адрес вашего сайта</label>
        <input id="site" name="site" inputmode="url" autocomplete="url" placeholder="адрес-вашего-сайта.ru" data-type="pizzeria-roma.it|zahnarzt-berlin.de|studio-yoga.com|ваш-сайт.ru">
        <button class="btn" type="submit">Бесплатный разбор {AR}</button>
      </form>
      <div class="sign">
        <div class="ph" aria-hidden="true">фото</div>
        <div><b>Андрей Потехин</b><small>25 лет в бизнесе · 15 в маркетинге · EN · DE · IT · славянские языки</small></div>
      </div>
    </div>
    <article class="sheet" aria-label="Пример протокола проверки">
      <div class="top"><span>ПРОТОКОЛ · ПРИМЕР</span><span>[ДАТА]</span></div>
      <h2>Куда уходит рекламный бюджет</h2>
      <ul class="rows">
        <li style="--i:0"><span>Боты и нецелевой трафик</span><span class="st bad">✕ утечка</span><span class="note" aria-hidden="true">вот здесь утекает ↙</span><svg class="circle" aria-hidden="true" viewBox="0 0 220 50" preserveAspectRatio="none"><ellipse cx="110" cy="25" rx="106" ry="21" transform="rotate(-2 110 25)"></ellipse></svg></li>
        <li style="--i:1"><span>Клики из рекламы</span><span class="st">✓ в норме</span></li>
        <li style="--i:2"><span>Форма заявки на телефоне</span><span class="st bad">✕ не работает</span></li>
        <li style="--i:3"><span>Доступы к аналитике</span><span class="st bad">! только у подрядчика</span></li>
        <li style="--i:4"><span>Consent Mode v2</span><span class="st bad">✕ конверсии теряются</span></li>
        <li style="--i:5"><span>Стоимость одной продажи</span><span class="st">? никто не знает</span></li>
      </ul>
      <div class="fix">ГЛАВНОЕ ИСПРАВЛЕНИЕ: <span class="mark">починить форму на мобильном</span> — сначала её, потом всё остальное.</div>
      <div class="stamp" aria-hidden="true">ПРОВЕРЕНО<br><span>А. Потехин</span><br>GETNEUROB2B</div>
    </article>
  </div>
</section>

<section class="sec wrap" aria-labelledby="s1">
  <div class="inner">
    {sec_top('01 / Что я делаю', 'стр. 1')}
    <h2 class="h2 rv" id="s1">Больше продаж. Ниже стоимость привлечения клиента. <span class="mark">Выше прибыль.</span></h2>
    {cards([
        ('01', 'Для собственников', 'Поиск финансовых дыр в маркетинге. Найду, куда утекают деньги, и покажу, за что вы переплачиваете подрядчикам.', '/sobstvennikam/'),
        ('02', 'Диагностика', 'Глубокая проверка сайта и рекламы. Поищу технические и смысловые ошибки, из-за которых вы теряете клиентов прямо сейчас.', '/diagnostika/'),
        ('03', 'Апгрейд', 'Исправление и рост продаж. Перенастроим аналитику, воронку и кампании так, чтобы вложения наконец начали приносить прибыль.', '/apgreid/'),
        ('04', 'Видеореклама', 'Помогу привлечь новую аудиторию через видео на YouTube, Instagram и TikTok.', '/videoreklama/'),
        ('05', 'Сайты', 'Обновлю сайт, который устарел, или создам новый для бизнеса услуг — с ясной подачей и формой заявки.', '/saity/'),
    ], 'g3')}
  </div>
</section>

<section class="sec wrap" aria-labelledby="s2">
  <div class="inner">
    {sec_top('02 / Тревожные сигналы', 'стр. 2')}
    <h2 class="h2 rv" id="s2">Проверьте себя: сколько пунктов про вас?</h2>
    {alerts()}
    <blockquote class="quote rv"><p>Хуже всего не когда реклама не работает, а когда работает «нормально». Так можно годами переплачивать и не замечать.</p></blockquote>
  </div>
</section>

<section class="sec wrap" aria-labelledby="s3">
  <div class="inner">
    {sec_top('03 / Обо мне', 'стр. 3')}
    <h2 class="h2 rv" id="s3">Опыт и практика</h2>
    {about_block()}
  </div>
</section>
{cta()}'''
page('', 'GETNEUROB2B — маркетинговый консалтинг на стороне предпринимателя',
     'Найду, куда утекает рекламный бюджет: проверка сайта, рекламы и подрядчиков. Бесплатная базовая диагностика. Андрей Потехин.', home)


def inner_hero(kicker, title, lead, extra=''):
    return f'''<section class="hero wrap" aria-labelledby="h1">
  <div class="inner" style="min-height:0;grid-template-columns:minmax(0,1fr);padding:clamp(56px,7vw,96px) 0 clamp(48px,6vw,80px)">
    <div>
      <p class="kicker">{kicker}</p>
      <h1 class="h1" id="h1" style="max-width:14em">{title}</h1>
      <p class="lead">{lead}</p>
      {extra}
    </div>
  </div>
</section>
'''


# ---------------- СОБСТВЕННИКАМ ----------------
body = inner_hero('01 / Для собственников', 'Маркетинговый консалтинг на <span class="pen">стороне<svg aria-hidden="true" viewBox="0 0 300 30" preserveAspectRatio="none"><path d="M4 18 C 60 6, 140 26, 200 12 S 280 10, 296 16"></path></svg></span> предпринимателя',
                  'Ваш маркетолог отчитывается заявками, а в бизнесе пусто? Нахожу, куда сливается рекламный бюджет, и возвращаю контроль над маркетингом в ваши руки.')
body += f'''<section class="sec wrap" aria-labelledby="s1">
  <div class="inner">
    <blockquote class="quote rv" style="margin-top:0"><p>Хуже всего не когда реклама не работает, а когда работает «нормально». Так можно годами переплачивать и не замечать.</p></blockquote>
    <div style="margin-top:clamp(56px,7vw,96px)">{sec_top('Контроль бюджета / За что вы платите', 'Диагностика воронки продаж')}</div>
    <h2 class="h2 rv" id="s1">За что вы платите и что я проверяю</h2>
    {cards([
        ('01', 'Слив бюджета на площадках', 'Проверяю, не платите ли вы за пустые клики, ботов и нецелевой трафик, пока ваш маркетолог разводит руками.'),
        ('02', 'Имитация бурной деятельности', 'Оцениваю реальный КПД подрядчика: действительно ли он управляет ростом продаж или просто ведёт соцсети по привычке.'),
        ('03', 'Был клиент — и сплыл', 'Нахожу технические и смысловые дыры на сайте, из-за которых люди уходят к конкурентам, хотя вы уже заплатили за их привлечение.'),
        ('04', 'Маркетинг вслепую', 'Выстраиваю сквозную аналитику так, чтобы вы точно знали стоимость привлечения одной продажи, а не клика или заявки.'),
    ])}
    <blockquote class="quote rv"><p>Если маркетолог не может назвать вам точную стоимость привлечения реальной продажи — вы спонсируете его надежды, а не развиваете бизнес.</p></blockquote>
  </div>
</section>
<section class="sec wrap" aria-labelledby="s2">
  <div class="inner">
    <div class="about" style="margin-top:0">
      <div><h2 class="h2 rv" id="s2">Тревожные сигналы</h2>{alerts()}</div>
      <div class="rv"><h2 class="h2">Что вы получите на выходе</h2>
        <p class="sub">Чёткий список исправлений по порядку срочности: что изменить, зачем и как перепроверить результат. С вашим маркетологом я поговорю сам, отвечу на его вопросы и прослежу, чтобы всё исправили. <span class="mark">Если он не тянет — подберу другого</span> под ваши задачи и бюджет.</p></div>
    </div>
  </div>
</section>
<section class="sec wrap" aria-labelledby="s3">
  <div class="inner">
    {sec_top('GETNEUROB2B / Экспертиза', 'Опыт и практика')}
    <h2 class="h2 rv" id="s3">Обо мне</h2>
    {about_block()}
  </div>
</section>
{cta()}'''
page('sobstvennikam/', 'Для собственников — GETNEUROB2B', 'Маркетинговый консалтинг на стороне предпринимателя: найду, куда сливается рекламный бюджет, и верну контроль над маркетингом.', body)

# ---------------- ДИАГНОСТИКА ----------------
body = inner_hero('02 / Независимая оценка · сайт и реклама', 'Диагностика сайта и <span class="pen">рекламы<svg aria-hidden="true" viewBox="0 0 300 30" preserveAspectRatio="none"><path d="M4 18 C 60 6, 140 26, 200 12 S 280 10, 296 16"></path></svg></span>',
                  'Изучу ваш сайт и доступную информацию о рекламе. Если обнаружу ошибки, выберу самую важную и объясню, как её исправить. Начнём бесплатно.')
body += f'''<section class="sec wrap" aria-labelledby="s1">
  <div class="inner">
    {sec_top('Два формата / Бесплатно и платно', 'стр. 1')}
    <h2 class="h2 rv" id="s1">С чего начнём</h2>
    <div class="grid g2">
      <div class="card rv"><span class="tag">01 · Бесплатно</span><h3 style="font-size:clamp(26px,2.4vw,34px)">Базовый разбор</h3><p><b>Одно важное улучшение. Понятный порядок действий.</b></p>
        <p style="margin-top:12px">Изучу ваш сайт и доступную информацию о рекламе. Если обнаружу ошибки, выберу самую важную и объясню, как её исправить:</p>
        <ul><li>что обнаружено и как это влияет на результат;</li><li>что и в какой последовательности исправить;</li><li>как проверить, что исправление работает.</li></ul>
        <p style="margin-top:22px"><a class="btn" href="/kontakty/">Прислать сайт на разбор {AR}</a></p></div>
      <div class="card card--dark rv" style="transition-delay:.1s"><span class="tag">02 · Платно</span><h3 style="font-size:clamp(26px,2.4vw,34px)">Расширенный разбор</h3><p><b style="color:var(--paper)">Полная картина. Приоритеты. Задания исполнителям.</b></p>
        <p style="margin-top:12px">Проверю сайт и рекламную систему бизнеса в согласованном объёме:</p>
        <ul><li><b>Техническое состояние сайта:</b> ошибки, скорость загрузки, мобильная версия, формы и ссылки.</li><li><b>Техническая готовность к SEO:</b> доступность для индексации, структура, метаданные.</li><li><b>Аналитика:</b> Google Analytics, события и конверсии, связь с рекламными кабинетами.</li><li><b>GDPR / DSGVO и Consent Mode v2:</b> баннер согласий и передача данных. Ошибка здесь — это и юридический риск, и «ослепший» Google Ads, который теряет до 50% данных о конверсиях.</li><li><b>Реклама:</b> площадки, аудитории, объявления, распределение бюджета.</li><li><b>Путь до продажи:</b> соответствие рекламы посадочным страницам, качество и обработка обращений.</li><li><b>Стоимость обслуживания:</b> состав работы подрядчиков и обоснованность расходов.</li></ul>
        <p style="margin-top:14px">Подготовлю общий вывод: что работает, что изменить в первую очередь, какие задачи передать исполнителям и как проверить результат. Стоимость согласуем до начала работы.</p>
        <p style="margin-top:12px;font:13px var(--mono);color:#B9AFA3">Для проверки внутренних настроек аналитики и рекламы потребуются доступы на просмотр.</p>
        <p style="margin-top:22px"><a class="btn" href="/kontakty/">Обсудить расширенный разбор {AR}</a></p></div>
    </div>
  </div>
</section>
{cta()}'''
page('diagnostika/', 'Диагностика сайта и рекламы — GETNEUROB2B', 'Независимая диагностика сайта и рекламы: бесплатный базовый разбор и расширенный разбор с приоритетами и заданиями исполнителям.', body)

# ---------------- АПГРЕЙД ----------------
body = inner_hero('03 / Сайт · аналитика · реклама', 'Апгрейд сайта и <span class="pen">рекламы<svg aria-hidden="true" viewBox="0 0 300 30" preserveAspectRatio="none"><path d="M4 18 C 60 6, 140 26, 200 12 S 280 10, 296 16"></path></svg></span>',
                  'От найденных ошибок — к исправлениям. Организую работу и проверю результат.')
body += f'''<section class="sec wrap" aria-labelledby="s1">
  <div class="inner">
    {sec_top('Что улучшаем / Состав работ', 'зависит от диагностики')}
    <h2 class="h2 rv" id="s1">Что улучшаем</h2>
    <p class="sub rv">Состав работ зависит от результатов диагностики и задач бизнеса.</p>
    {cards([
        ('—', 'Сайт', 'Техническое состояние и ключевые элементы, влияющие на путь клиента.'),
        ('—', 'Аналитика', 'Точность данных, событий и конверсий, которые помогают оценивать результат.'),
        ('—', 'Реклама', 'Настройки кампаний, распределение бюджета и связь рекламы с целями бизнеса.'),
    ], 'g3')}
    <div class="card rv" style="margin-top:18px"><h3>Соответствие GDPR / DSGVO и проверка Consent Mode v2</h3><p>Проверяю корректность работы баннера согласий и передачи данных в аналитику. Некорректная настройка GDPR не только создаёт юридические риски и угрозу штрафов в ЕС, но и «ослепляет» алгоритмы Google Ads — <span class="mark">система теряет до 50% данных о конверсиях</span> и начинает работать вслепую.</p></div>
  </div>
</section>
<section class="sec wrap" aria-labelledby="s2">
  <div class="inner">
    {sec_top('Кто внедряет / Три варианта', 'выбираем после диагностики')}
    <h2 class="h2 rv" id="s2">Кто внедряет изменения</h2>
    <p class="sub rv">Выбираем подходящий вариант после диагностики и согласуем конкретные задачи.</p>
    <div class="grid g3">
      <div class="card rv"><span class="tag">01 / Ваш маркетолог</span><h3>Исправления по моим рекомендациям</h3><p>Подготовлю пошаговые рекомендации: что изменить на сайте, в аналитике и рекламе, в какой последовательности и как проверить результат. Обсужу их с вашим маркетологом, отвечу на вопросы и проверю выполненные исправления.</p></div>
      <div class="card rv" style="transition-delay:.08s"><span class="tag">02 / Новый исполнитель</span><h3>Подбор под задачи и бюджет</h3><ul style="margin-top:0"><li>Если качество работы вас не устраивает — подберу квалифицированного исполнителя.</li><li>Если обслуживание обходится слишком дорого — найду исполнителя с сопоставимым качеством на более выгодных условиях.</li></ul><p style="margin-top:10px">Объясню, что нужно исправить, и проверю выполнение.</p></div>
      <div class="card rv" style="transition-delay:.16s"><span class="tag">03 / Настрою и обучу</span><h3>Контроль рекламы — вашему сотруднику</h3><p>Если рекламы немного и повседневный контроль можно свести к простым действиям, с ним справится администратор или офис-менеджер. Я выполню настройки сайта, аналитики и рекламы, обучу сотрудника и передам чек-листы: что проверять, что делать при отклонениях и когда обращаться ко мне.</p></div>
    </div>
  </div>
</section>
<section class="sec wrap" aria-labelledby="s3">
  <div class="inner">
    {sec_top('Как проходит работа / Четыре шага', 'объём и цена — заранее')}
    <h2 class="h2 rv" id="s3">Как проходит работа</h2>
    <p class="sub rv">Согласуем план после диагностики и заранее определим объём работ и стоимость.</p>
    <ol class="steps">
      <li style="--i:0"><span class="n">ШАГ 1</span><h3>Определяю приоритеты</h3><p>Что исправить первым, чтобы быстрее увидеть эффект.</p></li>
      <li style="--i:1"><span class="n">ШАГ 2</span><h3>Согласую объём и стоимость</h3><p>До начала работ, без сюрпризов.</p></li>
      <li style="--i:2"><span class="n">ШАГ 3</span><h3>Организую внедрение</h3><p>С вашим маркетологом, новым исполнителем или сам.</p></li>
      <li style="--i:3"><span class="n">ШАГ 4</span><h3>Проверяю исправления и данные</h3><p>Убеждаюсь, что всё работает и цифры сходятся.</p></li>
    </ol>
  </div>
</section>
{cta()}'''
page('apgreid/', 'Апгрейд сайта и рекламы — GETNEUROB2B', 'От найденных ошибок к исправлениям: сайт, аналитика, реклама, GDPR и Consent Mode v2. Организую работу и проверю результат.', body)

# ---------------- ВИДЕОРЕКЛАМА ----------------
body = inner_hero('04 / Видеореклама · привлечение новых клиентов', 'Покажись <span class="pen">крупным<svg aria-hidden="true" viewBox="0 0 300 30" preserveAspectRatio="none"><path d="M4 18 C 60 6, 140 26, 200 12 S 280 10, 296 16"></path></svg></span> планом!',
                  'Помогу привлечь новую аудиторию через видео на YouTube, Instagram и TikTok.',
                  '<div class="video rv" style="margin-top:40px;max-width:880px"><div><div class="play" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M8 5l11 7-11 7z" fill="#fff"></path></svg></div>[ ролик с YouTube — тот же, что на текущем сайте ]</div></div>')
body += f'''<section class="sec wrap" aria-labelledby="s1">
  <div class="inner">
    {sec_top('Форматы / YouTube · Instagram · TikTok', 'стр. 1')}
    <h2 class="h2 rv" id="s1">Пусть увидят. Заинтересуются. <span class="mark">Обратятся.</span></h2>
    {cards([
        ('01', 'Знакомство: о компании', 'Познакомлю новую аудиторию с компанией.'),
        ('02', 'Продукт: показать предложение', 'Покажу продукт в действии или результат услуги.'),
        ('03', 'Объяснение: раскрыть услугу', 'Объясню, как работает ваше предложение.'),
        ('04', 'Приглашение: на мероприятие', 'Приглашу аудиторию на событие или презентацию.'),
        ('05', 'Повторный контакт: вернуться к интересу', 'Помогу напомнить о себе тем, кто уже заинтересовался.'),
    ], 'g3')}
  </div>
</section>
<section class="sec wrap" aria-labelledby="s2">
  <div class="inner">
    {sec_top('Воронка / Пример пути клиента', 'стр. 2')}
    <h2 class="h2 rv" id="s2">Больше людей на входе в вашу воронку</h2>
    <div class="funnel">
      <div style="--i:0"><span>01</span>Видео</div><div style="--i:1"><span>02</span>Интерес</div><div style="--i:2"><span>03</span>Сайт</div><div style="--i:3"><span>04</span>Повторная реклама</div><div style="--i:4"><span>05</span>Обращение</div>
    </div>
    <p class="mono rv" style="font-size:13px;color:var(--mute);margin-top:14px">Пример пути клиента. Просмотр ролика сам по себе ещё не подтверждает интерес.</p>
    <div class="grid g2">
      <div class="card card--dark rv"><h3>Начать можно с небольшого бюджета</h3><p>Запущу тест. Проверю интерес к предложению, переходы на сайт и обращения. По результатам предложу дальнейший бюджет.</p></div>
      <div class="card rv"><h3>Как организую создание ролика</h3><p>Обсуждаю идею и задачу, подбираю исполнителей под формат проекта. Использую ваши фото и видео, AI-сцены и монтаж. Работаю дистанционно с клиентами из любой страны; съёмку организую, если она нужна.</p></div>
    </div>
  </div>
</section>
{cta('Черновик видео — без предоплаты', 'Подготовлю короткий фрагмент ролика без предоплаты. Вы оцените стиль и направление; создание полной версии обсудим отдельно. Расскажите о бизнесе и задаче, которую должен решить ролик.', 'Обсудить видеорекламу')}'''
page('videoreklama/', 'Видеореклама — GETNEUROB2B', 'Видеореклама на YouTube, Instagram и TikTok: форматы, тест с небольшого бюджета, черновик видео без предоплаты.', body)

# ---------------- САЙТЫ ----------------
body = inner_hero('05 / Web design · сайты для бизнеса услуг', 'Нужен новый сайт или <span class="pen">редизайн?<svg aria-hidden="true" viewBox="0 0 300 30" preserveAspectRatio="none"><path d="M4 18 C 60 6, 140 26, 200 12 S 280 10, 296 16"></path></svg></span>',
                  'Обновлю сайт, который устарел, или создам новый для бизнеса услуг — с ясной подачей и формой заявки.')
body += f'''<section class="sec wrap" aria-labelledby="s1">
  <div class="inner">
    <div class="about" style="margin-top:0">
      <div class="rv">
        {sec_top('Сайты / Для услуг', 'этот сайт — мой кейс')}
        <h2 class="h2" id="s1">Сайты для услуг</h2>
        <p class="sub">Структура помогает посетителю понять, чем вы занимаетесь, почему стоит обратиться и как оставить заявку.</p>
        <ul class="alerts ok"><li style="--i:0">Редизайн действующего сайта или разработка нового</li><li style="--i:1">Понятная подача услуг и адаптация для мобильных экранов</li><li style="--i:2">Форма заявки для связи с потенциальным клиентом</li></ul>
        <h3 style="margin:40px 0 8px;font-size:26px">Моя специализация</h3>
        <p style="margin:0;color:var(--ink-2)">Создаю сайты для компаний и специалистов, которые продают услуги. Интернет-магазины и каталоги товаров в эту услугу не входят.</p>
      </div>
      <div class="card card--dark rv price" style="align-self:start;padding:clamp(28px,3vw,44px)">
        <small>Стоимость разработки</small>
        <h3 style="margin:0;font-size:28px">Сайт, похожий на этот</h3>
        <b>от <span data-to="600">600</span> €</b>
        <p>Итоговая стоимость зависит от структуры и объёма страниц. Состав работ согласуем заранее.</p>
        <p style="margin-top:18px"><a class="btn" href="/kontakty/" style="background:var(--red)">Обсудить сайт {AR}</a></p>
        <p style="font:13px var(--mono);color:#B9AFA3;margin-top:6px">Можно прислать ссылку на текущий сайт и коротко описать задачу.</p>
      </div>
    </div>
  </div>
</section>
'''
page('saity/', 'Сайты для бизнеса услуг — GETNEUROB2B', 'Редизайн или новый сайт для бизнеса услуг: ясная подача, мобильная версия, форма заявки. От 600 €.', body)

# ---------------- БЛОГ ----------------
body = inner_hero('06 / Блог', 'Заметки о маркетинге <span class="pen">без<svg aria-hidden="true" viewBox="0 0 300 30" preserveAspectRatio="none"><path d="M4 18 C 60 6, 140 26, 200 12 S 280 10, 296 16"></path></svg></span> иллюзий',
                  'Разборы, ошибки и практические советы для собственников бизнеса.')
body += f'''<section class="sec wrap" aria-labelledby="s1">
  <div class="inner">
    {sec_top('Статьи / Последние записи', '[перенести из текущего блога]')}
    <h2 class="sr" id="s1">Статьи</h2>
    {cards([
        ('[дата]', '[Заголовок статьи из текущего блога]', '[Короткое описание — 1–2 предложения]'),
        ('[дата]', '[Заголовок статьи из текущего блога]', '[Короткое описание — 1–2 предложения]'),
        ('[дата]', '[Заголовок статьи из текущего блога]', '[Короткое описание — 1–2 предложения]'),
    ], 'g3')}
  </div>
</section>
{cta()}'''
page('blog/', 'Блог — GETNEUROB2B', 'Заметки о маркетинге для собственников бизнеса: разборы, ошибки, практические советы.', body)

# ---------------- КОНТАКТЫ ----------------
body = inner_hero('07 / Контакты', 'Пришлите сайт и опишите <span class="pen">задачу<svg aria-hidden="true" viewBox="0 0 300 30" preserveAspectRatio="none"><path d="M4 18 C 60 6, 140 26, 200 12 S 280 10, 296 16"></path></svg></span>',
                  'Я лично разберу техническое состояние, рекламу и найду точки потери денег.')
body += f'''<section class="sec wrap" aria-labelledby="s1">
  <div class="inner">
    <div class="about" style="margin-top:0">
      <form class="form rv" name="zayavka" method="POST" action="/kontakty/spasibo/" data-netlify="true" netlify-honeypot="bot-field">
        <h2 class="sr" id="s1">Форма заявки</h2>
        <input type="hidden" name="form-name" value="zayavka">
        <p class="hidden"><label>Не заполняйте <input name="bot-field"></label></p>
        <div class="field"><label for="f-name">Имя *</label><input id="f-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="f-contact">Email или телефон *</label><input id="f-contact" name="contact" autocomplete="email" required></div>
        <div class="field"><label for="f-site">Адрес сайта</label><input id="f-site" name="site" inputmode="url" placeholder="ваш-сайт.ru"></div>
        <div class="field"><label for="f-msg">Задача</label><textarea id="f-msg" name="message" placeholder="Что беспокоит: реклама, сайт, подрядчик, видео…"></textarea></div>
        <label class="consent"><input type="checkbox" name="consent" required><span>Согласен на обработку данных для ответа на заявку, как описано в <a href="#">политике конфиденциальности</a>. *</span></label>
        <div><button class="btn" type="submit">Отправить заявку {AR}</button></div>
      </form>
      <div class="rv">
        <div class="card"><span class="tag">Что будет дальше</span>
          <ol style="margin:14px 0 0;padding-left:20px;color:var(--ink-2)"><li style="margin:8px 0">Изучу сайт и доступную информацию о рекламе.</li><li style="margin:8px 0">Выберу одну главную ошибку и объясню, как её исправить.</li><li style="margin:8px 0">Если нужна большая работа — объём, цену и сроки согласуем заранее.</li></ol></div>
        <div class="card" style="margin-top:18px"><span class="tag">Напрямую</span><p style="margin-top:10px">[email]<br>[Telegram / WhatsApp]</p></div>
        <p class="langs">Работаю с проектами на рынках: английский, немецкий, итальянский и все славянские языки.</p>
      </div>
    </div>
  </div>
</section>
'''
page('kontakty/', 'Контакты — GETNEUROB2B', 'Пришлите сайт и опишите задачу — бесплатная базовая диагностика сайта и рекламы.', body)

body = inner_hero('Заявка получена', 'Спасибо! Заявка <span class="pen">принята<svg aria-hidden="true" viewBox="0 0 300 30" preserveAspectRatio="none"><path d="M4 18 C 60 6, 140 26, 200 12 S 280 10, 296 16"></path></svg></span>',
                  'Я изучу сайт и вернусь с ответом. А пока можно почитать, как проходит диагностика.',
                  f'<p style="margin-top:32px"><a class="btn btn--ghost" href="/diagnostika/">Как проходит диагностика {AR}</a></p>')
PAGES.append(('kontakty/spasibo/', '08', 'Спасибо'))
page('kontakty/spasibo/', 'Спасибо — GETNEUROB2B', 'Заявка получена.', body)
print('ok')
