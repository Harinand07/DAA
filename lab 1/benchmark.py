import time,tracemalloc,random
from sorting_algorithms import bubble_sort,selection_sort,insertion_sort,merge_sort,quick_sort,heap_sort
alg={"Bubble Sort":bubble_sort,"Selection Sort":selection_sort,"Insertion Sort":insertion_sort,"Merge Sort":merge_sort,"Quick Sort":quick_sort,"Heap Sort":heap_sort}
sizes=[100,500,1000]
random.seed(42)
print("Algorithm,Size,Condition,Time_ms,Peak_Memory_KB")
for n in sizes:
    data={"Sorted":list(range(n)),"Reverse-Sorted":list(range(n,0,-1)),"Random":[random.randint(0,100000) for _ in range(n)]}
    for name,f in alg.items():
        for cond,a in data.items():
            ts=[]; ms=[]
            for _ in range(3):
                tracemalloc.start(); s=time.perf_counter(); f(a); ts.append((time.perf_counter()-s)*1000)
                _,peak=tracemalloc.get_traced_memory(); tracemalloc.stop(); ms.append(peak/1024)
            print(f"{name},{n},{cond},{sum(ts)/3:.4f},{max(ms):.2f}")
