#!/usr/bin/env python3

from logdb import questao1, questao2, questao3

print("Quais foram os tres artigos mais populares de todos os tempos?")
questao = questao1()
for title in questao:
    print("O artigo {} teve {} views.".format(title[0], title[1]))
# pula uma linha em branco
print("")

print(" Quem sao os autores de artigos mais populares de todos os tempos?")
questao2 = questao2()
for autor in questao2:
    print("O autor {} teve {} de views".format(autor[0], autor[1]))
# pula uma linha em branco
print("")

print("Em quais dias mais de 1% das requisicoes resultaram em erros? ")
questao3 = questao3()
for erro in questao3:
    print("Em {} houve {} % de erros.".format(erro[0], erro[1]))
