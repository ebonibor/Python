import psycopg2

# Параметры подключения к вашей базе данных PostgreSQL
dbname = "ServiceCenter"
user = "postgres"
password = "Jpc3djzs"
host = "localhost"

# Функция для установления соединения с базой данных
def connect():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    return conn

# Функция для добавления нового клиента
def add_client(name, surname, contact_number, email):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO "Client" ("FirstName", "LastName", "ContactNumber", "Email") VALUES (%s, %s, %s, %s)', (name, surname, contact_number, email))
        conn.commit()
    except psycopg2.Error as e:
        print("Ошибка при добавлении клиента:", e)
    finally:
        cursor.close()
        conn.close()

# Функция для получения списка клиентов
def get_clients():
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM "Client"')
        clients = cursor.fetchall()  # Получаем всех клиентов в виде списка кортежей
        return clients
    except psycopg2.Error as e:
        print("Ошибка при получении списка клиентов:", e)
    finally:
        cursor.close()
        conn.close()

# Функция для обновления данных клиента
def update_client(client_id, name):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE clients SET name = %s WHERE id = %s", (name, client_id))
        conn.commit()
    except psycopg2.Error as e:
        print("Ошибка при обновлении клиента:", e)
    finally:
        cursor.close()
        conn.close()

# Функция для удаления клиента
def delete_client(client_id):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clients WHERE id = %s", (client_id,))
        conn.commit()
    except psycopg2.Error as e:
        print("Ошибка при удалении клиента:", e)
    finally:
        cursor.close()
        conn.close()
