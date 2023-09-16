"""
Written by Nat Getahun

Insertion Sort
--------------
This sort works by first partitioning the list into two sections - sorted and
unsorted - then sequentially inserting all of the elements in the unsorted
section of the list into its appropriate location in the sorted section

Cases:
    List is empty or has 1 element: lst is already sorted
    List has > 1 elements: - assume lst[0] is sorted and lst[1:] is unsorted
                               - denote sorted and unsorted portions by S & U
                           - get the first element N in U
                           - shift elements in S rightward until appropriate
                           index I for N is found
                               - I = index in S s.t. all elements before I are
                               <= N and all elements after I are >= N
                           - once index is found, insert N into S at I
                           - repeat until lst is sorted
                           - notice: after every iteration, len(S)++ & len(U)--
                           - if sorting in nondecreasing order, this process
                           shifts all elements in S that are > N rightward

Complexity:
    Time: O(n^2) (O(n) when list is sorted or close)
    Space: O(1)
"""
# ------------------------------------------------------------------------------
from __future__ import annotations
from typing import List, Callable
from time import perf_counter


# recursive method
def insertion_sort_rcr(lst: List[int], prnt: bool=True) -> List[int]:
    pass


# iterative methods
def insertion_sort_itr1(lst: List[int], prnt: bool=True) -> None:
    """Sort by shifting elements rightward, then inserting current element"""
    if prnt:
        print(f"Iterative Version 1\n\tUnsorted: {lst}")

    for i in range(1, len(lst)):
        curr = lst[i]
        j = i
        while j >= 1 and lst[j - 1] > curr:
            lst[j] = lst[j - 1]
            j -= 1

        lst[j] = curr

    if prnt:
        print(f"\tSorted: {lst}")


def insertion_sort_itr2(lst: List[int], prnt: bool=True) -> None:
    """Sort by swapping elements leftward until lst[0:i + 1] is sorted"""
    if prnt:
        print(f"Iterative Version 2\n\tUnsorted: {lst}")

    for i in range(1, len(lst)):
        j = i
        while j >= 1 and lst[j - 1] > lst[j]:
            tmp = lst[j]
            lst[j] = lst[j - 1]
            lst[j - 1] = tmp
            j -= 1

    if prnt:
        print(f"\tSorted: {lst}")


def insertion_sort_itr_visualizer(lst: List[int]) -> None:
    print(f"Visualizer\nUnsorted: {lst}\n")

    for i in range(1, len(lst)):
        curr = lst[i]
        j = i
        lst[i] = '_'
        print(f"Sorted lst: {lst[:i + 1]} -> adding {curr}")
        while j >= 1 and lst[j - 1] > curr:
            lst[j] = lst[j - 1]
            lst[j - 1] = '_'
            j -= 1
            print(f"\t{lst[:i + 1]}")

        lst[j] = curr
        print(f"Done adding {curr}: {lst[:i + 1]}\n")

    print(f"Sorted: {lst}")


# main helpers
def test_versions(lst: List[int], versions: List[Callable]) -> None:
    for version in versions:
        version(lst[:])


def time_versions(lst: List[int], versions: List[Callable]) -> None:
    for version in versions:
        start = perf_counter()
        for _ in range(1000):
            version(lst[:], False)
        end = perf_counter()

        print(f"{str(version).split()[1]} time: {(end - start) * 1000:.3f} μs")


# main
if __name__ == "__main__":
    lst = [1, 4, 2, 9, 10, 8, 19, 11, 5, 100, 7, 6, 0, 10, 10, 10]
    insertion_sort_itr_visualizer(lst[:]) # visualize the sorting process

    versions = [insertion_sort_itr1, insertion_sort_itr2]
    #test_versions(lst, versions)
    #time_versions(lst, versions)
