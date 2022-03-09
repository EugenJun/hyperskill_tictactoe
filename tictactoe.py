
grid = {0: " ", 1: " ", 2: " ",
        3: " ", 4: " ", 5: " ",
        6: " ", 7: " ", 8: " "
        }

winning_combinations = {
    1: [0, 3, 6],
    2: [1, 4, 7],
    3: [2, 5, 8],
    4: [0, 1, 2],
    5: [3, 4, 5],
    6: [6, 7, 8],
    7: [0, 4, 8],
    8: [2, 4, 6]
}

indexes = [value for value in grid.values()]

counter = 0

occupied_cells = []

grid_for_print = ""

counter_x = 0

counter_y = 0


def get_key(coords):
    grid = {0: [1, 1], 1: [1, 2], 2: [1, 3],
            3: [2, 1], 4: [2, 2], 5: [2, 3],
            6: [3, 1], 7: [3, 2], 8: [3, 3]
            }

    for key, value in grid.items():
        if coords == value:
            return key


def print_grid():
    indexes = [value for value in grid.values()]

    grid_for_print = f"---------\n| " \
                     f"{indexes[0]} {indexes[1]} {indexes[2]} |\n| " \
                     f"{indexes[3]} {indexes[4]} {indexes[5]} |\n| " \
                     f"{indexes[6]} {indexes[7]} {indexes[8]} |\n" \
                     f"---------"

    print(grid_for_print)


def update_grid():
    index = get_key([int(user_input_2[0]), int(user_input_2[1])])

    for i in range(len(indexes)):
        if i == index:
            if counter % 2 != 0:
                indexes[i] = "X"
            else:
                indexes[i] = "O"

    grid_for_print = f"---------\n| " \
                     f"{indexes[0]} {indexes[1]} {indexes[2]} |\n| " \
                     f"{indexes[3]} {indexes[4]} {indexes[5]} |\n| " \
                     f"{indexes[6]} {indexes[7]} {indexes[8]} |\n" \
                     f"---------"

    print(grid_for_print)


active = True

while active:

    if counter == 0:
        print_grid()
    else:
        pass

    while True:
        user_input_2 = input().split()
        print(f"Enter the coordinates: " + " ".join([num for num in user_input_2]))

        if not user_input_2[0].isdigit() or not user_input_2[1].isdigit():
            print("You should enter numbers!")
            continue

        index = get_key([int(user_input_2[0]), int(user_input_2[1])])

        if index in occupied_cells:
            print("This cell is occupied! Choose another one!")
            continue

        if int(user_input_2[0]) < 1 or int(user_input_2[0]) > 3 or \
                int(user_input_2[1]) < 1 or int(user_input_2[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            counter += 1
            occupied_cells.append(index)
            break

    update_grid()

    for key in winning_combinations.keys():
        for value in winning_combinations[key]:
            if indexes[value] == "X":
                counter_x += 1
                if counter_x == 3:
                    print("X wins")
                    active = False
                    break
                else:
                    pass
            elif indexes[value] == "O":
                counter_y += 1
                if counter_y == 3:
                    print("O wins")
                    active = False
                    break
                else:
                    pass
        else:
            counter_x = 0
            counter_y = 0

    if (counter == 9 and counter_x != 3) and (counter == 9 and counter_y != 3):
        print("Draw")
        active = False
