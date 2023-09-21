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

Cases:
    List has less than 2 elements: cannot halve -> return itself
    List has 2+ elements: - divide list into two halves
                          - merge sort those halves
                          - we now have two sorted lists
                          - merge into one sorted list

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""
from __future__ import annotations
from typing import List
from sort_analytics import test_versions, time_versions


def merge_sort(lst: List[int], prnt: bool=True) -> List[int]:
    """Wrapper for recursive implementation for printing purposes"""
    if prnt:
        print(f"Merge Sort\n\tUnsorted: {lst}")

    lst = _merge_sort(lst)

    if prnt:
        print(f"\tSorted: {lst}")

    return lst


def _merge_sort(lst: List[int]) -> List[int]:
    """Sort list by dividing, sorting components, then merging back into one"""
    if len(lst) < 2:
        return lst

    mid_idx = len(lst) // 2
    return merge(_merge_sort(lst[:mid_idx]), _merge_sort(lst[mid_idx:]))


def merge(lst1: List[int], lst2: List[int]) -> List[int]:
    """Merge two sorted lists into one"""
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    if lst1[0] < lst2[0]:
        return lst1[:1] + merge(lst1[1:], lst2)
    if lst1[0] > lst2[0]:
        return lst2[:1] + merge(lst1, lst2[1:])

    return lst1[:1] + lst2[:1] + merge(lst1[1:], lst2[1:])


# main
if __name__ == "__main__":
    # analytics
    versions = [merge_sort]

    test_versions(versions) # valid
    time_versions(versions) # 11.643 μs
