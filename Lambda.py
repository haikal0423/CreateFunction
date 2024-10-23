import math  # Library untuk melakukan operasi matematika
luas_lingkaran = lambda r: math.pi * r * r

# Lambda: cara cepat untuk membuat fungsi dalam satu baris, rumusnya: π × r²
# Contoh penggunaan: masukkan nilai jari-jari = 7
jari_jari = 7

# area: memanggil fungsi luas_lingkaran dengan jari-jari yang diberikan
area = luas_lingkaran(jari_jari)

# Menampilkan hasil dengan format dua angka di belakang koma (.2f)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")
