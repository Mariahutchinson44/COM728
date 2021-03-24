import sqlite3
import csv


def read_data_file(file_path):
    # read all the lines from the specified file and return them in a list
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        data_file = []
        for values in csv_reader:
            data_file.append(values)

    return data_file


def insert_to_db(bot_data):
    # The function should insert each item (record for a bot) from the list into the table users.
    db = sqlite3.connect("sqlite/bots.db")
    cursor = db.cursor()
    print("Inserting data into database...")
    for data in bot_data:
        sql = "INSERT INTO users " \
            "(name, maximum_speed, maximum_strength, date, manufacturer_id)" \
            "VALUES" \
            f"(?, ?, ?, ?, ?);"
        values = [data[0], data[1], data[2], data[3], data[4]]
        cursor.execute(sql,values)

    db.commit()
    db.close()
    print("Done! 3 records inserted.")


def run():
    print("Please enter a file path:")
    file_path = input()
    bot_data = read_data_file(file_path)
    insert_to_db(bot_data)



if __name__ == "__main__":
    run()
