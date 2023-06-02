class GerenciarPacientes:
    def __init__(self, nome_paciente, num_identificacao, estado_de_saude) -> None:
        self.nome_paciente = nome_paciente
        self.num_identificacao = num_identificacao
        self.estado_de_saude = estado_de_saude
        self.nome_paciente = []
        self.num_identificacao = []
        self.estado_de_saude = []


    def adicionar_paciente(self, nome, numero, estado_saude):
        self.nome_paciente.append(nome)
        self.num_identificacao.append(numero)
        self.estado_de_saude.append(estado_saude)

    def editar_paciente(self, nome, numero, estado_saude, novo_numero, novo_estado_saude):
        if nome in self.nome_paciente:
            index = self.nome_paciente.index(nome)
            if self.num_identificacao[index] == numero and self.estado_de_saude[index] == estado_saude:
                self.num_identificacao[index] = novo_numero
                self.estado_de_saude[index] = novo_estado_saude
                print(f'Dados do paciente {nome} atualizados. Novo número: {novo_numero}, novo estado de saúde: {novo_estado_saude}')
            else:
                print('Os dados fornecidos não correspondem ao paciente especificado.')
        else:
            print('O Paciente não está na lista')

    def remover_paciente(self, nome, numero, estado_saude):
        if nome in self.nome_paciente:
            index = self.nome_paciente.index(nome)
            if self.num_identificacao[index] >= numero:
                if self.estado_de_saude[index] == estado_saude:  # Verifica se o estado de saúde é o mesmo
                    self.num_identificacao[index] -= numero
                    if self.num_identificacao[index] == 0:
                        self.nome_paciente.pop(index)
                        self.num_identificacao.pop(index)
                        self.estado_de_saude.pop(index)
                    print(f'Paciente {nome} removido, número: {numero}, estado atual: {estado_saude}')
                else:
                    print('O estado de saúde não corresponde ao paciente especificado.')
            else:
                print('O número especificado não corresponde ao paciente especificado.')
        else:
            print('O Paciente não está na lista')

    def liberar_paciente(self, nome, numero, estado_saude):
        if nome in self.nome_paciente:
            index = self.nome_paciente.index(nome)
            if self.num_identificacao[index] >= numero:
                if self.estado_de_saude[index] == estado_saude:  # Verifica se o estado de saúde é o mesmo
                    if estado_saude != 'estável':  # Verifica se o estado de saúde é diferente de 'estável'
                        print('Não é possível liberar um paciente com estado de saúde diferente de "estável".')
                    else:
                        self.num_identificacao[index] -= numero
                        if self.num_identificacao[index] == 0:
                            self.nome_paciente.pop(index)
                            self.num_identificacao.pop(index)
                            self.estado_de_saude.pop(index)
                        print(f'Paciente {nome} alta liberada, número: {numero}, estado atual: {estado_saude}')
                else:
                    print('O estado de saúde não corresponde ao paciente especificado.')
            else:
                print('O número especificado não corresponde ao paciente especificado.')
        else:
            print('O Paciente não está na lista')


    def listar_pacientes(self):
        print(f'Pacientes: Nome: {self.nome_paciente}, estado: {self.estado_de_saude}, id: {self.num_identificacao}')

polly = GerenciarPacientes('teste', 1, 'bem')

polly.adicionar_paciente('polly', 1, 'em tratamento intensivo')
polly.listar_pacientes()
polly.remover_paciente('polly', 1, 'estavel')
polly.listar_pacientes()
polly.remover_paciente('polly', 1, 'em tratamento intensivo')
polly.adicionar_paciente('polly', 1, 'em tratamento intensivo')
polly.liberar_paciente('polly', 1, 'estável')
polly.editar_paciente('polly', 1, 'em tratamento intensivo', 1, 'estável')
polly.listar_pacientes()
polly.liberar_paciente('polly', 1, 'estável')