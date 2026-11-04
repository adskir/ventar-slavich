# GETNEUROB2B — новый сайт (черновик)

Статический сайт в стиле «Протокол проверки». Русская версия.

## Как устроено
- `src/build.py` — все тексты и шаблоны страниц. После правки: `python3 src/build.py` пересобирает все страницы.
- `assets/style.css`, `assets/main.js` — стили и анимации (лист протокола, печать, маркер, счётчики, печатающийся адрес сайта).
- `assets/og.jpg` — картинка-превью для ссылок.
- `bozze/` — три исходных направления (A, B, C).

## Страницы
`/` · `/sobstvennikam/` · `/diagnostika/` · `/apgreid/` · `/videoreklama/` · `/saity/` · `/blog/` · `/kontakty/` (+ `/kontakty/spasibo/`)

## Форма
Форма на `/kontakty/` — Netlify Forms (`data-netlify="true"`). В настройках Netlify должно быть включено Forms → Form detection.

## Ждём от заказчика (TODO)
- Портрет Андрея, email, Telegram/WhatsApp, реквизиты, политика конфиденциальности.
- Ссылка на ролик YouTube для страницы «Видеореклама».
- Статьи блога.
- Домен: `SITE_URL` в `src/build.py` (сейчас https://getneurob2b.com). Убрать `noindex` и `robots.txt` при запуске.
