# Booklet Imposer

A tool that converts a regular PDF into an imposed booklet layout for double-sided printing.

**Try it online:** [https://ansapple.github.io/booklet-imposer/](https://ansapple.github.io/booklet-imposer/)

## Requirements

- Python 3
- pypdf library
- flask (for web interface)

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Web Interface

1. Start the server:
```bash
source venv/bin/activate
python app.py
```

2. Open http://127.0.0.1:5000 in your browser

3. Drag and drop a PDF or click to browse

4. Click "Convert to Booklet" - the converted PDF downloads automatically

### Command Line

```bash
source venv/bin/activate
python3 booklet_imposer.py input.pdf output.pdf
```

Example:
```bash
python3 booklet_imposer.py document.pdf booklet.pdf
```

**Tip:** Run `deactivate` when done to exit the virtual environment.

## How It Works

1. Pads the document to a multiple of 4 pages (required for booklet folding)
2. Arranges pages in booklet order
3. Creates double-wide pages with two original pages side-by-side
4. Rotates back pages 180° for correct duplex orientation

## Printing Instructions

1. Print the output PDF double-sided (duplex)
2. No special flip settings needed - the script handles page rotation automatically
3. Fold the printed sheets in half
4. Pages will be in correct reading order

## Author

Created by [Hee1ko](https://github.com/Hee1ko)
