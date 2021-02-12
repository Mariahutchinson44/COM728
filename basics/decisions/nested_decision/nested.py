# ask cover type of book
print("What type of cover does the book have (soft/hard)?")
cover_type = input()

# decide if cover is hard or soft
if cover_type == "soft":
    # ask if perfect-bound
    print("Is the book perfect-bound (yes/no)?")
    binding = input()

    # decide if perfect-bound or not
    if binding == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")