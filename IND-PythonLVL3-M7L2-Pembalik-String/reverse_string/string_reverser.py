# Fungsi untuk membalikkan string
def reverse_string(s):
    # Tugas: Lengkapi fungsi ini
    reversed_string = ""

    for i in s:
        reversed_string = i + reversed_string
    '''
    Membuat string kosong untuk menyimpan hasil
    Melakukan iterasi untuk setiap karakter dalam string asli
    Menambahkan karakter saat ini ke awal string hasil
    Dengan cara ini, karakter terakhir akan menjadi pertama, kedua terakhir menjadi kedua, dst
    Mengembalikan string yang sudah dibalik
    '''
    return reversed_string


# Fungsi utama program
def main():
    # Meminta input string dari pengguna untuk dibalik
    user_input = input("Masukkan string yang ingin dibalik: ")
    # Memanggil fungsi reverse_string dengan string dari pengguna
    # Menampilkan string yang sudah dibalik ke layar
    print("String yang dibalik:", reverse_string(user_input))


# Memeriksa apakah program dijalankan secara langsung dan bukan diimpor sebagai modul
if __name__ == "__main__":
    main()  # Memanggil fungsi utama jika program dijalankan secara langsung
