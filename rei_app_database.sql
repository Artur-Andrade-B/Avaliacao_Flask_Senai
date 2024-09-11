CREATE DATABASE rei_app;
USE rei_app;

CREATE TABLE agendamento(
	id INT PRIMARY KEY AUTO_INCREMENT,
	data_a DATE NOT NULL,
    horario_a TIME NOT NULL
    );
    
ALTER TABLE agendamento
	ADD COLUMN fk_cliente_id INT,
    ADD COLUMN fk_servico_id INT,
    ADD COLUMN fk_funcionario_id INT;
    
ALTER TABLE agendamento ADD CONSTRAINT FK_cliente
	FOREIGN KEY (fk_cliente_id)
	REFERENCES cliente (id)
	ON DELETE CASCADE;
    
ALTER TABLE agendamento ADD CONSTRAINT FK_servico
	FOREIGN KEY (fk_servico_id)
	REFERENCES servico (id)
	ON DELETE CASCADE;
    
ALTER TABLE agendamento ADD CONSTRAINT FK_funcionario
	FOREIGN KEY (fk_funcionario_id)
	REFERENCES funcionario (id)
	ON DELETE CASCADE;
    
CREATE TABLE funcionario(
		id INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(80)
    );
    
 CREATE TABLE cliente(
		id INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(80),
        telefone CHAR(13),
        email Varchar(80),
        senha VARCHAR(256)
    );
    
CREATE TABLE servico(
		id INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(80),
        valor DECIMAL(8,2)
    );