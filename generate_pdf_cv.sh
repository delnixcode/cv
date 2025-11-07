#!/bin/bash
# Génère le PDF du CV à partir du HTML avec WeasyPrint

HTML_FILE="cv_vancouver_aiot.html"
PDF_FILE="cv_vancouver_aiot.pdf"

cd "$(dirname "$0")"

weasyprint "$HTML_FILE" "$PDF_FILE"

echo "PDF généré : $PDF_FILE dans le dossier cv/"