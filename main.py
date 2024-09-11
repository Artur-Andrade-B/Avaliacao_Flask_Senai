from flask import Flask, render_template
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

import hashlib
import getpass

from cliente import Cliente
from funcionario import Funcionario
from agendamento import Agendamento
from servico import Servico

from datetime import datetime, timezone

import urllib.parse



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

user = "root"
password = urllib.parse.quote_plus("senai@123")
host = "localhost"
database = "rei_app"

connection_string = f"mysql+pymysql://{user}:{password}@{host}/{database}"

engine = create_engine(connection_string)
metadata = MetaData()
metadata.reflect(engine)

base = automap_base(metadata=metadata)
base.prepare()

Session = sessionmaker(bind=engine)
session = Session()

Cliente = base.classes.cliente
Funcionario = base.classes.funcionario
Agendamento = base.classes.agendamento
Servico = base.classes.servico


app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/novocliente")
def criar_novo_cliente():
    return "cria cliente"

@app.route("/novoserviço")
def criar_novo_servico():
    return "cria um novo serviço"

@app.route("/novoagendamento")
def criar_novo_agendamento():
    return "cria um novo agendamento"

@app.route("/login")
def realizar_login():
    return "realiza login"

@app.route("/logout")
def realizar_logout():
    return "realiza logout"

app.run()