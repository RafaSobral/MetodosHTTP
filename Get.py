'''Importa a biblioteca necessaria para fazer requisicoes'''
import requests
'''Faz a requisicao no link da API'''
requisicao = requests.get("LINK DA API")
'''Printa a resposta da API para a requisicao. 200 = Sucess, 404 = Failed'''
print(requisicao)
'''printa o dicionario JSON retornado pela API'''
print(requisicao.json())

