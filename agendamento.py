class Agendamento:
    def __init__(self, id, data_a, horario_a, fk_cliente_id, fk_servico_id, fk_funcionario_id):
        self.id = id
        self.data_a = data_a
        self.horario_a = horario_a
        self.fk_cliente_id = fk_cliente_id
        self.fk_servico_id = fk_servico_id
        self.fk_funcionario_id = fk_funcionario_id