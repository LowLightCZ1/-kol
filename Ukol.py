rows = int(input())
colums = int(input())

field = [["o" for x in range(rows)] for y in range(colums)]

for y in range(colums):
    for x in range(rows):
        if x <= (rows + 1)/2:
            if y >= x and rows-y > x:
                field[x][y]="x"

for i in field:
    print("".join(i))
        
    

