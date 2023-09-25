"""
Written by Nat Getahun

Heap
----
Abstract base class for heap implementations
"""
from abc import ABC, abstractmethod

class Heap(ABC):
    @abstractmethod
    def insert(self, item):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def height(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def _swap(self, idx1, idx2):
        pass

    @abstractmethod
    def _sift_up(self, idx):
        pass

    @abstractmethod
    def _sift_down(self, idx):
        pass
