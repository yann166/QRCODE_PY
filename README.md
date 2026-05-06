# 🔲 QR Code Generator - Python

Générateur de codes QR avancé en Python avec options multiples et formats variés.

---

## ✨ Fonctionnalités

- ✅ **2 modes d'utilisation** : Simple ou Avancé
- ✅ **3 formats** : PNG, SVG (vectoriel), ASCII (texte)
- ✅ **4 niveaux de correction d'erreur** : L (7%), M (15%), Q (25%), H (30%)
- ✅ **Customization** : Taille, couleurs, bordures
- ✅ **Auto-ajustement** : Détection automatique de la version QR
- ✅ **Informations détaillées** : Dimensions, capacité, niveau de correction

---

## 📦 Installation

### Prérequis
- Python 3.6+
- pip

### Installation rapide

```bash
pip install qrcode[pil]
```

---

## 🚀 Utilisation

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

## 📊 Niveaux de Correction

| Niveau | Récupération | Utilisation |
|--------|------------|-----------|
| **L** | 7% | Codes simples |
| **M** | 15% | Recommandé 👍 |
| **Q** | 25% | Environnements difficiles |
| **H** | 30% | Qualité maximale |

---

## 🎨 Formats Disponibles

| Format | Type | Avantage |
|--------|------|---------|
| **PNG** | Image raster | Universel, facile à utiliser |
| **SVG** | Image vectorielle | Scalable sans perte de qualité |
| **ASCII** | Texte | Visualisation en console |

---

## 📝 Exemples de Code

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

## 📂 Fichiers du Projet

- `qr_code_modification.py` - **Version avancée** avec classe QRCodeGenerator
- `qr_code.py` - Version simple de démarrage
- `qrcode.txt` - Exemple d'export ASCII

---

## 📄 Licence

MIT License - Utilisez librement ! 📜

---

## 🤝 Auteur

Créé par ATZ Computers © 2026

## 📁 Project Structure

```
qr_code/
├── README.md                    # This file
├── qr_code.py                  # ✅ Simple version (3 lines)
├── qr_code_modification.py     # 🚀 Advanced version (QRCodeGenerator class)
└── qrcode.txt                  # Example ASCII output
```

### File Details

| File | Description |
|------|-------------|
| **qr_code.py** | Basic script to quickly create a QR code in PNG format |
| **qr_code_modification.py** | Complete class with advanced options and interactive modes |
| **qrcode.txt** | Example of a QR code in ASCII format |

---

## 🚀 Usage

### ✅ Option 1: Simple Version (Quick Start)

```bash
python qr_code.py
```

This script simply creates a QR code containing "yann24@gmail.com" and exports it to PNG.

**Code:**
```python
import qrcode

# Create a QR code object with the email data
img = qrcode.make('google.com')

# Save it as PNG image
img.save('qrcode.png')
```

### 🚀 Option 2: Advanced Version (Recommended)

```bash
python qr_code_modification.py
```

You have access to two interactive modes:

#### Mode 1: Interactive Mode (NEW with format selection!)
```
Choose 1 or 2: 1
📌 Enter the link or text for the QR code:
→ https://www.example.com

Error correction options:
  L - Low (7%)
  M - Medium (15%) ← Recommended
  Q - Good (25%)
  H - High (30%)

Choose L/M/Q/H (default: M): M

Output format:
  1 - PNG (raster image, recommended)
  2 - SVG (vector, scalable)
  3 - ASCII (text, simple visualization)

Choose 1/2/3 (default: 1): 1

✓ QR Code info:
  Version: 1
  Dimensions: 21×21 modules
  Correction: M
  Data: 26 characters

✓ Saved in: qrcode.png
```

#### Mode 2: Advanced Examples
Shows different configurations and export formats with auto-detection of parameters.

---

## 🎨 Features

### Export Formats
| Format | Advantages | Use Cases |
|--------|------------|-----------|
| **PNG** | Standard image, universally compatible | Web, printing, applications |
| **SVG** | Vector, scalable without quality loss | Responsive web, design |
| **ASCII** | Pure text, readable in terminal | Documentation, chat |

### Error Correction Levels

QR codes can be partially damaged and still remain readable thanks to error correction algorithms:

| Level | Recovery | Best For |
|-------|----------|----------|
| **L** | ~7% | QR codes in clean environments |
| **M** | ~15% | ⭐ General use (RECOMMENDED) |
| **Q** | ~25% | Printed QR codes, outdoor use |
| **H** | ~30% | Very harsh environments |

### Configurable Parameters

```python
QRCodeGenerator(
    data='my-text',             # Data to encode
    version=None,               # Version 1-40 (None = auto)
    error_correction='M',       # Level: L, M, Q, H
    box_size=10,               # Module size in pixels
    border=4                   # Border thickness in modules
)
```

---

## � Code Explanation

### Understanding the QRCodeGenerator Class

Here's a detailed breakdown of the main components:

#### 1. **Class Definition & Error Levels**

```python
class QRCodeGenerator:
    """Advanced QR code generator with multiple options."""
    
    # Dictionary mapping correction levels to constants
    ERROR_LEVELS = {
        'L': ERROR_CORRECT_L,  # ~7% recovery
        'M': ERROR_CORRECT_M,  # ~15% recovery
        'Q': ERROR_CORRECT_Q,  # ~25% recovery
        'H': ERROR_CORRECT_H,  # ~30% recovery
    }
```

**Explanation:**
- `ERROR_LEVELS` is a dictionary that stores error correction constants from the qrcode library
- Using a dictionary makes it easy to convert user input (like 'M') to library constants
- This is a common pattern for mapping user-friendly input to technical values

#### 2. **Constructor (`__init__`)**

```python
def __init__(self, data, version=None, error_correction='L', box_size=10, border=4):
    self.data = data                           # Store the text/URL to encode
    self.version = version                     # QR code size (1-40 or auto)
    self.error_correction = self.ERROR_LEVELS.get(
        error_correction.upper(),              # Convert input to uppercase
        ERROR_CORRECT_L                        # Default to 'L' if invalid
    )
    self.box_size = box_size                  # Size of each QR module in pixels
    self.border = border                      # Border thickness in modules
    self._validate_inputs()                   # Check all parameters are valid
```

**What each parameter does:**
- `data`: The actual content (email, URL, text)
- `version`: Determines QR size. `None` means auto-detect based on data length
- `error_correction`: How much the QR code can recover from damage
- `box_size`: How big each square is in pixels (10 = 10px per module)
- `border`: The white space around the QR code (standard is 4 modules)

#### 3. **Validation Method**

```python
def _validate_inputs(self):
    """Validates user inputs before creating QR code."""
    if not self.data:
        raise ValueError("Data cannot be empty")
    if self.box_size < 1:
        raise ValueError("box_size must be >= 1")
    if self.border < 0:
        raise ValueError("border must be >= 0")
    if self.version is not None and (self.version < 1 or self.version > 40):
        raise ValueError("version must be between 1 and 40")
```

**Why validation matters:**
- Catches errors early before trying to create the QR code
- Provides clear error messages to help users fix problems
- Prevents invalid combinations that would fail later

#### 4. **Creating the QR Object**

```python
def _create_qr(self, fit=True):
    """Creates the QR code object (doesn't save it yet)."""
    qr = qrcode.QRCode(
        version=self.version,
        error_correction=self.error_correction,
        box_size=self.box_size,
        border=self.border,
    )
    qr.add_data(self.data)                    # Add the data to encode
    qr.make(fit=fit)                          # Generate the QR pattern
    return qr
```

**Step-by-step:**
1. Create a QRCode object with parameters
2. Add the data (text/URL)
3. Generate the actual QR pattern
4. Return the object for further processing

#### 5. **Save Methods**

```python
def save_png(self, filename='qrcode.png', fill_color='black', back_color='white'):
    """Export to PNG (raster image)."""
    try:
        qr = self._create_qr()
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        print(f"✓ QR Code PNG saved: {filename}")
        return True
    except Exception as e:
        print(f"✗ Error saving PNG: {e}")
        return False
```

**Key concepts:**
- `try/except`: Catches any errors and prints helpful messages
- `make_image()`: Converts the QR data into an actual image
- `fill_color` / `back_color`: Allow customization (black/white by default)
- Returns `True`/`False` to indicate success

#### 6. **Information Method**

```python
def get_info(self):
    """Returns QR code information."""
    qr = self._create_qr()
    version = qr.version              # Version used (auto-detected if needed)
    modules = 17 + (4 * version)      # Calculate grid size (21x21 for v1, etc.)
    
    # Get the error correction level letter
    error_level = list(self.ERROR_LEVELS.keys())[
        list(self.ERROR_LEVELS.values()).index(self.error_correction)
    ]
    
    return {
        'version': version,
        'dimensions': f'{modules}×{modules} modules',
        'error_correction': error_level,
        'data_length': len(self.data),
    }
```

**The module calculation:**
- Version 1 = 17 + (4 × 1) = **21 × 21 modules**
- Version 10 = 17 + (4 × 10) = **57 × 57 modules**
- Version 40 = 17 + (4 × 40) = **177 × 177 modules**

---

## 📘 Examples

### Example 1: Simple Email in PNG
```python
from qr_code_modification import QRCodeGenerator

# Create a QR code for an email
qr = QRCodeGenerator(
    data='contact@example.com',
    error_correction='M'
)

# Save it as PNG
qr.save_png('my_email.png')
```

### Example 2: URL with High Correction
```python
# Create a URL QR code that can survive more damage
qr = QRCodeGenerator(
    data='https://www.example.com',
    error_correction='H',          # Maximum error correction
    box_size=15,                   # Larger modules (more visible)
    border=5                       # Thicker border
)

# Save with custom colors
qr.save_png('link.png', fill_color='blue', back_color='lightyellow')
```

### Example 3: Multiple Formats
```python
qr = QRCodeGenerator(data='My Text')

# Save in PNG
qr.save_png('code.png')

# Save in SVG (vector, scalable)
qr.save_svg('code.svg')

# Save in ASCII (text visualization)
qr.save_ascii('code.txt')

# Get info
info = qr.get_info()
print(f"Version: {info['version']}")
print(f"Dimensions: {info['dimensions']}")
```

### Example 4: Automatic Version Detection
```python
# Short data: auto-detects version 1
short_qr = QRCodeGenerator(data='Hi')
short_info = short_qr.get_info()
print(short_info['version'])  # Output: 1

# Long data: auto-detects higher version
long_qr = QRCodeGenerator(
    data='https://www.example.com/very/long/path?param=value&other=data'
)
long_info = long_qr.get_info()
print(long_info['version'])  # Output: 2 or higher
```

---

## 📊 Technical Specifications

### How QR Codes Work

1. **Data Encoding**: Text/URL is converted to binary data
2. **Modules**: Organized in a square grid (version 1 = 21×21, version 40 = 177×177)
3. **Error Correction**: Reed-Solomon codes add redundancy
4. **Position Markers**: 3 squares at corners for orientation
5. **Image Format**: Black and white pixels

### Data Capacity

Higher error correction means less data can be stored.

**Example (Version 10):**
- Correction L: Up to 1852 characters
- Correction M: Up to 1114 characters
- Correction Q: Up to 684 characters
- Correction H: Up to 434 characters

---

## 🔧 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'qrcode'"
```bash
pip install qrcode[pil]
```

### Error: "SVG not available"
Ensure PIL is installed:
```bash
pip install pillow
```

### QR code is too small/large
Adjust `box_size` (module size in pixels):
```python
QRCodeGenerator(data='...', box_size=20)  # Larger
```

---

## 📚 Additional Resources

- **qrcode Documentation**: https://github.com/lincolnloop/python-qrcode
- **ISO Specifications**: ISO/IEC 18004:2015 (QR Code specifications)
- **Reed-Solomon Codes**: Error correction algorithm

---

## 💡 Quick Tips

1. **For printed QR codes**: Use error correction 'Q' or 'H'
2. **For web**: Use 'SVG' format for better scalability
3. **For visibility**: Use `box_size=15` or higher
4. **For design**: Mix colors but ensure good contrast
5. **For reliability**: Always test scanning

---

## ✨ Project Notes

Built for learning QR code generation in Python. Perfect for creating:
- Contact information sharing
- URL shortening
- Event tickets
- Product labels
- Web applications

---

## 📝 License

This project is free to use and modify.

---

**Happy QR code generating!** 🎓YANN
