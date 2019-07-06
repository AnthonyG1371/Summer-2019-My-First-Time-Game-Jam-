# The script of the game goes in this file.

# v0.001 alpha     Project skeleton. Created protag_stats class to keep track of variables

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Valeria")

# The game starts here.

label start:

    # define and instantiates protagonists' stats
    python:
        protag_stats = main_stats(50,50,50)

    show screen stat_box(protag_stats)
    pause
    hide screen stat_box


    #Testing phone convorsation

    call phone_start
    call message_start("Darren","Hey Valeria, how's it going?")

    call reply_message("Doing fine.")

    call phone_end

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room
    scene background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy
    show person

    # These display lines of dialogue.

    "TEST VERSION. PLEASE IGNORE ANY LOGIC IN THIS."

    e "Currently, your character is morally netural at [protag_stats.morals] points."

    menu:
        e "A person drops $100. What do you do?"

        "Take the money. Not like they'll know where it went.":
            $protag_stats.morals = 0

        "Return the money. It was their hard earned cash":
            $protag_stats.morals = 100

    if protag_stats.morals == 0:
        e "Your character is morally bankrupt."
        scene bg black
        with dissolve
        "GAME OVER"
    elif protag_stats.morals > 90:
        e "Your character is an angel in society."

    if protag_stats.get_morals() == 0:
        e "Successful reload test."

    #e "Money on hand: $[r.money]"

    # This ends the game.

    return
