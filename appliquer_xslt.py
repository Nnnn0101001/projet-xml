"""
appliquer_xslt.py  –  Partie 3 : Transformation XML → HTML via XSLT
Utilise  : lxml
Usage    : python appliquer_xslt.py
"""

from lxml import etree


XML_FILE  = "resultats.xml"
XSLT_FILE = "transform.xslt"
HTML_OUT  = "report.html"


print(f"Lecture de {XML_FILE}...")
xml_doc = etree.parse(XML_FILE)


print(f"Chargement de {XSLT_FILE}...")
xslt_doc  = etree.parse(XSLT_FILE)
transform = etree.XSLT(xslt_doc)


print("Application de la transformation XSLT...")
html_result = transform(xml_doc)


with open(HTML_OUT, "wb") as f:
    f.write(etree.tostring(html_result, pretty_print=True, method="html"))

print(f"\nRapport généré avec succès : {HTML_OUT}")
print("  Ouvrez report.html dans votre navigateur pour voir le résultat.")
