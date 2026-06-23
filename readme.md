# 🌿 CannGuide

**Prozess-Guide · Dosierungsrechner · Chargenverwaltung · Prävention**

CannGuide ist eine umfassende, browserbasierte Web-App für die halbprofessionelle Herstellung von Cannabis-Edibles — von klassischer Cannabutter bis hin zu Vakuumdestillation und THCA-Kristallen. Schritt-für-Schritt Prozessführung mit Timern und Notizen, präziser Dosierungsrechner, Chargenverwaltung mit Diagrammen und ein vollständiger Präventions- und Sicherheitsbereich für den DACH-Raum. Alles in einer einzigen HTML-Datei, ohne Installation, ohne Backend.

**→ [Live auf GitHub Pages](https://quack-tic.github.io/cannguide)**

---

## Funktionen

### ☑ Interaktiver Prozess-Guide
Geführte Schritt-für-Schritt Herstellung für alle unterstützten Medien:
- **Checkboxen** zum Abhaken jedes Schritts
- **Countdown-Timer** pro Schritt (z.B. 40 Min Dekarboxylierung, 3h Infusion)
- **Notizfeld** pro Schritt — Beobachtungen während der Herstellung festhalten
- **Automatisches Speichern** als Charge am Ende, inkl. gesammelter Notizen

### 🌿 Unterstützte Medien

**Standard:**
| Medium | Besonderheit |
|---|---|
| Butter / Ghee / Kokosöl / Kokosfett | Alle Fette einzeln mit realistischen Effizienzwerten |
| MCT-Öl (C8/C10) | Für Kapseln, Tropfen und Gummies |
| Glycerin (VG) | Alkoholfrei, sublingual |
| Lecithin-Extraktion | Emulgierung, Freeze-Thaw Methode |
| Rosin / Live Resin | Lösungsmittelfrei, Hitzepresse, Fresh Press direkt in Edibles |
| Tinktur / QWET | Kaltextraktion bei –22°C empfohlen |
| FECO | Full Extract Cannabis Oil, Winterization |
| Hard Candy / Soft Candy / Gummies | Mit Emulgierungshinweisen |
| Backwaren | Hot-Spot-Prävention, Temperaturlimits |
| Kapseln | Gelatine und HPMC (vegan) |
| Exotisch | Honig, Schokolade, Getränke |

**⚗ Fortgeschritten (Laborequipment / Lösungsmittel):**
| Medium | Besonderheit |
|---|---|
| RSO | Rick Simpson Oil, Warmextraktion, Naphtha-Warnung |
| BHO / N-Butan (Closed Loop) | Shatter, Wax, Budder, Crumble, Live Resin, Sauce |
| THCA-Kristalle | Diamantmining, Heat Press, Zentrifugen-Separation |
| Vakuumdestillation | THC / CBD / CBG Fraktionierung, Siedepunkttabelle |

### ∑ Dosierungsrechner
- **Zwei Modi:** Rohmaterial (g × Wirkstoffgehalt %) oder Extrakt (g × Konzentrat %)
- **Extrakt-Typen:** Rosin, BHO Shatter/Wax/Öl, RSO, FECO, THCA-Kristalle, Destillat, Kief, eigener Wert
- **Träger-Konfiguration:** Trägermenge gesamt + Portionsgrösse → automatische Berechnung mg/Portion und Portionenanzahl
- **Plausibilitätsprüfung:** Erkennt unmögliche Verhältnisse (zu wenig Träger, physisch unmöglicher Wirkstoffgehalt pro Portion)
- **Effizienz-Voreinstellungen** je nach Medium (Butter 78%, Ghee 88%, Kokosöl 90%, Ethanol 92% usw.)
- **Intensitätsbewertung:** Niedrig / Mittel / Stark / Sehr stark
- Direkt als Charge speicherbar

### ⊡ Chargenverwaltung
- Chargen anlegen mit Name, Medium, Datum, Dosis, Portionen, Material, Rezept, Notizen
- Bearbeiten und löschen
- Export als JSON-Datei
- Chargen aus Guide oder Rechner automatisch übernehmen
- Daten werden im Browser (localStorage) gespeichert

### ⊞ Bibliothek
- **Lösungsmittel-Vergleich** mit Tabelle (Bindungskapazität, Eignung, Alkohol ja/nein)
- **Profi-Tricks:** Magnetrührer, Freeze-Thaw, Winterization, Terp Sauce zurückführen, Bloom verhindern
- **Dekarboxylierung:** Temperaturtabelle, Mason Jar, Sous-Vide
- **Troubleshooting:** Kein Effekt, Hot Spots, trübe Tinktur, klebrige Hard Candies
- **📖 Lexikon:** 17 Fachbegriffe mit Tags und Erklärungen (Shatter, Wax, Live Resin, HTFSE, Diamonds, Entourage-Effekt, Winterization, Purging, Closed Loop, Dekarb u.v.m.)

### ⛨ Prävention & Sicherheit
- **Dos & Don'ts:** Start Low Go Slow, sichere Lagerung, Risikogruppen, Wirkungsdauer
- **Bei OD / Panik:** Symptome, Erste-Hilfe-Schritte, 7-W-Notruf-Schema, Greening-Out-Protokoll
- **Sucht & Hilfe:** Fakten zu CUD, Warnzeichen, CUDIT-Hinweis, Harm Reduction
- **Anlaufstellen DACH:** Konkrete Nummern und Links für CH, DE, AT + internationale Ressourcen
- **Rechtliches:** CH (Pilotversuche), DE (CanG April 2024), AT (SMG) — mit Hinweis auf laufende Änderungen
- Notfallnummern immer direkt sichtbar auf den relevanten Tabs

### ⚙ Design-Anpassung
- 5 Farbschemata: Grün, Amber, Blau, Pink, Rot
- Hell- / Dunkel-Modus
- App-Titel anpassbar
- Alle Einstellungen werden im Browser gespeichert

---

## Sicherheitshinweise

> Diese App richtet sich an den DACH-Raum und berücksichtigt die aktuellen Rechtssituationen (Stand: Mitte 2025). Cannabis ist in vielen Regionen weiterhin illegal oder reguliert. Alle Informationen zu Herstellung, Dosierung und Konsum dienen ausschliesslich zu Bildungs- und Schadenminimierungszwecken.

**Materialhinweis:** Bei der Arbeit mit organischen Lösungsmitteln (Ethanol, N-Butan, Ether, Propanol) ausschliesslich **Glas oder Edelstahl** verwenden. Plastik- und Silikonmaterialien können bei längerem Kontakt mit diesen Substanzen Moleküle abgeben.

**QWET-Extraktion:** Für effektives Ausfallen von Wachsen und Lipiden wird **–22°C** empfohlen. Unterhalb von –18°C ist das Ausfallen kaum bis nicht beobachtbar.

---

## Installation & Nutzung

Die App besteht aus einer einzigen HTML-Datei (`index.html`) — keine Build-Tools, kein Node.js, kein Backend.

```bash
# Repository klonen
git clone https://github.com/quack-tic/edibles-workshop.git

# Direkt öffnen (lokal)
open index.html
```

### GitHub Pages aktivieren
1. Repository → Settings → Pages
2. Source: `main` Branch, `/ (root)`
3. App erreichbar unter `https://quack-tic.github.io/edibles-workshop`

### PWA installieren (Handy)
1. App im Mobile-Browser öffnen
2. **Android (Chrome):** Banner "Zum Startbildschirm hinzufügen" antippen, oder Menü → "App installieren"
3. **iOS (Safari):** Teilen-Symbol → "Zum Home-Bildschirm"
4. App erscheint mit eigenem Icon und läuft im Vollbild — auch offline verfügbar

### Offline-Nutzung
Nach dem ersten Aufruf cached der Service Worker alle Ressourcen. Die App funktioniert danach vollständig ohne Internetverbindung — ideal für die Küche.

---

## Technologie

- **Vanilla HTML / CSS / JavaScript** — keine Frameworks, keine Dependencies
- **Kein Backend, kein Server** — läuft vollständig im Browser
- **localStorage** für Chargen, Design-Einstellungen und App-Titel
- **CSS Custom Properties** für dynamisches Theming
- Getestet in Chrome, Firefox, Safari, Edge

---

## Projektstruktur

```
cannguide/
├── index.html          # Die komplette App
├── manifest.json       # PWA-Manifest (Name, Icon, Farben)
├── service-worker.js   # Offline-Caching
├── icons/
│   ├── icon-192.png    # App-Icon (192×192px)
│   └── icon-512.png    # App-Icon (512×512px)
└── README.md
```

> **Icons erstellen:** SVG-Datei auf [svgtopng.com](https://svgtopng.com) zu PNG konvertieren — einmal 192×192, einmal 512×512 exportieren.

---

## Geplante Erweiterungen

- [ ] Import von JSON-Chargen
- [ ] Druckansicht für Chargenberichte
- [ ] Rezept-Vorlagen speichern und wiederverwenden
- [ ] Mehrsprachigkeit (EN, FR)
- [ ] PWA / Offline-Unterstützung (Service Worker)

---

## Mitmachen

Issues und Pull Requests sind willkommen. Bitte sachliche Korrekturen zu Prozessschritten, Effizienzwerten oder Sicherheitshinweisen als Issue melden.

---

## Lizenz

MIT License — frei verwendbar, veränderbar und verteilbar mit Namensnennung.

---

## Autor

Erstellt von **quack-tic** · [github.com/quack-tic](https://github.com/quack-tic)

> *Dieses Projekt ist ein Bildungs- und Harm-Reduction-Tool. Es ersetzt keine medizinische oder rechtliche Beratung.*
