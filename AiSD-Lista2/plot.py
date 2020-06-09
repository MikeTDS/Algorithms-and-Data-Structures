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
    current = 100
    for row in data:
        if int(row[0]) != current:
            x_label.append(current)
            avgs.append(total/counter)
            total = int(row[1])
            counter = 1
            current += 100
        else:
            counter += 1
            total += int(row[1])
    return x_label, avgs

def avg_swaps(data):
    x_label = []
    avgs = []
    counter = 0
    total = 0
    current = 100
    for row in data:
        if int(row[0]) != current:
            x_label.append(current)
            avgs.append(total/counter)
            total = int(row[2])
            counter = 1
            current += 100
        else:
            counter += 1
            total += int(row[2])
    return x_label, avgs

def avg_time(data):
    x_label = []
    avgs = []
    counter = 0
    total = 0
    current = 100
    for row in data:
        if int(row[0]) != current:
            x_label.append(current)
            avgs.append(total/counter)
            total = float(row[3])
            counter = 1
            current += 100
        else:
            counter += 1
            total += float(row[3])
    return x_label, avgs

def compare_to_n(avg_c):
    xs, res = avg_c
    c_to_n = []
    for i in range(len(res)):
        c_to_n.append(float(res[i])/int(xs[i]))
    return xs, c_to_n

def swap_to_n(avg_s):
    xs, res = avg_s
    s_to_n = []
    for i in range(len(res)):
        s_to_n.append(float(res[i])/int(xs[i]))
    return xs, s_to_n


def plot_avg_compares(avg_c):
    plt.title('Average compares')
    plt.xlabel('n')
    plt.ylabel('avg compares')
    plt.plot(avg_c[0], avg_c[1])
    plt.savefig('plot_' + sys.argv[1] + '_avg_compares.png')
    plt.show()
    plt.cla()

def plot_avg_swaps(avg_s):
    plt.title('Average swaps')
    plt.xlabel('n')
    plt.ylabel('avg swaps')
    plt.plot(avg_s[0], avg_s[1])
    plt.savefig('plot_' + sys.argv[1] + '_avg_swaps.png')
    plt.show()
    plt.cla()

def plot_avg_time(avg_t):
    plt.title('Average time')
    plt.xlabel('n')
    plt.ylabel('avg time (ms)')
    plt.plot(avg_t[0], avg_t[1])
    plt.savefig('plot_' + sys.argv[1] + '_avg_time.png')
    plt.show()
    plt.cla()

def plot_c_to_n(c_to_n):
    plt.title('Average compares / n')
    plt.xlabel('n')
    plt.ylabel('avg compares / n')
    plt.plot(c_to_n[0], c_to_n[1])
    plt.savefig('plot_' + sys.argv[1] + '_compares_to_n.png')
    plt.show()
    plt.cla()

def plot_s_to_n(s_to_n):
    plt.title('Average swaps / n')
    plt.xlabel('n')
    plt.ylabel('avg swaps / n')
    plt.plot(s_to_n[0], s_to_n[1])
    plt.savefig('plot_' + sys.argv[1] + '_swaps_to_n.png')
    plt.show()
    plt.cla()

def plot_all_avg_compares(data, file_list):
    plt.title('Average compares')
    plt.xlabel('n')
    plt.ylabel('avg compares')
    all_avg_c = []
    for i in range(len(data)):
        avg_c = avg_compares(data[i])
        plt.plot(avg_c[0], avg_c[1], label = file_list[i])
        all_avg_c.append(avg_c)

    plt.savefig('plot_all_avg_compares.png')
    plt.legend()
    plt.show()
    plt.cla()
    return all_avg_c

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
    return all_avg_s

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

def plot_all_c_to_n(avg_c, file_list):
    plt.title('Average compare / n')
    plt.xlabel('n')
    plt.ylabel('avg compare / n')

    for i in range(len(avg_c)):
        c_to_n = compare_to_n(avg_c[i])
        plt.plot(c_to_n[0], c_to_n[1], label = file_list[i])
    
    plt.savefig('plot_all_avg_compares_to_n.png')
    plt.legend()
    plt.show()
    plt.cla()

def plot_all_s_to_n(avg_s, file_list):
    plt.title('Average swaps / n')
    plt.xlabel('n')
    plt.ylabel('avg swaps / n')

    for i in range(len(avg_s)):
        s_to_n = swap_to_n(avg_s[i])
        plt.plot(s_to_n[0], s_to_n[1], label = file_list[i]) 

    plt.savefig('plot_all_avg_swaps_to_n.png')
    plt.legend()
    plt.show()
    plt.cla()

def plot_all(file_list):
    data = []

    for file in file_list:
        inp_data = read_file(file)
        data.append(handle_data(inp_data[:-1]))

    avg_c = plot_all_avg_compares(data, file_list)
    avg_s = plot_all_avg_swaps(data, file_list)
    plot_all_avg_time(data, file_list)
    plot_all_c_to_n(avg_c, file_list)
    plot_all_s_to_n(avg_s, file_list)



def main():
    file_list = ['quick.data', 'merge.data', 'dp.data', 'hyb.data']
    if sys.argv[1] != '--all':
        input_data = read_file(sys.argv[1])
        data = handle_data(input_data[:-1])
        avg_c = avg_compares(data)
        avg_s = avg_swaps(data)
        avg_t = avg_time(data)
        c_to_n = compare_to_n(avg_c)
        s_to_n = compare_to_n(avg_s)
        plot_avg_compares(avg_c)
        plot_avg_swaps(avg_s)
        plot_avg_time(avg_t)
        plot_c_to_n(c_to_n)
        plot_s_to_n(s_to_n)

    else:
        plot_all(file_list)

    

    

if __name__ == "__main__":
    main()