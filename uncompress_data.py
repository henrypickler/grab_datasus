import os
import glob

current_directory = os.getcwd()
input_dir = f"bases_raw"
output_dir = f"bases_descomprimidas"
for path in glob.glob('./bases_raw/*.dbc'):
    file = path.split('/')[-1]
    print(file)
    os.system(f"Rscript dbc2csv.R ./{input_dir}/ ./{output_dir}/ {file}")