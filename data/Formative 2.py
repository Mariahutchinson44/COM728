def gang():
    print("Loading gang...")
    friends = ["Scooby Doo", "Shaggy Rogers", "Fred Jones", "Daphne Blake", "Velma Dinkley"]
    print(friends)
    print("Done!")
    return friends

def phrases(friends):
    quotes = {}
    for friend in friends:
        print(f"What does {friend} say?")
        quote = input()
        quotes[f"{friend}"] = quote
    return quotes

def save(quotes):
    with open("quotes.txt", "w") as file:
       for friend, quote in quotes.items():
            file.write(f"{friend}: {quote}\n")


friends = gang()
quotes = phrases(friends)
save(quotes)
print("The file contains...")
with open("quotes.txt") as file:
    print(file.read())
