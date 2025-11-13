import pytest
from main import fibonacci, bubble_sort, sieve_of_eratosthenes

class TestFibonacci:
    """ Классы эквивалентности:\n
    1. n = 0 (ни одного числа)
    2. n = 1 (только первое число)
    3. n > 1 (стандартный случай)
    4. Некорректные данные: отрицательные, нецелые, нечисловые
    """
    @pytest.mark.parametrize(
        "n, expected", [
            (0, []),
            (1, [0]),
            (2, [0, 1]),
            (5, [0, 1, 1, 2, 3]),
            (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        ])
    def test_valid_inputs(self, n, expected):
        assert fibonacci(n) == expected

    @pytest.mark.parametrize("n", [-1, -5, -100])
    def test_negative_input(self, n):
        with pytest.raises(ValueError, match="n не может быть отрицательным"):
            fibonacci(n)

    @pytest.mark.parametrize("n", [1.5, "5", None, [3]])
    def test_invalid_type(self, n):
        with pytest.raises(ValueError, match="n должно быть целым числом"):
            fibonacci(n)


class TestBubbleSort:
    """ Классы эквивалентности:\n
    1. Пустой список (любой тип)
    2. Список из одного элемента (любой тип)
    3. Список целых чисел
    4. Список вещественных чисел
    5. Список строк
    6. Список с разными числовыми типами
    7. Некорректные данные: несравнимые типы, не-список
    """
    @pytest.mark.parametrize("lst, expected", [
        # Тесты с целыми числами
        ([], []),
        ([42], [42]),
        ([3, 1, 2], [1, 2, 3]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([3, 1, 2, 3, 1], [1, 1, 2, 3, 3]),
        ([-5, 0, 5, -10], [-10, -5, 0, 5]),

        # Тесты с вещественными числами
        ([3.5, 1.2, 2.8], [1.2, 2.8, 3.5]),
        ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]),

        # Тесты со строками
        (["banana", "apple", "cherry"], ["apple", "banana", "cherry"]),
        (["z", "a", "m"], ["a", "m", "z"]),
        (["1", "10", "2"], ["1", "10", "2"]),  # Лексикографическая сортировка

        # Смешанные числовые типы
        ([1, 2.5, 3, 1.0], [1, 1.0, 2.5, 3]),
    ])
    def test_valid_generic_inputs(self, lst, expected):
        assert bubble_sort(lst) == expected

    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        sorted_list = list(range(1, 1001))
        assert bubble_sort(large_list) == sorted_list

    @pytest.mark.parametrize("invalid_input", [42, "not a list", None, {"key": "value"}])
    def test_invalid_input_type(self, invalid_input):
        with pytest.raises(ValueError, match="Аргумент должен быть списком"):
            bubble_sort(invalid_input)

    def test_incomparable_types(self):
        # Смешанные типы, которые нельзя сравнивать
        mixed_list = [1, "string", 3.5]
        with pytest.raises(TypeError):
            bubble_sort(mixed_list)

        # Более сложный случай с несравнимыми объектами
        class Incomparable:
            pass

        incomparable_list = [Incomparable(), Incomparable()]
        with pytest.raises(TypeError):
            bubble_sort(incomparable_list)


class TestSieveOfEratosthenes:
    """ Классы эквивалентности:\n
    1. n < 2 (нет простых чисел)
    2. n >= 2 (стандартный случай)
    3. Некорректные данные: отрицательные, нецелые, нечисловые
    """
    @pytest.mark.parametrize("n, expected", [
        (0, []),
        (1, []),
        (2, [2]),
        (3, [2, 3]),
        (10, [2, 3, 5, 7]),
        (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    ])
    def test_valid_inputs(self, n, expected):
        assert sieve_of_eratosthenes(n) == expected

    # Проверка производительности на большом числе
    def test_large_input(self):
        result = sieve_of_eratosthenes(10000)
        assert len(result) > 0  # Проверяем, что функция завершилась без ошибок
        assert result[-1] < 10000  # Последнее простое число должно быть < 10000

    @pytest.mark.parametrize("n", [-1, -10])
    def test_negative_input(self, n):
        with pytest.raises(ValueError, match="n не может быть отрицательным"):
            sieve_of_eratosthenes(n)

    @pytest.mark.parametrize("n", [3.5, "15", None, [10]])
    def test_invalid_type(self, n):
        with pytest.raises(ValueError, match="n должно быть целым числом"):
            sieve_of_eratosthenes(n)