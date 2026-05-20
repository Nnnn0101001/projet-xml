import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom

print("Lecture du fichier CSV...")

# Lire le fichier resultats_ml.csv
with open("resultats_ml.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    donnees = list(lecteur)

print(f"{len(donnees)} lignes trouvées")

# Créer la racine XML
racine = ET.Element("AnalyseML")

# Ajouter les résultats
for ligne in donnees:
    resultat = ET.SubElement(racine, "Resultat")
    
    for cle, valeur in ligne.items():
        # Remplacer espaces par _
        nom_balise = cle.replace(" ", "_")
        ET.SubElement(resultat, nom_balise).text = valeur
xml_str = minidom.parseString(ET.tostring(racine)).toprettyxml(indent="  ")

with open("resultats.xml", "w", encoding="utf-8") as f:
    f.write(xml_str)

print("Fichier XML créé avec succès : resultats.xml")
# ── Validation XSD ──────────────────────────────────────────
from lxml import etree

print("\nValidation XSD en cours...")
schema_doc = etree.parse("schema.xsd")
schema = etree.XMLSchema(schema_doc)
xml_doc = etree.parse("resultats.xml")

if schema.validate(xml_doc):
    print("✓ XML valide selon le schéma XSD !")
else:
    print("✗ Erreurs de validation :")
    for error in schema.error_log:
        print(f"   → {error.message}")