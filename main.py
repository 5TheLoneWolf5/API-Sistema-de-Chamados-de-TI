############

from fastapi import FastAPI
import sqlite3
from data import *
# import json

app = FastAPI()

# "connect()" creates a connection to the database in the current working directory, implicitly creating it if it does not exist.
conn = sqlite3.connect("gestaoAtivos.db")
cursor = conn.cursor()

############

# Creating objects and storing them.

so1 = So(dataSO[0]['ID'], dataSO[0]['SO'])
so2 = So(dataSO[1]['ID'], dataSO[1]['SO'])
so3 = So(dataSO[2]['ID'], dataSO[2]['SO'])
so4 = So(dataSO[3]['ID'], dataSO[3]['SO'])

setSo = [so1, so2, so3, so4]

inventario1 = Inventario(dataInventario[0]['ID'],
                         dataInventario[0]['Computador'],
                         dataInventario[0]['SO'])
inventario2 = Inventario(dataInventario[1]['ID'],
                         dataInventario[1]['Computador'],
                         dataInventario[1]['SO'])
inventario3 = Inventario(dataInventario[2]['ID'],
                         dataInventario[2]['Computador'],
                         dataInventario[2]['SO'])
inventario4 = Inventario(dataInventario[3]['ID'],
                         dataInventario[3]['Computador'],
                         dataInventario[3]['SO'])
inventario5 = Inventario(dataInventario[4]['ID'],
                         dataInventario[4]['Computador'],
                         dataInventario[4]['SO'])
inventario6 = Inventario(dataInventario[5]['ID'],
                         dataInventario[5]['Computador'],
                         dataInventario[5]['SO'])
inventario7 = Inventario(dataInventario[6]['ID'],
                         dataInventario[6]['Computador'],
                         dataInventario[6]['SO'])
inventario8 = Inventario(dataInventario[7]['ID'],
                         dataInventario[7]['Computador'],
                         dataInventario[7]['SO'])
inventario9 = Inventario(dataInventario[8]['ID'],
                         dataInventario[8]['Computador'],
                         dataInventario[8]['SO'])
inventario10 = Inventario(dataInventario[9]['ID'],
                          dataInventario[9]['Computador'],
                          dataInventario[9]['SO'])

setInventario = [
  inventario1, inventario2, inventario3, inventario4, inventario5, inventario6,
  inventario7, inventario8, inventario9, inventario10
]

departamento1 = Departamento(dataDepartamento[0]['ID'],
                             dataDepartamento[0]["Departamento"])
departamento2 = Departamento(dataDepartamento[1]['ID'],
                             dataDepartamento[1]["Departamento"])
departamento3 = Departamento(dataDepartamento[2]['ID'],
                             dataDepartamento[2]["Departamento"])
departamento4 = Departamento(dataDepartamento[3]['ID'],
                             dataDepartamento[3]["Departamento"])
departamento5 = Departamento(dataDepartamento[4]['ID'],
                             dataDepartamento[4]["Departamento"])

setDepartamento = [
  departamento1, departamento2, departamento3, departamento4, departamento5
]

usuario1 = Usuario(dataUsuario[0]['ID'], dataUsuario[0]['Nome'],
                   dataUsuario[0]['Computador'],
                   dataUsuario[0]['Departamento'])
usuario2 = Usuario(dataUsuario[1]['ID'], dataUsuario[1]['Nome'],
                   dataUsuario[1]['Computador'],
                   dataUsuario[1]['Departamento'])
usuario3 = Usuario(dataUsuario[2]['ID'], dataUsuario[2]['Nome'],
                   dataUsuario[2]['Computador'],
                   dataUsuario[2]['Departamento'])
usuario4 = Usuario(dataUsuario[3]['ID'], dataUsuario[3]['Nome'],
                   dataUsuario[3]['Computador'],
                   dataUsuario[3]['Departamento'])
usuario5 = Usuario(dataUsuario[4]['ID'], dataUsuario[4]['Nome'],
                   dataUsuario[4]['Computador'],
                   dataUsuario[4]['Departamento'])
usuario6 = Usuario(dataUsuario[5]['ID'], dataUsuario[5]['Nome'],
                   dataUsuario[5]['Computador'],
                   dataUsuario[5]['Departamento'])
usuario7 = Usuario(dataUsuario[6]['ID'], dataUsuario[6]['Nome'],
                   dataUsuario[6]['Computador'],
                   dataUsuario[6]['Departamento'])
usuario8 = Usuario(dataUsuario[7]['ID'], dataUsuario[7]['Nome'],
                   dataUsuario[7]['Computador'],
                   dataUsuario[7]['Departamento'])
usuario9 = Usuario(dataUsuario[8]['ID'], dataUsuario[8]['Nome'],
                   dataUsuario[8]['Computador'],
                   dataUsuario[8]['Departamento'])
usuario10 = Usuario(dataUsuario[9]['ID'], dataUsuario[9]['Nome'],
                    dataUsuario[9]['Computador'],
                    dataUsuario[9]['Departamento'])

setUsuario = [
  usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7,
  usuario8, usuario9, usuario10
]

chamado1 = Chamado(dataChamado[0]['ID'], dataChamado[0]['Usuario'],
                   dataChamado[0]['Problema'], dataChamado[0]['Prioridade'], dataChamado[0]['Data'])
chamado2 = Chamado(dataChamado[1]['ID'], dataChamado[1]['Usuario'],
                   dataChamado[1]['Problema'], dataChamado[1]['Prioridade'], dataChamado[1]['Data'])
chamado3 = Chamado(dataChamado[2]['ID'], dataChamado[2]['Usuario'],
                   dataChamado[2]['Problema'], dataChamado[2]['Prioridade'], dataChamado[2]['Data'])
chamado4 = Chamado(dataChamado[3]['ID'], dataChamado[3]['Usuario'],
                   dataChamado[3]['Problema'], dataChamado[3]['Prioridade'], dataChamado[3]['Data'])
chamado5 = Chamado(dataChamado[4]['ID'], dataChamado[4]['Usuario'],
                   dataChamado[4]['Problema'], dataChamado[4]['Prioridade'], dataChamado[4]['Data'])
chamado6 = Chamado(dataChamado[5]['ID'], dataChamado[5]['Usuario'],
                   dataChamado[5]['Problema'], dataChamado[5]['Prioridade'], dataChamado[5]['Data'])
chamado7 = Chamado(dataChamado[6]['ID'], dataChamado[6]['Usuario'],
                   dataChamado[6]['Problema'], dataChamado[6]['Prioridade'], dataChamado[6]['Data'])
chamado8 = Chamado(dataChamado[7]['ID'], dataChamado[7]['Usuario'],
                   dataChamado[7]['Problema'], dataChamado[7]['Prioridade'], dataChamado[7]['Data'])
chamado9 = Chamado(dataChamado[8]['ID'], dataChamado[8]['Usuario'],
                   dataChamado[8]['Problema'], dataChamado[8]['Prioridade'], dataChamado[8]['Data'])
chamado10 = Chamado(dataChamado[9]['ID'], dataChamado[9]['Usuario'],
                    dataChamado[9]['Problema'], dataChamado[9]['Prioridade'], dataChamado[9]['Data'])
chamado11 = Chamado(dataChamado[10]['ID'], dataChamado[10]['Usuario'],
                    dataChamado[10]['Problema'], dataChamado[10]['Prioridade'], dataChamado[10]['Data'])
chamado12 = Chamado(dataChamado[11]['ID'], dataChamado[11]['Usuario'],
                    dataChamado[11]['Problema'], dataChamado[11]['Prioridade'], dataChamado[11]['Data'])
chamado13 = Chamado(dataChamado[12]['ID'], dataChamado[12]['Usuario'],
                    dataChamado[12]['Problema'], dataChamado[12]['Prioridade'], dataChamado[12]['Data'])
chamado14 = Chamado(dataChamado[13]['ID'], dataChamado[13]['Usuario'],
                    dataChamado[13]['Problema'], dataChamado[13]['Prioridade'], dataChamado[13]['Data'])

setChamado = [
  chamado1, chamado2, chamado3, chamado4, chamado5, chamado6, chamado7,
  chamado8, chamado9, chamado10, chamado11, chamado12, chamado13, chamado14
]

############

# Creating tables.

cursor.execute("""CREATE TABLE IF NOT EXISTS so (
id INTEGER PRIMARY KEY,
descricao VARCHAR(12)
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS inventario (
id INTEGER PRIMARY KEY,
computador VARCHAR(12),
so INTEGER,
FOREIGN KEY (so) REFERENCES so(descricao)
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS departamento (
id INTEGER PRIMARY KEY,
descricao VARCHAR(15)
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS usuario (
id INTEGER PRIMARY KEY,
nome VARCHAR(20),
computador INTEGER,
departamento INTEGER,
FOREIGN KEY (computador) REFERENCES inventario(computador),
FOREIGN KEY (departamento) REFERENCES departamento(descricao)
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS chamado (
id INTEGER PRIMARY KEY,
usuario INTEGER,
problema TEXT,
prioridade varchar(6),
data DATE,
FOREIGN KEY (usuario) REFERENCES usuario(nome)
)""")

############

# Inserting data into tables.

try:
  for i in setSo:
    cursor.execute("SELECT id FROM so WHERE id = ?", (i.id, ))
    existingId = cursor.fetchone()
  
    if existingId is None:
      cursor.execute("INSERT INTO so (id, descricao) VALUES (?, ?)",
                     (i.id, i.descricao))
    else:
      print(
        f"The value that is stored with the following data: {i.id} is already registered."
      )
  
  conn.commit()

except Exception as e:
  conn.rollback()
  print(f"Error: {str(e)}")

###

try:
  for i in setInventario:
    cursor.execute("SELECT id FROM inventario WHERE id = ?", (i.id, ))
    existingId = cursor.fetchone()
  
    if existingId is None:
      cursor.execute(
        "INSERT INTO inventario (id, computador, so) VALUES (?, ?, ?)",
        (i.id, i.computador, i.so))
    else:
      print(
        f"The value that is stored with the following data: {i.id} is already registered."
      )
  
  conn.commit()

except Exception as e:
  conn.rollback()
  print(f"Error: {str(e)}")

###

try:
  for i in setDepartamento:
    cursor.execute("SELECT id FROM departamento WHERE id = ?", (i.id, ))
    existingId = cursor.fetchone()
  
    if existingId is None:
      cursor.execute("INSERT INTO departamento (id, descricao) VALUES (?, ?)",
                     (i.id, i.descricao))
    else:
      print(
        f"The value that is stored with the following data: {i.id} is already registered."
      )
  
  conn.commit()

except Exception as e:
  conn.rollback()
  print(f"Error: {str(e)}")
  
###

try:
  for i in setUsuario:
    cursor.execute("SELECT id FROM usuario WHERE id = ?", (i.id, ))
    existingId = cursor.fetchone()
  
    if existingId is None:
      cursor.execute(
        "INSERT INTO usuario (id, nome, departamento, computador) VALUES (?, ?, ?, ?)",
        (i.id, i.nome, i.departamento, i.computador))
    else:
      print(
        f"The value that is stored with the following data: {i.id} is already registered."
      )
  
  conn.commit()

except Exception as e:
  conn.rollback()
  print(f"Error: {str(e)}")

###

try:
  for i in setChamado:
    cursor.execute("SELECT id FROM chamado WHERE id = ?", (i.id, ))
    existingId = cursor.fetchone()
  
    if existingId is None:
      cursor.execute(
        "INSERT INTO chamado (id, usuario, problema, prioridade, data) VALUES (?, ?, ?, ?, ?)",
        (i.id, i.usuario, i.problema, i.prioridade, i.data
         ))  # Also: % and dictionaries for placeholder (besides "?").
    else:
      print(
        f"The value that is stored with the following data: {i.id} is already registered."
      )
  
  conn.commit()

except Exception as e:
  conn.rollback()
  print(f"Error: {str(e)}")

# # For testing
# conn.commit()
# cursor.execute("SELECT * FROM chamado")
# test = cursor.fetchall()
# print(test)

# API.

@app.get("/")
async def root():
  return "API - Sistema de Chamados de TI (docs)",  {"/sistemas-operacionais/", "/inventario/", "/departamentos/", "/usuarios/", "/chamados/"}

@app.get("/sistemas-operacionais/")
async def get_os():

  cursor.execute("SELECT id, descricao FROM so")
  so = cursor.fetchall()
  # conn.close()

  json = []

  for i in so:
    id, descricao = i
    json.append({"id": id, "descricao": descricao})

  return json

@app.get("/inventario/")
async def get_inventario():

  cursor.execute("SELECT id, computador, so FROM inventario")
  inventario = cursor.fetchall()
  # conn.close()

  json = []

  for i in inventario:
    id, computador, so = i
    json.append({"id": id, "computador": computador, "so": so})

  return json

@app.get("/departamentos/")
async def get_departamentos():

  cursor.execute("SELECT id, descricao FROM departamento")
  inventario = cursor.fetchall()
  # conn.close()

  json = []

  for i in inventario:
    id, descricao = i
    json.append({"id": id, "descricao": descricao})

  return json

@app.get("/usuarios/")
async def get_usuarios():

  cursor.execute("SELECT id, nome, departamento, computador FROM usuario")
  usuario = cursor.fetchall()
  # conn.close()

  json = []

  for i in usuario:
    id, nome, departamento, computador = i
    json.append({
      "id": id,
      "nome": nome,
      "departamento": departamento,
      "computador": computador
    })

  return json

@app.get("/chamados/")
async def get_chamados():

  cursor.execute("SELECT id, usuario, problema, prioridade, data FROM chamado")
  chamado = cursor.fetchall()
  # conn.close()

  json = []

  for i in chamado:
    id, usuario, problema, prioridade, data = i
    json.append({
      "id": id,
      "usuario": usuario,
      "problema": problema,
      "prioridade": prioridade,
      "data": data
    })

  return json

"""

A small test:
def chamadoTest():

  ownConn = sqlite3.connect("gestaoAtivos.db")
  cursor = ownConn.cursor()
  cursor.execute("SELECT id, usuario, problema, prioridade FROM chamado")
  chamado = cursor.fetchall()
  ownConn.close()
And then, "chamado = chamadoTest()" when calling the function.
This way, it doesn't interfere with the occuring connection.

"""