import random

bot_point = 0
user_point = 0
playing = True


def game_mechanics():
    global user_point, bot_point, result
    item = ["stone", "paper", "scissor"]
    bot_pick = random.choice(item)
    while True:
        user_pick = input("enter a choice: ").strip().lower()
        if user_pick in item:
            break
        else :
            print("Invalid input pick either stone , paper or scissor")
    if user_pick == bot_pick:
        result = "draw"
        user_point += 1
        bot_point += 1
    elif (
        user_pick == "scissor"
        and bot_pick == "paper"
        or user_pick == "stone"
        and bot_pick == "scissor"
        or user_pick == "paper"
        and bot_pick == "stone"
    ):
        result = "win"
        user_point += 2
    else:
        result = "lose"
        bot_point += 2

    print(
        f"you picked {user_pick} the bot picked {bot_pick} you {result} \n \tpoints \nbot : {bot_point} || you : {user_point}"
    )


while playing:
    game_mechanics()
    playing = input(
        "Do you want to continue ? ... \n pick 'y' to continue playing , type anything else to exit: "
    ).strip().lower()
    if playing != "y":
        playing = False
