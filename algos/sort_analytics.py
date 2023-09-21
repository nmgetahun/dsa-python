from __future__ import annotations
from typing import List, Callable
from time import perf_counter

DEFAULT_LIST = [1, 4, 2, 9, 10, 8, 19, 11, 5, 100, 7, 6, 0, 10, 10, 10]

def test_versions(versions: List[Callable], lst: List[int]=None, prnt=False) -> None:
    if not lst:
        lst = DEFAULT_LIST[:]

    print("Testing versions")
    sorted_lst = sorted(lst)

    for version in versions:
        test_lst = lst[:]
        return_val = version(test_lst, prnt)
        if return_val:
            test_lst = return_val

        valid_sort = ("Invalid", "Valid")[test_lst == sorted_lst]
        print(f"\t{str(version).split()[1]}: {valid_sort}")

    print()


def time_versions(versions: List[Callable], lst: List[int]=None) -> None:
    if not lst:
        lst = DEFAULT_LIST[:]

    print("Timing versions")

    for version in versions:
        start = perf_counter()
        for _ in range(1000):
            version(lst[:], False)
        end = perf_counter()

        print(f"\t{str(version).split()[1]}: {(end - start) * 1000:.3f} μs")