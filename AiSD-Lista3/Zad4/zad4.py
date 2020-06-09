import sys
import os
import random
import time
import math

comp = 0


#quick_sort
def quick_sort(array, start, end):
    if start >= end:
        return
    i = partition(array, start, end)
    quick_sort(array, start, i-1)
    quick_sort(array, i+1, end)

def partition(array, start, end):
    global comp
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        comp += 1
        if array[j] < pivot:
            i += 1
            array[j], array[i] = array[i], array[j]

    array[i+1], array[end] = array[end], array[i+1]

    return i+1

#dual pivot quick sort
def dual_pivot_qs(array, start, end):
    if end <= start:
        return
    i, k = partition_dpqs(array, start, end)
    dual_pivot_qs(array, start, i-1)
    dual_pivot_qs(array, i+1, k-1)
    dual_pivot_qs(array, k+1, end)

def partition_dpqs(array, start, end):
    global comp
    p = start
    q = end
    i = start + 1
    k = end - 1
    j = i
    d = 0
    
    comp += 1
    if array[q] < array[p]:
        array[p],array[q] = array[q],array[p]

    while j <= k:
        if d > 0:
            comp += 1
            if array[j] < array[p]:       
                array[i],array[j] = array[j],array[i]
                i += 1
                j += 1
                d += 1

            else:
                comp += 1
                if array[j] < array[q]:                 
                    j += 1
                else:
                    array[j],array[k] = array[k],array[j]
                    k -= 1
                    d -= 1

        else:
            comp += 1
            while array[q] < array[k]:
                k -= 1
                d -= 1
                comp += 1
            if j <= k:
                comp += 1
                if array[k] < array[p]:
                    array[k],array[j],array[i] = array[j],array[i],array[k]
                    i += 1
                    d += 1
                else:
                    array[j], array[k] = array[k], array[j]
                j += 1    
    i -= 1
    k += 1
    array[p], array[i] = array[i], array[p]
    array[q], array[k] = array[k], array[q]
    return i, k

#select quick sort
def select_quick_sort(array,start,end):
    if start >= end:
        return
    pivot_id = find_median(array,start,end)
    i = select_partition(array,start,end,pivot_id)
    quick_sort(array, start, i-1)
    quick_sort(array, i+1, end)

#select dual pivot quick sort
def select_dpqs(array,start,end):
    if end <= start:
        return
    i1 = find_median(array,start,start+(end-start)//2)
    k1 = find_median(array,start+(end-start)//2,end)
    i, k = select_partition_dpqs(array,start,end,i1,k1)
    dual_pivot_qs(array, start, i-1)
    dual_pivot_qs(array, i+1, k-1)
    dual_pivot_qs(array, k+1, end)

def find_median(array,start,end):
    if end-start < 5:
        return insertion_sort(array,start,end)
    for i in range(start,end,5):
        sub_end = i+4
        if sub_end > end:
            sub_end = end
        insertion_sort(array,i,sub_end)
    
    mid = (end-start)//10 + start + 1
    return find_median(array,start,start + math.ceil((i-start)/5))

def insertion_sort(array,start,end):
    global comp
    i = start + 1
    while i <= end:
        j = i
        comp += 1
        while j>start and array[j-1] > array[j]:
            array[j-1],array[j] = array[j],array[j-1]
            comp += 1
            j -= 1
        i += 1
    return math.ceil((start+end)/2)

def select_partition(array,start,end,pivot_id):
    global comp
    val = array[pivot_id]
    array[pivot_id],array[end] = array[end],array[pivot_id]
    idd = start
    for i in range(start,end):
        comp += 1
        if array[i] < val:
            array[idd],array[i] = array[i],array[idd]
            idd += 1
    array[idd],array[end] = array[end],array[idd]
    return idd 

def select_partition_dpqs(array,start,end,i1,k1):
    array[i1],array[start] = array[start],array[i1]
    array[k1],array[end] = array[end],array[k1]
    return partition_dpqs(array,start,end)

#check if sorted
def is_sorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

#random array
def gen_random_array(size):
    res = []
    for i in range(size):
        res.append(random.getrandbits(16))
    return res

def test_algorithms():
    global comp
    data = ''
    comp1, comp2, comp3, comp4 = 0,0,0,0
    t1,t2,t3,t4 = 0,0,0,0
    for n in range(100,10001,100):
        print('Working on size: ' + str(n))
        comp1, comp2, comp3, comp4 = 0,0,0,0
        t1,t2,t3,t4 = 0,0,0,0
        for i in range(10):
            array = gen_random_array(n)

            copy = array[:]        
            start = time.time()
            quick_sort(copy,0,n-1)
            end = time.time()-start
            if not is_sorted(copy):
                exit(1)
            comp1 += comp
            t1 += end
            comp = 0

            copy = array[:]
            start = time.time()
            dual_pivot_qs(copy,0,n-1)
            end = time.time()-start
            if not is_sorted(copy):
                exit(1)
            comp2 += comp
            t2 += end
            comp = 0

            copy = array[:]
            start = time.time()
            select_quick_sort(copy,0,n-1)
            end = time.time()-start
            if not is_sorted(copy):
                exit(1)
            comp3 += comp
            t3 += end
            comp = 0

            copy = array[:]
            start = time.time()
            select_dpqs(copy,0,n-1)
            end = time.time()-start
            if not is_sorted(copy):
                exit(1)
            comp4 += comp
            t4 += end
            comp = 0

        comp1 //= 10
        comp2 //= 10
        comp3 //= 10
        comp4 //= 10
        t1 /= 10
        t2 /= 10
        t3 /= 10
        t4 /= 10

        data += (str(n) + ';' + str(comp1) + ';' + str(t1) + ';' + str(comp2) + ';' + str(t2) + ';' + str(comp3) + ';' + str(t3) + ';' + str(comp4) + ';' + str(t4) + '\n')

    if os.path.exists('alg.data'):
        os.remove('alg.data')
    with open('alg.data', 'a') as file:
        file.write(data)
def main():
    test_algorithms()

if __name__ == '__main__':
    main()