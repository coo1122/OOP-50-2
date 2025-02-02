import sqlite3

db = sqlite3.connect("Users.db")
cursor = db.cursor()


def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
                   """)
    db.commit()


create_table()


def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    db.commit()
    print(f"Добавлен {name}")


# add_user("Adilet", 20, "football")
# add_user("Ramazan", 20, "swimming")
# add_user("Shah", 20, "volleyball")
# add_user("Uluk", 20, "basketball")


def update_user_by_rowid(name=None, age=None, hobby=None, rowid=None):
    if name:
        cursor.execute(
            'UPDATE users SET name = ? WHERE rowid = ?',
            (name, rowid)
        )
    if age:
        cursor.execute(
            'UPDATE users SET age = ? WHERE rowid = ?',
            (age, rowid)
        )
    if hobby:
        cursor.execute(
            'UPDATE users SET hobby = ? WHERE name = ?',
            (hobby, name)
        )

    db.commit()
    print('Update success')


# update_user_by_rowid(name="Вася", hobby="Гулять")


def delete_user_by_rowid(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    db.commit()
    print('DELETE success')


# delete_user_by_rowid(2)


def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(f"-----{users}")

    if users:
        print("Список всех пользователей:")
        for user in users:
            print(f"Name: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")
    else:
        print(f"Список пользователей пуст")


# get_all_users()

def detail_view_user_by_id(id):
    cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
    user = cursor.fetchone()
    if user:
        print(f"Пользователь №{id}: {user}")
    else:
        print(f"Пользователь с id {id} не существует.")

# detail_view_user_by_id(4)

db.close()