import json
# first function reads in and returns data
def read(file_path):
    print("Reading...", end="")
    with open(file_path) as file:
        data = json.load(file)
        print("Done!")
        return data

def save(file_path, data):
    print("Exporting...", end="")
    # The function should then open the specified file for writing.
    with open(file_path, "w") as file:
        # without the indent=4, it exported the data all on one line
        # The function should then write the data to the file.
        json.dump(data, file, indent=4)
        print("Done!")

def run():
    # calls first function, and stores returned value
    json_data = read("robocity.json")
    # calls second function and passes it the value to export
    save("exported.json", json_data)

if __name__ == "__main__":
  run()
