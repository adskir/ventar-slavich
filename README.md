# Waypoint — сайт (RU + DE)

Статический сайт: консалтинг, онлайн-маркетинг, видеореклама. Русская версия в корне `/`, немецкая в `/de/`.

## Как устроено
- `src/content.py` — все тексты RU/DE, контакты, записи блога (кейсы, статьи, советы).
- `src/legal.py` — Impressum, Datenschutz, AGB (черновик, места для данных помечены жёлтым).
- `src/build.py` — генератор. После правки текстов: `python3 src/build.py` — пересобирает все страницы, `sitemap.xml` и `robots.txt`.
- `assets/` — стили, шрифт Inter (локально, без Google Fonts), иллюстрации SVG, favicon.

## Структура
```
/                Home            /de/
/consulting/     Consulting      /de/consulting/
/marketing/      Marketing       /de/marketing/
/video-ads/      Video Ads       /de/video-ads/
/blog/ (+ /blog/consulting|marketing|video-ads/)
/contact/
/impressum/ /privacy/ /terms/ /sitemap/
```

## Ждём от заказчика (TODO)
- Тексты кейсов и статей (сейчас в блоге только карточки).
- Домен (в `SITE_URL` стоит https://waypoint.consulting), email, данные для Impressum и AGB.
- Своя форма Formspree (сейчас временная), фото/иллюстрации если нужны вместо SVG.
