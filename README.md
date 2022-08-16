# Downloading and extracting data from DATASUS

First gather the prefix for each link by going to `https://datasus.saude.gov.br/transferencia-de-arquivos/` and choosing your source. For example, to download "Equipes de saúde em MG de 2007 a 2021" we get an arbitrary link to extract the prefix, I got `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EP/EPMG2101.dbc` which I then remove the date and suffix and end up with `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EP/EPMG`. Then I

1) Put this prefix I got to `get_links.py` and run it. It should output a `links.json` file.
2) Run `python download_data.py` in this folder to download every `.dbc` file into `bases_raw`.
3) Then `python uncompress_data.py` to decompress every file into the directory `bases_descomprimidas`.

And you're done!