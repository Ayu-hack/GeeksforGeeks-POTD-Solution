import pyqrcode
import png
from pyqrcode import QRCode
import os

try:
    # Put link here 
    s = "your link here"

    # Generate QR code 
    url = pyqrcode.create(s)

    # Define the output directory
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Create and save the SVG file 
    svg_path = os.path.join(output_dir, "myqr.svg")
    url.svg(svg_path, scale=8)

    # Create and save the PNG file 
    png_path = os.path.join(output_dir, "myqr.png")
    url.png(png_path, scale=8)

    print("QR code generated successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
