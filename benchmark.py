import time
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
plt.show()
