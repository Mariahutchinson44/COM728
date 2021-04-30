import matplotlib.pyplot as plt
import csv

def read_data():
    with open('temps.csv') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        # create a dictionary to store the data as key value pairs
        data = {'week1': [], 'week2': []}
        # read the csv file and append to list
        for line in csv_reader:
            data['week1'].append(float(line[0].strip()))
            data['week2'].append(float(line[1].strip()))
    return data


# create 2 subplots, one as a line graph, the other as a bar chart
def run():
    data = read_data()
    # arrange vertically
    fig, (ax1, ax2) = plt.subplots(2, 1)
    # share same x-axis
    # first plot week 1, second week 2
    ax1.plot(range(len(data['week1'])), data['week1'])
    ax2.plot(range(len(data['week2'])), data['week2'])
    plt.show()


if __name__ == "__main__":
    run()
