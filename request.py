import random

class Request():
    def __init__(
                    self,
                    id_modelo=int(random.randint(1,1000)),
                    #version=random.randint(1,1000),
                    variable=int(random.randint(1,1000)),
                    nivel=int(random.randint(1,1000)),
                    pasada=int(random.randint(1,1000))
                ):
        self.id_modelo = int(id_modelo)
        #self.version   = str(version)
        self.variable  = int(variable)
        self.nivel     = int(nivel)
        self.pasada    = int(pasada)
        self.string    = str(self.id_modelo) + str(self.variable) + str(self.nivel) + str(self.pasada)
        self.integer   = int(str(self))

    def __repr__(self):
        return self.string

    def __str__(self):
        return self.string

    def __eq__(self,other):
        return self.id_modelo == other.id_modelo and self.variable == other.variable and self.nivel == other.nivel and self.pasada == other.pasada


    @staticmethod
    def create_from_df(df,hash_function=hash):
        reqs = []
        for i,row in df.iterrows():
            req = Request(row['id_modelo'],row['variable'],row['nivel'],row['pasada'])
            reqs.append(req)
        return dict.fromkeys(reqs)
