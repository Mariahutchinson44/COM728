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
          "FROM events e " \
          "INNER JOIN organisations o ON e.host_id = o.id " \
          "INNER JOIN locations l ON o.location_id = l.id"

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
          "FROM events e " \
          "INNER JOIN events_presenters ep ON ep.event_id = e.id " \
          "INNER JOIN presenters p on ep.presenter_id = p.id " \
          f"WHERE e.id = {event_id} "

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()


    print(f"The name of the event is: {record[0]}")
    print("The presenters for this event are as follows:")
    for record in records:
        # first name, last name
        print(f"{record[1]} {record[2]})")

# Display a list of all events for a specific presenter
def display_events_for_presenter(presenter_id):
    db = sqlite3.connect("events.db")
    cursor = db.cursor()
    sql = "SELECT first_name, last_name, events.name " \
          "FROM presenters p " \
          "INNER JOIN events_presenters ep ON ep.presenter_id = p.id " \
          "INNER JOIN events e on ep.event_id = e.id " \
          f"WHERE p.id = {presenter_id} "

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()

    print(f"The name of the presenter is: {record[0], record[1]}")
    print("The events for this presenter are as follows:")
    for record in records:
        print(f"{record[2]}")