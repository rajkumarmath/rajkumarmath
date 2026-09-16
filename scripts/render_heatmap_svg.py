import json
from pathlib import Path

DATA = Path("data/contributions.json")
OUTPUT = Path("assets/contrib-heatmap.svg")

WIDTH = 900
HEIGHT = 180

CELL = 12
GAP = 4

COLORS = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353"
]

with open(DATA, "r", encoding="utf-8") as f:
    days = json.load(f)

days = days[-371:]

while len(days) < 371:
    days.insert(
        0,
        {
            "date": "",
            "level": 0
        }
    )

svg = f'''<svg
xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<rect
width="100%"
height="100%"
rx="12"
fill="#0d1117"/>

<text
x="30"
y="30"
font-family="monospace"
font-size="18"
fill="#c9d1d9">
GitHub Contributions
</text>
'''

for index, day in enumerate(days):

    week = index // 7
    weekday = index % 7

    x = 30 + week * (CELL + GAP)
    y = 50 + weekday * (CELL + GAP)

    level = int(day.get("level", 0))

    color = COLORS[
        min(level, len(COLORS) - 1)
    ]

    delay = index * 0.004

    svg += f'''
<rect
x="{x}"
y="{y}"
width="{CELL}"
height="{CELL}"
rx="3"
fill="{color}"
opacity="0">

<animate
attributeName="opacity"
from="0"
to="1"
dur="0.25s"
begin="{delay}s"
fill="freeze"/>

</rect>
'''

svg += f'''
<text
x="30"
y="{HEIGHT - 18}"
font-family="monospace"
font-size="12"
fill="#8b949e">
Less
</text>

<text
x="800"
y="{HEIGHT - 18}"
font-family="monospace"
font-size="12"
fill="#8b949e">
More
</text>

</svg>
'''

OUTPUT.parent.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT.write_text(
    svg,
    encoding="utf-8"
)

print(f"Created: {OUTPUT}")