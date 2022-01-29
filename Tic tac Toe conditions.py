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
check_2
while check == True:
    user_input = input("Enter the coordinates: ")
    user_input = list(user_input)
    for i in user_input:
        if " " in user_input:
            user_input.remove(" ")
        if not i.isnumeric():
            print("You should enter numbers!")
            break
        else:
            integer_user = int(i)
            if integer_user >= 4:
                print("Coordinates should be from 1 to 3")
                break
            for cord in cells:
                if cord == "_":
                    x = int(user_input[0])
                    y = int(user_input[1])
                    index_ = (((x - 1) * 3) + (y + 2)) - 3
                    cells[index_] = "X"
                    check = False
                    check_2 = False
                    break
                elif cord == 'X' or cord == "O":
                    print("This cell is occupied! Choose another one!")
                    break