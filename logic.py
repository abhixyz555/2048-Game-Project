import random


def new_game(n):
    matrix = []

    for i in range(n):
        # give you a matrix with all values as 0 initially
        matrix.append([0] * n)
    return matrix


def add_two(mat):
    a = random.randint(0, len(mat)-1)   # random positions in the rows
    b = random.randint(0, len(mat)-1)   # random positions in the coloumns
    while(mat[a][b] != 0):   # while the space is not empty or 0
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2   # empty positions are filled with 2

    return mat


def game_state(mat):
    # Anywhere 2048 is present
    for i in range(len(mat)):    # for row
        for j in range(len(mat[0])):   # for coloumn
            if mat[i][j] == 2048:   # if anywhere 2048 is present then you won the game
                return 'win'
    # Every Row and Coloumn except last row and last coloumn
    for i in range(len(mat)-1):    # for every 2 there will be 3
        for j in range(len(mat[0])-1):   # for every 2 there will be 3
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    # Anywhere 0 is present
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:   # if there is an empty position then the game is not over yet
                return 'not over'
    for k in range(len(mat)-1):  # to check the left/right entries on the last row
        # if consecutive elements are equal in the last row
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'
    for j in range(len(mat)-1):  # check up/down entries on last column
        # if consecutive elements are equal in the last coloumn
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'
    return 'lose'   # if all the conditions are failed then you have lost the game


def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        # for ith row & for the jth element we'll store len-j-1 position, for 0 it is 3 for 1 it is 2 for 2 it is 1 & for 3 it is 0
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new


def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            # in transpose the matrix at ith & jth will be appended at jth & ith
            new[i].append(mat[j][i])
    return new


def cover_up(mat):
    new = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    done = False
    for i in range(4):
        count = 0   # at each row, position is initially 0
        for j in range(4):
            if mat[i][j] != 0:    # if the position is not equal to 0 or empty
                new[i][count] = mat[i][j]   # then we fill the position with 2
                if j != count:   # if the position of previous element is not same as the new element then change is happening
                    done = True
                count += 1   # position will move step by step
    # now all the zeros are at the right side of the row & all the non-zero numbers are on the left side of row
    return (new, done)


def merge(mat):
    done = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                # if j = j + 1 then you just double it then move on to the next coloumn & so on
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True   # if merging is happening then change will take place
    return (mat, done)


def up(game):
    print("up")
    # return matrix after shifting up
    game = transpose(game)
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(game)
    return (game, done)


def down(game):
    print("down")
    game = reverse(transpose(game))
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return (game, done)


def left(game):
    print("left")
    # return matrix after shifting left
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    return (game, done)


def right(game):
    print("right")
    # return matrix after shifting right
    game = reverse(game)
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = reverse(game)
    return (game, done)
