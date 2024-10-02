
### 1. Implement Quicksort

#### Non-Random Pivot Quicksort

This will be the standard version, where you select a fixed pivot, typically the first or last element of the array.

python

Copy code

`def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Non-random pivot (first element)
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)`

#### Random Pivot Quicksort

Here, the pivot will be randomly chosen from the array.

python

Copy code

`import random

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)  # Random pivot
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort_random(less) + equal + quicksort_random(greater)`

### 2\. Benchmarks for Non-Random Pivot Quicksort

You'll need to generate three types of arrays (best, worst, and average cases) and measure the time taken for sorting them for different sizes nnn.

#### 2a. Best Case

For the best case, where the pivot always divides the array evenly, you can provide a perfectly balanced array.

python

Copy code

`def generate_best_case(n):
    return sorted([i for i in range(n)])  # Sorted array`

#### 2b. Worst Case

For the worst case, the pivot will always partition the array in a highly unbalanced way, such as providing an already sorted array in reverse order.

python

Copy code

`def generate_worst_case(n):
    return sorted([i for i in range(n)], reverse=True)  # Reverse sorted array`

#### 2c. Average Case

The average case can be simulated by generating arrays with uniformly distributed random values.

python

Copy code

`import random

def generate_average_case(n):
    return [random.randint(0, 100000) for _ in range(n)]  # Random array`

### 3\. Plotting the Benchmarks

You can use Python's `time` module and `matplotlib` to measure and plot the execution times for the three cases.

python

Copy code

`import time
import matplotlib.pyplot as plt

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
plt.show()`

### 4\. Deriving the Average Runtime Complexity

The average runtime complexity of Quicksort is O(nlog⁡n)O(n \log n)O(nlogn).

How to Derive?
1.  In each recursive step, the array is divided into two parts by the pivot, with one part having about n/2n/2n/2 elements on average.
2.  The recurrence relation for the average case is T(n)=2T(n/2)+O(n)T(n) = 2T(n/2) + O(n)T(n)=2T(n/2)+O(n), where O(n)O(n)O(n) is the time spent on partitioning.
3.  Using the Master Theorem for divide and conquer algorithms, this recurrence resolves to O(nlog⁡n)O(n \log n)O(nlogn).
