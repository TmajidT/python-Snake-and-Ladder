import copy

import dice


def start_playing(main_board):

    #x is the number of rows
    x = len(main_board)
    # y is the number of columns
    y = len(main_board[0])


    #copy main_board to main_board_copy
    main_board_copy = copy.deepcopy(main_board)


    #an important part of the code
    player1_location = [x - 1,0,2,0,0]
    player2_location = [x - 1,0,1,0,0]
         # x location     y location     player number      counter     on_edge(1 == is on the edge     0 == is not on the edge)


    temp_location1 = [0,0]
    temp_location2 = [0,0]
    # x loc    y loc


    player_number = 1       # player numbers    1 and 0
    game_is_on = True
    dice_rolled = True
    dice_number = 0         #dice number        1 , 2 , . . . , 6
    pick_player = True
    game_has_2_player = True            #if false == player 0 is a bot      else both player are real players


    #get the number of real players     1 or 2
    while(1):
        choice = int(input("does game need 2 players or 1 player and 1 bot?   enter the number of real players: "))
        if(choice == 2):
            game_has_2_player = True
            break
        elif(choice == 1):
            game_has_2_player = False
            break



    #pick the first player that starts playing
    while(pick_player):
        print("lets pick the player who starts the game :)")
        print("you should get a 6 on the dice!")
        if(game_has_2_player):
            dice_number = dice.get_dice_number(player_number)
        elif (game_has_2_player == False) and (player_number == 1):
            dice_number = dice.get_dice_number(player_number)
        elif (game_has_2_player == False) and (player_number == 0):         #if its bot's turn this code runs
            dice_number = dice.get_dice_for_bot()

        if(dice_number != 6):
            if (player_number):
                player_number = 0
            else:
                player_number = 1
        else:
            print("player " + str(player_number + 1) + " you won and you can go first :)")
            break


    #main loop that runs the game
    while game_is_on:

        print(main_board)

        #dice_number = dice.get_dice_number(player_number)
        #if(dice_number == 6):
        #    dice_number = dice.get_dice_prize()


        if(game_has_2_player):
            dice_number = dice.get_dice_number(player_number)
            if(dice_number == 6):
                dice_number = dice.get_dice_prize()                         #get the prize
        elif (game_has_2_player == False) and (player_number == 1):
            dice_number = dice.get_dice_number(player_number)
            if(dice_number == 6):
                dice_number = dice.get_dice_prize()
        elif (game_has_2_player == False) and (player_number == 0):         #if its bot's turn this code runs
            dice_number = dice.get_dice_for_bot()
            if(dice_number == 6):
                dice_number = dice.get_dice_prize_for_bot()


        #dice_number = int(dice.get_dice_number_cheate(player_number))          #if you want to cheate

        #store data in temp_location
        temp_location1[0] = player1_location[0]
        temp_location1[1] = player1_location[1]
        temp_location2[0] = player2_location[0]
        temp_location2[1] = player2_location[1]

        #find player's new location
        if(player_number):
            player1_location = get_player_location(player1_location,dice_number,x,y)
            if(main_board_copy[player1_location[0] , player1_location[1]] != 0) and (int(main_board_copy[player1_location[0] , player1_location[1]] / 100) == 1):
                player1_location = find_snake_tail(main_board_copy,player1_location)
            elif(main_board_copy[player1_location[0] , player1_location[1]] != 0) and (int(main_board_copy[player1_location[0] , player1_location[1]] / 100) == 2):
                player1_location = find_ladder_start(main_board_copy,player1_location)
        else:
            player2_location = get_player_location(player2_location,dice_number,x,y)
            if(main_board_copy[player2_location[0] , player2_location[1]] != 0) and (int(main_board_copy[player2_location[0] , player2_location[1]] / 100) == 1):
                player2_location = find_snake_tail(main_board_copy,player2_location)
            elif(main_board_copy[player2_location[0] , player2_location[1]] != 0) and (int(main_board_copy[player2_location[0] , player2_location[1]] / 100) == 2):
                player2_location = find_ladder_start(main_board_copy,player2_location)


        #change player's turn
        if(player_number):
            player_number = 0
        else:
            player_number = 1

        main_board[temp_location1[0],temp_location1[1]] = main_board_copy[temp_location1[0],temp_location1[1]]  #fix the main_board after player moves
        main_board[temp_location2[0],temp_location2[1]] = main_board_copy[temp_location2[0],temp_location2[1]]
        main_board[player1_location[0],player1_location[1]] = player1_location[2]  #shows player 1
        main_board[player2_location[0],player2_location[1]] = player2_location[2]  #shows player 2


        if(player1_location[0] < 0):
            print("congratulations player 1 , you won the game :D")
            break
        elif (player2_location[0] < 0):
            print("congratulations player 2 , you won the game :D")
            break


    return 1

#تابع بازگشتی
def get_player_location(player_location,dice_number,main_boardX,main_boardY):

    #if player is on the edge
    if (player_location[4] == 1) and (player_location[1] == main_boardY - 1) and (dice_number > 0):
        dice_number -= 1
        player_location[3] += 1
        player_location[0] -= 1
        player_location[4] = 0
    elif (player_location[4] == 1) and (player_location[1] == 0) and (dice_number > 0) and (player_location[3] != 0):
        dice_number -= 1
        player_location[3] += 1
        player_location[0] -= 1
        player_location[4] = 0


    if(player_location[3] % 2 == 0) and (dice_number > 0):
        for j in range(0,dice_number):
            player_location[1] += 1
            dice_number -= 1
            if(player_location[1] >= main_boardY - 1):
                player_location[4] = 1
                get_player_location(player_location,dice_number,main_boardX,main_boardY)
                break
    elif (player_location[3] % 2 != 0) and (dice_number > 0):
        for j in range(0,dice_number):
            player_location[1] -= 1
            dice_number -= 1
            if(player_location[1] <= 0):
                player_location[4] = 1
                get_player_location(player_location,dice_number,main_boardX,main_boardY)
                break

    return player_location





def find_snake_tail(main_board_copy, player_location):
    end_loop = False
    snake_number = main_board_copy[player_location[0], player_location[1]]

    for i in range(player_location[0], len(main_board_copy)):
        for j in range(0, len(main_board_copy[0])):
            if (j != player_location[1]) and (snake_number == main_board_copy[i, j]):
                player_location[0] = i
                player_location[1] = j
                player_location[3] = len(main_board_copy) + 1 - i
                end_loop = True
                break
        if (end_loop):
            break

    return player_location



def find_ladder_start(main_board_copy, player_location):
    end_loop = False
    ladder_number = main_board_copy[player_location[0], player_location[1]]
    for i in range(0,len(main_board_copy) ):
        for j in range(0,len(main_board_copy[0])):
            if(ladder_number == main_board_copy[i, j]):
                player_location[0] = i
                player_location[1] = j
                player_location[3] = len(main_board_copy) + 1 - i
                end_loop = True
                break
        if(end_loop):
            break

    return player_location