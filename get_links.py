import json

link_base = "ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EP/EPMG"
link_suffix = ".dbc"
anos = range(2007, 2022)
meses = range(1, 13)

links = []

for ano in anos:
    for mes in meses:
        links.append(f"{link_base}{str(ano)[2:]}{str(mes).zfill(2)}{link_suffix}")

with open("links.json", "w") as links_file:
    json.dump(links, links_file)