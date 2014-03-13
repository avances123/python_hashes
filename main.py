import pandas as pd
import sys
import time
import json
import math
from request import Request
import hash_functions



HASHFUNCTS = {
    'python_id'       : hash_functions.python_id,
    'python_tuple'    : hash_functions.python_tuple,
    'python_integer'  : hash_functions.python_integer,
    'python_string'   : hash_functions.python_string,
    'scamm'           : hash_functions.scamm,
    'fnv1_32'         : hash_functions.fnv1_32,
    'murmur3_32'      : hash_functions.murmur3_32,
    #'h_lookup3'       : hash_functions.h_lookup3,
    'super_fast_hash' : hash_functions.super_fast_hash,
    'murmur2_x64_64a' : hash_functions.murmur2_x64_64a,
    'fnv1a_64'        : hash_functions.fnv1a_64,

}


def estudio_hashes(df,functs=HASHFUNCTS.keys()):
    results = {}
    for f in functs:
        setattr(Request, '__hash__', HASHFUNCTS[f])
        dict_r = Request.create_from_df(df)
        start_time = time.time()
        dict_scan(dict_r)
        stop_time = time.time()
        results[f] = stop_time - start_time
        print "key: Request (hash: %s) = %f seconds" % (f,stop_time - start_time)

    return results

def incrementa_nrows():
    results = {}
    for i in xrange(22):        
        nrows = int(math.pow(2,i))
        print "Num rows: %s" % nrows
        raw_data = pd.io.parsers.read_csv(sys.argv[1],compression='gzip',sep="|",nrows=nrows)
        results[nrows] = estudio_hashes(raw_data)
        #print json.dumps(results[nrows],sort_keys=True,indent=4, separators=(',', ': '))
    with open("hash_results.csv", "w") as outfile:
        json.dump(results, outfile, indent=4)


def dict_scan(d):
    for key in d.keys():
        d[key]


if __name__ == '__main__':

    # Leo el csv
    print("Cargando dataset")
    raw_data = pd.io.parsers.read_csv(sys.argv[1],compression='gzip',sep="|",nrows=10000)
    data = pd.DataFrame()
    data['strings']  = raw_data['id_modelo'].apply(str) + raw_data['version'].apply(str) + raw_data['variable'].apply(str) + raw_data['nivel'].apply(str) + raw_data['pasada'].apply(str)
    data['integers'] = data['strings'].apply(int)


    # TODO: Si queremos guardar todos los nodos para una key: http://stackoverflow.com/a/6795385/472866
    print("Creando diccionarios")
    dict_s = dict(zip(data.strings , raw_data.id_nodo))
    dict_i = dict(zip(data.integers, raw_data.id_nodo))
    
    

    print("Midiendo tiempos")
    incrementa_nrows()    

    
    start_time = time.time()
    nodos = dict_scan(dict_i)
    stop_time = time.time()
    print "key: int = %f seconds" % (stop_time - start_time)

    
