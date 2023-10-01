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

def generateRole():
    roles = data.roles
    sql = ""
    for i in range(len(roles)):
        sql += f"INSERT INTO role (id, nama) VALUES('{i}','{roles[i]}');\n"
    return sql

def generateCategory():
    kategori = data.kategori
    sql = ""
    for k in kategori:
        kode = "#"+getRandomCode('%%%???', alfabet)
        codeCategory.append(kode)
        sql += f"INSERT INTO kategori (kode, jenis) VALUES('{kode}','{k}');\n"
    return sql

def generateCustomers():
    sql = ""
    for i in range(500):
        nama = fake.first_name() +' '+ fake.last_name()
        jenis_kelamin = random.choice(["L","P"])
        nomor_telepon = "08"+fake.msisdn()
        alamat = fake.address()
        sql += f"INSERT INTO pelanggan (id, nama, jenis_kelamin, nomor_telepon, alamat) VALUES('{i}','{nama}', '{jenis_kelamin}', '{nomor_telepon}', '{alamat}');\n"
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
    sql = ""
    for i in range(500):
        username = fake.first_name()+fake.simple_profile()["username"]
        password = username+"123"
        email = username+"@gmail.com"
        jenis_kelamin = random.choice(["L","P"])
        nomor_telepon = "08"+fake.msisdn()
        alamat = fake.address()
        id_role = random.randint(0,7)
        usernameAccounts.append(username)
        sql += f"INSERT INTO akun (username, password, email, jenis_kelamin, nomor_telepon, alamat, id_role) VALUES('{username}','{password}', '{email}', '{jenis_kelamin}', '{nomor_telepon}', '{alamat}', '{id_role}');\n"
    return sql

def generateProduct():
    sql = ""
    for i in range(500):
        kode = getRandomCode('???-%%%', alfabet)
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
        sql += f"INSERT INTO supplier (id, nama, alamat, nomor_telepon, perusahaan) VALUES('{i}','{nama}', '{alamat}', '{nomor_telepon}', '{perusahaan}');\n"
    return sql

def generatePurchase():
    sql = ""
    for i in range(500):
        kode = f"{i}{i+1}{i+2}{getRandomCode('-%%%', alfabet)}"
        waktu = fake.iso8601()
        biaya_kirim = random.randrange(20000,100000, 2000)
        id_supplier = random.randrange(0,499)
        username_akun = random.choice(usernameAccounts)
        codePurchase.append(kode)
        sql += f"INSERT INTO pembelian (kode, waktu, biaya_kirim, id_supplier, username_akun) VALUES('{kode}','{waktu}', {biaya_kirim}, '{id_supplier}', '{username_akun}');\n"
    return sql

def generatePurchaseDetail():
    sql = ""
    for i in range(500):
        kode = f"{i}{i+1}{i+2}{getRandomCode('-%%%', alfabet)}"
        harga = random.randrange(1000, 50000, 500)
        jumlah = random.randrange(10, 100, 10)
        kode_pembelian = random.choice(codePurchase)
        kode_barang = random.choice(codeProducts)
        sql += f"INSERT INTO detail_pembelian (kode, harga, jumlah, kode_pembelian, kode_barang) VALUES('{kode}',{harga}, {jumlah}, '{kode_pembelian}', '{kode_barang}');\n"
    return sql

def generateTransaction():
    sql = ""
    for i in range(500):
        kode = f"{i}{i+1}{i+2}{getRandomCode('-%%%', alfabet)}"
        waktu = fake.iso8601()
        username_akun = random.choice(usernameAccounts)
        kode_metode_pembayaran = random.choice(codePayment)
        id_pelanggan = random.randint(0,499)
        codeTransactions.append(kode)
        sql += f"INSERT INTO transaksi (kode, waktu, username_akun, kode_metode_pembayaran, id_pelanggan) VALUES('{kode}','{waktu}', '{username_akun}', '{kode_metode_pembayaran}', '{id_pelanggan}');\n"
    return sql

def generateTransactionDetail():
    sql = ""
    for i in range(500):
        kode = f"{i}{i+1}{i+2}{getRandomCode('-%%%', alfabet)}"
        harga = random.randrange(500, 50000, 500)
        jumlah = random.randint(0,10)
        kode_transaksi = random.choice(codeTransactions)
        kode_barang = random.choice(codeProducts)
        sql += f"INSERT INTO detail_transaksi (kode, harga, jumlah, kode_transaksi, kode_barang) VALUES('{kode}',{harga}, {jumlah}, '{kode_transaksi}', '{kode_barang}');\n"
    return sql

def generateSQL(sql, filename):
    with open(filename, "w") as f:
        f.write(sql) 

def generateFile():
    sqlRole = generateRole()
    sqlCategory = generateCategory()
    sqlCustomers = generateCustomers()
    sqlPaymentMethods = generatePaymentMethods()
    sqlAccount = generateAccount()
    sqlProduct = generateProduct()
    sqlSupplier = generateSupplier()
    sqlPurchase = generatePurchase()
    sqlPurchaseDetail = generatePurchaseDetail()
    sqlTransaction = generateTransaction()
    sqlTransactionDetail = generateTransactionDetail()

    allSql = sqlRole+sqlCategory+sqlCustomers+sqlPaymentMethods+sqlAccount+sqlProduct+sqlSupplier+sqlPurchase+sqlPurchaseDetail+sqlTransaction+sqlTransactionDetail
    generateSQL(allSql, "all-table.sql")

