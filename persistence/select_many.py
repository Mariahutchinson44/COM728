import sqlite3

def retrieve_bots(num_bots=None):
    # connect to database
    db = sqlite3.connect("sqlite/bots.db")
    cursor = db.cursor()

    sql = "SELECT * FROM users"
    cursor.execute(sql)

    if num_bots == None:
        # retrieve all records
        records = cursor.fetchall()
    else:
        records = cursor.fetchmany(num_bots)

    db.close()

    for record in records:
        print(record)

def run():
    print("First 3 bots in the system:")
    retrieve_bots(3)


if __name__ == "__main__":
    run()