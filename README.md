# Booklet Imposer

A Python script that converts a regular PDF into an imposed booklet layout for double-sided printing.

## Requirements

- Python 3
- pypdf library

### Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or install directly:
```bash
pip install pypdf
```

## Usage

```bash
source venv/bin/activate
python3 booklet_imposer.py input.pdf output.pdf
```

### Example

```bash
python3 booklet_imposer.py document.pdf booklet.pdf
```

## How It Works

1. **Page Calculation**: Pads the document to a multiple of 4 pages (required for booklet folding)

2. **Page Ordering**: Arranges pages in booklet order where:
   - Sheet 1 front: pages [last, 1]
   - Sheet 1 back: pages [2, second-to-last]
   - Sheet 2 front: pages [second-to-last-2, 3]
   - And so on...

3. **Imposition**: Creates double-wide pages with two original pages side-by-side

4. **Back Page Rotation**: Rotates back pages (odd indices) 180° and swaps left/right positions to ensure correct orientation when printing duplex so that it doesn't require printer setting adjustments

## Printing Instructions

1. Print the output PDF double-sided (duplex)
2. No special flip settings needed - the script handles page rotation automatically
3. Fold the printed sheets in half
4. Pages will be in correct reading order



## Author

Created by [Hee1ko](https://github.com/Hee1ko)
