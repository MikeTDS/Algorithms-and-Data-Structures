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

def avg_compares(data):
    x_label = []
    avgs = []
    counter = 0
    total = 0
    x_data = [10,50,100,500,1000,5000,10000,50000,100000]
    idd = 0
    current = x_data[idd]
    for row in data:
        if int(row[0]) != current:
            x_label.append(current)
            avgs.append(total/counter)
            total = int(row[1])
            counter = 1
            idd += 1
            current = x_data[idd]
        else:
            counter += 1
            total += int(row[1])
    x_label.append(current)
    avgs.append(total/counter)
    return x_label, avgs

def avg_swaps(data):
    x_label = []
    avgs = []
    counter = 0
    total = 0
    x_data = [10,50,100,500,1000,5000,10000,50000,100000]
    idd = 0
    current = x_data[idd]
    for row in data:
        if int(row[0]) != current:
            x_label.append(current)
            avgs.append(total/counter)
            total = int(row[2])
            counter = 1
            idd += 1
            current = x_data[idd]
        else:
            counter += 1
            total += int(row[2])
    x_label.append(current)
    avgs.append(total/counter)
    return x_label, avgs

def avg_time(data):
    x_label = []
    avgs = []
    counter = 0
    total = 0
    x_data = [10,50,100,500,1000,5000,10000,50000,100000]
    idd = 0
    current = x_data[idd]
    for row in data:
        if int(row[0]) != current:
            x_label.append(current)
            avgs.append(total/counter)
            total = float(row[3])
            counter = 1
            idd += 1
            current = x_data[idd]
        else:
            counter += 1
            total += float(row[3])
    x_label.append(current)
    avgs.append(total/counter)
    return x_label, avgs

def memory_usage(data):
    x_label = []
    avgs = []
    counter = 0
    total = 0
    x_data = [10,50,100,500,1000,5000,10000,50000,100000]
    idd = 0
    current = x_data[idd]
    for row in data:
        if int(row[0]) != current:
            x_label.append(current)
            avgs.append(total/counter)
            total = float(row[4])
            counter = 1
            idd += 1
            current = x_data[idd]
        else:
            counter += 1
            total += float(row[4])
    x_label.append(current)
    avgs.append(total/counter)
    return x_label, avgs

def plot_all_avg_compares(data, file_list):
    plt.title('Average compares')
    plt.xlabel('n')
    plt.ylabel('avg compares')
    all_avg_s = []
    for i in range(len(data)):
        avg_s = avg_compares(data[i])
        plt.plot(avg_s[0], avg_s[1], label = file_list[i]) 
        all_avg_s.append(avg_s)

    plt.savefig('plot_all_avg_compares.png')
    plt.legend()
    plt.show()
    plt.cla()

def plot_all_avg_swaps(data, file_list):
    plt.title('Average swaps')
    plt.xlabel('n')
    plt.ylabel('avg swaps')
    all_avg_s = []
    for i in range(len(data)):
        avg_s = avg_swaps(data[i])
        plt.plot(avg_s[0], avg_s[1], label = file_list[i]) 
        all_avg_s.append(avg_s)

    plt.savefig('plot_all_avg_swaps.png')
    plt.legend()
    plt.show()
    plt.cla()

def plot_all_avg_time(data, file_list):
    plt.title('Average time')
    plt.xlabel('n')
    plt.ylabel('avg time')

    for i in range(len(data)):
        avg_t = avg_time(data[i])
        plt.plot(avg_t[0], avg_t[1], label = file_list[i])
    
    plt.savefig('plot_all_avg_time.png')
    plt.legend()
    plt.show()
    plt.cla()

def plot_all_mem_usage(data, file_list):
    plt.title('Average memory usage')
    plt.xlabel('n')
    plt.ylabel('avg mem-usage')

    for i in range(len(data)):
        avg_t = memory_usage(data[i])
        plt.plot(avg_t[0], avg_t[1], label = file_list[i])
    
    plt.savefig('plot_all_mem_usage.png')
    plt.legend()
    plt.show()
    plt.cla()

def plot_all(file_list):
    data = []

    for file in file_list:
        inp_data = read_file(file)
        data.append(handle_data(inp_data[:-1]))

    plot_all_avg_compares(data, file_list)
    plot_all_avg_swaps(data, file_list)
    plot_all_avg_time(data, file_list)
    plot_all_mem_usage(data, file_list)

def main():
    file_list = ['quick.data', 'merge.data', 'dp.data', 'hyb.data', 'radix.data']
    plot_all(file_list)
if __name__ == "__main__":
    main()