#!/usr/bin/env python3

from logdb import questao1, questao2, questao3

print("Quais foram os tres artigos mais populares de todos os tempos?")
questao = questao1()
for title in questao:
    print(title)
# pula uma linha em branco
print("O artigo ", title[1], " teve ", title[2], "views")

print(" Quem sao os autores de artigos mais populares de todos os tempos?")
questao2 = questao2()
for autor in questao2:
    print(autor[1], "teve ", autor[2], " de views")
# pula uma linha em branco
print("")

print("Em quais dias mais de 1% das requisicoes resultaram em erros? ")
questao3 = questao3()
for erro in questao3:
    print("Em ", erro[1], "houve ", erro[2], " erros")
