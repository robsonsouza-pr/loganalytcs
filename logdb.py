#!/usr/bin/env python3
"""Classe responsavel por fazer consultas ao banco de dados e exibir o resultad
o na tela"""

import datetime
import psycopg2

# definindo o nome do banco de dados
DBNAME = "news"


def questao1():
    # conecta no banco
    db = psycopg2.connect(database=DBNAME)
    # cursor eh um objeto que permite executar queries
    c = db.cursor()
    c.execute(
        "select a.title, count(l.id) as acessos from articles a inner jo" +
        "in log l on a.slug = substring(l.path from 10)  group by a." +
        "title order by acessos desc limit 3"
    )
    return c.fetchall()
    # fecha a conexao
    db.close()


def questao2():
    # conecta no banco
    db = psycopg2.connect(database=DBNAME)
    # cursor eh um objeto que permite executar queries
    c = db.cursor()
    c.execute(
        "select au.name, count(l.id) as acessos from articles a" +
        " inner join authors au on au.id = a.author " +
        " inner join log l on a.slug =  substring(l.path from 10) " +
        " group by au.name order by acessos desc limit 3"
    )
    return c.fetchall()
    # fecha a conexao
    db.close()


def questao3():
    # conecta no banco
    db = psycopg2.connect(database=DBNAME)
    # cursor eh um objeto que permite executar queries
    c = db.cursor()
    c.execute(
        "select to_char(l.time, 'dd/mm/yyyy') as data," +
        " cast((com_erro.count_erro/total.count_total) as numeric(10,3))*100" +
        " as p_erro from log l, " +
        " ( select to_char(time, 'dd/mm/yyyy') as data_total, " +
        " cast(count(*) as numeric(10,3)) as count_total " +
        " from log group by data_total) as total, " +
        " ( select to_char(time, 'dd/mm/yyyy') as data_erro, " +
        " cast(count(*) as numeric(10,3)) as count_erro " +
        " from log where status like '%404%' group by data_erro) as com_erro" +
        " where l.status like '%404%' " +
        " and to_char(time, 'dd/mm/yyyy') = total.data_total " +
        " and to_char(time, 'dd/mm/yyyy') = com_erro.data_erro" +
        " group by  data, p_erro " +
        " having (cast((com_erro.count_erro/total.count_total) as " +
        " numeric(10,3))*100) > 1 " +
        " order by data"
    )
    return c.fetchall()
    # fecha a conexao
    db.close()
