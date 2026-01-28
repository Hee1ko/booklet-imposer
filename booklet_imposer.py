#!/usr/bin/env python3
import sys
from pypdf import PdfReader, PdfWriter, Transformation, PageObject
from pypdf.generic import RectangleObject

def create_booklet(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    
    num_pages = len(reader.pages)
    total_pages = ((num_pages + 3) // 4) * 4
    
    # Get page dimensions
    first_page = reader.pages[0]
    width = float(first_page.mediabox.width)
    height = float(first_page.mediabox.height)
    
    # Build page order for booklet
    page_order = []
    sheets = total_pages // 4
    
    for sheet in range(sheets):
        # Front of sheet: last page (right), first page (left)
        back_num = total_pages - (sheet * 2)
        front_num = (sheet * 2) + 1
        page_order.append((back_num, front_num))  # right, left
        
        # Back of sheet: second page (left), second-to-last (right)
        second_num = (sheet * 2) + 2
        second_last_num = total_pages - (sheet * 2) - 1
        page_order.append((second_num, second_last_num))  # left, right
    
    # Create output
    writer = PdfWriter()
    
    for idx, (left_num, right_num) in enumerate(page_order):
        # Create double-wide page
        new_page = PageObject.create_blank_page(width=width * 2, height=height)
        new_page.mediabox = RectangleObject([0, 0, width * 2, height])
        
        # Back pages (odd indices) need 180° rotation and swapped positions
        is_back = idx % 2 == 1
        
        if is_back:
            # Rotate 180° and swap left/right for back side
            if right_num <= num_pages:
                right_page = reader.pages[right_num - 1]
                new_page.merge_transformed_page(right_page, Transformation().rotate(180).translate(tx=width, ty=height))
            if left_num <= num_pages:
                left_page = reader.pages[left_num - 1]
                new_page.merge_transformed_page(left_page, Transformation().rotate(180).translate(tx=width * 2, ty=height))
        else:
            # Front pages - normal orientation
            if left_num <= num_pages:
                left_page = reader.pages[left_num - 1]
                new_page.merge_page(left_page)
            if right_num <= num_pages:
                right_page = reader.pages[right_num - 1]
                new_page.merge_transformed_page(right_page, Transformation().translate(tx=width, ty=0))
        
        writer.add_page(new_page)
    
    with open(output_pdf, 'wb') as f:
        writer.write(f)
    
    print(f"✓ Created booklet: {output_pdf}")
    print(f"  Original pages: {num_pages}, Sheets to print: {len(page_order)}")
    print(f"  Print double-sided (flip on short edge) and fold in half")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 booklet_imposer.py input.pdf output.pdf")
        sys.exit(1)
    
    create_booklet(sys.argv[1], sys.argv[2])
