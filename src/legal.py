# Rechtstexte (Entwurf). Alles mit class="todo" muss vom Kunden ausgefüllt
# und vor dem Livegang rechtlich geprüft werden (z. B. Anwalt oder eRecht24-Generator).

T = '<span class="todo">'
E = "</span>"

LEGAL = {
    "impressum": {
        "title": "Impressum",
        "html": f"""
<h2>Angaben gemäß § 5 DDG</h2>
<p>{T}[Vor- und Nachname / Firmenname]{E}<br>{T}[Straße und Hausnummer]{E}<br>{T}[PLZ] München{E}<br>Deutschland</p>
<h2>Kontakt</h2>
<p>Telefon: +49 152 1017 3689<br>E-Mail: {T}hello@waypoint.consulting{E}</p>
<h2>Umsatzsteuer-ID</h2>
<p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: {T}[DE…]{E}</p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
<p>{T}[Name, Anschrift wie oben]{E}</p>
<h2>EU-Streitschlichtung</h2>
<p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
""",
    },
    "privacy": {
        "title": "Datenschutzerklärung",
        "html": f"""
<h2>1. Verantwortlicher</h2>
<p>{T}[Name / Firma, Anschrift, E-Mail]{E}</p>
<h2>2. Hosting und Server-Logfiles</h2>
<p>Beim Aufruf dieser Website verarbeitet unser Hosting-Anbieter {T}[Anbieter, Land]{E} technisch notwendige Daten (IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browser). Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (sicherer Betrieb der Website).</p>
<h2>3. Kontaktformular</h2>
<p>Die im Formular angegebenen Daten (Name, Kontakt, Nachricht) verwenden wir ausschließlich zur Bearbeitung Ihrer Anfrage (Art. 6 Abs. 1 lit. b DSGVO). Das Formular wird über Formspree (Formspree Inc., USA) übermittelt; die Übermittlung in die USA erfolgt auf Grundlage der EU-Standardvertragsklauseln.</p>
<h2>4. WhatsApp und Telegram</h2>
<p>Wenn Sie uns über WhatsApp oder Telegram kontaktieren, gelten zusätzlich die Datenschutzbestimmungen dieser Anbieter.</p>
<h2>5. Cookies und Schriftarten</h2>
<p>Diese Website setzt keine Tracking- oder Marketing-Cookies. Schriftarten werden lokal vom eigenen Server geladen; es findet keine Verbindung zu Google Fonts statt.</p>
<h2>6. Speicherdauer</h2>
<p>Anfragen löschen wir, sobald sie erledigt sind und keine gesetzlichen Aufbewahrungspflichten bestehen.</p>
<h2>7. Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht auf Beschwerde bei einer Datenschutz-Aufsichtsbehörde, z. B. dem Bayerischen Landesamt für Datenschutzaufsicht.</p>
""",
    },
    "terms": {
        "title": "Allgemeine Geschäftsbedingungen",
        "html": f"""
<p>{T}Entwurf — die AGB müssen vom Kunden bereitgestellt bzw. rechtlich geprüft werden.{E}</p>
<h2>1. Geltungsbereich</h2>
<p>Diese AGB gelten für alle Beratungs-, Marketing- und Videoproduktionsleistungen von {T}[Name / Firma]{E}.</p>
<h2>2. Vertragsschluss</h2>
<p>Ein Vertrag kommt durch schriftliche Auftragsbestätigung oder Angebotsannahme zustande.</p>
<h2>3. Leistungen und Mitwirkung</h2>
<p>Umfang und Termine ergeben sich aus dem jeweiligen Angebot. Der Kunde stellt die erforderlichen Informationen und Zugänge rechtzeitig bereit.</p>
<h2>4. Vergütung und Zahlung</h2>
<p>{T}[Zahlungsbedingungen]{E}</p>
<h2>5. Werbebudgets</h2>
<p>Werbebudgets (z. B. Google Ads, Meta Ads) werden direkt vom Kunden an die Plattformen gezahlt und sind nicht Teil der Vergütung, sofern nicht anders vereinbart.</p>
<h2>6. Nutzungsrechte</h2>
<p>{T}[Regelung zu Nutzungsrechten an Videos und Materialien]{E}</p>
<h2>7. Haftung</h2>
<p>{T}[Haftungsregelung]{E}</p>
<h2>8. Schlussbestimmungen</h2>
<p>Es gilt deutsches Recht. Gerichtsstand ist, soweit zulässig, München.</p>
""",
    },
}
