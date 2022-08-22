# Downloading and extracting data from DATASUS

First gather the prefix for each link by going to `https://datasus.saude.gov.br/transferencia-de-arquivos/` and choosing your source. For example, to download "Equipes de saúde em MG de 2007 a 2021" we get an arbitrary link to extract the prefix, I got `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EP/EPMG2101.dbc` which I then remove the date and suffix and end up with `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EP/EPMG`. Then I

1) Put the prefix obtainded in `get_links.py`'s variable named `link_base` and run it. It should output a `links.json` file.
2) Run `python download_data.py` in this folder to download every `.dbc` file into the folder `bases_raw`.
3) Now that you've downloaded the data, run `python uncompress_data.py` to decompress every file from `.dbc` to `.csv` into the directory `bases_descomprimidas`.

And you're done!
