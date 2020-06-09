from matplotlib import pyplot as plt

def get_data():
    with open('alg.data', 'r') as file:
        data = file.read()
    temp = data.split('\n')
    fin = []
    for row in temp:
        fin.append(row.split(';'))
    return fin[:-1]

def plot_one(data, n, ver, lab):
    x_lab = []
    y_lab = []
    for i in data:
        x_lab.append(int(i[0]))
        if ver == 0:
            y_lab.append(int(i[n]))
        else:
            y_lab.append(float(i[n+1]))
    plt.plot(x_lab,y_lab, label = lab[n//2])
    plt.legend

def plot(data,ver,lab):
    for i in range(1,8,2):
        plot_one(data,i,ver,lab)

def main():
    label = ['quick sort', 'dual pivot quick sort', 'select quick sort', 'select dual pivot quick sort' ]
    data = get_data()
    plt.title('Compares')
    plot(data,0,label)
    plt.legend()
    plt.savefig('compares.png')
    plt.show()
    plt.cla()
    plt.title('Time')
    plot(data,1,label)
    plt.legend()
    plt.savefig('sort_time.png')
    plt.show()
    plt.cla()

if __name__ == "__main__":
    main()