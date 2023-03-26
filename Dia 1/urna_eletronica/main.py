from urna_eletronica import UrnaEletronica

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