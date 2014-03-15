import pandas as pd
import time
import argparse
from multiprocessing import Pool



# Pillas las claves y busca cada una en el dict
def dict_scan(d):
    for key in d.keys():
        d[key]









def read_file(line):
	#print line
	return int(''.join(line.rstrip('\n').split('|'))[:-1])

# Pillo los argumentos
parser = argparse.ArgumentParser()
parser.add_argument('data_file')
parser.add_argument('--nrows',type=int)
args = parser.parse_args()

# Leo el csv en un DataFrame
print "Cargando %s ..." % args.data_file
ints = []
pool = Pool(processes=4)
with open(args.data_file, 'rb') as f:
	fl = list(f)[1:args.nrows]
	ints = pool.map(read_file,fl)


# creo un diccionario con los enteros
dict_i = dict.fromkeys(ints)

# Lo recorro y mido
start_time = time.time()
dict_scan(dict_i)
stop_time = time.time()
print "Recorridas %d claves en [%f] segundos" % (len(dict_i),stop_time - start_time)