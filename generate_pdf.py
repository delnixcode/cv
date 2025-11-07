#!/usr/bin/env python3
"""
Script Python pour générer un PDF à partir du CV HTML
Utilise Playwright pour un rendu de haute qualité
"""

import os
import sys
from pathlib import Path
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
    
    # Définir les chemins des fichiers
    current_dir = Path(__file__).parent
    html_file = current_dir / "cv_vancouver_aiot.html"
    pdf_file = current_dir / "cv_vancouver_aiot.pdf"
    
    print("🚀 Générateur de PDF pour CV")
    print("=" * 40)
    print(f"Fichier HTML : {html_file}")
    print(f"Fichier PDF  : {pdf_file}")
    print()
    
    # Générer le PDF
    success = generate_pdf_from_html(str(html_file), str(pdf_file))
    
    if success:
        print(f"\n✨ Le PDF a été généré avec succès !")
        print(f"📄 Vous pouvez maintenant ouvrir : {pdf_file}")
    else:
        print(f"\n💥 Échec de la génération du PDF")
        sys.exit(1)

if __name__ == "__main__":
    main()
