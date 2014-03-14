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
    # 'fnv1_32'         : hash_functions.fnv1_32,
    # 'murmur3_32'      : hash_functions.murmur3_32,
    # 'h_lookup3'       : hash_functions.h_lookup3,
    # 'super_fast_hash' : hash_functions.super_fast_hash,
    # 'murmur2_x64_64a' : hash_functions.murmur2_x64_64a,
    # 'fnv1a_64'        : hash_functions.fnv1a_64,

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

    results = {}
    for i in xrange(22):        
        nrows = int(math.pow(2,i))
        print "Num rows: %s" % nrows
        raw_data = pd.io.parsers.read_csv(sys.argv[1],compression='gzip',sep="|",nrows=nrows)
        results[nrows] = run_functions_test(raw_data)
        #print json.dumps(results[nrows],sort_keys=True,indent=4, separators=(',', ': '))
    with open("hash_results.csv", "w") as outfile:
        json.dump(results, outfile, indent=4)


    
