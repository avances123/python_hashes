import random

class Request():
    def __init__(
                    self,
                    id_modelo=random.randint(1,1000),
                    version=random.randint(1,1000),
                    variable=random.randint(1,1000),
                    nivel=random.randint(1,1000),
                    pasada=random.randint(1,1000)
                ):
        self.id_modelo = int(id_modelo)
        self.version   = int(version)
        self.variable  = int(variable)
        self.nivel     = int(nivel)
        self.pasada    = int(pasada)
        self.string    = str(id_modelo) + str(version) + str(variable) + str(nivel) + str(pasada)
        self.integer    = str(id_modelo) + str(version) + str(variable) + str(nivel) + str(pasada)

    def __repr__(self):
        return self.string

    def __str__(self):
        return self.string

    def __eq__(self,other):
        return self.id_modelo == other.id_modelo and self.version == other.version and self.variable == other.variable and self.nivel == other.nivel and self.pasada == other.pasada


    @staticmethod
    def create_from_df(df,hash_function=hash):
        reqs = []
        for i,row in df.iterrows():
            req = Request(row['id_modelo'],row['version'],row['variable'],row['nivel'],row['pasada'])
            reqs.append(req)
        return dict.fromkeys(reqs)
