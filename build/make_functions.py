#!/usr/bin/env python

from urllib.parse import urlparse
from build.make_spreadsheets import emit_docs
from bs4 import BeautifulSoup

import sys

with open(sys.argv[1]) as f:
    html_doc = f.read()

url = sys.argv[2]
p = urlparse(sys.argv[2])
base_url = f"{p.scheme}//{p.netloc}"

soup = BeautifulSoup(html_doc, 'html.parser')

def description(cells):
    td = cells[3]
    for a in td.find_all("a"):
        if a.string.startswith("Learn more"):
            a.string.replace_with(f"\n\nLearn more: {base_url}{a['href']}")
    return td.get_text()

def emit_function(name, description):
    print(f"def {name}(*args) -> Function:")
    emit_docs(description, 4)
    print(f'    return Function("{name}", args)')
    print()


print(f"# Generated from names extracted from {url}")
print()
print(f"from gigamonkeys.formulas import Function")
print()

for table in soup.find_all("table"):
    cols = [th.get_text().lower() for th in table.thead.tr.find_all("th")]

    for tr in table.tbody.find_all("tr"):
        cells = [c for c in tr.children]
        name = cells[1].get_text().replace(".", "_")
        emit_function(name, description(cells))
