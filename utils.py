from faker import Faker
fake = Faker()
import pandas as pd

def getRandomCode(text, letter):
    kode = fake.bothify(text=text, letters=letter)
    return kode

def getData(sheet:str, rowsTotal:int):
    dfs = pd.read_excel("data.xlsx", sheet_name=sheet, nrows=rowsTotal)
    return dfs.to_numpy()