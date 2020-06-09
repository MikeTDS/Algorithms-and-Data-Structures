import sys
import random
import math
import time


random_compares = 0
random_swaps = 0
select_compares = 0
select_swaps = 0


def read_params():
    param = sys.argv[1]
    param2 = ''
    if len(sys.argv)>2:
        param2 = sys.argv[2]
    if param != '-r' and param != '-p':
        sys.stderr.write('Wrong parameters.\n')
        exit(1)
    return param, param2

def read_input():
    n = int(input('n: '))
    k = int(input('k: '))
    return n, k

def gen_array(param,n):
    array = []
    if param == '-r':
        array = [random.getrandbits(8) for i in range(n)]
    else:
        array = [(i+1) for i in range(n)]
        for i in range(n):
            p = random.randint(i,n-1)
            array[i],array[p] = array[p],array[i]
    return array   

def run_alogrithms(array,n,k):
    global random_compares
    global random_swaps
    global select_compares
    global select_swaps

    sys.stderr.write('Array: ' + str(array) + '\n')
    sys.stderr.write('k: ' + str(k) + '\n')

    sys.stderr.write('RANDOMIZED SELECT \n')
    copy1 = array[:]
    x1 = randomized_select(copy1,0,n-1,k)

    sys.stderr.write('SELECT \n')
    copy2 = array[:]
    x2 = select(copy2,0,n-1,k-1)

    #sprawdzam, czy oba alogrytmy zwrocily to samo
    if(copy1[x1]!=copy2[x2]):
        sys.stderr.write('ERROR: Could not find element.')
        exit(1)

    sys.stderr.write('FINISHED \n')
    sys.stderr.write('RANDOMIZED SELECT: Total compares = ' + str(random_compares) + ' Total swaps = ' + str(random_swaps) + '\n')
    sys.stderr.write('SELECT: Total compares = ' + str(select_compares) + ' Total swaps = ' + str(select_swaps) + '\n')

    for i in range(len(copy1)):
        if i!=x1:
            print(copy1[i], end=' ')
        else:
            print('[' + str(copy1[i]) + ']', end=' ')
    print()

def randomized_select(array,start,end,i):
    if start == end:
        return start
    q = randomized_partition(array,start,end)
    k = q - start + 1
    if i == k:
        return q
    elif i<k:
        return randomized_select(array, start, q-1, i)
    else:
        return randomized_select(array, q+1, end, i-k)

def randomized_partition(array, start, end):
    global random_compares
    global random_swaps
    i = random.randint(start,end)
    sys.stderr.write('Random Pivot: ' + str(array[i]) + '\n')
    random_swaps += 1
    array[end],array[i] = array[i],array[end]

    x = array[end]
    i = start-1
    for j in range(start,end):
        random_compares += 1
        sys.stderr.write('Comparing: ' + str(array[j]) + ', ' + str(x) + '\n')
        if array[j] <= x:
            i += 1
            random_swaps += 1
            sys.stderr.write('Swapping: ' + str(array[i]) + ', ' + str(array[j]) + '\n')
            array[i],array[j] = array[j],array[i]
    random_swaps += 1
    sys.stderr.write('Swapping: ' + str(array[i+1]) + ', ' + str(array[end]) + '\n')
    array[i+1],array[end] = array[end],array[i+1]
    return i+1

def select(array,start,end,n):
    if start == end:
        return start
    pivot_id = find_median(array,start,end)
    sys.stderr.write('Median Pivot: ' + str(array[pivot_id]) + '\n')
    pivot_id = partition(array,start,end,pivot_id,n)
    if n == pivot_id:
        return n
    elif n < pivot_id:
        return select(array,start,pivot_id-1,n)
    else:
        return select(array,pivot_id+1,end,n)

def find_median(array,start,end):
    if end-start < 5:
        return insertion_sort(array,start,end)
    for i in range(start,end,5):
        sub_end = i+4
        if sub_end > end:
            sub_end = end
        insertion_sort(array,i,sub_end)
    
    mid = (end-start)//10 + start + 1
    return select(array,start,start + math.ceil((i-start)/5),mid)

def insertion_sort(array,start,end):
    global select_compares
    global select_swaps
    i = start + 1
    while i <= end:
        j = i
        select_compares += 1
        sys.stderr.write('Comparing: ' + str(array[j-1]) + ', ' + str(array[j]) + '\n')
        while j>start and array[j-1] > array[j]:
            select_swaps += 1
            sys.stderr.write('Swapping: ' + str(array[j]) + ', ' + str(array[j-1]) + '\n')
            array[j-1],array[j] = array[j],array[j-1]
            select_compares += 1
            sys.stderr.write('Comparing: ' + str(array[j-1]) + ', ' + str(array[j]) + '\n')
            j -= 1
        i += 1
    return math.ceil((start+end)/2)

def partition(array,start,end,pivot_id,n):
    global select_compares
    global select_swaps
    val = array[pivot_id]
    array[pivot_id],array[end] = array[end],array[pivot_id]
    idd = start
    for i in range(start,end):
        select_compares += 1
        sys.stderr.write('Comparing: ' + str(array[i]) + ', ' + str(val) + '\n')
        if array[i] < val:
            select_swaps += 1
            sys.stderr.write('Swapping: ' + str(array[i]) + ', ' + str(val) + '\n')
            array[idd],array[i] = array[i],array[idd]
            idd += 1
    sys.stderr.write('Swapping: ' + str(array[idd]) + ', ' + str(array[end]) + '\n')
    array[idd],array[end] = array[end],array[idd]
    return idd 

def standard_deviation(args,avg):
    up_sum = 0
    for i in range(len(args)):
        up_sum += pow((args[i]-avg),2)
    return math.sqrt(up_sum/len(args))

def main():
    param, param2 = read_params()
    n, k = read_input()
    if param2 == '--stat':
        reps = int(sys.argv[3])
        last_sel = 0
        last_rand = 0
        sels = []
        rands = []
        for i in range(reps):
            array = gen_array(param,n)
            run_alogrithms(array,n,k)
            sels.append(select_compares-last_sel)
            last_sel = select_compares
            rands.append(random_compares-last_rand)
            last_rand = random_compares
        avg_select_compares = select_compares/reps
        avg_random_compares = random_compares/reps

        print('RANDOMIZED SELECT average compares: ' + str(avg_random_compares) + ' standard deviation: ' + str(standard_deviation(rands,avg_random_compares)))
        print('SELECT average compares: ' + str(avg_select_compares)+ ' standard deviation: ' + str(standard_deviation(sels,avg_select_compares)))
        print()

    else:
        array = gen_array(param,n)
        run_alogrithms(array,n,k)

if __name__ == "__main__":
    main()
