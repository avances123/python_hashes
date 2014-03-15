import time
import argparse
import multiprocessing 


# Pilla las claves y busca cada una en el dict
def dict_scan(d):
    for key in d.keys():
        d[key]


def read_line(line):
	#print line
	#return int(''.join(line.rstrip('\n').split('|'))[:-1])
	key  = ''.join(line.rstrip('\n').split('|'))[:-1]
	nodo = ''.join(line.rstrip('\n').split('|'))[-1]
	return (key,nodo)

# Pillo los argumentos
parser = argparse.ArgumentParser()
parser.add_argument('data_file')
parser.add_argument('--nrows',type=int)
parser.add_argument('--repeat',type=int,default=10)
args = parser.parse_args()

# Leo el csv y lo convierto a una lista de enteros
pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
print "Cargando %s ..." % args.data_file
start_time = time.time()
with open(args.data_file, 'rb') as f:
	fl = list(f)[1:args.nrows]
	tuples = pool.map(read_line,fl)
stop_time = time.time()
print "Cargado en %s en [%f] segundos" %(args.data_file,stop_time - start_time) 


# creo un diccionario con los enteros
dict_i = dict(tuples)


# Lo recorro y mido (repito 10 veces)
times = []
for i in xrange(args.repeat):
	start_time = time.time()
	dict_scan(dict_i)
	stop_time = time.time()
	lapse = stop_time - start_time
	times.append(lapse)

print "Recorridas %d claves en [%f] segundos" % (len(dict_i),sum(times)/args.repeat)
