from pathlib import Path
from PIL import Image

INPUT = Path("source-prepped.png")
OUTPUT = Path("assets/rajkumar-ascii.svg")

WIDTH = 90
FONT_SIZE = 7
LINE_HEIGHT = 8

RAMP = "@%#*+=-:. "


def main():

    if not INPUT.exists():
        print("ERROR: source-prepped.png not found.")
        print("Run prep_photo.py first.")
        return

    img = Image.open(INPUT).convert("L")

    aspect_ratio = img.height / img.width

    height = max(
        1,
        int(WIDTH * aspect_ratio * 0.5)
    )

    img = img.resize(
        (WIDTH, height)
    )

    pixels = img.load()

    rows = []

    for y in range(height):

        row = []

        for x in range(WIDTH):

            brightness = pixels[x, y]

            index = int(
                brightness / 255 *
                (len(RAMP) - 1)
            )

            row.append(RAMP[index])

        rows.append(
            "".join(row)
        )

    svg_width = WIDTH * FONT_SIZE
    svg_height = height * LINE_HEIGHT

    svg = f'''<svg
xmlns="http://www.w3.org/2000/svg"
width="{svg_width}"
height="{svg_height}"
viewBox="0 0 {svg_width} {svg_height}">

<rect
width="100%"
height="100%"
fill="#0d1117"/>

<style>
.ascii {{
    font-family: monospace;
    font-size: {FONT_SIZE}px;
    fill: #58a6ff;
}}
</style>
'''

    for i, row in enumerate(rows):

        escaped = (
            row
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

        y = (i + 1) * LINE_HEIGHT
        delay = i * 0.06

        svg += f'''
<text
class="ascii"
x="0"
y="{y}"
opacity="0">{escaped}

<animate
attributeName="opacity"
from="0"
to="1"
dur="0.12s"
begin="{delay:.2f}s"
fill="freeze"/>

</text>
'''

    svg += "</svg>"

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT.write_text(
        svg,
        encoding="utf-8"
    )

    print(f"Created: {OUTPUT}")


if __name__ == "__main__":
    main()