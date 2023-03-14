import psycopg2

def connect():
    with psycopg2.connect(dbname='testdb', user='postgres', password='123', host='localhost') as connect:
        cursor = connect.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Tasks(Numbers text,Name text,Categorys text, Complexity integer, Count text)')
        connect.commit()
def update(title):
    with psycopg2.connect(dbname='testdb', user='postgres', password='123', host='localhost') as connect:
        cursor = connect.cursor()
        cursor.execute(f'INSERT INTO Tasks VALUES(%s, %s, %s, %s, %s)', tuple(title))
        connect.commit()

def get_data():
    with psycopg2.connect(dbname='testdb', user='postgres', password='123', host='localhost') as connect:
        cursor = connect.cursor()
        cursor.execute('SELECT Numbers FROM Tasks')
        connect.commit()
lst = [800,'math']


def get_result(lst):
    with psycopg2.connect(dbname='testdb', user='postgres', password='123', host='localhost') as connect:
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM Tasks WHERE complexity = {lst[0]} and categorys = '{lst[1]}' ORDER BY RANDOM() LIMIT 10")
        cursor.fetchall()
print(get_result(lst))


def test(lst):
    connection = psycopg2.connect(dbname='testdb', user='postgres', password='123', host='localhost')
    cursor = connection.cursor()
    cursor.execute(f"SELECT name, categorys, complexity FROM Tasks WHERE complexity = {lst[0]} and categorys = '{lst[1]}' ORDER BY RANDOM() LIMIT 10")
    return cursor.fetchall()

def test2(a):
    connection = psycopg2.connect(dbname='testdb', user='postgres', password='123', host='localhost')
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM Tasks WHERE name = '{a}'")
    return cursor.fetchall()