import pandas as pd
import sys
import time

    

def dict_scan(d):
    for key in d.keys():
        nodo = d[key]



if __name__ == '__main__':

    # Leo el csv
    raw_data = pd.io.parsers.read_csv(sys.argv[1],compression='gzip',sep="|",nrows=None)
    print("Cargado raw_data, shape:",raw_data.shape)
    # Creo una columna de strings y otra de enteros, son nuestras keys (no son unicas, hay 875684 unicas)
    data = pd.DataFrame()
    data['strings'] = raw_data['id_modelo'].apply(str) + raw_data['version'].apply(str) + raw_data['variable'].apply(str) + raw_data['nivel'].apply(str) + raw_data['pasada'].apply(str)
    data['integers'] = data['strings'].apply(int)

    
    # Meto las keys y los values en los diccionarios
    # TODO: Si queremos guardar todos los nodos para una key: http://stackoverflow.com/a/6795385/472866
    dict_s = dict(zip(data.strings , raw_data.id_nodo))
    dict_i = dict(zip(data.integers, raw_data.id_nodo))
    


    start_time = time.time()
    nodos = dict_scan(dict_i)
    stop_time = time.time()
    print(stop_time - start_time, "seconds")
    


    
