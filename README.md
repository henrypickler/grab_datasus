# Downloading and extracting data from DATASUS

First gather a list of download links from datasus. We provided one for "Equipes de saúde em MG de 2017 a 2021" as example.

- Run `python download_data.py` in this folder to download every `.dbc` file into `bases_raw`.
- Then `python uncompress_data.py` to decompress every file into the directory `bases_descomprimidas`.

You're all done!