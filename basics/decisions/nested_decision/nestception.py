# ask where to look
print("Where should I look (bedroom/bathroom/lab or other)?")
location = input()

# decide if cover is hard or soft
if location == "bedroom":
    # ask where
    print("Where in the bedroom should I look (under the bed or other)?")
    bedroom_location = input()

    # decide on response
    if bedroom_location == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery." )
elif location == "bathroom":
    # ask where
    print("Where in the bathroom should I look (in the bathtub or other)?")
    bathroom_location = input()

    # decide on response
    if bathroom_location == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")

elif location == "lab":
    # ask where
    print("Where in the lab should I look (on the table or other)?")
    lab_location = input()

    # decide on response
    if lab_location == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

else:
    print("I do not know where that is but I will keep looking.")