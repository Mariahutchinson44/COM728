def export(file_path, num_bots):
    print("Exporting...")
    with open(file_path, "a") as file:
        # repeats for number of bots to be exported
        for count in range(num_bots):
            print("Please enter the bot id:")
            bot_id = int(input())
            print("Please enter the bot name:")
            bot_name = input()
            print("Please enter the bot paint:")
            bot_paint = input()
            #appends each bot to the file, then a new line
            file.write(f"{bot_id},{bot_name},{bot_paint}\n")
        print("Done!")


def run():
    export("exported_bots.csv", 2)


if __name__ == "__main__":
    run()
