from __future__ import annotations
from typing import List, Callable
from time import perf_counter


def test_versions(lst: List[int], versions: List[Callable], prnt=False) -> None:
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


def time_versions(lst: List[int], versions: List[Callable]) -> None:
    print("Timing versions")

    for version in versions:
        start = perf_counter()
        for _ in range(1000):
            version(lst[:], False)
        end = perf_counter()

        print(f"\t{str(version).split()[1]}: {(end - start) * 1000:.3f} μs")