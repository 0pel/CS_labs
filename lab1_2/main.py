def bubble_sort(arr: list[int], order='asc') -> list[int]:
    n = len(arr)
    should_swap = (lambda x, y: x > y) if order == 'asc' else (lambda x, y: x < y)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if should_swap(arr[j], arr[j + 1]):
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

        print("Исходный массив:", numbers)

        print("\nВыберите направление сортировки:")
        print("1 - По возрастанию")
        print("2 - По убыванию")

        choice = input("Ваш выбор (1/2): ").strip()
        while choice not in ['1', '2']:
            print("Ошибка: введите 1 или 2")
            choice = input("Ваш выбор (1/2): ").strip()

        order = 'asc' if choice == '1' else 'desc'

        sorted_numbers = bubble_sort(numbers, order)

        direction = "возрастанию" if order == 'asc' else "убыванию"
        print(f"\nОтсортированный массив по {direction}:")
        print(sorted_numbers)

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()