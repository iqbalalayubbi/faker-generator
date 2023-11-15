from faker import Faker
import data
from utils import getRandomCode, getData
import random

fake = Faker()

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
codePayment = []
usernameAccounts = []
codePurchase = []
codeProducts = []
codeTransactions = []

def generateCategory():
    kategori = getData("kategori", 500)
    sql = ""
    for i in range(len(kategori)):
        kode = kategori[i][0]

        sql += f"INSERT INTO KATEGORI (KODE_KATEGORI, JENIS_KATEGORI) VALUES('{kode}','{kategori[i][1]}');\n"
    return sql

def generateMembers():
    sql = ""
    for i in range(500):
        nama = fake.first_name() +' '+ fake.last_name()
        jenis_kelamin = random.choice(["L","P"])
        nomor_telepon = "08"+fake.msisdn()
        alamat = fake.address()

        sql += f"INSERT INTO MEMBER (ID_MEMBER, NAMA_MEMBER, JENIS_KELAMIN_MEMBER, NOMOR_TELEPON_MEMBER, ALAMAT_MEMBER) VALUES('{i+1}','{nama}', '{jenis_kelamin}', '{nomor_telepon}', '{alamat}');\n"
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

            sql += f"INSERT INTO METODE_PEMBAYARAN (KODE_METODE_PEMBAYARAN, NAMA_METODE_PEMBAYARAN, JENIS_METODE_PEMBAYARAN) VALUES('{kode}','{nama}', '{jenis}');\n"
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

        sql += f"INSERT INTO AKUN (USERNAME_AKUN, PASSWORD_AKUN, EMAIL_AKUN, JENIS_KELAMIN_AKUN, NOMOR_TELEPON_AKUN, ALAMAT_AKUN, ROLE) VALUES('{username}','{password}', '{email}', '{jenis_kelamin}', '{nomor_telepon}', '{alamat}', '{role}');\n"
    return sql

def generateProduct():
    products = getData("products", 4999)
    sql = ""
    for i in range(len(products)):
        kode = getRandomCode('???-%%%', alfabet)+str(i)
        barcode = fake.ean(length=13)
        nama = products[i][1]
        harga_beli = random.randrange(500, 100000, 500)
        harga_jual = harga_beli+2000
        berat = str(random.randrange(100,1000,100))
        stok = random.randint(0,100)
        kode_kategori = products[i][0]
        codeProducts.append(kode)

        sql += f"INSERT INTO BARANG (KODE_BARANG, BARCODE_BARANG, NAMA_BARANG, HARGA_BELI_BARANG, HARGA_JUAL_BARANG, BERAT_BARANG, STOK_BARANG, KODE_KATEGORI) VALUES('{kode}','{barcode}', '{nama}', {harga_beli}, {harga_jual}, {berat}, {stok}, '{kode_kategori}');\n"
    return sql

def generateSupplier():
    sql = ""
    for i in range(500):
        nama = fake.last_name()+fake.name()
        alamat = fake.address()+fake.city()
        nomor_telepon = "08"+fake.msisdn()
        perusahaan = fake.company_suffix()+fake.bs()

        sql += f"INSERT INTO SUPPLIER (ID_SUPPLIER, NAMA_SUPPLIER, ALAMAT_SUPPLIER, NOMOR_TELEPON_SUPPLIER, PERUSAHAAN_SUPPLIER) VALUES('{i+1}','{nama}', '{alamat}', '{nomor_telepon}', '{perusahaan}');\n"
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

        sql += f"INSERT INTO RESTOCK (KODE_RESTOCK, WAKTU_RESTOCK, BIAYA_KIRIM_RESTOCK, HARGA_RESTOCK, TOTAL_BARANG_RESTOCK, ID_SUPPLIER, USERNAME_AKUN) VALUES('{kode}','{waktu}', '{biaya_kirim}', '{harga}', '{total}', '{id_supplier}', '{username_akun}');\n"
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
        kode_product = random.choice(codeProducts)

        sql += f"INSERT INTO TRANSAKSI (KODE_TRANSAKSI, WAKTU_TRANSAKSI, HARGA_TRANSAKSI, TOTAL_TRANSAKSI, USERNAME_AKUN, KODE_BARANG, KODE_METODE_PEMBAYARAN, ID_MEMBER) VALUES('{kode}','{waktu}', '{harga}', '{total}', '{username_akun}', '{kode_product}', '{kode_metode_pembayaran}', '{id_member}');\n"
    return sql

def generateSQL(sql, filename):
    with open(filename, "w", encoding="utf-8") as f:
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
    generateSQL(allSql, "insert-data.sql")