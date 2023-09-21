"""
Written by Nat Getahun

Merge Sort
----------
Given two sorted arrays of lengths n and m, we can merge the two arrays into one
sorted array of length n + m by repeatedly adding the smallest element at the
front of both arrays to our new list; this takes O(n + m) time. Using this
method, we can also divide up an unsorted list into halves, sort those, and then
merge the two halves in O(n) (O(n / 2 + n / 2)) time. Merge sort works by
combining these two principles and recursively halving then merging our list
to sort it in O(nlogn) time.

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""
from __future__ import annotations
from typing import List, Callable
from time import perf_counter


def merge_sort(lst: List[int], prnt: bool=True) -> List[int]:
    """Wrapper for recursive implementation for printing purposes"""
    if prnt:
        print(f"Merge Sort\n\tUnsorted: {lst}")

    lst = _merge_sort(lst)

    if prnt:
        print(f"\tSorted: {lst}")

    return lst


def _merge_sort(lst: List[int]) -> List[int]:
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    return merge(_merge_sort(lst[:mid]), _merge_sort(lst[mid:]))


def merge(lst1: List[int], lst2: List[int]) -> List[int]:
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    if lst1[0] < lst2[0]:
        return lst1[:1] + merge(lst1[1:], lst2)
    if lst1[0] > lst2[0]:
        return lst2[:1] + merge(lst1, lst2[1:])

    return lst1[:1] + lst2[:1] + merge(lst1[1:], lst2[1:])


# main helpers
def test_versions(lst: List[int], versions: List[Callable]) -> None:
    print("Testing verions")
    sorted_lst = sorted(lst)

    for version in versions:
        test_lst = lst[:]
        return_val = version(test_lst, True)
        if return_val:
            test_lst = return_val

        valid_sort = ("Invalid", "Valid")[test_lst == sorted_lst]
        print(f"\t{str(version).split()[1]}: {valid_sort}")


def time_versions(lst: List[int], versions: List[Callable]) -> None:
    print("Timing verions")

    for version in versions:
        start = perf_counter()
        for _ in range(1000):
            version(lst[:], False)
        end = perf_counter()

        print(f"\t{str(version).split()[1]} time: {(end - start) * 1000:.3f}μs")


# main
if __name__ == "__main__":
    lst = [1, 4, 2, 9, 10, 8, 19, 11, 5, 100, 7, 6, 0, 10, 10, 10]
    versions = [merge_sort]

    test_versions(lst, versions)