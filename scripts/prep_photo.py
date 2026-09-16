from pathlib import Path
import sys

import cv2
import numpy as np
from PIL import Image
from rembg import remove


def main():
    if len(sys.argv) < 2:
        print("Usage: python prep_photo.py source-photo.jpeg")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"ERROR: File not found: {input_path}")
        sys.exit(1)

    print(f"Loading: {input_path}")

    with open(input_path, "rb") as f:
        input_bytes = f.read()

    print("Removing background...")

    output_bytes = remove(input_bytes)

    temp_path = Path("source-nobg.png")
    temp_path.write_bytes(output_bytes)

    print("Processing image...")

    image = Image.open(temp_path).convert("RGBA")

    background = Image.new(
        "RGBA",
        image.size,
        (255, 255, 255, 255)
    )

    background.alpha_composite(image)

    rgb = np.array(background.convert("RGB"))

    gray = cv2.cvtColor(
        rgb,
        cv2.COLOR_RGB2GRAY
    )

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    output_path = Path("source-prepped.png")

    Image.fromarray(enhanced).save(output_path)

    print()
    print("SUCCESS!")
    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()