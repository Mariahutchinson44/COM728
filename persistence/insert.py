import sqlite3


def get_bot_from_user():
    print("Please enter the bot name:")
    name = input()
    print("Please enter maximum speed:")
    speed = int(input())
    print("Please enter maximum strength:")
    strength = int(input())
    print("Please enter creation date:")
    date = input()
    print("Please enter manufacturer id:")
    manufacturer = int(input())
    new_bot_data = [name, speed, strength, date, manufacturer]
    return new_bot_data


def insert_bot_in_db(data):
    db = sqlite3.connect("sqlite/bots.db")
    cursor = db.cursor()
    sql = "INSERT INTO users " \
        "(name, maximum_speed, maximum_strength, date, manufacturer_id)"\
        "VALUES"\
        f"('{data[0]}', {data[1]}, {data[2]}, '{data[3]}', {data[4]});"

    cursor.execute(sql)

    db.commit()

    row_id = cursor.lastrowid
    print("The record has been added to the database.")
    print(f"The record id is {row_id}")

    db.close()


def run():
   bot_data = get_bot_from_user()
   insert_bot_in_db(bot_data)


if __name__ == "__main__":
    run()
