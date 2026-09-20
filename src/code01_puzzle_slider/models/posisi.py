
class Posisi:
    def __init__(self, data):
        self.data = data    # 3x3
        self.posisiNol = -1
        for index, item in enumerate(self.data):
            if item == 0:
                self.posisiNol = index

        if self.posisiNol == -1:
            raise ValueError("Item 0 tidak ditemukan.")


    def keAtas(self):
        if self.posisiNol >= 6 :
            raise IndexError("Tidak bisa digeser ke atas lagi.")

        temp_list = list(self.data)
        temp_nilai = temp_list[self.posisiNol]
        temp_list[self.posisiNol] = temp_list[self.posisiNol + 3]
        temp_list[self.posisiNol + 3] = temp_nilai
        return Posisi(tuple(temp_list))

    def keBawah(self):
        if self.posisiNol < 3 :
            raise IndexError("Tidak bisa digeser ke bawah lagi.")

        temp_list = list(self.data)
        temp_nilai = temp_list[self.posisiNol]
        temp_list[self.posisiNol] = temp_list[self.posisiNol - 3]
        temp_list[self.posisiNol - 3] = temp_nilai
        return Posisi(tuple(temp_list))

    def keKanan(self):
        if self.posisiNol in (0, 3, 6) :
            raise IndexError("Tidak bisa digeser ke kanan lagi.")

        temp_list = list(self.data)
        temp_nilai = temp_list[self.posisiNol]
        temp_list[self.posisiNol] = temp_list[self.posisiNol - 1]
        temp_list[self.posisiNol - 1] = temp_nilai
        return Posisi(tuple(temp_list))

    def keKiri(self):
        if self.posisiNol in (2, 5, 8) :
            raise IndexError("Tidak bisa digeser ke kiri lagi.")

        temp_list = list(self.data)
        temp_nilai = temp_list[self.posisiNol]
        temp_list[self.posisiNol] = temp_list[self.posisiNol + 1]
        temp_list[self.posisiNol + 1] = temp_nilai
        return Posisi(tuple(temp_list))

    def display(self):
        temp_list = list(self.data)
        print(temp_list[0], " ", temp_list[1], " ", temp_list[2])
        print(temp_list[3], " ", temp_list[4], " ", temp_list[5])
        print(temp_list[6], " ", temp_list[7], " ", temp_list[8])

