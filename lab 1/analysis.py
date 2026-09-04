import time
import tracemalloc
import random
import matplotlib.pyplot as plt

from sorting_algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort
)

# Sorting algorithms
algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

# Input sizes
input_sizes = [100, 500, 1000]

# Store results
times = {name: [] for name in algorithms}
memory = {name: [] for name in algorithms}

random.seed(42)

# Experimental analysis
for size in input_sizes:

    data = [random.randint(0, 100000) for _ in range(size)]

    for name, algorithm in algorithms.items():

        # Measure execution time
        tracemalloc.start()

        start_time = time.perf_counter()

        algorithm(data)

        end_time = time.perf_counter()

        # Measure memory
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        execution_time = (end_time - start_time) * 1000
        peak_memory = peak / 1024

        times[name].append(execution_time)
        memory[name].append(peak_memory)

        print(
            f"{name} | Input Size: {size} | "
            f"Time: {execution_time:.4f} ms | "
            f"Memory: {peak_memory:.2f} KB"
        )


# -------------------------------
# Execution Time Graph
# -------------------------------

plt.figure()

for name in algorithms:
    plt.plot(
        input_sizes,
        times[name],
        marker="o",
        label=name
    )

plt.xlabel("Input Size")
plt.ylabel("Execution Time (ms)")
plt.title("Sorting Algorithms - Execution Time")
plt.legend()
plt.grid(True)

plt.savefig("sorting_execution_time.png")
plt.show()


# -------------------------------
# Memory Consumption Graph
# -------------------------------

plt.figure()

for name in algorithms:
    plt.plot(
        input_sizes,
        memory[name],
        marker="o",
        label=name
    )

plt.xlabel("Input Size")
plt.ylabel("Peak Memory (KB)")
plt.title("Sorting Algorithms - Memory Consumption")
plt.legend()
plt.grid(True)

plt.savefig("sorting_memory_consumption.png")
plt.show()