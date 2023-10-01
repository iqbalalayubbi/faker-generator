from faker import Faker
import data
from utils import getRandomCode
import random

fake = Faker()

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generateRole():
    roles = data.roles
    sql = ""
    for i in range(len(roles)):
        sql += f"INSERT INTO role (id, nama) VALUES(`{i}`,`{roles[i]}`)\n"
    return sql

def generateKategori():
    kategori = data.kategori
    sql = ""
    for k in kategori:
        kode = "#"+getRandomCode('%%%???', alfabet)
        sql += f"INSERT INTO kategori (kode, jenis) VALUES(`{k}`,`{kode}`)\n"
    return sql

def generateSQL(sql, filename):
    with open(filename, "w") as f:
        f.write(sql) 

def generateFile():
    sqlRole = generateRole()
    sqlKategori = generateKategori()
    generateSQL(sqlRole, "role.sql")
    generateSQL(sqlKategori, "kategori.sql")

