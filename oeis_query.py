#!/usr/bin/env python3
import sys
import urllib.parse

import click
import requests
from lxml import html

SEARCH_URL = "https://oeis.org/search?q={}&sort=&language=english&go=Search"


@click.command()
@click.argument("numbers", required=True, nargs=-1, type=int)
def cli(numbers):
    numbers = [str(num) for num in numbers]
    query = " ".join(numbers)
    query = urllib.parse.quote_plus(query)
    url = SEARCH_URL.format(query)
    headers = {
        "Content-Type": "text/html",
    }
    try:
        print("fetching oeis website...")
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print("Failure trying to access OEIS website")
        print("Try again in a few minutes")
        raise SystemExit(e)

    tree = html.fromstring(response.content)

    # Sequence name at xpath:
    # //html/body/center[2]/table/tbody/tr/td/table[X]/tbody/tr[3]/td/table/tbody/tr/td[3]
    table = tree.xpath("//html/body/center[2]/table[1]")[0]
    tables = table.xpath("tr/td/table")
    if len(tables) == 1:
        # If the only one means no sequence found
        print("No sequence match")
        sys.exit(0)

    for i, _ in enumerate(tables, 1):
        if i > 5:
            break
        sequence = tables[i].xpath("tr[3]/td/table[1]/tr/td[3]")[0].text
        print(i, "-", sequence.strip())
