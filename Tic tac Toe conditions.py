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
check_2 = True
while check == True:
    user_input = input("Enter the coordinates: ")
    user_input = list(user_input)
    if " " in user_input:
        user_input.remove(" ")
    print(user_input)
    if len(user_input) <2 :
        print("You should enter numbers!")
        continue
    if len(user_input[0]) >=2 or len(user_input[1]) >=2 :
        print("You should enter numbers!")
        continue
    if not user_input[0].isnumeric() or not user_input[1].isnumeric():
        print("You should enter numbers!")
        continue
    else:
        x = int(user_input[0])
        y = int(user_input[1])
        if x >=4 or y >=4:
            print("You should choose coordinates from 1 to 3!")
            continue
        index_ = (((x - 1) * 3) + (y + 2)) - 3
        if cells[index_] == "X" or cells[index_] == "O":
            print("That cell is occupied! Please choose another one!")
            continue
        else:
            cells[index_] = "X"
            check = False
            check_2 = False
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
