# bidimensional array(table)
max1 = 0
m = [
    [8, 2, 22, 97, 38],
    [49, 49, 99, 40, 17],
    [81, 49, 31, 73, 55],
    [52, 70, 95, 23, 4],
    [22, 31, 16, 71, 51]
]
# Proccessing it in paralel
# and calculating max product between 4 nearest neighbors
for row in m:
    for i in range(0, len(row)-3):
        prod = row[i]*row[i+1]*row[i+2]*row[i+3]
        if prod > max1:
            max1 = prod
            prod_numbers = [row[i], row[i+1], row[i+2], row[i+3]]
print(max1)
print(prod_numbers)
# Proccessing it diagonally left right
# and calculating max product between 4 nearest neighbors
max2 = 0
for j in range(0, len(m)-3):
    for i in range(0, len(row)-3):
        prod_diagonally = m[j][i]*m[j+1][i+1]*m[j+2][i+2]*m[j+3][i+3]
        if prod_diagonally > max2:
            max2 = prod_diagonally
            prod_numbers_diagonally = [
                m[j][i], m[j+1][i+1], m[j+2][i+2], m[j+3][i+3]]
print(max2)
print(prod_numbers_diagonally)
# Proccessing it diagonally right left
# and calculating max product between 4 nearest neighbors
max3 = 0
for j in range(0, len(m)-3):
    for i in range(len(row)-1, 2, (-1)):
        prod_diagonally = m[j][i]*m[j+1][i-1]*m[j+2][i-2]*m[j+3][i-3]
        if prod_diagonally > max3:
            max3 = prod_diagonally
            prod_numbers_diagonally_rl = [
                m[j][i], m[j+1][i-1], m[j+2][i-2], m[j+3][i-3]]
print(max3)
print(prod_numbers_diagonally_rl)
# Proccessing it perpendicularly
# and calculating max product between 4 nearest neighbors
max4 = 0
for j in range(0, len(m)-3):
    for i in range(0, len(row)):
        prod_perp = m[j][i]*m[j+1][i]*m[j+2][i]*m[j+3][i]
        if prod_perp > max4:
            max4 = prod_perp
            prod_numbers_perp = [m[j][i], m[j+1][i], m[j+2][i], m[j+3][i]]
print(max4)
print(prod_numbers_perp)

final_list = [max1, max2, max3, max4]
final_list.sort()
# max produs from this 2D array
print('max produs from this 2D array is: ', final_list[-1])
