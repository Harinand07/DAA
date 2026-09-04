def bubble_sort(a):
    a=a.copy()
    for i in range(len(a)-1):
        swapped=False
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]: a[j],a[j+1]=a[j+1],a[j]; swapped=True
        if not swapped: break
    return a

def selection_sort(a):
    a=a.copy()
    for i in range(len(a)-1):
        k=min(range(i,len(a)),key=a.__getitem__)
        a[i],a[k]=a[k],a[i]
    return a

def insertion_sort(a):
    a=a.copy()
    for i in range(1,len(a)):
        key=a[i]; j=i-1
        while j>=0 and a[j]>key: a[j+1]=a[j]; j-=1
        a[j+1]=key
    return a

def merge_sort(a):
    if len(a)<=1: return a.copy()
    m=len(a)//2; l=merge_sort(a[:m]); r=merge_sort(a[m:])
    out=[]; i=j=0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]: out.append(l[i]); i+=1
        else: out.append(r[j]); j+=1
    return out+l[i:]+r[j:]

def quick_sort(a):
    if len(a)<=1: return a.copy()
    pivot=a[len(a)//2]
    return quick_sort([x for x in a if x<pivot])+[x for x in a if x==pivot]+quick_sort([x for x in a if x>pivot])

def heap_sort(a):
    import heapq
    h=a.copy(); heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

if __name__=="__main__":
    data=[64,25,12,22,11,90,34]
    alg={"Bubble Sort":bubble_sort,"Selection Sort":selection_sort,"Insertion Sort":insertion_sort,"Merge Sort":merge_sort,"Quick Sort":quick_sort,"Heap Sort":heap_sort}
    print("Python Sorting Algorithm Demonstration")
    for n,f in alg.items(): print(f"{n:18}: {f(data)}")
