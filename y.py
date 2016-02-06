from typing import List, Callable, Any
from typing import TypeVar
from random import *
import math

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


def map(collection: List[T], callback: Callable[[T], T]) -> List[T]:
    def tail_map(col, acc):
        if len(col) > 0:
            head, *tail = col
            return tail_map(tail, acc + [callback(head)])
        else:
            return acc

    return tail_map(collection, [])


def reduce(collection: List[T], callback: Callable[[T, T], T], initialize_value: T):
    def tail_reduce(data, acc):
        if len(data) != 0:
            head, *tail = data
            return tail_reduce(tail, callback(acc, head))
        else:
            return acc

    return tail_reduce(collection, initialize_value)


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


def first(collection: List[T], predicate: Callable[[T], bool]) -> T:
    result = filter(collection, predicate)
    if len(result) == 0:
        raise Exception("No element achieve predicate")
    else:
        return result[0]


def reject(collection: List[T], predicate: Callable[[T], bool]) -> List[T]:
    result = filter(collection, lambda x: not predicate(x))
    return result


def every(collection: List[T], predicate: Callable[[T], bool]) -> List[T]:
    result = filter(collection, predicate)
    return len(collection) == len(result)


def some(collection: List[T], predicate: Callable[[T], bool]) -> List[T]:
    result = filter(collection, predicate)
    return len(result) > 0


def contains(collection: List[T], value: T) -> List[T]:
    return some(collection, lambda x: x == value)


def max(collection: List[T], iterate: Callable[[T], Any] = lambda x: x) -> T:
    def tail_max(data, acc):
        if len(data) != 0:
            head, *tail = data
            if iterate(head) > iterate(acc):
                return tail_max(tail, head)
            else:
                return tail_max(tail, acc)
        else:
            return acc

    return tail_max(collection, collection[0]) if len(collection) > 0 else None


def min(collection: List[T], iterate: Callable[[T], Any] = lambda x: x) -> T:
    def tail_min(data, acc):
        if len(data) != 0:
            head, *tail = data
            if iterate(head) < iterate(acc):
                return tail_min(tail, head)
            else:
                return tail_min(tail, acc)
        else:
            return acc

    return tail_min(collection, collection[0]) if len(collection) > 0 else None


def size(collection: List[T]):
    return len(collection)


def sample(collection: List[T], count: int) -> List[T]:
    n = max([min([count, len(collection)]), 0])
    tmp_collection = collection
    last = len(collection)
    for x in range(0, n):
        rand = randrange(0, last - 1)
        tmp_collection[x], tmp_collection[rand] = tmp_collection[rand], tmp_collection[x]
    return tmp_collection[0:count]
