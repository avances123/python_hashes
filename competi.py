import pandas as pd
import time
import argparse



# Pillas las claves y busca cada una en el dict
def dict_scan(d):
    for key in d.keys():
        d[key]


# Pillo los argumentos
parser = argparse.ArgumentParser()
parser.add_argument('data_file')
parser.add_argument('--nrows',type=int)
args = parser.parse_args()

# Leo el csv en un DataFrame
print "Cargando %s ..." % args.data_file
raw_data = pd.io.parsers.read_csv(args.data_file,compression='gzip',sep="|",nrows=args.nrows)

# Creo otro dataframe con las columnas concatenadas
data = pd.DataFrame()
data['integers'] = (
	raw_data['id_modelo'].apply(str) + 
	raw_data['version'].apply(str) + 
	raw_data['variable'].apply(str) + 
	raw_data['nivel'].apply(str) + 
	raw_data['pasada'].apply(str)
).apply(int)


# creo un diccionario con los enteros
dict_i = dict.fromkeys(data.integers)

# Lo recorro y mido
start_time = time.time()
dict_scan(dict_i)
stop_time = time.time()
print "Recorridas %d claves en [%f] segundos" % (len(dict_i),stop_time - start_time)