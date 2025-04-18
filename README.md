# Baspro-Tugas-Pertemuan-6
### Program Penjumlahan Matriks 5x5

Program ini dibuat untuk menghitung hasil **penjumlahan dua buah matriks berukuran 5x5** menggunakan bahasa pemrograman Python.

---

## Deskripsi

Program akan melakukan penjumlahan matriks `A` dan `B` secara manual (tanpa menggunakan library seperti NumPy), lalu menyimpan hasilnya di matriks `hasil`, dan menampilkannya ke layar.

---

## Input

Dua buah matriks 5x5:

- Matriks A berisi angka-angka yang telah ditentukan.
- Matriks B juga berisi angka-angka yang telah ditentukan.

### Contoh:

```python
First_Matriks = [
    [6, 10, 12, 1, 4],
    [0, 16, 11, 7, 4],
    [1, 10, 9, 17, 4],
    [9, 5, 14, 13, 4],
    [8, 6, 0, 19, 4]
]

Second_Matriks = [
    [0, 3, 1, 1, 11],
    [3, 6, 7, 12, 2],
    [1, 9, 13, 4, 5],
    [10, 10, 10, 10, 10],
    [1, 6, 7, 1, 8]
]
```

---


### Perhitungan Elemen Matriks

```python
for i in range(5):
    row = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += First_Matriks[i][k] * Second_Matriks[k][j]
        row.append(total)
    result.append(row)

print("Hasil Perkalian Matriks 5x5:")
for row in result:
    print(row)
```

Penjelasan:
- `i` digunakan untuk iterasi baris.
- `j` digunakan untuk iterasi kolom.
- Elemen pada posisi `[i][j]` dari matriks A dan B dijumlahkan, lalu ditambahkan ke dalam list `row`.
- Setelah semua elemen pada satu baris dijumlahkan, `row` ditambahkan ke list `result`.
- Fungsi `add_matrices()` dipanggil dan hasilnya disimpan di variabel `result`.
- Setiap baris dalam `result` dicetak satu per satu ke layar.

## Matriks Hasil

Contoh hasil output dari program (tergantung nilai matriks A dan B):

```
[56, 220, 270, 188, 188]
[133, 289, 353, 310, 189]
[213, 338, 386, 331, 278]
[163, 337, 384, 259, 341]
[212, 274, 268, 274, 322]
```
