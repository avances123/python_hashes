

# Colecciones de funciones hash
def python(req):
    return hash((req.id_modelo,req.version,req.variable,req.nivel,req.pasada))

def python_id(req):
    return id(req)

def scamm(req):
    return abs(req.variable * (req.id_modelo + 1) * (req.nivel + 1) + req.pasada) % 20000000



import pyhash
#https://code.google.com/p/pyfasthash/

h_fnv1_32 = pyhash.fnv1_32()
def fnv1_32(req):
    return h_fnv1_32(req.string)


h_lookup3 = pyhash.lookup3_big()
def lookup3(req):
    return h_lookup3(req.string)

h_super_fast_hash = pyhash.super_fast_hash()
def super_fast_hash(req):
    return h_super_fast_hash(req.string)


h_murmur2_x64_64a = pyhash.murmur2_x64_64a()
def murmur2_x64_64a(req):
    return h_murmur2_x64_64a(req.string)


h_murmur3_32 = pyhash.murmur3_32()
def murmur3_32(req):
    return h_murmur3_32(req.string)

h_fnv1a_64 = pyhash.fnv1a_64()
def fnv1a_64(req):
    return h_fnv1a_64(req.string)

    