from code01_puzzle_slider.models.posisi import Posisi
from code01_puzzle_slider.models.step import Step


class Solver:
    def __init__(self, posisiAwal: Posisi, posisiAkhir: Posisi):
        self.posisiAwal = posisiAwal
        self.posisiAkhir = posisiAkhir
        self.steps = []

    def generateNextPositions(self, posisi: Posisi):
        posisiBerikutnya = []

        try:
            posisiBerikutnya.append(
                posisi.keAtas()
            )
        except IndexError:
            pass

        try:
            posisiBerikutnya.append(
                posisi.keBawah()
            )
        except IndexError:
            pass

        try:
            posisiBerikutnya.append(
                posisi.keKanan()
            )
        except IndexError:
            pass

        try:
            posisiBerikutnya.append(
                posisi.keKiri()
            )
        except IndexError:
            pass

        return posisiBerikutnya

    def compare(self, posisi1: Posisi, posisi2: Posisi):
        return posisi1.data == posisi2.data

    def displaySteps(self):
        print("=======awal=======")
        self.posisiAwal.display()
        for i,step in enumerate(self.steps):
            print(f"======={i}=======")
            step.display()