import sqlite3


def retrieve_bot():
    # connect to database
    db = sqlite3.connect("sqlite/bots.db")
    cursor = db.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    # retrieve a single record and display
    single_row = cursor.fetchone()
    print(f"Single bot in the system: \n{single_row}")
    db.close()


def retrieve_bots():
    # connect to database
    db = sqlite3.connect("sqlite/bots.db")
    cursor = db.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    # retrieve all records
    records = cursor.fetchall()
    print("\nAll bots in the system:")
    for record in records:
        print(record)
    db.close()


def run():
    retrieve_bot()
    retrieve_bots()


if __name__ == "__main__":
    run()