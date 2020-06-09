import sys
import os
import random
import time
import math
import tracemalloc

def read_params():
    sort_type = ''
    comp = ''
    stat = ''
    repeats = ''
    for i in range(len(sys.argv)):
        try:
            if sys.argv[i] == '--type':
                sort_type = sys.argv[i+1]
            elif sys.argv[i] == '--comp':
                comp = sys.argv[i+1]
            elif sys.argv[i] == '--stat':
                stat = sys.argv[i+1]
                repeats = int(sys.argv[i+2])
        except:
            pass
    return (sort_type, comp, stat, repeats)

def handle_input(inp):
    if inp[0] != '' and inp[1] != '':
        if inp[0] not in ('insert', 'merge', 'quick', 'dp', 'hyb', 'radix'):
            print('Wrong type.')
            exit(1)
        if inp[1] not in ('>=', '<='):
            try:
                inp[1].split()
            except:
                print('Wrong comparator.')
                exit(1)
    else:
        print("Too few parameters.")
        exit(1)

def read_size():
    try:
        res = int(input('Size: '))
    except:
        print('Wrong size.')
        exit(1)
    return res

def read_array(size):
    temp = str(input('To sort: ')).split()
    if len(temp) != size:
        print('Wrong size.')
        exit(1)
    for i in range(len(temp)):
        try:
            temp[i] = int(temp[i])
        except:
            pass
    return temp

def choose_strategy(inp, size, array):
    tracemalloc.start()
    if inp[0] == 'quick':
        start = time.time()
        c, s = quick_sort(array, 0, size-1, inp[1], inp[2])
        end = time.time()
        total = (end-start)*1000

    elif inp[0] == 'insert':
        start = time.time()
        c, s = insert_sort(array,0, size-1, inp[1], inp[2])
        end = time.time()
        total = (end-start)*1000

    elif inp[0] == 'merge':
        start = time.time()
        c, s = merge_sort(array, 0, size-1, inp[1], inp[2])
        end = time.time()
        total = (end-start)*1000
    
    elif inp[0] == 'dp':
        start = time.time()
        c, s = dual_pivot_qs(array, 0, size-1, inp[1], inp[2])
        end = time.time()
        total = (end-start)*1000

    elif inp[0] == 'hyb':
        start = time.time()
        c, s = hybrid_sort(array, 0, size-1, inp[1], inp[2])
        end = time.time()
        total = (end-start)*1000
    
    elif inp[0] == 'radix':
        start = time.time()
        c, s = radix_sort(array, 0, size-1, inp[1], inp[2])
        end = time.time()
        total = (end-start)*1000
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    if inp[2] == '':
        sys.stderr.write('Total compares: ' + str(c) + ' Total swaps: ' + str(s) + ' Total sort time: ' + str(total) + 'ms\n')
    else:
        with open(inp[2], 'a') as file:
            file.write(str(size) + ';' + str(c) + ';' + str(s) + ';' + str(total) + ';' + str(peak/10**6) + '\n')

def compare(a, b, comp, s_type):

    if s_type == '':
        if comp == '<=' and a < b:
            return True
        elif comp == '>=' and a > b:
            return True
        elif comp != '>=' and comp != '<=':
            try:
                if comp.index(a) < comp.index(b):
                    return True
            except:
                print('Can not compare - unknown element.')
                exit(1)
    else:
        if comp == '<=' and a <= b:
            return True
        elif comp == '>=' and a >= b:
            return True
        elif comp != '>=' and comp != '<=':
            try:
                if comp.index(a) <= comp.index(b):
                    return True
            except:
                print('Can not compare - unknown element.')
                exit(1)
    return False

#quick_sort
def quick_sort(array, start, end, comp, out):
    compares = 0
    swaps = 0
    print_err = False

    if out == '':
        print_err = True

    if start >= end:
        return compares, swaps

    i, c, s = partition(array, start, end, comp, out)
    compares += c
    swaps += s

    c, s = quick_sort(array, start, i-1, comp, out)
    compares += c
    swaps += s

    c, s = quick_sort(array, i+1, end, comp, out)
    compares += c
    swaps += s

    return compares, swaps

def partition(array, start, end, comp, out):
    compares = 0
    swaps = 0
    print_err = False

    if out == '':
        print_err = True

    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if print_err:
                sys.stderr.write('Compare: ' + str(array[j]) + ', ' + str(pivot) + '\n')
        compares += 1
        if compare(array[j], pivot, comp, ''):
            i += 1
            swaps += 1
            if print_err:
                sys.stderr.write('Swap: ' + str(array[i]) + ', ' + str(array[j]) + '\n')
            array[j], array[i] = array[i], array[j]

    swaps += 1
    array[i+1], array[end] = array[end], array[i+1]

    return i+1, compares, swaps

#insertion sort
def insert_sort(array, start, end, comp, out):
    compares = 0
    moves = 0
    print_err = False

    if out == '':
        print_err = True

    for i in range(start, end+1):
        key = array[i]
        j = i-1
        if print_err:
            sys.stderr.write('Compare: ' + str(key) + ', ' + str(array[j]) + '\n')
        compares += 1
        while j >= 0 and compare(key, array[j], comp, ''):
            if print_err:
                sys.stderr.write('Move: ' + str(array[j]) + ' to id: ' + str(j+1) + '\n')
            moves += 1
            array[j+1] = array[j]
            j -= 1
            if print_err:
                sys.stderr.write('Compare: ' + str(key) + ', ' + str(array[j]) + '\n')
            compares += 1

        if(array[j+1] != key):
            if print_err:
                sys.stderr.write('Move: ' + str(key) + ' to id: ' + str(j+1) + '\n')
            moves += 1
            array[j+1] = key

    return compares, moves
#merge sort
def merge_sort(array, start, finish, comp, out):
    compares = 0
    settings = 0

    if start >= finish:
        return compares, settings

    i = (start + finish)//2
    c, s = merge_sort(array, start, i, comp, out)
    compares += c
    settings += s
    c, s = merge_sort(array, i+1, finish, comp, out)
    compares += c
    settings += s
    c, s = merge(array, start, finish, i, comp, out)
    compares += c
    settings += s
    return compares, settings

def merge(array, start, finish, mid, comp, out):
    left_arr = array[start:mid+1]
    right_arr = array[mid+1:finish+1]
    left_id = 0
    right_id = 0
    sorted_id = start
    compares = 0
    settings = 0
    print_err = False

    if out == '':
        print_err = True

    while left_id < len(left_arr) and right_id < len(right_arr):
        if print_err:
            sys.stderr.write('Compare: ' + str(left_arr[left_id]) + ', ' + str(right_arr[right_id]) + '\n')
        compares += 1
        if compare(left_arr[left_id], right_arr[right_id], comp, 'weak'):
            if print_err:
                sys.stderr.write('Setting: ' + str(left_arr[left_id]) + ' with id: ' + str(sorted_id) + '\n')
            settings += 1
            array[sorted_id] = left_arr[left_id]
            left_id += 1

        else:
            if print_err:
                sys.stderr.write('Setting: ' + str(right_arr[right_id]) + ' with id: ' + str(sorted_id) + '\n')
            settings += 1
            array[sorted_id] = right_arr[right_id]
            right_id += 1

        sorted_id += 1

    while left_id < len(left_arr):
        if print_err:
            sys.stderr.write('Setting: ' + str(left_arr[left_id]) + ' with id: ' + str(sorted_id) + '\n')
        settings += 1
        array[sorted_id] = left_arr[left_id]
        left_id += 1
        sorted_id += 1
        
    while right_id < len(right_arr):
        if print_err:
            sys.stderr.write('Setting: ' + str(right_arr[right_id]) + ' with id: ' + str(sorted_id) + '\n')
        settings += 1
        array[sorted_id] = right_arr[right_id]
        right_id += 1
        sorted_id += 1

    return compares, settings

#dual pivot quick sort
def dual_pivot_qs(array, start, end, comp, out):
    compares = 0
    swaps = 0
    if end <= start:
        return compares, swaps

    i, k, c, s = partition_dpqs(array, start, end, comp, out)
    compares += c
    swaps += s
    c, s = dual_pivot_qs(array, start, i-1, comp, out)
    compares += c
    swaps += s
    c, s = dual_pivot_qs(array, i+1, k-1, comp, out)
    compares += c
    swaps += s
    c, s = dual_pivot_qs(array, k+1, end, comp, out)
    compares += c
    swaps += s
    return compares, swaps

def partition_dpqs(array, start, end, comp, out):
    stats = ''
    compares = 0
    swaps = 0
    p = start
    q = end
    i = start + 1
    k = end - 1
    j = i
    d = 0
    print_err = False

    if out == '':
        print_err = True

    if print_err:
        sys.stderr.write('Compare: ' + str(array[p]) + ', ' + str(array[q]) + '\n')
    compares += 1
    if compare(array[q], array[p], comp, ''):
        if print_err:
            sys.stderr.write('Swap: ' + str(array[p]) + ', ' + str(array[q]) + '\n')
        swaps += 1
        array[p],array[q] = array[q],array[p]

    while j <= k:
        if d > 0:
            if print_err:
                sys.stderr.write('Compare: ' + str(array[j]) + ', ' + str(array[p]) + '\n')
            compares += 1
            if compare(array[j], array[p], comp, ''):        
                if print_err:
                    sys.stderr.write('Swap: ' + str(array[i]) + ', ' + str(array[j]) + '\n')
                swaps += 1
                array[i],array[j] = array[j],array[i]
                i += 1
                j += 1
                d += 1

            else:
                if print_err:
                        sys.stderr.write('Compare: ' + str(array[j]) + ', ' + str(array[q]) + '\n')
                compares += 1
                if compare(array[j], array[q], comp, ''):                 
                    j += 1
                else:
                    if print_err:
                        sys.stderr.write('Swap: ' + str(array[j]) + ', ' + str(array[k]) + '\n')
                    swaps += 1
                    array[j],array[k] = array[k],array[j]
                    k -= 1
                    d -= 1

        else:
            compares += 1
            if print_err:
                sys.stderr.write('Compare: ' + str(array[k]) + ', ' + str(array[q]) + '\n')
            while compare(array[q], array[k], comp, ''):
                k -= 1
                d -= 1
                if print_err:
                    sys.stderr.write('Compare: ' + str(array[k]) + ', ' + str(array[q]) + '\n')
                compares += 1
            if j <= k:
                if print_err:
                        sys.stderr.write('Compare: ' + str(array[k]) + ', ' + str(array[p]) + '\n')
                compares += 1
                if compare(array[k], array[p], comp, ''):
                    array[k],array[j],array[i] = array[j],array[i],array[k]
                    if print_err:
                        sys.stderr.write('Rotate: ' + str(array[k]) + ', ' + str(array[j]) + ', ' + str(array[i]) +'\n')
                    swaps += 3
                    i += 1
                    d += 1
                else:
                    if print_err:
                        sys.stderr.write('Swap: ' + str(array[j]) + ', ' + str(array[k]) + '\n')
                    swaps += 1
                    array[j], array[k] = array[k], array[j]
                j += 1
    
    i -= 1
    k += 1
    if array[p] != array[i]:
        array[p], array[i] = array[i], array[p]
        if print_err:
            sys.stderr.write('Swap: ' + str(array[p]) + ', ' + str(array[i]) + '\n')
        swaps += 1
    if array[q] != array[k]:
        array[q], array[k] = array[k], array[q]
        if print_err:
            sys.stderr.write('Swap: ' + str(array[q]) + ', ' + str(array[k]) + '\n')
        swaps += 1

    return i, k, compares, swaps

def hybrid_sort(array, start, end, comp, out):
    compare = 0
    swaps = 0
    div = (end-start)//2
    c, s = quick_sort(array, start, div, comp, out)
    compare += c
    swaps += s
    c, s = quick_sort(array, div+1, end, comp, out)
    compare += c
    swaps += s
    c, s = merge(array, start, end, div, comp, out)
    compare += c
    swaps += s
    return compare, swaps

#radix sort
def radix_sort(array, start, end, comp, out):
    maxi = max(array[start:end+1])
    exp = 1
    sets = 0
    while maxi//exp > 0:
        s = counting_sort(array,start,end,comp,out,exp)
        sets += s
        exp *= 10
    return 0, sets

def counting_sort(array,start,end,comp,out,exp):
    n = end+1 - start
    res = [None]*n
    count = [0]*10
    sets = 0
    if comp == '<=':
        for i in range(start,n):
            index = array[i]//exp
            count[(index)%10] += 1

        for i in range(1,10):
            count[i] += count[i-1]       
        
        i = n-1
        while i>=0:
            index = array[i]//exp
            res[count[(index)%10]-1] = array[i]
            count[(index)%10] -= 1
            i -= 1
            sets += 1     
    else:
        for i in range(start,n):
            index = 9-array[i]//exp
            count[(index)%10] += 1

        for i in range(1,10):
            count[i] += count[i-1]
        i = n-1
        while i>=0:
            index = 9-array[i]//exp
            res[count[(index)%10]-1] = array[i]
            count[(index)%10] -= 1
            i -= 1
            sets += 1

    array[start:end+1] = res 
    return sets
#check if sorted
def is_sorted(array, comp):
    if comp == '<=':
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                return False
    elif comp == '>=':
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                return False
    return True

#count sorted
def count_sorted_elements(array, copy):
    counter = 0
    for i in range(len(array)):
        if array[i] != copy[i]:
            counter += 1
    return counter

#random array
def gen_random_array(size):
    res = []
    for i in range(size):
        res.append(random.randint(100,999))
    return res

def main():
    size = 0
    array = []
    
    read_input = read_params()
    handle_input(read_input)
    
    if read_input[2] == '':
        size = read_size()
        array = read_array(size)
        array_copy = array.copy()
        choose_strategy(read_input, size, array)
        if(is_sorted(array, read_input[1])):
            print('Sorted elements: ' + str(count_sorted_elements(array, array_copy)))
            print(array)
        else:
            print('Could not sort.')
            exit(1)
    
    else:
        try:
            k = int(read_input[3])
        except:
            print('Wrong repeats number.')
            exit(1)
        
        if os.path.exists(read_input[2]):
            os.remove(read_input[2])

        n = 10
        count = 0
        while n <= 100000:
            for i in range(k):
                arr = gen_random_array(n)
                print('Working on size: ' + str(n))
                choose_strategy(read_input, n, arr)
                if(not is_sorted(arr, read_input[1])):
                    print('Could not sort.')
                    exit(1)

            if count%2 == 0:
                n*=5
            else:
                n*=2
            count += 1

if __name__ == '__main__':
    main()