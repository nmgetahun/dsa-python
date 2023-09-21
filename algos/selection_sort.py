"""
Written by Nat Getahun

Selection Sort
--------------
We start by getting the minimum element of the list, and assigning it to the 0th
index by swapping it with the first element. We then get the minimum element of
the list sans the first element and swap it with the second element. Continue
doing this until we reach the last index, at which point our list is sorted.

Complexity:
    Time: O(n^2)
    Space: O(1)
"""
from __future__ import annotations
from typing import List
from sort_analytics import test_versions, time_versions, DEFAULT_UNSORTED_LIST


def selection_sort(lst: List[int], prnt: bool=True) -> None:
    """Sort by moving smallest element to start of current sublist til sorted"""
    if prnt:
        print(f"Selection Sort\n\tUnsorted: {lst}")

    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j

        if min_idx != i:
            tmp = lst[i]
            lst[i] = lst[min_idx]
            lst[min_idx] = tmp

    if prnt:
        print(f"\tSorted: {lst}")


def selection_sort_visualizer(lst: List[int]) -> None:
    print(f"Visualizer\n\tUnsorted: {lst}\n")

    pass

    print(f"\tSorted: {lst}\nVisualizer Done\n\n")


# main
if __name__ == "__main__":
    # visualize the sorting process
    #selection_sort_visualizer(DEFAULT_UNSORTED_LIST[:])

    # analytics
    versions = [selection_sort]

    test_versions(versions) # valid
    time_versions(versions)
    # short: 6.240 µs
    # long: 13.256 s