"""Baut die Pages-Seite aus app/ nach _site/.

app/index.html ist ohne Dokumentrahmen geschrieben (für das Claude-Artifact).
Für GitHub Pages bekommt sie Doctype, Kopfzeilen für die App-Installation
(Manifest, Symbole) und die Anmeldung des Offline-Moduls (sw.js).

Aufruf: python3 tools/build_site.py [Versionskennung]
"""
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / "app"
SITE = ROOT / "_site"
VERSION = sys.argv[1] if len(sys.argv) > 1 else "lokal"

src = (APP / "index.html").read_text(encoding="utf-8")
src = re.sub(r'^<meta charset="utf-8">\n<title>.*?</title>\n', "", src)
links, rest = src.split("<style>", 1)
style, body = rest.split("</style>", 1)

head = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Qui est-ce ?</title>
<meta name="author" content="Jan Wilsker-Wiesen">
<meta name="description" content="Jeu de devinettes pour l'Unité 1 de Découvertes 2 : les vêtements, les couleurs et le look. Un jeu de Jan Wilsker-Wiesen, créé avec Claude.">
<meta name="theme-color" content="#2d4c9e">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Qui est-ce ?">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icons/favicon-32.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
{links.strip()}
<style>
:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}
body{{font-size:16px}}
img{{max-width:100%}}
{style.strip()}
</style>
</head>
<body>"""

register = """
<script>
// Fonctionne aussi sans Internet après la première visite
if('serviceWorker' in navigator){window.addEventListener('load',()=>{navigator.serviceWorker.register('sw.js').catch(()=>{})})}
</script>
</body>
</html>
"""

if SITE.exists():
    shutil.rmtree(SITE)
SITE.mkdir()
(SITE / "index.html").write_text(head + body.rstrip() + register, encoding="utf-8")
shutil.copytree(APP / "icons", SITE / "icons")
shutil.copy(APP / "manifest.webmanifest", SITE)
# neue Versionskennung, damit die iPads die neue Fassung laden
sw = (APP / "sw.js").read_text(encoding="utf-8").replace("__VERSION__", VERSION)
(SITE / "sw.js").write_text(sw, encoding="utf-8")
(SITE / ".nojekyll").touch()
print(f"_site/ gebaut (Version {VERSION})")
