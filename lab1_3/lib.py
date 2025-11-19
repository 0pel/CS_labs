from typing import Any, Iterable


def count_common_elements(*lists: Iterable[Any]):
    if not lists:
        return 0

    # 1. Преобразуем первый список в множество (убираем дубликаты внутри него)
    # 2. Ищем пересечение (.intersection) с остальными списками
    common_set = set(lists[0]).intersection(*lists[1:])
    return len(common_set)
