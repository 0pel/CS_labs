from typing import Protocol, Any


class Comparable(Protocol):
    def __gt__(self, other: Any) -> bool: ...

    def __lt__(self, other: Any) -> bool: ...


def fibonacci(n: int) -> list[int]:
    """
    Генерирует первые n чисел Фибоначчи.
    :arg n: Количество чисел Фибоначчи для генерации. Должно быть неотрицательным целым числом.
    :raise ValueError: Если n не является целым числом или отрицательным.
    :return: Список из n чисел Фибоначчи. Для n <= 0 возвращает пустой список.
    """
    if not isinstance(n, int):
        raise ValueError("n должно быть целым числом")
    if n < 0:
        raise ValueError("n не может быть отрицательным")

    if n == 0:
        return []
    if n == 1:
        return [0]

    fib_list = [0, 1]

    for _ in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list[:n]


def bubble_sort[T: Comparable](lst: list[T]) -> list[T]:
    """
    Сортирует список элементов методом пузырька.
    :arg lst: Список элементов для сортировки. Элементы должны поддерживать сравнение.
    :return: Новый отсортированный список. Исходный список не изменяется.
    :raise ValueError: Если аргумент не является списком.
    :raise TypeError: Если элементы в списке не поддерживают сравнение между собой.
    """
    if not isinstance(lst, list):
        raise ValueError("Аргумент должен быть списком")

    # Создаем копию, чтобы не изменять исходный список
    sorted_list = lst.copy()
    length = len(sorted_list)

    # Тривиальный случай списка
    if length <= 1:
        return sorted_list

    # Сортировка пузырьком
    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                swapped = True

        # Если внутренний цикл не сделал ни одной перестановки - список отсортирован
        if not swapped:
            break
    return sorted_list


def sieve_of_eratosthenes(n: int) -> list[int]:
    """
    Находит все простые числа до заданного числа n включительно с помощью решета Эратосфена.
    :arg n: Верхняя граница диапазона поиска простых чисел. Должно быть неотрицательным целым числом.
    :return: Список простых чисел от 2 до n. Для n < 2 возвращает пустой список.
    :raise ValueError: Если n не является целым положительным числом.
    """
    if not isinstance(n, int):
        raise ValueError("n должно быть целым числом")
    if n < 0:
        raise ValueError("n не может быть отрицательным")

    if n < 2:
        return []

    # Инициализируем массив булевых значений
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 и 1 не являются простыми

    # Основной алгоритм
    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            # Помечаем все кратные current как составные
            for multiple in range(current * current, n + 1, current):
                sieve[multiple] = False

    # Собираем простые числа
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes


def main() -> None:
    lst = [1, 2, 4, 7, 3, 5]
    print(bubble_sort(lst))


if __name__ == '__main__':
    main()
