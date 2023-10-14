# Importações de módulos


# Definição de tipos de dados
class Cidade:
    def __init__(self, id, estado, cidade):
        self.id = id
        self.estado = estado
        self.cidade = cidade

class GPS:
    def __init__(self, id, la, lo):
        self.id = id
        self.la = la
        self.lo = lo

class DataItem:
    def __init__(self, key, city, GPS):
        self.key = key
        self.city = city
        self.GPS = GPS

MAX = 5570

def getCidades(arquivo):
    cidades = []

    with open(arquivo, 'r') as f:
        next(f)  # Ignora a primeira linha com cabeçalho
        for line in f:
            parts = line.split(';')
            cod = int(parts[0].strip())
            uf = parts[1].strip()
            cid = parts[2].strip()
            cidade_obj = Cidade(cod, uf, cid)
            cidades.append(cidade_obj)

    return cidades

def getGps(localizacoes):
    local = []

    with open(localizacoes, 'r') as f:
        next(f)  # Ignora a primeira linha com cabeçalho
        for line in f:
            parts = line.split(';')
            cod = int(parts[0].strip())
            la = float(parts[1].strip())
            lo = float(parts[2].strip())
            gps_obj = GPS(cod, la, lo)
            local.append(gps_obj)

    return local

def getItens(cities, local):
    dados = []

    for city in cities:
        for gps in local:
            if city.id == gps.id:
                item = DataItem(city.id, city, gps)
                dados.append(item)

    return dados