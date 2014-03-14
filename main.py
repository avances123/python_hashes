import pandas as pd
import time
import json
import math
import argparse
from request import Request
import hash_functions



HASHFUNCTS = {
    'python_tuple'        : hash_functions.python_tuple,
    'python_integer'      : hash_functions.python_integer,
    'scamm'               : hash_functions.scamm,
    'scamm_con_version_1' : hash_functions.scamm_con_version_1,
    'scamm_con_version_2' : hash_functions.scamm_con_version_2,
}




def dict_scan(d):
    for key in d.keys():
        d[key]



def run_functions_test(df,functs=HASHFUNCTS.keys()):
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



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Measure times of hash functions in python')
    parser.add_argument('data_file')
    args = parser.parse_args()
    

    results = {}
    for i in xrange(22):        
        nrows = int(math.pow(2,i))
        print "Num rows: %s" % nrows
        raw_data = pd.io.parsers.read_csv(args.data_file,compression='gzip',sep="|",nrows=nrows)
        results[nrows] = run_functions_test(raw_data)
    with open("resultados.json", "w") as outfile:
        json.dump(results, outfile, indent=4)



    
