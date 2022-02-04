# write your code here _XXOOXOXO and XXOOXOXO_
cells = "         "
empty_cells = "123456789"
empty_space = " "

def Board():
    print(f"""---------
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
---------""")
   #printing first Board - empty
Board()

empty_cells = list(empty_cells)
cells = list(cells)
check = True
change = True

while True:
    #conditions of winning
    wc_1 = empty_cells[0] == empty_cells[3] == empty_cells[6] or empty_cells[0] == empty_cells[1] == empty_cells[2] or empty_cells[0] == empty_cells[4] == empty_cells[8]
    wc_2 = empty_cells[1] == empty_cells[4] == empty_cells[7] or empty_cells[3] == empty_cells[4] == empty_cells[5] or empty_cells[2] == empty_cells[4] == empty_cells[6]
    wc_3 = empty_cells[6] == empty_cells[7] == empty_cells[8] or empty_cells[2] == empty_cells[5] == empty_cells[8]
    if abs(cells.count("X") - cells.count("O")) >= 2:
        print("Impossible")
        break
    elif wc_1 and wc_2 or wc_1 and wc_3 or wc_2 and wc_3:
        print("Impossible")
        break
    elif wc_1:
        print(cells[0], "wins")
        break
    elif wc_2:
        print(cells[4], "wins")
        break
    elif wc_3:
        print(cells[8], "wins")
        break
    elif empty_space not in cells:
        print("Draw")
        break
    user_input = input("Enter the coordinates: ")
    user_input = list(user_input)
    if " " in user_input:
        user_input.remove(" ")
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
        #exchanging matrice position to index in cells
        index_ = (((x - 1) * 3) + (y + 2)) - 3
        if cells[index_] == "X" or cells[index_] == "O":
            print("That cell is occupied! Please choose another one!")
            continue
        print(cells)
        if change == True:
            cells[index_] = "X"
            empty_cells[index_] = "X"
            change = False
            Board()
            continue
        elif change == False:
            cells[index_] = "O"
            empty_cells[index_] = "O"
            Board()
            change = True
