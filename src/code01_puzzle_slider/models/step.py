from code01_puzzle_slider.models.posisi import Posisi
from typing import Self

class Step:
    def __init__(self, posisi: Posisi, parent: Self = None):
        self.posisi = posisi
        self.parent = parent

