class UrnaEletronica:
    def __init__(self, candidatos):
        self.candidatos = candidatos

    def exibe_candidatos(self):
        print("#############################################################################")
        for candidato in self.candidatos:
            print(f'Candidato {candidato["nome_candidato"]}, partido {candidato["nome_partido"]}')
            
        print("#############################################################################")

    def adiciona(self, candidato):
        self.candidatos.append(candidato)

    def remover(self):
        self.candidatos.pop()

    def atualizar(self, indice, chave, valor):
        try:
            self.candidatos[indice][chave] = valor 

        except IndexError:
            print(f"Índice inválido")




    