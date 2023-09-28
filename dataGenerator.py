from faker import Faker

fake = Faker()

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
allProvinces = []

def generateRole():
    roles = [
        "Kasir",
        "Sales Associate",
        "Manajer",
        "Asisten Manajer Toko",
        "Visual Merchandiser",
        "Customer Service Representative",
        "Marketing",
        "IT Support"
    ]

    sql = ""
    for i in range(len(roles)):
        sql += f"INSERT INTO role (id, nama) VALUES(`{i}`,`{roles[i]}`)\n"
    return sql

def generateKategori():
    kategori = [
        "Elektronik",
        "Fashion",
        "Kecantikan dan Perawatan Pribadi",
        "Makanan dan Minuman",
        "Rumah dan Taman",
        "Olahraga dan Kesehatan",
        "Hobi dan Mainan",
        "Otomotif",
        "Elektronik Rumah Tangga",
        "Perlengkapan Kantor",
        "Perhiasan",
        "Tas",
        "Sepatu",
        "Pakaian Wanita",
        "Pakaian Pria",
        "Kosmetik",
        "Alat-alat Taman",
        "Produk Makanan Organik",
        "Wine dan Minuman Keras",
        "Peralatan Olahrag"
    ]
    sql = ""
    for k in kategori:
        kode = "#"+fake.bothify(text='%%%???', letters=alfabet)
        sql += f"INSERT INTO kategori (kode, jenis) VALUES(`{k}`,`{kode}`)\n"
    return sql

def generateProvince():
    provinces = [
        "Aceh",
        "Sumatera Utara",
        "Sumatera Barat",
        "Riau",
        "Kepulauan Riau",
        "Jambi",
        "Bengkulu",
        "Sumatera Selatan",
        "Bangka Belitung",
        "Lampung",
        "Banten",
        "DKI Jakarta",
        "Jawa Barat",
        "Jawa Tengah",
        "DI Yogyakarta",
        "Jawa Timur",
        "Bali",
        "Nusa Tenggara Barat",
        "Nusa Tenggara Timur",
        "Kalimantan Barat",
        "Kalimantan Tengah",
        "Kalimantan Selatan",
        "Kalimantan Timur",
        "Kalimantan Utara",
        "Sulawesi Utara",
        "Gorontalo",
        "Sulawesi Tengah",
        "Sulawesi Barat",
        "Sulawesi Selatan",
        "Sulawesi Tenggara",
        "Maluku",
        "Maluku Utara",
        "Papua Barat",
        "Papua"
    ]
    capitals = [
        "Banda Aceh",
        "Medan",
        "Padang",
        "Pekanbaru",
        "Tanjung Pinang",
        "Jambi",
        "Bengkulu",
        "Palembang",
        "Pangkal Pinang",
        "Bandar Lampung",
        "Serang",
        "Jakarta",
        "Bandung",
        "Semarang",
        "Yogyakarta",
        "Surabaya",
        "Denpasar",
        "Mataram",
        "Kupang",
        "Pontianak",
        "Palangkaraya",
        "Banjarmasin",
        "Samarinda",
        "Tanjung Selor",
        "Manado",
        "Gorontalo",
        "Palu",
        "Mamuju",
        "Makassar",
        "Kendari",
        "Ambon",
        "Sofifi",
        "Manokwari",
        "Jayapura"
    ]
    sql = ""
    for i in range(len(provinces)):
        kode = fake.bothify(text='%%%-???', letters=alfabet)
        data = {
            "kode" : kode,
            "province" : provinces[i],
            "capital" : capitals[i]
        }
        allProvinces.append(data)
        sql += f"INSERT INTO kategori (kode, nama, ibukota) VALUES(`{data['kode']}`, `{data['province']}`, `{data['capital']}`)\n"
    return sql

def generateCity():
    city = [
        "Jakarta",
        "Surabaya",
        "Bandung",
        "Medan",
        "Semarang",
        "Palembang",
        "Makassar",
        "Depok",
        "Bekasi",
        "Tangerang",
        "Bogor",
        "Malang",
        "Yogyakarta",
        "Batam",
        "Pekanbaru",
        "Balikpapan",
        "Samarinda",
        "Padang",
        "Banjarmasin",
        "Pontianak",
        "Manado",
        "Denpasar",
        "Bandar Lampung",
        "Jambi",
        "Surakarta",
        "Ambon",
        "Palu",
        "Kendari",
        "Gorontalo",
        "Mataram",
        "Tomohon",
        "Bitung",
        "Kotamobagu",
        "Luwuk",
        "Bau-Bau",
        "Tual",
        "Serui",
        "Merauke",
        "Timika",
        "Sorong",
        "Nabire",
        "Jayapura",
        "Biak",
        "Manokwari",
        "Fakfak",
        "Bima",
        "Dompu",
        "Sumbawa Besar",
        "Praya",
        "Selong",
        "Waingapu",
        "Ruteng",
        "Ende",
        "Maumere",
        "Larantuka",
        "Kefamenanu",
        "Atambua",
        "Singkawang",
        "Tarakan",
        "Palangkaraya",
        "Banjarbaru",
        "Kotamobagu",
        "Tanjungbalai",
        "Tebingtinggi",
        "Pematangsiantar",
        "Binjai",
        "Gunungsitoli",
        "Telukdalam",
        "Padangsidempuan",
        "Rantau Prapat"
    ]
    provinces = [
        "DKI Jakarta",
        "Jawa Timur",
        "Jawa Barat",
        "Sumatera Utara",
        "Jawa Tengah",
        "Sumatera Selatan",
        "Sulawesi Selatan",
        "Jawa Barat",
        "Jawa Barat",
        "Banten",
        "Jawa Barat",
        "Jawa Timur",
        "DI Yogyakarta",
        "Kepulauan Riau",
        "Riau",
        "Kalimantan Timur",
        "Kalimantan Timur",
        "Sumatera Barat",
        "Kalimantan Selatan",
        "Kalimantan Barat",
        "Sulawesi Utara",
        "Bali",
        "Lampung",
        "Jambi",
        "Jawa Tengah",
        "Maluku",
        "Sulawesi Tengah",
        "Sulawesi Tenggara",
        "Gorontalo",
        "Nusa Tenggara Barat",
        "Sulawesi Utara",
        "Sulawesi Utara",
        "Sulawesi Utara",
        "Sulawesi Tengah",
        "Sulawesi Tenggara",
        "Maluku",
        "Papua",
        "Papua",
        "Papua",
        "Papua Barat",
        "Papua",
        "Papua",
        "Papua",
        "Papua Barat",
        "Papua Barat",
        "Nusa Tenggara Barat",
        "Nusa Tenggara Barat",
        "Nusa Tenggara Barat",
        "Nusa Tenggara Barat",
        "Nusa Tenggara Barat",
        "Nusa Tenggara Timur",
        "Nusa Tenggara Timur",
        "Nusa Tenggara Timur",
        "Nusa Tenggara Timur",
        "Nusa Tenggara Timur",
        "Nusa Tenggara Timur",
        "Nusa Tenggara Timur",
        "Kalimantan Barat",
        "Kalimantan Utara",
        "Kalimantan Tengah",
        "Kalimantan Selatan",
        "Sulawesi Utara",
        "Sumatera Utara",
        "Sumatera Utara",
        "Sumatera Utara",
        "Sumatera Utara",
        "Sumatera Utara",
        "Sumatera Utara",
        "Sumatera Utara",
        "Sumatera Utara"
    ]
    sql = ""
    for i in range(len(city)):
        kode = fake.bothify(text='%%%-???', letters=alfabet)
        sql += f"INSERT INTO kategori (kode, nama, kode_provinsi) VALUES(`{kode}`, `{city[i]}`, `{getCodeProvince(provinces[i])}`)\n"
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
