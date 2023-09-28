from faker import Faker
import data

fake = Faker()

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
allProvinces = []

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
        kode = "#"+fake.bothify(text='%%%???', letters=alfabet)
        sql += f"INSERT INTO kategori (kode, jenis) VALUES(`{k}`,`{kode}`)\n"
    return sql

def generateProvince():
    provinces = data.provinces
    capitals = data.capitals
    sql = ""
    for i in range(len(provinces)):
        kode = fake.bothify(text='%%%-???', letters=alfabet)
        temp_data = {
            "kode" : kode,
            "province" : provinces[i],
            "capital" : capitals[i]
        }
        allProvinces.append(temp_data)
        sql += f"INSERT INTO kategori (kode, nama, ibukota) VALUES(`{temp_data['kode']}`, `{temp_data['province']}`, `{temp_data['capital']}`)\n"
    return sql

def generateCity():
    city = data.city
    sql = ""
    for c in city:
        kode = fake.bothify(text='%%%-???', letters=alfabet)
        sql += f"INSERT INTO kategori (kode, nama, kode_provinsi) VALUES(`{kode}`, `{c['city']}`, `{getCodeProvince(c['province'])}`)\n"
    return sql

def generateSQL(sql, filename):
    with open(filename, "w") as f:
        f.write(sql) 

def generateFile():
    sqlRole = generateRole()
    sqlKategori = generateKategori()
    sqlProvince = generateProvince()
    sqlCity = generateCity()
    generateSQL(sqlRole, "role.sql")
    generateSQL(sqlKategori, "kategori.sql")
    generateSQL(sqlProvince, "province.sql")
    generateSQL(sqlCity, "city.sql")

def getCodeProvince(province):
    for p in allProvinces:
        if (p["province"] == province):
            return p["kode"]    

generateFile()
