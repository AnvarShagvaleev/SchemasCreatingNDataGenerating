import sqlite3
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///shop.db') # создаем БД

# считываем данные с Excel
categories = pd.read_excel('DataFull.xlsx', sheet_name='sr.1') 
products = pd.read_excel('DataFull.xlsx', sheet_name='sr.2', index_col='id')
sells = pd.read_excel('DataFull.xlsx', sheet_name='sr.3', index_col='id')
suppliers = pd.read_excel('DataFull.xlsx', sheet_name='sr.4', index_col='id')
sup_to_prod = pd.read_excel('DataFull.xlsx', sheet_name='sr.5', index_col='id')

# заполняем БД сущностями и записями в них
categories.to_sql('categories', con=engine, if_exists='append')
products.to_sql('products', con=engine, if_exists='append')
sells.to_sql('sells', con=engine, if_exists='append')
suppliers.to_sql('suppliers', con=engine, if_exists='append')
sup_to_prod.to_sql('sup_to_prod', con=engine, if_exists='append')