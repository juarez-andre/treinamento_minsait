

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

candidatos =[
    {"nome_candidato": "Lula", "nome_partido": "PT"},
    {"nome_candidato": "Ciro", "nome_partido": "PDT"},
    {"nome_candidato": "Bolsonaro", "nome_partido": "PSL"},
    {"nome_candidato": "Marina Silva", "nome_partido": "Rede"},
]

# TESTANDO
urna = UrnaEletronica(candidatos)

urna.exibe_candidatos()
urna.adiciona({"nome_candidato": "João", "nome_partido": "PNFI"})
urna.exibe_candidatos()
urna.remover()
urna.atualizar(1, "nome_candidato", "Pedro")
urna.exibe_candidatos()



    