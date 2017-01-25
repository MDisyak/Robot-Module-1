import csv
import matplotlib.pyplot as plt
def main():
    y =


    fig = figure()
    with open(fileName, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for column in plots:
            y.append(int(column[col]))
    plt.plot(y)
    plt.show()


if __name__ == '__main__':
    main()
    show()