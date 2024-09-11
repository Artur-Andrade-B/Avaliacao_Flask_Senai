from flask import Flask, render_template

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