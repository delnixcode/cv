#!/bin/bash
# Génère le PDF du CV à partir du HTML avec WeasyPrint

# Vérifier et installer WeasyPrint si nécessaire
if ! command -v weasyprint &> /dev/null; then
    echo "WeasyPrint n'est pas installé. Installation en cours..."
    sudo apt update && sudo apt install -y weasyprint
    if [ $? -ne 0 ]; then
        echo "Erreur lors de l'installation de WeasyPrint."
        exit 1
    fi
    echo "WeasyPrint installé."
fi

HTML_FILE="cv_vancouver_aiot.html"
PDF_FILE="cv_vancouver_aiot.pdf"

cd "$(dirname "$0")"

weasyprint "$HTML_FILE" "$PDF_FILE"

echo "PDF généré : $PDF_FILE dans le dossier cv/"