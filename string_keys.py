import cProfile
import pstats
import pandas as pd
import sys

    

def lectura(d):
    """
    FUNCTION TO BENCHMARK: dict scan
    """  
    nodos = []
    for key in d.keys():
        nodos.append(d[key])
    return nodos



if __name__ == '__main__':

    # Leo el csv
    raw_data = pd.io.parsers.read_csv(sys.argv[1],compression='gzip',sep="|",nrows=None)
    print("Cargado raw_data, shape:",raw_data.shape)
    # Creo una columna de strings y otra de enteros concatenando, son nuestras keys (no son unicas)
    data = pd.DataFrame()
    data['string'] = raw_data['id_modelo'].apply(str) + raw_data['version'].apply(str) + raw_data['variable'].apply(str) + raw_data['nivel'].apply(str) + raw_data['pasada'].apply(str)
    data['integer'] = data['string'].apply(int)

    
    # Meto las keys y los values en los diccionarios
    dict_s = dict(zip(data.string , raw_data.id_nodo))
    print("Cargado dict de strings, numero de claves:",len(dict_s))
    dict_i = dict(zip(data.integer, raw_data.id_nodo))
    print("Cargado dict de integers, numero de claves:",len(dict_i))
    # TODO: Si queremos guardar todos los nodos para una key: http://stackoverflow.com/a/6795385/472866


    nodos = []
    cProfile.run("nodos = lectura(dict_s)",'.stats_lectura_s')
    r_stats = pstats.Stats('.stats_lectura_s')
    r_stats.print_stats()
    print("longitud resultado lista con los nodos:",len(nodos))

    nodos = []
    cProfile.run("nodos = lectura(dict_s)",'.stats_lectura_i')
    r_stats = pstats.Stats('.stats_lectura_i')
    r_stats.print_stats()
    print("longitud resultado lista con los nodos:",len(nodos))    
    
