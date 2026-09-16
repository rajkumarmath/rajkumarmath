from pathlib import Path

OUTPUT = Path("assets/info-card.svg")

lines = [
    ("ROLE", "AI &amp; Data Science Engineer"),
    ("EDUCATION", "B.Tech — AI & Data Science"),
    ("UNIVERSITY", "REVA University"),
    ("FOCUS", "AI / ML / GenAI"),
    ("LANGUAGES", "Python / Java / SQL"),
    ("FRAMEWORKS", "FastAPI / React / Streamlit"),
    ("BUILDING", "AI Document Authenticity"),
    ("PROJECT", "Parkmate / Adethix AI"),
]

WIDTH = 600
ROW_HEIGHT = 34
HEIGHT = 100 + len(lines) * ROW_HEIGHT

svg = f'''<svg
xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<rect
x="5"
y="5"
width="{WIDTH - 10}"
height="{HEIGHT - 10}"
rx="14"
fill="#0d1117"
stroke="#30363d"
stroke-width="2"/>

<text
x="30"
y="45"
font-family="monospace"
font-size="24"
font-weight="bold"
fill="#58a6ff">
rajkumar@github
</text>

<line
x1="30"
y1="62"
x2="{WIDTH - 30}"
y2="62"
stroke="#30363d"/>

'''

for i, (key, value) in enumerate(lines):

    y = 95 + i * ROW_HEIGHT
    delay = i * 0.15

    svg += f'''
<g opacity="0">

<text
x="30"
y="{y}"
font-family="monospace"
font-size="16"
font-weight="bold"
fill="#79c0ff">
{key}
</text>

<text
x="175"
y="{y}"
font-family="monospace"
font-size="16"
fill="#c9d1d9">
{value}
</text>

<animate
attributeName="opacity"
from="0"
to="1"
dur="0.5s"
begin="{delay}s"
fill="freeze"/>

</g>
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

print(f"Created {OUTPUT}")