# Qui est-ce ?

Ein Ratespiel für den Französischunterricht (Découvertes 2, Unité 1, Atelier B): Kleidung, Farben und Aussehen. Die Schülerinnen und Schüler stellen Fragen auf Französisch, drehen Karten um und finden die geheime Person.

Ein Spiel von Jan Wilsker-Wiesen, erstellt mit Claude.

**Spielen:** https://wilsker-wiesen.github.io/qui-est-ce/ (im Browser; auf dem iPad über „Teilen → Zum Home-Bildschirm“ wie eine App, danach auch ohne Internet)

## Spielmodi

- **Zu zweit (2 iPads):** Beide geben denselben Spielcode ein und bekommen dieselben 24 Personen. Gefragt und geantwortet wird laut auf Französisch. Geantwortet wird immer mit *mon personnage*, damit *il / elle* nicht verrät, ob es ein Junge oder ein Mädchen ist.
- **Gegen den Computer:** Fragen aus Wortbausteinen bauen. Der Computer fragt zurück, die Antwort wird aus vier Sätzen gewählt. Falsche Antworten werden durchgestrichen und erklärt (*ne … pas de*, *les cheveux / les yeux*, Angleichung der Farbe), dann wird neu gewählt.

## Wortschatz

Aus dem Lektionsvokabular der Unité 1 (Schülerbuch S. 178–179) und dem Lektionstext (*pantalon baggy*, S. 18). Wörter, die im Buch blau als Ergänzung stehen, sind im Spiel mit „en plus“ markiert.

- **Kleidung:** casquette, lunettes, t-shirt, chemise, chemisier, pull, sweat-shirt, veste, anorak, robe, pantalon, pantalon baggy, jean, jupe, short, chaussettes, chaussures. Jedes Stück hat im Spiel ein kleines Symbol, damit sich ähnliche Stücke (chemise / chemisier) unterscheiden lassen.
- **Farben:** rouge, bleu, vert, jaune, noir, blanc, gris, orange, marron (mit Angleichung).
- **Aussehen:** les cheveux longs / courts / bruns / blonds / roux / noirs, les yeux bleus / verts / marron, un garçon / une fille.

## Verteilung der Merkmale

Die 24 Personen werden aus dem Spielcode erzeugt, aber nicht zufällig verteilt: 12 Jungen und 12 Mädchen, jede Haarfarbe kommt bei langen und bei kurzen Haaren vor, jede Augenfarbe bei Jungen und Mädchen je viermal, Brille, Mütze und Socken je sechsmal. Mädchen haben Wimpern, Ohrringe und rötliche Lippen, damit das Geschlecht auch bei kurzen Haaren eindeutig ist. Augen sind immer sichtbar (Mütze sitzt darüber, Brillengläser sind durchsichtig).

## Sprache

Anleitungen, Knöpfe und Hinweise lassen sich per Flagge zwischen Französisch und Deutsch umschalten (auf der Startseite pro Kasten, im Spiel für alles). Fragen und Antworten bleiben immer französisch.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `app/index.html` | das ganze Spiel in einer Datei, ohne Dokumentrahmen (so läuft es auch als Claude-Artifact) |
| `app/sw.js` | Offline-Modul; `__VERSION__` wird beim Veröffentlichen ersetzt |
| `app/manifest.webmanifest`, `app/icons/` | App-Name und Symbole für „Zum Home-Bildschirm“ |
| `tools/build_site.py` | baut `_site/` für GitHub Pages |
| `.github/workflows/pages.yml` | veröffentlicht bei jedem Push auf `main` automatisch |

Lokal ansehen: `python3 tools/build_site.py && python3 -m http.server -d _site`

Zweite Adresse (Claude-Artifact, gleiche Datei): https://claude.ai/artifact/JJJ7HA1C3hxABM4cVPViBf
