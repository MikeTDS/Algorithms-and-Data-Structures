import numpy
from matplotlib import pyplot as plt
import sys

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def handle_data(input_data):
    data = []
    temp = input_data.split('\n')
    for i in temp:
        data.append(i.split(';'))
    return data

def compares_data(data):
    x_label = []
    compares = []
    for row in data:
        x_label.append(int(row[0]))
        compares.append(int(row[1]))
    return x_label, compares

def time_data(data):
    x_label = []
    timee = []
    for row in data:
        x_label.append(int(row[0]))
        timee.append(float(row[2]))
    return x_label, timee

def plot_compares(comp):
    plt.title('Compares')
    plt.xlabel('n')
    plt.ylabel('compares')
    plt.plot(comp[0], comp[1])
    plt.savefig('plot_bst_compares.png')
    plt.show()
    plt.cla()

def plot_time(timee):
    plt.title('Time')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.plot(timee[0], timee[1])
    plt.savefig('plot_bst_time.png')
    plt.show()
    plt.cla()

def main():
    input_data = read_file('bst.data')
    data = handle_data(input_data[:-1])
    comp = compares_data(data)
    timee = time_data(data)
    plot_compares(comp)
    plot_time(timee)

    

if __name__ == "__main__":
    main()