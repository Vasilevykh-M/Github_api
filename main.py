import psycopg2 #https://www.psycopg.org/docs/
import sqlite3 #https://docs.python.org/3/library/sqlite3.html
from class_table import *
import re
import xlrd, xlwt, openpyxl #https://habr.com/ru/post/232291/

def postgres_con(request): # подключение к БД postgres
    try:
        con = psycopg2.connect(
            database="supply",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432"
        )

        cur = con.cursor()
        cur.execute(request)
        rows = []

        if re.search('SELECT.+', request):
            rows = cur.fetchall()
        else:
            con.commit()
        print("Complete!!!")
        con.close()
        return rows
    except psycopg2.Error as error:
        print("Error connect!!!")

def sqlite_con(): # подключение к БД Sqlite
    try:
        con = sqlite3.connect("C:\\Users\\Михаил\\Desktop\\Прога\\Прога чистая\\Распределенки\\DB_supply.db")
        cur = con.cursor()
        cur.execute('''SELECT * FROM supply''')
        rows = cur.fetchall()
        print("Complete")
        con.close()
        return  rows
    except sqlite3.Error as error:
        print("Error connect!!!")

def import_data():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test')


if __name__ == '__main__':
    rows = sqlite_con()

    countrys_list = []
    citys_list = []
    stores_list = []
    products_list = []
    product_groups_list = []
    supplys_list = []

    for row in rows:
        countrys_list.append(Country(row[0], row[1]))
        citys_list.append(City(row[2], row[3]))
        stores_list.append(Store(row[4], row[5]))
        products_list.append(Product(row[6], row[7], row[8], row[9]))
        product_groups_list.append(Product_group(row[9], row[10]))
        supplys_list.append(Supply(row[0], row[2], row[4], row[6], row[12], row[11]))

    for egge in product_groups_list:
        if postgres_con("SELECT COUNT(*) FROM product_group WHERE id_product_group = {0}".format(str(egge.id_product_group)))[0][0] == 0:
            postgres_con("INSERT INTO product_group (id_product_group, product_group) VALUES ({0}, '{1}')".format(
                str(egge.id_product_group), egge.product_group))

    for egge in products_list:
        if postgres_con("SELECT COUNT(*) FROM product WHERE id_product = {0}".format(str(egge.id_product)))[0][0] == 0:
            postgres_con("INSERT INTO product (id_product, product, price, id_product_group) VALUES ({0}, '{1}', {2}, {3})".format(
                str(egge.id_product), egge.product, egge.price, egge.id_product_group))

    for egge in citys_list:
        if postgres_con("SELECT COUNT(*) FROM city WHERE id_city = {0}".format(str(egge.id_city)))[0][0] == 0:
            postgres_con("INSERT INTO city (id_city, city) VALUES ({0}, '{1}')".format(
                str(egge.id_city), egge.city))

    for egge in countrys_list:
        if postgres_con("SELECT COUNT(*) FROM country WHERE id_country = {0}".format(str(egge.id_country)))[0][0] == 0:
            postgres_con("INSERT INTO country (id_country, country) VALUES ({0}, '{1}')".format(
                str(egge.id_country), egge.country))

    for egge in stores_list:
        if postgres_con("SELECT COUNT(*) FROM store WHERE id_store = {0}".format(str(egge.id_store)))[0][0] == 0:
            postgres_con("INSERT INTO store (id_store, store) VALUES ({0}, '{1}')".format(
                str(egge.id_store), egge.store))

    for egge in supplys_list:
        if postgres_con(
                "SELECT COUNT(*) "
                "FROM supply "
                "WHERE id_country = {0} AND id_city = {1} AND id_store = {2} AND id_product = {3} AND shipping_date = '{4}'".
                                format(str(egge.id_store), str(egge.id_city), str(egge.id_store), str(egge.id_product), str(egge.shipping_date)))[0][0] == 0:
            postgres_con("INSERT INTO supply (id_country, id_city, id_store, id_product, shipping_date, cout_product) VALUES ({0}, {1}, {2}, {3}, '{4}', {5})".format(
                str(egge.id_country), str(egge.id_city), str(egge.id_store), str(egge.id_product), str(egge.shipping_date), str(egge.count_product)))



