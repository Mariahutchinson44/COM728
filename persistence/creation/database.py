import sqlite3


# Display a list of all presenters with their organisations
def display_presenters():
    db = sqlite3.connect("events.db")
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
    db = sqlite3.connect("events.db")
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
    db = sqlite3.connect("events.db")
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
        print(f"{record[1]} {record[2]})")


# Display a list of all events for a specific presenter
def display_events_for_presenter(presenter_id):
    db = sqlite3.connect("events.db")
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
