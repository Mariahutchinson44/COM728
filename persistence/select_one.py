import sqlite3


def retrieve_bot():
    # connect to database
    db = sqlite3.connect("sqlite/bots.db")
    cursor = db.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    # retrieve a single record and display
    single_row = cursor.fetchone()
    print(single_row)
    db.close()


def run():
    retrieve_bot()


if __name__ == "__main__":
    run()