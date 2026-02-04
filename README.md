# Booklet Imposer

Convert any PDF into an imposed booklet layout for double-sided printing.

## Option 1: Use Online (Recommended)

**[https://ansapple.github.io/booklet-imposer/](https://ansapple.github.io/booklet-imposer/)**

1. Open the link above
2. Drag and drop your PDF (or click to browse)
3. Click "Convert to Booklet"
4. Download starts automatically

All processing happens in your browser — your files never leave your device.

## Option 2: Run Locally

### Web Interface

```bash
# Setup (first time only)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run server
python app.py
```

Open http://127.0.0.1:5000 in your browser.

### Command Line

```bash
source venv/bin/activate
python3 booklet_imposer.py input.pdf output.pdf
```

## Printing Instructions

1. Print double-sided (duplex)
2. Fold the printed sheets in half
3. Staple along the fold
4. Pages will be in correct reading order

## How It Works

- Pads document to a multiple of 4 pages
- Arranges pages in booklet imposition order
- Creates double-wide spreads
- Rotates back pages 180° for correct duplex orientation

## Author

Created by [Hee1ko](https://github.com/Hee1ko)
