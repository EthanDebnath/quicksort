import time
import matplotlib.pyplot as plt

import sys
sys.setrecursionlimit(2000)  # Increase recursion limit to avoid hitting the default recursion depth


def quicksort(arr):
    stack = [(0, len(arr) - 1)]
    
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        
        pivot = arr[start]
        low = start + 1
        high = end
        
        while True:
            while low <= high and arr[high] >= pivot:
                high -= 1
            while low <= high and arr[low] <= pivot:
                low += 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
            else:
                break
        
        arr[start], arr[high] = arr[high], arr[start]
        
        stack.append((start, high - 1))
        stack.append((high + 1, end))
    
    return arr

def generate_best_case(n):
    return sorted([i for i in range(n)])  # Sorted array

def generate_worst_case(n):
    return sorted([i for i in range(n)], reverse=True)  # Reverse sorted array

import random

def generate_average_case(n):
    return [random.randint(0, 100000) for _ in range(n)]  # Random array

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)  # Random pivot
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort_random(less) + equal + quicksort_random(greater)


def benchmark(quicksort_func, generate_input_func, n_values):
    times = []
    for n in n_values:
        arr = generate_input_func(n)
        start = time.time()
        quicksort_func(arr)
        end = time.time()
        times.append(end - start)
    return times

n_values = [10, 100, 1000, 10000, 50000]

# Benchmark for best, worst, and average cases
best_times = benchmark(quicksort, generate_best_case, n_values)
worst_times = benchmark(quicksort, generate_worst_case, n_values)
average_times = benchmark(quicksort, generate_average_case, n_values)

# Plotting the results
plt.plot(n_values, best_times, label='Best Case')
plt.plot(n_values, worst_times, label='Worst Case')
plt.plot(n_values, average_times, label='Average Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (s)')
plt.legend()
plt.show()
