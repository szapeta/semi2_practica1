import accessBDD

def inicio():
    bdd = accessBDD
    data = bdd.sqlSelect("*", "datos", "")
    return data