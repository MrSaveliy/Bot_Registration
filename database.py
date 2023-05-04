import sqlite3

database = sqlite3.connect("users_list")
cursor = database.cursor()
#cursor.execute('CREATE TABLE users(id INTEGER, gender TEXT, name TEXT, phone INTEGER, age INTEGER, city TEXT, university TEXT)')

def add_user(message):
    cursor.execute("SELECT id FROM users WHERE id=?", (message.chat.id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?)", 
                    (message.chat.id, 
                    "gender", "name","phone","age", "city","university"))
        database.commit()
    else:
        return False

def add_user_gender(message):
    cursor.execute("UPDATE users set gender=? WHERE id=?", (message.text, message.chat.id,))
    database.commit()

def add_user_name(message):
    cursor.execute("UPDATE users set name=? WHERE id=?", (message.text, message.chat.id,))
    database.commit()

def add_user_phone(message):
    cursor.execute("UPDATE users set phone=? WHERE id=?", (message.text, message.chat.id,))
    database.commit()

def add_user_age(message):
    cursor.execute("UPDATE users set age=? WHERE id=?", (message.text, message.chat.id,))
    database.commit()

def add_user_city(message):
    cursor.execute("UPDATE users set city=? WHERE id=?", (message.text, message.chat.id,))
    database.commit()

def add_user_university(message):
    cursor.execute("UPDATE users set university=? WHERE id=?", (message.text, message.chat.id,))
    database.commit()

def get_user_gender(user_id):
    cursor.execute("SELECT gender FROM users WHERE id=?", (user_id,))
    user_gender = cursor.fetchone()[0]
    return user_gender

def get_user_name(user_id):
    cursor.execute("SELECT name FROM users WHERE id=?", (user_id,))
    user_name = cursor.fetchone()[0]
    return user_name

def get_user_phone(user_id):
    cursor.execute("SELECT phone FROM users WHERE id=?", (user_id,))
    user_phone = cursor.fetchone()[0]
    return user_phone

def get_user_age(user_id):
    cursor.execute("SELECT age FROM users WHERE id=?", (user_id,))
    user_age = cursor.fetchone()[0]
    return user_age

def get_user_city(user_id):
    cursor.execute("SELECT city FROM users WHERE id=?", (user_id,))
    user_city = cursor.fetchone()[0]
    return user_city

def get_user_university(user_id):
    cursor.execute("SELECT university FROM users WHERE id=?", (user_id,))
    user_university = cursor.fetchone()[0]
    return user_university                             