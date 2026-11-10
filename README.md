#  QR Code Generator - Python

Générateur de codes QR avancé en Python avec options multiples et formats variés.

---

##  Fonctionnalités

-  **2 modes d'utilisation** : Simple ou Avancé
-  **3 formats** : PNG, SVG (vectoriel), ASCII (texte)
- **4 niveaux de correction d'erreur** : L (7%), M (15%), Q (25%), H (30%)
- **Customization** : Taille, couleurs, bordures
-  **Auto-ajustement** : Détection automatique de la version QR
-  **Informations détaillées** : Dimensions, capacité, niveau de correction

---

##  Installation

### Prérequis
- Python 3.6+
- pip

### Installation rapide

```bash
pip install qrcode[pil]
```

---

##  Utilisation

### Mode 1 : Simple (Interactif)

```bash
python qr_code_modification.py
```

Tapez `1` puis entrez :
- Le lien/texte à encoder
- Le niveau de correction (L/M/Q/H)
- Le format (1=PNG, 2=SVG, 3=ASCII)

### Mode 2 : Exemples Automatiques

```bash
python qr_code_modification.py
```

Tapez `2` pour voir 4 exemples :
1. **Version fixe** (v10) - QR code de taille prédéfinie
2. **Auto-ajusté** - Détection automatique
3. **Multi-formats** - Export PNG + SVG + ASCII
4. **Correction maximale** - Meilleure récupération d'erreurs

---

##  Niveaux de Correction

| Niveau | Récupération | Utilisation |
|--------|------------|-----------|
| **L** | 7% | Codes simples |
| **M** | 15% | Recommandé  |
| **Q** | 25% | Environnements difficiles |
| **H** | 30% | Qualité maximale |

---

##  Formats Disponibles

| Format | Type | Avantage |
|--------|------|---------|
| **PNG** | Image raster | Universel, facile à utiliser |
| **SVG** | Image vectorielle | Scalable sans perte de qualité |
| **ASCII** | Texte | Visualisation en console |

---

##  Exemples de Code

### Création simple
```python
from qr_code_modification import QRCodeGenerator

qr = QRCodeGenerator(data='https://google.com')
qr.save_png('mon_qr.png')
```

### Avec options
```python
qr = QRCodeGenerator(
    data='https://exemple.com',
    error_correction='H',  # Correction maximale
    box_size=15,           # Taille des modules
    border=4               # Bordure
)
qr.save_svg('mon_qr.svg')
```

### Infos du QR code
```python
info = qr.get_info()
print(info)
# {'version': 1, 'dimensions': '21×21 modules', 'error_correction': 'H', 'data_length': 19}
```

---

##  Fichiers du Projet

- `qr_code_modification.py` - **Version avancée** avec classe QRCodeGenerator
- `qr_code.py` - Version simple de démarrage
- `qrcode.txt` - Exemple d'export ASCII

---

##  Licence

MIT License 

---

##  Auteur
Créé par YANN © 2026

