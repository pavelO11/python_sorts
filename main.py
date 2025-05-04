"""
# 🏆Популярные алгоритмы сортировки
**Описание**: Этот файл содержит реализацию и анализ основных алгоритмов сортировки,
часто используемых в учебных и практических задачах.

## 🔍 Содержание
- Bubble Sort (пузырьковая сортировка)
- Merge Sort (сортировка слиянием)
- Insertion Sort (сортировка вставками)
- Shell Sort (улучшенная сортировка вставками)
- Selection Sort (сортировка выбором)

## 📊 Сложность алгоритмов (big O notation)
| Сортировка       | Средний случай | Худший случай | Примечание                |
|------------------|----------------|---------------|---------------------------|
| Bubble Sort      | O(n²)          | O(n²)         | Простая, но неэффективная |
| Merge Sort       | O(n log n)     | O(n log n)    | Устойчивая, требует памяти|
| Insertion Sort   | O(n²)          | O(n²)         | Эффективна для малых данных |
| Shell Sort       | O(n log n)*    | O(n²)         | Зависит от последовательности шагов |
| Selection Sort   | O(n²)          | O(n²)         | Минимум обменов |

* - для оптимальных последовательностей шагов
"""

import random

# Глобальный список для всех сортировок
data = [19, 2, 31, 45, 6, 11, 121, 27]


# Bubble Sort 🫧
def bubble_sort():
    global data
    for iter_num in range(len(data) - 1, 0, -1):
        for index in range(iter_num):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]


# Merge Sort 🔃
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_list = merge_sort(arr[:middle])
    right_list = merge_sort(arr[middle:])
    return merge(left_list, right_list)


def merge(left_half, right_half):
    result = []
    while left_half and right_half:
        if left_half[0] < right_half[0]:
            result.append(left_half.pop(0))
        else:
            result.append(right_half.pop(0))
    return result + left_half + right_half


# Insertion Sort ⎀
def insertion_sort():
    global data
    for i in range(1, len(data)):
        j = i - 1
        next_element = data[i]
        while j >= 0 and data[j] > next_element:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = next_element


# Shell Sort
def shell_sort():
    global data
    gap = len(data) // 2
    while gap > 0:
        for i in range(gap, len(data)):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 2


# Selection Sort 🔂
def selection_sort():
    global data
    for index in range(len(data)):
        min_index = index
        for j in range(index + 1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[index], data[min_index] = data[min_index], data[index]


if __name__ == "__main__":
    # Bubble Sort
    data = [random.randint(1, 10**6) for _ in range(10000)]
    bubble_sort()
    print("Bubble Sort:", data)

    # Merge Sort
    data = [random.randint(1, 10**6) for _ in range(10000)]
    sorted_data = merge_sort(data.copy())
    print("Merge Sort:", sorted_data)

    # Insertion Sort
    data = [random.randint(1, 10**6) for _ in range(10000)]
    insertion_sort()
    print("Insertion Sort:", data)

    # Shell Sort
    data = [random.randint(1, 10**6) for _ in range(10000)]
    shell_sort()
    print("Shell Sort:", data)

    # Selection Sort
    data = [random.randint(1, 10**6) for _ in range(10000)]
    selection_sort()
    print("Selection Sort:", data)