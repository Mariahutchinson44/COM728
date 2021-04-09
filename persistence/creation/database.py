import sqlite3
import csv
records = []

def load_csv_data():
    with open("events.csv") as file:
        csv_reader = csv.reader(file)
        # identify and ignore headings
        next(csv_reader)
        for value in csv_reader:
            # append each list to the global variable
            records.append(value)
    return records

def create_database():
    db = sqlite3.connect("events3.db")
    cursor = db.cursor()
    sql = "CREATE TABLE locations (" \
          "id INTEGER NOT NULL UNIQUE," \
          "city TEXT NOT NULL UNIQUE," \
          "country TEXT NOT NULL," \
          "PRIMARY KEY(id AUTOINCREMENT)" \
          ");"
    cursor.execute(sql)
    db.commit()

    sql = "CREATE TABLE organisations (" \
          "id INTEGER NOT NULL UNIQUE," \
          "name TEXT NOT NULL UNIQUE," \
          "location_id INTEGER NOT NULL," \
          "PRIMARY KEY(id AUTOINCREMENT)," \
          "FOREIGN KEY(location_id) REFERENCES locations(id)" \
          ");"
    cursor.execute(sql)
    db.commit()

    sql = "CREATE TABLE events (" \
          "id INTEGER NOT NULL UNIQUE," \
          "name TEXT NOT NULL," \
          "type TEXT NOT NULL CHECK(type == 'presentation' OR type == 'workshop' OR type == 'seminar')," \
          "host_id INTEGER," \
          "PRIMARY KEY(id AUTOINCREMENT)," \
          "FOREIGN KEY(host_id) REFERENCES organisations(id)" \
          ");"
    cursor.execute(sql)
    db.commit()

    sql = "CREATE TABLE presenters (" \
          "id INTEGER NOT NULL UNIQUE," \
          "first_name TEXT NOT NULL," \
          "last_name TEXT NOT NULL," \
          "organisation_id INTEGER," \
          "PRIMARY KEY(id AUTOINCREMENT)," \
          "FOREIGN KEY(organisation_id) REFERENCES organisations(id)" \
          ");"
    cursor.execute(sql)
    db.commit()

    sql = "CREATE TABLE events_presenters (" \
          "presenter_id INTEGER NOT NULL," \
          "event_id INTEGER NOT NULL," \
          "FOREIGN KEY(presenter_id) REFERENCES presenters(id)," \
          "FOREIGN KEY(event_id) REFERENCES events(id)" \
          ");"
    cursor.execute(sql)
    db.commit()

    db.close()

def load_database(events):
    # Locations, Organisations, Events, Presenters, Events_Presenters
    # If the name already exists then you retrieve the existing id otherwise you insert the record and get the new
    # id that has been generated.
    # to avoid duplicates in the database you should ensure that a suitable constraint has been added to the
    # relevant table(i.e.should have unique records).

    for event in events:

        db = sqlite3.connect("events3.db")
        cursor = db.cursor()

        # ****SORTED*****
        city, country = event[2].split(",")
        value = [city]
        values = [city, country]
        # checks if city exists before inserting in table
        sql = "SELECT id FROM locations WHERE city = ?"
        cursor.execute(sql, value)
        # this data is returned as an empty list is it does not exist [],
        # or as a list containing a single-item tuple in the form [(n,)]
        data = cursor.fetchall()
        if len(data) == 0:
            sql = "INSERT INTO locations " \
                  "(city, country) " \
                  "VALUES " \
                  "(?, ?)"
            cursor.execute(sql, values)
            db.commit()
            # this will become the FK in organisations table
            pres_org_loc_id = cursor.lastrowid
        else:
            # unpacks single item tuple to get id
            (pres_org_loc_id,) = data[0]


        # ***SORTED***
        city, country = event[6].split(",")
        value = [city]
        values = [city, country]
        # checks if city exists before inserting in table
        sql = "SELECT id FROM locations WHERE city = ?"
        cursor.execute(sql, value)
        # this data is returned as an empty list is it does not exist [],
        # or as a list containing a single-item tuple in the form [(n,)]
        data = cursor.fetchall()
        if len(data) == 0:
            sql = "INSERT INTO locations " \
                  "(city, country) " \
                  "VALUES " \
                  "(?, ?)"
            cursor.execute(sql, values)
            db.commit()
            # this will become the FK in organisations table
            event_org_loc_id = cursor.lastrowid
        else:
            # unpacks single item tuple to get id
            (event_org_loc_id,) = data[0]

        values = [event[1], pres_org_loc_id]
        value = [event[1]]
        # Check if organisation exists before inserting into table
        sql = "SELECT id FROM organisations WHERE name = ?"
        cursor.execute(sql, value)
        # this data is returned as an empty list is it does not exist [],
        # or as a list containing a single-item tuple in the form [(n,)]
        data = cursor.fetchall()
        if len(data) == 0:
            sql = "INSERT INTO organisations " \
              "(name, location_id) " \
              "VALUES " \
              "(?, ?)"
            cursor.execute(sql, values)
            db.commit()
            # This will become the FK in the presenters table
            pres_org_id = cursor.lastrowid
        else:
            # unpacks single item tuple to get id
            (pres_org_id,) = data[0]

        values = [event[4], event_org_loc_id]
        value = [event[4]]
        # Check if organisation exists before inserting into table
        sql = "SELECT id FROM organisations WHERE name = ?"
        cursor.execute(sql, value)
        # this data is returned as an empty list is it does not exist [],
        # or as a list containing a single-item tuple in the form [(n,)]
        data = cursor.fetchall()
        if len(data) == 0:
            sql = "INSERT INTO organisations " \
              "(name, location_id) " \
              "VALUES " \
              "(?, ?)"
            cursor.execute(sql, values)
            db.commit()
            # This will become the FK in the events table
            host_org_id = cursor.lastrowid
        else:
            # unpacks single item tuple to get id
            (host_org_id,) = data[0]

        values = [event[3], event[5], host_org_id]
        value = [event[3], event[5]]
        # Check if event name AND type exists before inserting into table
        sql = "SELECT id FROM events WHERE name = ? AND type = ?"
        cursor.execute(sql, value)
        # this data is returned as an empty list is it does not exist [],
        # or as a list containing a single-item tuple in the form [(n,)]
        data = cursor.fetchall()
        if len(data) == 0:
            sql = "INSERT INTO events " \
                  "(name, type, host_id) " \
                  "VALUES " \
                  "(?, ?, ?)"
            cursor.execute(sql, values)
            db.commit()
            # this will become the FK for the events_presenters table
            event_id = cursor.lastrowid
        else:
            # unpacks single item tuple to get id
            (event_id,) = data[0]

        # convert from comma separated string to a list
        presenters_list = event[0].split(",")
        for presenter in presenters_list:
            first_name, last_name = presenter.split()
            values = [first_name, last_name, pres_org_id]
            value = [first_name, last_name]
            # Check if presenter first_name AND last_name exists before inserting into table
            sql = "SELECT id FROM presenters WHERE first_name = ? AND last_name = ?"
            cursor.execute(sql, value)
            # this data is returned as an empty list is it does not exist [],
            # or as a list containing a single-item tuple in the form [(n,)]
            data = cursor.fetchall()
            if len(data) == 0:
                sql = "INSERT INTO presenters " \
                      "(first_name, last_name, organisation_id) " \
                      "VALUES " \
                      "(?, ?, ?)"
                cursor.execute(sql, values)
                db.commit()
                # this will become the FK for the events_presenters table
                presenter_id = cursor.lastrowid
            else:
                # unpacks single item tuple to get id
                (presenter_id,) = data[0]

            values = [presenter_id, event_id]
            # check if presenter_id AND event_id exists before inserting
            sql = "SELECT rowid FROM events_presenters WHERE presenter_id = ? AND event_id = ?"
            cursor.execute(sql, values)
            # this data is returned as an empty list is it does not exist [],
            # or as a list containing a single-item tuple in the form [(n,)]
            data = cursor.fetchall()
            if len(data) == 0:
                sql = "INSERT INTO events_presenters " \
                      "(presenter_id, event_id) " \
                      "VALUES " \
                      "(?, ?)"
            cursor.execute(sql, values)
            db.commit()

    db.close()

# Display a list of all presenters with their organisations
def display_presenters():
    db = sqlite3.connect("events3.db")
    cursor = db.cursor()
    sql = "SELECT first_name, last_name, organisations.name " \
          "FROM presenters " \
          "INNER JOIN organisations ON presenters.organisation_id = organisations.id"

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()

    for record in records:
        print(record)


# Display a list of all events with their locations
def display_events():
    db = sqlite3.connect("events3.db")
    cursor = db.cursor()
    sql = "SELECT events.name, locations.city, locations.country " \
          "FROM events " \
          "INNER JOIN organisations ON events.host_id = organisations.id " \
          "INNER JOIN locations ON organisations.location_id = locations.id"

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()

    for record in records:
        print(record)


# Display a list of all presenters for a specified event
def display_presenters_for_event(event_id):
    db = sqlite3.connect("events3.db")
    cursor = db.cursor()
    sql = "SELECT events.name, first_name, last_name " \
          "FROM events " \
          "INNER JOIN events_presenters ON events_presenters.event_id = events.id " \
          "INNER JOIN presenters on events_presenters.presenter_id = presenters.id " \
          f"WHERE events.id = {event_id} "

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()

    event_name = ""
    for _ in range(1):
        for record in records:
            event_name = record[0]

    print(f"The name of the event is: {event_name}\n")
    print("The presenters for this event are as follows:")

    for record in records:
        # first name, last name
        print(f"{record[1]} {record[2]}")


# Display a list of all events for a specific presenter
def display_events_for_presenter(presenter_id):
    db = sqlite3.connect("events3.db")
    cursor = db.cursor()
    sql = "SELECT first_name, last_name, events.name " \
          "FROM presenters " \
          "INNER JOIN events_presenters ON events_presenters.presenter_id = presenters.id " \
          "INNER JOIN events on events_presenters.event_id = events.id " \
          f"WHERE presenters.id = {presenter_id} "

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()

    first_name = ""
    last_name = ""
    for _ in range(1):
        for record in records:
            first_name = record[0]
            last_name = record[1]

    print(f"The name of the presenter is: {first_name} {last_name}\n")
    print("The events for this presenter are as follows:")
    for record in records:
        print(f"{record[2]}")
