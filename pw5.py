import random
import time
import sys

sys.setrecursionlimit(200_000)

def partition(arr, low, high, ascending):
  
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        
        condition = (arr[j] <= pivot) if ascending else (arr[j] >= pivot)
        
        if condition:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def _quick_sort_recursive(arr, low, high, ascending):
   
    if low < high:
    
        pi = partition(arr, low, high, ascending)
        
        
        _quick_sort_recursive(arr, low, pi - 1, ascending)
        _quick_sort_recursive(arr, pi + 1, high, ascending)

def quick_sort(arr, ascending=True):

    _quick_sort_recursive(arr, 0, len(arr) - 1, ascending)

def is_sorted(arr, ascending=True):

    for i in range(len(arr) - 1):
        if ascending:
            if arr[i] > arr[i + 1]:
                return False
        else:
            if arr[i] < arr[i + 1]:
                return False
    return True


if __name__ == "__main__":
    sizes = [1_000, 10_000, 100_000]
    
    for size in sizes:
     
        array = [random.uniform(0.0, 1000.0) for _ in range(size)]
        
     
        start_time = time.time()
        quick_sort(array, ascending=True)
        end_time = time.time()
        
        execution_time = end_time - start_time
        sorted_correctly = is_sorted(array, ascending=True)
        
        print(f"Розмір масиву: {size:7} | Час: {execution_time:.4f} сек | Відсортовано правильно: {sorted_correctly}")