from faker import Faker
import data
from utils import getRandomCode
import random

fake = Faker()

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
codePayment = []
codeCategory = []
usernameAccounts = []
codePurchase = []
codeProducts = []
codeTransactions = []

def generateCategory():
    kategori = data.kategori
    sql = ""
    for i in range(len(kategori)):
        kode = "#"+getRandomCode('%%%???', alfabet)+str(i)
        codeCategory.append(kode)

        sql += f"INSERT INTO kategori (kode, jenis) VALUES('{kode}','{kategori[i]}');\n"
    return sql

def generateMembers():
    sql = ""
    for i in range(500):
        nama = fake.first_name() +' '+ fake.last_name()
        jenis_kelamin = random.choice(["L","P"])
        nomor_telepon = "08"+fake.msisdn()
        alamat = fake.address()

        sql += f"INSERT INTO member (id, nama, jenis_kelamin, nomor_telepon, alamat) VALUES('{i+1}','{nama}', '{jenis_kelamin}', '{nomor_telepon}', '{alamat}');\n"
    return sql

def generatePaymentMethods():
    sql = ""
    payment = data.payment_method
    for p in payment:
        for j in p["jenis"]:
            kode = getRandomCode('???-???', alfabet)
            nama = p["nama"]
            jenis = j
            codePayment.append(kode)

            sql += f"INSERT INTO metode_pembayaran (kode, nama, jenis) VALUES('{kode}','{nama}', '{jenis}');\n"
    return sql

def generateAccount():
    roles = data.roles
    sql = ""
    for i in range(500):
        username = fake.first_name()+fake.simple_profile()["username"]+str(i)
        password = username+"123"
        email = username+"@gmail.com"
        jenis_kelamin = random.choice(["L","P"])
        nomor_telepon = "08"+fake.msisdn()
        alamat = fake.address()
        role = roles[random.randint(0,7)]
        usernameAccounts.append(username)

        sql += f"INSERT INTO akun (username, password, email, jenis_kelamin, nomor_telepon, alamat, role) VALUES('{username}','{password}', '{email}', '{jenis_kelamin}', '{nomor_telepon}', '{alamat}', '{role}');\n"
    return sql

def generateProduct():
    sql = ""
    for i in range(500):
        kode = getRandomCode('???-%%%', alfabet)+str(i)
        barcode = fake.ean(length=13)
        nama = "product"+str(i+1)
        harga_beli = random.randrange(500, 100000, 500)
        harga_jual = harga_beli+2000
        berat = str(random.randrange(100,1000,100))
        stok = random.randint(0,100)
        kode_kategori = random.choice(codeCategory)
        codeProducts.append(kode)

        sql += f"INSERT INTO barang (kode, barcode, nama, harga_beli, harga_jual, berat, stok, kode_kategori) VALUES('{kode}','{barcode}', '{nama}', {harga_beli}, {harga_jual}, {berat}, {stok}, '{kode_kategori}');\n"
    return sql

def generateSupplier():
    sql = ""
    for i in range(500):
        nama = fake.last_name()+fake.name()
        alamat = fake.address()+fake.city()
        nomor_telepon = "08"+fake.msisdn()
        perusahaan = fake.company_suffix()+fake.bs()

        sql += f"INSERT INTO supplier (id, nama, alamat, nomor_telepon, perusahaan) VALUES('{i+1}','{nama}', '{alamat}', '{nomor_telepon}', '{perusahaan}');\n"
    return sql

def generateRestock():
    sql = ""
    for i in range(500):
        kode = f"{i}{getRandomCode('-%%%', alfabet)}"
        waktu = fake.iso8601()
        biaya_kirim = random.randrange(20000,100000, 2000)
        username_akun = random.choice(usernameAccounts)
        codePurchase.append(kode)
        harga = random.randrange(50000,500000, 10000)
        total = random.randrange(0,100)
        id_supplier = random.randrange(1,500)


        sql += f"INSERT INTO restock (kode, waktu, biaya_kirim, harga, total, id_supplier, username_akun) VALUES('{kode}','{waktu}', '{biaya_kirim}', '{harga}', '{total}', '{id_supplier}', '{username_akun}');\n"
    return sql

def generateTransaction():
    sql = ""
    for i in range(500):
        kode = f"{i}{i+1}{i+2}{getRandomCode('-%%%', alfabet)}"
        waktu = fake.iso8601()
        username_akun = random.choice(usernameAccounts)
        kode_metode_pembayaran = random.choice(codePayment)
        id_member = random.randint(1,500)
        codeTransactions.append(kode)
        harga = random.randrange(1000,100000, 10000)
        total = random.randrange(0,50)

        sql += f"INSERT INTO transaksi (kode, waktu, harga, total, username_akun, kode_metode_pembayaran, id_member) VALUES('{kode}','{waktu}', '{harga}', '{total}', '{username_akun}', '{kode_metode_pembayaran}', '{id_member}');\n"
    return sql

def generateSQL(sql, filename):
    with open(filename, "w") as f:
        f.write(sql) 

def generateFile():
    sqlCategory = generateCategory()
    sqlCustomers = generateMembers()
    sqlPaymentMethods = generatePaymentMethods()
    sqlAccount = generateAccount()
    sqlProduct = generateProduct()
    sqlSupplier = generateSupplier()
    sqlPurchase = generateRestock()
    sqlTransaction = generateTransaction()

    allSql = sqlCategory+sqlCustomers+sqlPaymentMethods+sqlAccount+sqlProduct+sqlSupplier+sqlPurchase+sqlTransaction
    generateSQL(allSql, "all-table.sql")

