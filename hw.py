list_number = int(input('수를 입력하세요 : '))
data = [[0] * list_number for i in range(list_number)]
column = 0
row = -1
value = 0
way = 1

def snail_array(column, row, value, way, list_number):
    for i in range(0, list_number):
        value += 1
        row = row + way
        data[column][row] = value

    list_number -= 1

    for i in range(0, list_number):
        value += 1
        column = column + way
        data[column][row] = value

    way = way * -1

    if list_number == 0:
        return 0

    snail_array(column, row, value, way, list_number)

snail_array(column, row, value, way, list_number)

for column in range(list_number):
    print(data[column])
