#Matriks 5x5 menggunakan append
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

result = []

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
