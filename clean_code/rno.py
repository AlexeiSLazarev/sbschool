def bubble_sort_with_temp(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Без использования временной переменной
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort_with_temp(array)
print("Sorted array with temp:", sorted_array)