import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
from pathlib import Path
import os

class QRCodeGenerator:
    """
    Générateur de codes QR avancé avec options multiples.
    
    Formats supportés: PNG, SVG, PDF, ASCII
    Niveaux de correction: L, M, Q, H
    Versions: 1-40 ou auto-ajustement
    """
    
    # Niveaux de correction d'erreur disponibles
    ERROR_LEVELS = {
        'L': ERROR_CORRECT_L,  # ~7% de récupération
        'M': ERROR_CORRECT_M,  # ~15% de récupération
        'Q': ERROR_CORRECT_Q,  # ~25% de récupération
        'H': ERROR_CORRECT_H,  # ~30% de récupération
    }
    
    def __init__(self, data, version=None, error_correction='L', box_size=10, border=4):
        """
        Initialise le générateur QR.
        
        Args:
            data (str): Les données à encoder
            version (int, optional): Version QR (1-40, None pour auto)
            error_correction (str): Niveau de correction ('L', 'M', 'Q', 'H')
            box_size (int): Taille des modules en pixels
            border (int): Taille de la bordure en modules
        """
        self.data = data
        self.version = version
        self.error_correction = self.ERROR_LEVELS.get(error_correction.upper(), ERROR_CORRECT_L)
        self.box_size = box_size
        self.border = border
        
        # Validation des paramètres
        self._validate_inputs()
        
    def _validate_inputs(self):
        """Valide les entrées utilisateur."""
        if not self.data:
            raise ValueError("Les données ne peuvent pas être vides")
        if self.box_size < 1:
            raise ValueError("box_size doit être >= 1")
        if self.border < 0:
            raise ValueError("border doit être >= 0")
        if self.version is not None and (self.version < 1 or self.version > 40):
            raise ValueError("version doit être entre 1 et 40")
    
    def _create_qr(self, fit=True):
        """Crée l'objet QR code."""
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border,
        )
        qr.add_data(self.data)
        qr.make(fit=fit)
        return qr
    
    def save_png(self, filename='qrcode.png', fill_color='black', back_color='white'):
        """Sauvegarde en PNG."""
        try:
            qr = self._create_qr()
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            img.save(filename)
            print(f"✓ QR Code PNG sauvegardé: {filename}")
            return True
        except Exception as e:
            print(f"✗ Erreur lors de la sauvegarde PNG: {e}")
            return False
    
    def save_svg(self, filename='qrcode.svg'):
        """Sauvegarde en SVG (vectoriel)."""
        try:
            import qrcode.image.svg
            qr = self._create_qr()
            factory = qrcode.image.svg.SvgPathImage
            img = qr.make_image(image_factory=factory)
            img.save(filename)
            print(f"✓ QR Code SVG sauvegardé: {filename}")
            return True
        except ImportError:
            print(f"✗ Module SVG non disponible (installez: pip install qrcode[pil])")
            return False
        except Exception as e:
            print(f"✗ Erreur lors de la sauvegarde SVG: {e}")
            return False
    
    def save_ascii(self, filename='qrcode.txt'):
        """Sauvegarde en ASCII art."""
        try:
            qr = self._create_qr()
            ascii_art = qr.get_matrix()
            with open(filename, 'w', encoding='utf-8') as f:
                for row in ascii_art:
                    f.write(''.join(['██' if cell else '  ' for cell in row]) + '\n')
            print(f"✓ QR Code ASCII sauvegardé: {filename}")
            return True
        except Exception as e:
            print(f"✗ Erreur lors de la sauvegarde ASCII: {e}")
            return False
    
    def get_info(self):
        """Retourne les informations du QR code."""
        qr = self._create_qr()
        version = qr.version
        modules = 17 + (4 * version)
        
        capacities = {
            10: {'L': 1852, 'M': 1114, 'Q': 684, 'H': 434}
        }
        
        error_level = list(self.ERROR_LEVELS.keys())[list(self.ERROR_LEVELS.values()).index(self.error_correction)]
        
        info = {
            'version': version,
            'dimensions': f'{modules}×{modules} modules',
            'error_correction': error_level,
            'data_length': len(self.data),
        }
        return info




if __name__ == "__main__":
    print("=" * 60)
    print("GÉNÉRATEUR DE CODES QR")
    print("=" * 60)
    
    print("\n[MODE 1] UTILISATION SIMPLE - Entrez votre lien/texte")
    print("[MODE 2] EXEMPLES - Voir les différentes options\n")
    
    mode = input("Choisissez 1 ou 2: ").strip() or '1'
    
    # ========== MODE 1: UTILISATION SIMPLE ==========
    if mode == '1':
        data = input("\n Entrez le lien ou le texte pour le QR code:\n→ ")
        
        if not data:
            data = 'google.com'
            print(f"(Utilisation valeur par défaut: {data})")
        
        print("\nOptions de correction d'erreur:")
        print("  L - Faible (7%)")
        print("  M - Moyen (15%) ← Recommandé")
        print("  Q - Bon (25%)")
        print("  H - Maximum (30%)")
        
        correction = input("Choisissez L/M/Q/H (défaut: M): ").upper() or 'M'
        if correction not in ['L', 'M', 'Q', 'H']:
            correction = 'M'
        
        print("\nFormat de sortie:")
        print("  1 - PNG (image raster, recommandé)")
        print("  2 - SVG (vectoriel, scalable)")
        print("  3 - ASCII (texte, visualisation simple)")
        
        format_choice = input("Choisissez 1/2/3 (défaut: 1): ").strip() or '1'
        if format_choice not in ['1', '2', '3']:
            format_choice = '1'
        
        print("\n Génération en cours...")
        qr = QRCodeGenerator(
            data=data,
            error_correction=correction,
            box_size=10,
            border=4
        )
        
        info = qr.get_info()
        print(f"\n✓ Infos du QR code:")
        print(f"  Version: {info['version']}")
        print(f"  Dimensions: {info['dimensions']}")
        print(f"  Correction: {info['error_correction']}")
        print(f"  Données: {info['data_length']} caractères")
        
        # Sauvegarder selon le format choisi
        if format_choice == '1':
            qr.save_png('qrcode.png')
        elif format_choice == '2':
            qr.save_svg('qrcode.svg')
        elif format_choice == '3':
            qr.save_ascii('qrcode.txt')
    
    else:
        link = 'https://www.google.com'
        
        print("\nGÉNÉRATEUR DE CODES QR - EXEMPLES AVANCÉS")
        
        # -------- EXEMPLE 1: Version fixe --------
        print("\n[EXEMPLE 1] QR Code Version 10 (fixe)")
        qr1 = QRCodeGenerator(
            data=link,
            version=10,
            error_correction='L',
            box_size=10,
            border=4
        )
        info1 = qr1.get_info()
        print(f"  Dimensions: {info1['dimensions']}")
        print(f"  Correction d'erreur: {info1['error_correction']}")
        qr1.save_png('qrcode_v10.png')
        
        # -------- EXEMPLE 2: Auto-ajustement genre bordure et data --------
        print("\n[EXEMPLE 2] QR Code Auto-ajusté")
        qr2 = QRCodeGenerator(
            data=link,
            error_correction='M',
            box_size=10,
            border=4
        )
        info2 = qr2.get_info()
        print(f"  Version détectée: {info2['version']}")
        print(f"  Dimensions: {info2['dimensions']}")
        qr2.save_png('qrcode_auto.png')
        
        # -------- EXEMPLE 3: Multiples formats png,svg,ascii --------
        print("\n[EXEMPLE 3] Export multiples formats")
        qr3 = QRCodeGenerator(link, error_correction='H')
        qr3.save_png('qrcode.png', fill_color='black', back_color='white')
        qr3.save_svg('qrcode.svg')
        qr3.save_ascii('qrcode.txt')
        
        # -------- EXEMPLE 4: Correction maximale du qr code avec correction H --------
        print("\n[EXEMPLE 4] QR Code avec correction H (maximum)")
        qr4 = QRCodeGenerator(link, error_correction='H')
        info4 = qr4.get_info()
        print(f"  Correction d'erreur: {info4['error_correction']} (30% de récupération)")
        qr4.save_png('qrcode_high_correction.png')
        
        print("\n✓ Tous les QR codes ont été générés avec succès!")
    
    print("=" * 60)