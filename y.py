from typing import List

def range(start: int, end: int) -> List[int]:
    def gen(start, end):
        while start <= end:
            yield start
            start += 1

    if start < end:
        return list(gen(start, end))
    else:
        raise Exception("Invalid Parameter Error")


def each(collection):
    return 0


def filter(collection, predicate):
    result = []
    return result


