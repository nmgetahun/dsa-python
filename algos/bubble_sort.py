"""
Written by Nat Getahun

Bubble Sort
-----------
As the name implies, this sort successively bubbles up the largest element to
the end of the list, then decremenets the length of the list we're working with
by 1 until we reach the beginning of the list (which by now will be the
smallest element).

Complexity:
    Time: O(n^2) (O(n) for sorted list)
    Space: O(1)
"""
from __future__ import annotations
from typing import List
from sort_analytics import test_versions, time_versions, DEFAULT_UNSORTED_LIST


def bubble_sort(lst: List[int], prnt: bool=True) -> None:
    """Sort by swapping mismatched elements of current sublist until sorted"""
    if prnt:
        print(f"Bubble Sort\n\tUnsorted: {lst}")

    for i in range(len(lst))[::-1]:
        swapped = False
        for j in range(i):
            if lst[j] > lst[j + 1]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp
                swapped = True

        if not swapped:
            break

    if prnt:
        print(f"\tSorted: {lst}")


def bubble_sort_visualizer(lst: List[int]) -> None:
    print(f"Visualizer\n\tUnsorted: {lst}\n")

    for i in range(len(lst))[::-1]:
        swapped = False
        print(f"\tIteration {len(lst) - i}")
        for j in range(i):
            if lst[j] > lst[j + 1]:
                # pretty printing
                print(f"\t\tPre:  {lst}")
                lst_split = str(lst).split()
                gap1 = len(' '.join(lst_split[:j]))
                gap2 = len(lst_split[j]) - 1 * (lst_split[j][0] == '[')
                print(f"\t\t      {gap1 * ' '} ^{gap2 * ' '}^")

                # actual work
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp
                swapped = True

                print(f"\t\tPost: {lst}\n\n")

        if not swapped:
            break

    print(f"\tSorted: {lst}\nVisualizer Done\n\n")


# main
if __name__ == "__main__":
    # visualize the sorting process
    bubble_sort_visualizer(DEFAULT_UNSORTED_LIST[:]) # output is quite long

    # analytics
    versions = [bubble_sort]

    test_versions(versions) # valid
    time_versions(versions)
    # short: 8.443 µs
    # long: 33.583 s