import database as database


def menu():
    # display menu options and return integer
    print("""
      Please select one of the following options:
      
      [0] Load database
      [1] Display presenters
      [2] Display events
      [3] Display presenters for event
      [4] Display events for presenter

      Your selection:
      """)
    response = int(input())
    return response


def run():
    response = menu()
    if response == 0:
        events = database.load_csv_data()
        database.create_database()
        database.load_database(events)
    elif response == 1:
        database.display_presenters()
    elif response == 2:
        database.display_events()
    elif response == 3:
        print("Please enter event id")
        event_id = int(input())
        database.display_presenters_for_event(event_id)
    elif response == 4:
        print("Please enter presenter id")
        presenter_id = int(input())
        database.display_events_for_presenter(presenter_id)
    else:
        print("Invalid selection")


if __name__ == "__main__":
    run()
