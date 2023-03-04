
import start

import dice

import play_time

print("*****************************************************")
print("hi :) ")
print("you are playing snake an ladders")
print("*****************************************************")


game_is_on = True
while(game_is_on):
    #get the size of board
    size = start.get_size()

    #create the main game board and fill it with snakes
    matrix = start.get_snake_location(size[0],size[1])
    print(matrix)

    #get the ladder locations from the player
    start.get_ladder_location(matrix)
    print(matrix)

    #playe the game
    play_time.start_playing(matrix)

    print("*****************************************************")
    while(game_is_on):
        num = int(input("game ended :))   if you want to play again enter '0' and if you want to exit, enter '1' : "))
        if(num == 0):
            break
        elif(num == 1):
            print("byyy :)")
            game_is_on = False
            break