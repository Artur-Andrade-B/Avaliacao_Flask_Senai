from flask import Flask, render_template, request, redirect, jsonify
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
import pymysql
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
    return render_template("index.html")

@app.route("/cadastrocliente")
def cadastro_cliente():
    return render_template("cadastro_usuario.html")

@app.route("/novocliente", methods=["POST"])
def criar_novo_cliente():
    nome = request.form["id_user"]
    senha_s = request.form["i_pass"]
    senha_h = hash_password(senha_s)
    email = request.form["i_email"]
    tel = request.form['i_tel']
    user = Cliente(nome=nome, telefone=tel, email=email, senha=senha_h)
    
    if session.query(Cliente).filter_by(nome=nome).first():
        session.rollback()
        mensagem = "nome de usuario ja existe"
    
    else:
        if user:
            try:
                session.add(user)
                session.commit()
                mensagem = "cadastro efetuado com sucesso"
            except:
                session.rollback()
                mensagem = "erro ao realizar cadastro"
                raise
            finally:
                session.close()
        else:
            mensagem = "erro de ao conectar com o banco"        
        
    return render_template("index.html", mensagem = mensagem)

@app.route("/novoserviço")
def criar_novo_servico():
    return render_template("solicitacao_de_servico.html")

@app.route("/novoagendamento")
def criar_novo_agendamento():
    return render_template("pagina_agendamento.html")

@app.route("/login")
def realizar_login():
    return render_template("login_usuario.html")

@app.route("/e_login", methods=["POST"])
def efetuar_login():
    nome = request.form["id_user"]
    user = session.query(Cliente).filter_by(nome=nome).first()
    password_s = request.form["i_pass"]
    password_h = hash_password(password_s)
    if user.nome == request.form["id_user"] and user.senha == password_h:
        try:
            return render_template("acesso_cliente.html", user=user, nome=nome)
        except:
            session.rollback()
            mensagem = "erro ao realizar login"
        finally:
            session.close()
    else:
        mensagem = "Os dados do login estão incorretos"
        return render_template("index.html", mensagem = mensagem)

@app.route("/logout")
def realizar_logout():
    return "realiza logout"

app.run()