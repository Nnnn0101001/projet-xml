"""
appliquer_xslt.py  –  Partie 3 : Transformation XML → HTML via XSLT
Utilise  : lxml
Usage    : python appliquer_xslt.py
"""

from lxml import etree

# ── Chemins des fichiers ──────────────────────────────────────
XML_FILE  = "resultats.xml"
XSLT_FILE = "transform.xslt"
HTML_OUT  = "report.html"

# ── Étape 1 : Chargement du fichier XML ──────────────────────
print(f"Lecture de {XML_FILE}...")
xml_doc = etree.parse(XML_FILE)

# ── Étape 2 : Chargement et compilation de la feuille XSLT ───
print(f"Chargement de {XSLT_FILE}...")
xslt_doc  = etree.parse(XSLT_FILE)
transform = etree.XSLT(xslt_doc)

# ── Étape 3 : Application de la transformation ───────────────
print("Application de la transformation XSLT...")
html_result = transform(xml_doc)

# ── Étape 4 : Écriture du rapport HTML ───────────────────────
with open(HTML_OUT, "wb") as f:
    f.write(etree.tostring(html_result, pretty_print=True, method="html"))

print(f"\nRapport généré avec succès : {HTML_OUT}")
print("  Ouvrez report.html dans votre navigateur pour voir le résultat.")
