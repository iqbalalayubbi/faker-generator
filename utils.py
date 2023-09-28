from faker import Faker
fake = Faker()

def getRandomCode(text, letter):
    kode = fake.bothify(text=text, letters=letter)
    return kode