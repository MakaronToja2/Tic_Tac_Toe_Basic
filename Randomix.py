# write your code here _XXOOXOXO and XXOOXOXO_
cells = input("Enter cells: ")
empty_space = "_"

print(f"""---------
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
---------""")
cells = list(cells)
check = True
while check == True:
    user_input = (input("Enter the coordinates: "))
    user_input = list(user_input)
    if " " in user_input:
        user_input.remove(" ")
    for x in user_input:
        print(user_input)
        if not x.isnumeric():
            print("You should enter numbers!")
            break
        for item in user_input:
            x = int(item)
        if x >= 4:
            print("Coordinates should be from 1 to 3")
            break
        for i in cells:
            if i == "_":
                for i in user_input:
                    if i.isnumeric():
                        x = int(user_input[0])
                        y = int(user_input[1])
                        index_ = (((x - 1) * 3) + (y + 2)) - 3
                        cells[index_] = "X"
                        check = False
                        break

            else:
                print("This cell is occupied! Choose another one!")
                break


print(f"""---------
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
---------""")

wc_1 = cells[0] == cells[3] == cells[6] or cells[0] == cells[1] == cells[2] or cells[0] == cells[4] == cells[8]
wc_2 = cells[1] == cells[4] == cells[7] or cells[3] == cells[4] == cells[5] or cells[2] == cells[4] == cells[6]
wc_3 = cells[6] == cells[7] == cells[8] or cells[2] == cells[5] == cells[8]

if abs(cells.count("X")-cells.count("O"))>=2:
    print("Impossible")
elif wc_1 and wc_2 or wc_1 and wc_3 or wc_2 and wc_3:
    print("Impossible")
elif wc_1:
    print(cells[0],"wins")
elif wc_2:
    print(cells[4],"wins")
elif wc_3:
    print(cells[8],"wins")
elif empty_space in cells:
    print("Game not finished")
elif empty_space not in cells:
    print("Draw")