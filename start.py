
import numpy

import copy

# to get the game board's size
def get_size():

    size = [0 , 0]
            #length and width
    temp = 0

    wrongNum = True

    #get length
    while(wrongNum):
        temp = int(input("Enter the length: "))
        if(temp > 0):
            size[0] = temp
            wrongNum = False

    wrongNum = True

    # get width
    while (wrongNum):
        temp = int(input("Enter the width: "))
        if (temp > 0):
            size[1] = temp
            wrongNum = False

    return size



#get enemy (snake) locations
# x is the length that we get from get_size
# y is the width that we get from get_size
def get_snake_location(x,y):

    #creates an empty matrix filled with '0'
    main_board = numpy.zeros((x,y))

    # we use wrongNum for 'while' loops
    wrongNum = True

    number_of_enemys = 0
    while(wrongNum):
        print("---------------------------")
        number_of_enemys = int(input("enter the number of enemys : "))
        if (number_of_enemys) > 0:
            wrongNum = False

    wrongNum = True

    #guide the player
    temp_matrix = copy.deepcopy(main_board)     #copy main_board to temp_matrix
    for i in range(0,x):
        temp_matrix[i,0] = i + 1
    for j in range(0,y):
        temp_matrix[0,j] = j + 1
    print("this is your board : ")
    print(temp_matrix)

    #create empty matrix
    enemy_head_location = numpy.zeros((number_of_enemys,3))
    enemy_tail_location = numpy.zeros((number_of_enemys, 3))
    #store datas in enemy_location
    for i in range(0,number_of_enemys):
        while(wrongNum):
            enemy_head_location[i, 0] = int(input("enter Snake " + str(i + 1) + "  head  Row : "))
            if(enemy_head_location[i,0] > 0) and (enemy_head_location[i,0] <= x):
                break

        while (wrongNum):
            enemy_head_location[i, 1] = int(input("enter Snake " + str(i + 1) + "  head  Column : "))
            if (enemy_head_location[i, 1] > 0) and (enemy_head_location[i, 1] <= x):
                break

        enemy_head_location[i, 2] = int(i + 1) #snake number


        while (wrongNum):
            enemy_tail_location[i, 0] = int(input("enter Snake " + str(i + 1) + " tail Row : "))
            if (enemy_tail_location[i, 0] > 0) and (enemy_tail_location[i, 0] <= x):
                break

        while (wrongNum):
            enemy_tail_location[i, 1] = int(input("enter Snake " + str(i + 1) + "  head  Column : "))
            if (enemy_tail_location[i, 1] > 0) and (enemy_tail_location[i, 1] <= x):
                break

        enemy_tail_location[i, 2] = int(i + 1)


    #sort lists by the first column
    enemy_head_location = enemy_head_location[enemy_head_location[:,0].argsort()]
    enemy_tail_location = enemy_tail_location[enemy_tail_location[:,0].argsort()]


    # transfer enemy_head_location data to main_board
    counterX = 0
    for i in range(0,x + 1):
        if(counterX > number_of_enemys):
            break
        if(i == enemy_head_location[counterX,0]):
            for j in range(0,y + 1):
                if(j == enemy_head_location[counterX,1]):
                    main_board[i - 1,j - 1] = int(enemy_head_location[counterX,2]) + 100
                    i = enemy_head_location[counterX,0]
                    counterX +=1
                    break
        if (counterX > len(enemy_head_location) - 1):
            break


    # transfer enemy_tail_location data to main_board
    counterX = 0
    for i in range(0, x + 1):
        if (counterX > number_of_enemys):
            break
        if (i == enemy_tail_location[counterX, 0]):
            for j in range(0, y + 1):
                if (j == enemy_tail_location[counterX, 1]):
                    main_board[i - 1, j - 1] = int(enemy_tail_location[counterX, 2]) + 100
                    i = enemy_tail_location[counterX, 0]
                    counterX += 1
                    break
        if (counterX > len(enemy_tail_location) - 1):
            break

    return main_board




def get_ladder_location(main_board):

    #x is the number of rows
    x = len(main_board)
    # y is the number of columns
    y = len(main_board[0])

    # we use wrongNum for 'while' loops
    wrongNum = True

    number_of_ladders = 0
    while(wrongNum):
        print("---------------------------")
        number_of_ladders = int(input("enter the number of ladders : "))
        if (number_of_ladders) > 0:
            wrongNum = False

    wrongNum = True

    #guide the player
    temp_matrix = copy.deepcopy(main_board)     #copy main_board to temp_matrix
    for i in range(0,x):
        temp_matrix[i,0] = i + 1
    for j in range(0,y):
        temp_matrix[0,j] = j + 1
    print("this is your board : ")
    print(temp_matrix)

    #create empty matrix
    ladder_start = numpy.zeros((number_of_ladders,3))
    ladder_end = numpy.zeros((number_of_ladders, 3))
    #store data
    for i in range(0,number_of_ladders):

        while(wrongNum):
            ladder_start[i, 0] = int(input("enter Ladder " + str(i + 1) + "  start  Row : "))
            if(ladder_start[i,0] > 0) and (ladder_start[i,0] <= x):
                break

        while (wrongNum):
            ladder_start[i, 1] = int(input("enter Ladder " + str(i + 1) + "  start  Column : "))
            if (ladder_start[i, 1] > 0) and (ladder_start[i, 1] <= x):
                break

        ladder_start[i, 2] = int(i + 1)


        while (wrongNum):
            ladder_end[i, 0] = int(input("enter Ladder " + str(i + 1) + " end Row : "))
            if (ladder_end[i, 0] > 0) and (ladder_end[i, 0] <= x):
                break

        while (wrongNum):
            ladder_end[i, 1] = int(input("enter Ladder " + str(i + 1) + " end Column : "))
            if (ladder_end[i, 1] > 0) and (ladder_end[i, 1] <= x):
                break

        ladder_end[i, 2] = int(i + 1)

    #sort lists by the first column
    ladder_start = ladder_start[ladder_start[:,0].argsort()]
    ladder_end = ladder_end[ladder_end[:,0].argsort()]


    # transfer data to main_board
    counterX = 0
    for i in range(0,x + 1):
        if(counterX > number_of_ladders):
            break
        if(i == ladder_start[counterX,0]):
            for j in range(0,y + 1):
                if(j == ladder_start[counterX,1]):
                    main_board[i - 1,j - 1] = int(ladder_start[counterX,2]) + 200
                    i = ladder_start[counterX,0]
                    counterX +=1
                    break
        if (counterX > len(ladder_start) - 1):
            break


    # transfer data to main_board
    counterX = 0
    for i in range(0, x + 1):
        if (counterX > number_of_ladders):
            break
        if (i == ladder_end[counterX, 0]):
            for j in range(0, y + 1):
                if (j == ladder_end[counterX, 1]):
                    main_board[i - 1, j - 1] = int(ladder_end[counterX, 2]) + 200
                    i = ladder_end[counterX, 0]
                    counterX += 1
                    break
        if (counterX > len(ladder_end) - 1):
            break


    return main_board