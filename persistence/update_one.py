import sqlite3


def get_bot_id_from_user():
    print("Please enter bot id:")
    bot_id = int(input())
    return bot_id


def display_bot_from_db(bot_id):
    db = sqlite3.connect("sqlite/bots.db")
    cursor = db.cursor()

    sql = f"SELECT * FROM users WHERE id={bot_id}"
    cursor.execute(sql)
    # retrieve a single record and display
    bot = cursor.fetchone()
    print("\nCurrent bot details are as follows:")
    print(f"id: {bot[0]}, name: {bot[1]}, maximum_speed: {bot[2]}, maximum_strength: {bot[3]}, " \
          f" date: {bot[4]}, manufacturer: {bot[5]}")
    db.close()



def get_bot_details_from_user():
    print("\nWhat field would you like to change?")
    change = input()
    print(f"\nWhat is the new value for {change}?")
    new_value = input()

    details = [change, new_value]
    return details


def update_bot_in_db(bot_id, details):
    db = sqlite3.connect("sqlite/bots.db")
    cursor = db.cursor()
    sql = f"UPDATE users SET {details[0]}='{details[1]}' WHERE id={bot_id}"
    cursor.execute(sql)
    # sql = "UPDATE users SET ?=? WHERE id=?"
    # values = [details[0], details[1], bot_id]
    cursor.execute(sql)

    db.commit()
    db.close()
    print("\nThe record has been updated.")

def run():
    bot_id = get_bot_id_from_user()
    display_bot_from_db(bot_id)
    details = get_bot_details_from_user()
    update_bot_in_db(bot_id, details)


if __name__ == "__main__":
    run()