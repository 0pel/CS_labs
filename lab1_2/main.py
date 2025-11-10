def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def main():
    try:
        n = int(input("Введите количество чисел для сортировки: "))

        if n <= 0:
            print("Ошибка: количество чисел должно быть положительным!")
            return

        numbers = []
        print(f"Введите {n} чисел:")
        for i in range(n):
            num = float(input(f"Число {i + 1}: "))
            numbers.append(num)

        print("Исходный массив:\n", numbers)

        sorted_numbers = bubble_sort(numbers)

        print("Отсортированный массив:\n", sorted_numbers)

    except ValueError:
        print("Ошибка: введите корректное число!")


if __name__ == "__main__":
    main()