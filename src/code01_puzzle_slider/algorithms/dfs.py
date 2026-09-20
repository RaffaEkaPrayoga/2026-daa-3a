from code01_puzzle_slider.models.step import Step

class DFS:
    def solve(self):
        self.steps = []

        # Posisi awal sudah sama dengan posisi akhir
        if self.compare(self.posisiAwal, self.posisiAkhir):
            self.steps = [self.posisiAwal]
            return self.steps

        # Queue menggunakan list biasa
        queue = []

        # Menyimpan path untuk setiap posisi
        queue.append(Step(self.posisiAwal))

        # Menyimpan posisi yang sudah dikunjungi
        is_found = False
        visited = []
        visited.append(self.posisiAwal.data)

        while len(queue) > 0 and not is_found:
            print("Visited: ", len(visited))
            # Ambil posisi paling depan dari queue
            current = queue.pop()

            # Generate posisi-posisi berikutnya
            posisiBerikutnya = self.generateNextPositions(current.posisi)

            for posisiBaru in posisiBerikutnya:

                # Skip jika sudah pernah dikunjungi
                if posisiBaru.data in visited:
                    continue

                # Tandai sebagai sudah dikunjungi
                visited.append(posisiBaru.data)

                # Masukkan ke belakang queue
                queue.append(Step(posisiBaru, current))

                # Sudah sampai tujuan?
                if self.compare(posisiBaru, self.posisiAkhir):
                    is_found = True
                    break
        
        # Traceback steps
        current = queue.pop()
        if self.compare(current.posisi, self.posisiAkhir):
            while current.parent != None:
                self.steps.insert(0, current.posisi)
                current = current.parent

        return self.steps
