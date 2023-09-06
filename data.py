class So:
  def __init__(self, id, descricao):
    self.id = id
    self.descricao = descricao

class Inventario:
  def __init__(self, id, computador, so):
    self.id = id
    self.computador = computador
    self.so = so

class Departamento:
  def __init__(self, id, descricao): 
    self.id = id
    self.descricao = descricao

class Usuario:
  def __init__(self, id, nome, computador, departamento):
    self.id = id
    self.nome = nome
    self.computador = computador
    self.departamento = departamento

class Chamado:
  def __init__(self, id, usuario, problema, prioridade, data):
    self.id = id
    self.usuario = usuario
    self.problema = problema
    self.prioridade = prioridade
    self.data = data

dataSO = [{
    "ID": 1,
    "SO": "Windows"
}, {
    "ID": 2,
    "SO": "Linux"
}, {
    "ID": 3,
    "SO": "Xenix"
}, {
    "ID": 4,
    "SO": "MacOS"
}]

# Required
dataInventario = [{
    "ID": 1,
    "Computador": "NTRJ001",
    "SO": 1
}, {
    "ID": 2,
    "Computador": "DTRJ002",
    "SO": 2
}, {
    "ID": 3,
    "Computador": "DTRJ003",
    "SO": 1
}, {
    "ID": 4,
    "Computador": "NTRJ004",
    "SO": 1
}, {
    "ID": 5,
    "Computador": "NTSP005",
    "SO": 2
}, {
    "ID": 6,
    "Computador": "NTRJ006",
    "SO": 1
}, {
    "ID": 7,
    "Computador": "DTRJ007",
    "SO": 3
}, {
    "ID": 8,
    "Computador": "DTRJ008",
    "SO": 1
}, {
    "ID": 9,
    "Computador": "NTRJ009",
    "SO": 4
}, {
    "ID": 10,
    "Computador": "NTSP0010",
    "SO": 2
}]

# Required
dataDepartamento = [{
    "ID": 1,
    "Departamento": "TI"
}, {
    "ID": 2,
    "Departamento": "Compras"
}, {
    "ID": 3,
    "Departamento": "Faturamento"
}, {
    "ID": 4,
    "Departamento": "RH"
}, {
    "ID": 5,
    "Departamento": "Produção"
}]

# Required
dataUsuario = [{
    "ID": 1,
    "Nome": "João",
    "Computador": 1,
    "Departamento": 1
}, {
    "ID": 2,
    "Nome": "Paulo",
    "Computador": 2,
    "Departamento": 2
}, {
    "ID": 3,
    "Nome": "Pedro",
    "Computador": 3,
    "Departamento": 3
}, {
    "ID": 4,
    "Nome": "Maria",
    "Computador": 4,
    "Departamento": 4
}, {
    "ID": 5,
    "Nome": "Flavia",
    "Computador": 5,
    "Departamento": 3
}, {
    "ID": 6,
    "Nome": "Andreia",
    "Computador": 6,
    "Departamento": 2
}, {
    "ID": 7,
    "Nome": "Carmen",
    "Computador": 7,
    "Departamento": 5
}, {
    "ID": 8,
    "Nome": "Judite",
    "Computador": 8,
    "Departamento": 4
}, {
    "ID": 9,
    "Nome": "Gloria",
    "Computador": 9,
    "Departamento": 2
}, {
    "ID": 10,
    "Nome": "Andre",
    "Computador": 10,
    "Departamento": 2
}]

# Required
dataChamado = [{
    "ID": 1,
    "Usuario": 1,
    "Problema": "Bug",
    "Prioridade": "Baixa",
    "Data": "2023-03-12"
}, {
    "ID": 2,
    "Usuario": 2,
    "Problema": "Error 404",
    "Prioridade": "Alta",
    "Data": "2022-05-12"
}, {
    "ID": 3,
    "Usuario": 3,
    "Problema": "Bug",
    "Prioridade": "Baixa",
    "Data": "2021-03-02"
}, {
    "ID": 4,
    "Usuario": 4,
    "Problema": "Error 134",
    "Prioridade": "Normal",
    "Data": "2020-11-15"
}, {
    "ID": 5,
    "Usuario": 5,
    "Problema": "Bug",
    "Prioridade": "Normal",
    "Data": "2021-02-05"
}, {
    "ID": 6,
    "Usuario": 6,
    "Problema": "Error 404",
    "Prioridade": "Alta",
    "Data": "2023-03-20"
}, {
    "ID": 7,
    "Usuario": 7,
    "Problema": "Bug",
    "Prioridade": "Baixa",
    "Data": "2023-03-18"
}, {
    "ID": 8,
    "Usuario": 8,
    "Problema": "Error 23",
    "Prioridade": "Baixa",
    "Data": "2022-12-04"
}, {
    "ID": 9,
    "Usuario": 9,
    "Problema": "Bug",
    "Prioridade": "Normal",
    "Data": "2023-05-15"
}, {
    "ID": 10,
    "Usuario": 10,
    "Problema": "Error 43",
    "Prioridade": "Alta",
    "Data": "2021-03-01"
}, {
    "ID": 11,
    "Usuario": 3,
    "Problema": "Error 404",
    "Prioridade": "Alta",
    "Data": "2023-07-13"
}, {
    "ID": 12,
    "Usuario": 4,
    "Problema": "Bug",
    "Prioridade": "Baixa",
    "Data": "2019-01-02"
}, {
    "ID": 13,
    "Usuario": 3,
    "Problema": "Bug",
    "Prioridade": "Baixa",
    "Data": "2023-08-17"
}, {
    "ID": 14,
    "Usuario": 7,
    "Problema": "Error 32",
    "Prioridade": "Normal",
    "Data": "2020-07-11"
}]