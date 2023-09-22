"""
Written by Nat Getahun

Counting Sort
--------
The sort only works if we know a priori that the given list has only nonnegative
integers. If it does, we simply create a new list that spans the range of the
present integers, with which we'll count the occurrence of each integer in the
og list. We then reconstruct our list sequentially based on these counts to
ensure that the end result is sorted. For instance, rather than actually attempt
to sort a list like [4, 3, 1, 2] by comparing values to one another, we can
count that each num in [1,4] occurs once, then create a new list containing one
of each num in [1,4].

Complexity:
    Time: O(n + k) (k = range of integers in list)
    Space: O(n + k)
"""
from __future__ import annotations
from typing import List, Optional
from sort_analytics import test_versions, time_versions


def counting_sort(lst: List[int], prnt: bool=True) -> List[int]:
    """Wrapper for _counting_sort that returns new list"""
    return _counting_sort(lst, prnt, in_place=False)


def counting_sort_in_place(lst: List[int], prnt: bool=True) -> None:
    """Wrapper for _counting_sort that sorts 'in place'"""
    _counting_sort(lst, prnt, in_place=True)


def _counting_sort(lst: List[int], prnt: bool, in_place: bool) -> Optional[List[int]]:
    """Sort by counting occurrences of each num then reconstructing the list"""
    if prnt:
        print(f"Counting Sort {'In-place' * in_place}\n\tUnsorted: {lst}")

    # get range of integers in list
    lo = hi = lst[0]
    for n in lst:
        if n > hi:
            hi = n
        elif n < lo:
            lo = n

    # count occurrences of each integer in list
    counts = [0] * (hi - lo + 1)

    for n in lst:
        counts[n - lo] += 1

    # reconstruct list
    if in_place:
        idx = 0
        for i, ct in enumerate(counts):
            if ct > 0:
                n = i + lo
                for j in range(idx, ct + idx):
                    lst[j] = n
                idx += ct

        if prnt:
            print(f"\tSorted: {lst}")
    else:
        lst = []
        for i, ct in enumerate(counts):
            if ct > 0:
                lst.extend([i + lo] * ct)

        if prnt:
            print(f"\tSorted: {lst}")

        return lst


# main
if __name__ == "__main__":
    # analytics
    versions = [counting_sort, counting_sort_in_place]

    test_versions(versions) # valid
    time_versions(versions)
    # short:
    #    counting_sort: 4.642 µs
    #    counting_sort_in_place: 5.404 µs
    #
    # long:
    #    counting_sort: 415.566 µs (kinda nutty)
    #    counting_sort_in_place: 447.992 µs