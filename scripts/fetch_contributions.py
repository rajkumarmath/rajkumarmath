import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup

USERNAME = "rajkumarmath"

URL = f"https://github.com/users/{USERNAME}/contributions"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    URL,
    headers=headers,
    timeout=30
)

response.raise_for_status()

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

days = []

for rect in soup.select("td.ContributionCalendar-day"):

    date = rect.get("data-date")

    if not date:
        continue

    level = rect.get(
        "data-level",
        "0"
    )

    days.append({
        "date": date,
        "level": int(level)
    })

output = Path("data/contributions.json")

output.parent.mkdir(
    parents=True,
    exist_ok=True
)

output.write_text(
    json.dumps(
        days,
        indent=2
    ),
    encoding="utf-8"
)

print(
    f"Saved {len(days)} contribution days"
)