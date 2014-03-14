

# Colecciones de funciones hash
def python_tuple(req):
    return hash((req.id_modelo,req.variable,req.nivel,req.pasada,req.version))

def scamm(req):
    # El siguiente valor se utiliza para almacenar la asociacion entre
    # datos y nodos. Puede ser uno de la siguiente lista.
    # 53 97 193 389 769 1543 3079 6151 12289 24593 49157 98317
    # 196613 393241 786433 1572869 3145739 6291469 12582917 25165843
    # 50331653 100663319 201326611 402653189 805306457 1610612741
    #HASH_WIS = 1572869

    return abs(req.variable * (req.id_modelo + 1) * (req.nivel + 1) + req.pasada) % 1572869


def scamm_con_version_1(req):
    #return abs(req.variable * (req.id_modelo + 1) * (req.nivel + 1) * (req.version + 1) + req.pasada) % 1572869
    return abs(req.variable * (req.id_modelo + 1) * (req.nivel + 1) + (req.version * req.pasada)) % 1572869

def scamm_con_version_2(req):
    return abs(req.variable * (req.id_modelo + 1) * (req.nivel + 1) * (req.version + 1) + req.pasada) % 1572869



def python_id(req):
    return id(req)

def python_string(req):
    """
    Hashing a string key
    """
    return hash(req.string)

def python_integer(req):
    """
    Hashing an integer key
    """
    return hash(req.integer)


    
