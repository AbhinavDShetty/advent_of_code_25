import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from typing import List

load_dotenv()

SESSION = os.getenv("AOC_SESSION")
YEAR = int(os.getenv("YEAR", 2025))

HEADERS = {
    "User-Agent": "advent-of-code-runner"
}

def fetch_real_input(day: int) -> str:
    if not SESSION:
        raise RuntimeError("AOC_SESSION missing in .env")

    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    r = requests.get(url, cookies={"session": SESSION}, headers=HEADERS)

    if r.status_code != 200:
        raise RuntimeError(f"Failed to fetch real input: {r.status_code}")

    return r.text.rstrip("\n")

def fetch_example_inputs(day: int) -> List[str]:
    url = f"https://adventofcode.com/{YEAR}/day/{day}"
    r = requests.get(url, cookies={"session": SESSION} if SESSION else None, headers=HEADERS)

    if r.status_code != 200:
        raise RuntimeError(f"Failed to fetch puzzle page: {r.status_code}")

    soup = BeautifulSoup(r.text, "html.parser")

    blocks = []

    for pre in soup.find_all("pre"):
        code = pre.find("code")
        text = code.get_text() if code else pre.get_text()
        blocks.append(text.rstrip("\n"))

    if not blocks:
        raise RuntimeError("No example inputs found on puzzle page!")

    return blocks
