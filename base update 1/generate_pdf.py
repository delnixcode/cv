#!/usr/bin/env python3
"""
Script Python pour générer un PDF à partir du CV HTML
Utilise Playwright pour un rendu de haute qualité
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

# Vérifier et installer les dépendances si nécessaire
def check_and_install_dependencies():
    """Vérifie et installe Playwright si nécessaire"""
    try:
        import playwright
        print("Playwright est déjà installé.")
    except ImportError:
        print("Playwright n'est pas installé. Installation en cours...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
            print("Playwright installé. Installation de Chromium...")
            subprocess.check_call(["playwright", "install", "chromium"])
            print("Chromium installé.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'installation : {e}")
            sys.exit(1)

# Importer Playwright après vérification
check_and_install_dependencies()
from playwright.sync_api import sync_playwright

def generate_pdf_from_html(html_file, output_file):
    """
    Génère un PDF à partir d'un fichier HTML
    
    Args:
        html_file (str): Chemin vers le fichier HTML
        output_file (str): Chemin de sortie pour le PDF
    """
    
    # Vérifier que le fichier HTML existe
    if not os.path.exists(html_file):
        print(f"Erreur : Le fichier {html_file} n'existe pas")
        return False
    
    try:
        with sync_playwright() as p:
            print("Démarrage du navigateur...")
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Convertir le chemin en URL file://
            html_path = os.path.abspath(html_file)
            file_url = f"file://{html_path}"
            
            print(f"Chargement de {html_file}...")
            page.goto(file_url)
            
            # Attendre que la page soit complètement chargée
            page.wait_for_load_state('networkidle')
            
            print("Génération du PDF...")
            # Configuration PDF optimisée pour un CV
            page.pdf(
                path=output_file,
                format='A4',
                margin={
                    'top': '0px',
                    'bottom': '0px', 
                    'left': '0px',
                    'right': '0px'
                },
                print_background=True,  # Inclure les arrière-plans (important pour votre sidebar grise)
                prefer_css_page_size=True
            )
            
            browser.close()
            print(f"✅ PDF généré avec succès : {output_file}")
            return True
            
    except Exception as e:
        print(f"❌ Erreur lors de la génération du PDF : {e}")
        print("Assurez-vous que Playwright est correctement installé avec:")
        print("playwright install chromium")
        return False

def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description="Génère un PDF à partir d'un fichier HTML de CV.")
    parser.add_argument("html_file", help="Chemin du fichier HTML source")
    parser.add_argument("pdf_file", help="Chemin du fichier PDF cible")
    args = parser.parse_args()

    print("🚀 Générateur de PDF pour CV")
    print("=" * 40)
    print(f"Fichier HTML : {args.html_file}")
    print(f"Fichier PDF  : {args.pdf_file}")
    print()
    success = generate_pdf_from_html(args.html_file, args.pdf_file)
    if success:
        print(f"\n✨ Le PDF a été généré avec succès !")
        print(f"📄 Vous pouvez maintenant ouvrir : {args.pdf_file}")
    else:
        print(f"\n💥 Échec de la génération du PDF")
        sys.exit(1)

if __name__ == "__main__":
    main()
