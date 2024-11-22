import random
import os

class TebakNamaPemain:
    def __init__(self):
        self.pemain_bola = [
            "Lionel Messi", "Cristiano Ronaldo", "Neymar", 
            "Kylian Mbappe", "Erling Haaland", "Luka Modric",
            "Karim Benzema", "Mohamed Salah", "Harry Kane",
            "Robert Lewandowski"
        ]
        self.pilihan = random.choice(self.pemain_bola).lower()
        self.petunjuk = self._buat_petunjuk()
        self.tebakan_salah = 0

    def _buat_petunjuk(self):
        return ''.join('_' if c.isalpha() else c for c in self.pilihan)

    def mainkan(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Selamat datang di game tebak nama pemain bola!")
        print("Tebak huruf dalam nama pemain bola yang terkenal.\n")
        
        while '_' in self.petunjuk and self.tebakan_salah < 6:
            print(f"Nama pemain: {self.petunjuk}")
            print(f"Tebakan salah: {self.tebakan_salah} dari 6")
            tebakan = input("Masukkan satu huruf: ").lower()

            if len(tebakan) != 1 or not tebakan.isalpha():
                print("Masukkan hanya satu huruf!\n")
                continue

            if tebakan in self.pilihan:
                print(f"Benar! Huruf '{tebakan}' ada di nama pemain.\n")
                self.petunjuk = ''.join(
                    self.pilihan[i] if self.pilihan[i] == tebakan else self.petunjuk[i]
                    for i in range(len(self.pilihan))
                )
            else:
                print(f"Salah! Huruf '{tebakan}' tidak ada di nama pemain.\n")
                self.tebakan_salah += 1

        if '_' not in self.petunjuk:
            print(f"Selamat! Kamu berhasil menebak: {self.pilihan.title()}")
        else:
            print(f"Sayang sekali, kamu kalah. Nama pemain yang benar adalah: {self.pilihan.title()}")

# Main program
if __name__ == "__main__":
    game = TebakNamaPemain()
    game.mainkan()