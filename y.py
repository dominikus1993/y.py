from typing import List, Callable
from typing import TypeVar

T = TypeVar("T")


def range(start: int, end: int) -> List[int]:
    def gen(start, end):
        while start <= end:
            yield start
            start += 1

    if start < end:
        return list(gen(start, end))
    else:
        raise Exception("Invalid Parameter Error")


def each(collection: List[T], callback: Callable[[T], T]):
    for element in collection:
        callback(element)
    return collection


def filter(collection: List[T], predicate: Callable[[T], bool]) -> List[T]:
    def tail_filter(data, acc):
        if len(data) != 0:
            head, *tail = data
            if predicate(head):
                return tail_filter(tail, acc + [head])
            else:
                return tail_filter(tail, acc)
        else:
            return acc

    return tail_filter(collection, [])
