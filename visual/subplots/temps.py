import matplotlib.pyplot as plt

def read_data(file_path_name):
    temps = []
    with open(file_path_name) as file:
        for line in file:
            temps.append(line.strip())


def run():


if __name__ == "__main__":
    run()
