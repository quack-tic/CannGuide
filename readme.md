# 🌿 CannGuide

**Prozess-Guide · Dosierungsrechner · Chargenverwaltung · Prävention**

> ⚠️ **Dieses Projekt befindet sich in aktiver Entwicklung.** Features, Inhalte und Struktur ändern sich laufend. Das Projekt ist bereits online — für Feedback, Vorstellungszwecke und erste Nutzung.

**→ [Live auf GitHub Pages](https://quack-tic.github.io/cannguide)**

---

## Was ist CannGuide?

CannGuide ist eine browserbasierte Progressive Web App (PWA) für die Herstellung, Dosierung und den sicheren Umgang mit Cannabis-Edibles im DACH-Raum. Alles läuft vollständig im Browser — keine Installation, kein Backend, keine Abhängigkeiten. Die gesamte App steckt in einer einzigen HTML-Datei.

Der Fokus liegt auf zwei Dingen: **praxisnaher Prozessführung** (von Cannabutter bis Vakuumdestillation) und **verantwortungsvollem Konsum** (Dosierung, Prävention, Harm Reduction).

---

## Zwei Ausrichtungen

Das Projekt entwickelt sich in zwei parallele Versionen:

### 🌐 Full PWA — GitHub Pages
Die vollständige Version mit allen Inhalten, direkt über den Browser nutzbar:
- Alle Herstellungsmethoden inkl. fortgeschrittener Extraktion (BHO, QWET, RSO, FECO, THCA-Kristalle, Vakuumdestillation)
- Schritt-für-Schritt Prozessführung mit Timern und Notizen
- Vollständiger Dosierungsrechner mit Körpergewicht, Toleranz, Geschlecht/Metabolismus
- Chargenverwaltung mit Diagrammen und Export
- Prävention & Harm Reduction für den DACH-Raum

**→ [quack-tic.github.io/cannguide](https://quack-tic.github.io/cannguide)**

### 🤖 Store-Lite — Google Play (geplant)
Eine angepasste Version für den Google Play Store via Trusted Web Activity (TWA):
- Ausschliesslich lebensmitteltaugliche Methoden (Butter, Öle, Gummies, Backwaren, Kapseln usw.)
- Fortgeschrittene Extraktionsguides entfallen (lösungsmittel- und laborbasierte Methoden)
- Gleicher Dosierungsrechner, Chargenverwaltung und Prävention
- Geobeschränkt auf CH + DE
- Onboarding mit Alterstor und Präventionshinweis

---

## Aktueller Stand

### ✅ Fertig
- Interaktiver Prozess-Guide für alle Methoden (Standard + Fortgeschritten)
- Dosierungsrechner mit Körpergewicht, Toleranzstufen, Geschlecht/Metabolismus-Toggle, Inhalationsrechner
- Chargenverwaltung mit Charts, Vergleich, Export und Print
- Bibliothek: Lösungsmittelvergleich, Lexikon, Dekarboxylierung, Troubleshooting, Profi-Tricks
- Prävention: Dos & Don'ts, OD-Protokoll, Sucht & Hilfe, Anlaufstellen DACH, Rechtslage CH/DE/AT
- PWA (Offline-Nutzung via Service Worker, installierbar auf Android & iOS)
- DE/EN Sprachumschalter (Basis)
- Design-Einstellungen: Farbthemen, Hell-/Dunkel-Modus

### 🔧 In Arbeit / Geplant
- Prävention: Inhalations-spezifische Inhalte (Lungengesundheit, Dabbing-Temperaturen, Tabakbeimischung)
- Lexikon: Erweiterung mit Inhalationsbegriffen
- Kosten & Zeitaufwand pro Methode
- Onboarding-Tour für Erstnutzer
- Play Store: TWA-Integration via bubblewrap CLI, Digital Asset Links, Geo-Beschränkung
- Community-Rezeptteilen (Phase 3, evaluiert: Supabase / GitHub Issues / Netlify Forms)
- Vollständige DE/EN Übersetzung (zum Abschluss)

---

## Funktionen im Überblick

### ☑ Prozess-Guide
Geführte Schritt-für-Schritt Herstellung mit Checkboxen, Countdown-Timern und Notizfeldern pro Schritt. Abgeschlossene Guides lassen sich direkt als Charge speichern.

**Standard-Methoden:** Butter, Ghee, Kokosöl, MCT-Öl, Glycerin, Lecithin, Rosin, Tinktur/QWET, FECO, Hard/Soft Candy, Gummies, Backwaren, Kapseln, Honig, Schokolade, Getränke

**⚗ Fortgeschritten:** RSO, BHO/N-Butan (Closed Loop), THCA-Kristalle, Vakuumdestillation

### ∑ Dosierungsrechner
Zwei Modi (Rohmaterial / Extrakt), Effizienz-Voreinstellungen je Medium, Körpergewicht, Toleranz, Geschlecht/Metabolismus, Inhalationstab, Intensitätsbewertung, Plausibilitätsprüfung.

### ⊡ Chargenverwaltung
Chargen anlegen, bearbeiten, vergleichen. Export als JSON. Diagramme: Dosisverteilung, Medien, Portionen. Automatische Übernahme aus Guide und Rechner.

### ⊞ Bibliothek & Lexikon
Lösungsmittelvergleich, Dekarboxylierungstabellen, Troubleshooting, Profi-Tricks, Fachbegriff-Lexikon mit Tags und Erklärungen.

### ⛨ Prävention & Harm Reduction
Dos & Don'ts, Greening-Out-Protokoll, Sucht & Hilfe, konkrete Anlaufstellen für CH / DE / AT, Rechtslage DACH (Stand 2025). Notfallnummern immer direkt sichtbar.

---

## Technologie

- **Vanilla HTML / CSS / JavaScript** — keine Frameworks, keine Build-Tools
- **Eine einzige HTML-Datei** — vollständig portabel
- **localStorage** für Chargen, Einstellungen und Titel
- **Service Worker** für Offline-Nutzung
- **Chart.js** für Diagramme (CDN)
- PWA-konform: installierbar, offline-fähig, Manifest

---

## Installation & Nutzung

```bash
# Repository klonen
git clone https://github.com/quack-tic/cannguide.git

# Direkt im Browser öffnen
open index.html

# Oder lokal mit Server (empfohlen für PWA-Features)
npx serve .
```

**PWA installieren:**
- Android (Chrome): Menü → „App installieren" oder „Zum Startbildschirm"
- iOS (Safari): Teilen → „Zum Home-Bildschirm"

---

## Sicherheitshinweis

> CannGuide richtet sich an den DACH-Raum und berücksichtigt die aktuellen Rechtssituationen (Stand: Mitte 2025). Alle Informationen zu Herstellung, Dosierung und Konsum dienen ausschliesslich zu Bildungs- und Schadenminimierungszwecken. Das Tool ersetzt keine medizinische oder rechtliche Beratung.

Bei der Arbeit mit organischen Lösungsmitteln ausschliesslich Glas oder Edelstahl verwenden. Für QWET-Extraktion werden –22°C empfohlen.

---

## Mitmachen

Feedback, Korrekturen zu Prozessschritten, Effizienzwerten oder Sicherheitshinweisen als [Issue](https://github.com/quack-tic/cannguide/issues) melden. Pull Requests willkommen.

---

## Lizenz

MIT License — frei verwendbar und veränderbar mit Namensnennung.

---

## Autor

Erstellt von **quack-tic** · [github.com/quack-tic](https://github.com/quack-tic)
