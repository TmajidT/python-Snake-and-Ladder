
#when you roll the dice

import random

def dice_rolled():
    #returns a random integer between 1 and 6
    return random.randint(1, 6)


def get_dice_number(player_number):
    dice_roll = True
    dice_number = 0
    while dice_roll:
        dice_number = input("it's player " + str(player_number + 1) + "'s turn. press '0' to roll the dice : ")
        if (int(dice_number) == 0):
            dice_roll = False
            break

    dice_number = dice_rolled()

    print("---------------------------------------------------------------------")
    print("dice number : " + str(dice_number))
    print("---------------------------------------------------------------------")

    return dice_number


#cheate codes for me :)
#don't use it :)
def get_dice_number_cheate(player_number):

    dice_number = input("it's player " + str(player_number + 1) + "'s turn. enter the dice number : ")

    print("---------------------------------------------------------------------")
    print("dice number : " + str(dice_number))
    print("---------------------------------------------------------------------")

    return dice_number


def get_dice_prize():
    dice_roll = True
    dice_number = 0
    while dice_roll:
        dice_number = input("you got 6 ! press '0' to roll the dice and get your prize : ")
        if (int(dice_number) == 0):
            break

    dice_number = dice_rolled() + 6


    print("---------------------------------------------------------------------")
    print("dice number : " + str(dice_number))
    print("---------------------------------------------------------------------")

    return dice_number


def get_dice_for_bot():
    dice_number = dice_rolled()

    print("---------------------------------------------------------------------")
    print("bot's dice number : " + str(dice_number))
    print("---------------------------------------------------------------------")

    return dice_number


def get_dice_prize_for_bot():

    dice_number = dice_rolled() + 6

    print("---------------------------------------------------------------------")
    print("bot's dice prize number : " + str(dice_number))
    print("---------------------------------------------------------------------")


    return dice_number