"""
Written by Nat Getahun

Insertion Sort
--------------
This sort works by first partitioning the list into two sections - sorted and
unsorted - then sequentially inserting all of the elements in the unsorted
section of the list into its appropriate location in the sorted section

Cases:
    List is empty or has 1 element: lst is already sorted
    List has 1+ elements: - assume lst[0] is sorted and lst[1:] is unsorted
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
    Time: O(n^2) (O(n) for sorted list)
    Space: O(1)
"""
# ------------------------------------------------------------------------------
from __future__ import annotations
from typing import List
from sort_analytics import test_versions, time_versions, DEFAULT_UNSORTED_LIST


# recursive method
def insertion_sort_rcr(lst: List[int], prnt: bool=True) -> List[int]:
    """Wrapper for recursive implementation for printing purposes"""
    if prnt:
        print(f"Recursive Version\n\tUnsorted: {lst}")

    lst = _insertion_sort_rcr(lst)

    if prnt:
        print(f"\tSorted: {lst}")

    return lst


def _insertion_sort_rcr(lst: List[int]) -> List[int]:
    """Sort by inserting elements into progressively lengthening sorted lst"""
    if len(lst) < 2:
        return lst

    return insert_rcr(_insertion_sort_rcr(lst[:-1]), lst[-1])


def insert_rcr(lst: List[int], element: int) -> None:
    """Insert element into lst (assumed to be sorted)"""
    if not lst:
        return [element]

    if element < lst[0]:
        return [element] + lst

    return lst[:1] + insert_rcr(lst[1:], element)


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
    print(f"Visualizer\n\tUnsorted: {lst}\n")

    for i in range(1, len(lst)):
        curr = lst[i]
        j = i
        lst[i] = '_'
        print(f"\tSorted lst: {lst[:i + 1]} -> adding {curr}")
        while j >= 1 and lst[j - 1] > curr:
            lst[j] = lst[j - 1]
            lst[j - 1] = '_'
            j -= 1
            print(f"\t\t{lst[:i + 1]}")

        lst[j] = curr
        print(f"\tDone adding {curr}: {lst[:i + 1]}\n")

    print(f"\tSorted: {lst}\nVisualizer Done\n\n")


# main
if __name__ == "__main__":
    # visualize the sorting process
    insertion_sort_itr_visualizer(DEFAULT_UNSORTED_LIST[:])

    # analytics
    versions = [insertion_sort_rcr, insertion_sort_itr1, insertion_sort_itr2]

    test_versions(versions) # all valid
    time_versions(versions)
    # short:
    #    insertion_sort_rcr: 14.305 μs
    #    insertion_sort_itr1: 4.675 μs
    #    insertion_sort_itr2: 6.099 μs
    #
    # long:
    #    insertion_sort_rcr: 368.911 s (SLOW AS FUCK)
    #    insertion_sort_itr1: 18.539 s
    #    insertion_sort_itr2: 27.327 s
