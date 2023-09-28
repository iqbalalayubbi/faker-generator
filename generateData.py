from faker import Faker
import data
from utils import getRandomCode
import random

fake = Faker()

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
allProvinces = []
cityCode = []
addressCode = []

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

def generateProvince():
    provinces = data.provinces
    capitals = data.capitals
    sql = ""
    for i in range(len(provinces)):
        kode = getRandomCode('%%%-???', alfabet)
        temp_data = {
            "kode" : kode,
            "province" : provinces[i],
            "capital" : capitals[i]
        }
        allProvinces.append(temp_data)
        sql += f"INSERT INTO provinsi (kode, nama, ibukota) VALUES(`{temp_data['kode']}`, `{temp_data['province']}`, `{temp_data['capital']}`)\n"
    return sql

def generateCity():
    city = data.city
    sql = ""
    for c in city:
        kode = getRandomCode('%%%-???', alfabet)
        cityCode.append(kode)
        sql += f"INSERT INTO kota (kode, nama, kode_provinsi) VALUES(`{kode}`, `{c['city']}`, `{getCodeProvince(c['province'])}`)\n"
    return sql

def generateAddress():
    sql = ""
    for i in range(500):
        kode = getRandomCode('???-???-???', alfabet)
        addressCode.append(kode)
        sql += f"INSERT INTO alamat (kode, jalan, kelurahan, kode_pos, kecamatan, kode_kota) VALUES(`{kode}`, `{fake.street_name()}`, `{fake.street_suffix()}`, `{fake.postcode()}`, `{fake.city()}`, `{random.choice(cityCode)}`)\n"
    return sql

def generateCustomer():
    sql = ""
    for i in range(500):
        id = i
        nama = fake.first_name() +' '+ fake.last_name()
        jenis_kelamin = random.choice(["L","P"])
        nomor_telepon = "08"+fake.msisdn()
        kode_alamat = random.choice(addressCode)
        sql += f"INSERT INTO pelanggan (id, nama, jenis_kelamin, nomor_telepon, kode_alamat) VALUES(`{id}`, `{nama}`, `{jenis_kelamin}`, `{nomor_telepon}`, `{kode_alamat}`)\n"
    return sql

def generatePaymentMethod():
    sql = ""
    for payment in data.payment_method:
        for j in payment["jenis"]:
            kode = "#"+getRandomCode("%%??", alfabet)        
            sql += f"INSERT INTO alamat (kode, nama, jenis) VALUES(`{kode}`, `{payment['nama']}`, `{j}`)\n"
    return sql

def generateSQL(sql, filename):
    with open(filename, "w") as f:
        f.write(sql) 

def generateFile():
    sqlRole = generateRole()
    sqlKategori = generateKategori()
    sqlProvince = generateProvince()
    sqlCity = generateCity()
    sqlAddress = generateAddress()
    sqlCustomer = generateCustomer()
    sqlPaymentMethod = generatePaymentMethod()

    generateSQL(sqlRole, "role.sql")
    generateSQL(sqlKategori, "kategori.sql")
    generateSQL(sqlProvince, "province.sql")
    generateSQL(sqlCity, "city.sql")
    generateSQL(sqlAddress, "address.sql")
    generateSQL(sqlCustomer, "customer.sql")
    generateSQL(sqlPaymentMethod, "payment method.sql")

def getCodeProvince(province):
    for p in allProvinces:
        if (p["province"] == province):
            return p["kode"]    
