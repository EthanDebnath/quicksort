
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Non-random pivot (first element)
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
