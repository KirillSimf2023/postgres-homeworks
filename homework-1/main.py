"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv



def main():

    insert_to_DB("INSERT INTO customers VALUES (%s,%s,%s)",'customers_data.csv')
    insert_to_DB("INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s)", 'employees_data.csv')
    insert_to_DB("INSERT INTO orders VALUES (%s,%s,%s,%s,%s)", 'orders_data.csv')




def insert_to_DB(query, file_name):
    # CONNECT TO DB
    conn = psycopg2.connect(host="localhost", database="North", user="postgres", password="0000")
    try:
        with conn:
            with conn.cursor() as cur:
                with open(f'north_data/{file_name}', 'r', encoding='UTF-8') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        # проверяет является ли ряд названием колонок
                        if row[0] == 'customer_id' or row[0] == 'order_id' or row[0] == 'employee_id':
                            continue
                        cur.execute(query, row)
    finally:
        conn.close()






if __name__ == '__main__':
    main()



