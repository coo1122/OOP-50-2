import sqlite3

db = sqlite3.connect("UsersGrades.db")
cursor = db.cursor()


def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            usersid INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
                   """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades(
            gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER,
            subject VARCHAR (100) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (userid) REFERENCES users(usersid)
        )
                   """)

    db.commit()
    # print("Таблицы созданы или обновлены")


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


def add_grade_for_user(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (user_id, subject, grade)
    )
    db.commit()
    print(f"Добавлена оценка за предмет {subject} пользователю {user_id}")

# add_grade_for_user(4,"Math",5)
# add_grade_for_user(4,"History",4)
# add_grade_for_user(4,"English",3)
# add_grade_for_user(4,"Python",2)
# add_grade_for_user(4,"Java",1)

create_tables()