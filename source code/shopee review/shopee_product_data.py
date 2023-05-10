import pandas as pd
import mysql.connector

# json data
# product_data = pd.read_json('data\shopee_product_spiill.json')

# mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="spill_data"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM shopee_product_spiill")

def show_all_data():
    product_data = mycursor.fetchall()

    for row in product_data:
        print(row)

def get_one_data():
    return mycursor.fetchone()

def get_all_data():
    return mycursor.fetchall()

def get_all_data_as_dict():
    product_data = mycursor.fetchall()
    columns = [desc[0] for desc in mycursor.description]
    
    result_list = []
    for row in product_data:
        result_dict = dict(zip(columns, row))
        result_list.append(result_dict)
    return result_list

print(get_all_data_as_dict()[0])

# for item in get_all_data_as_dict():
#     print(item)