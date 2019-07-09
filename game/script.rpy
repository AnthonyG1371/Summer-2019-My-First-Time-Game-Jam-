# The script of the game goes in this file.
# The Death Contract Script

# v0.001 alpha     Project skeleton. Created protag_stats class to keep track of variables.
# v0.002 alpha     Added the draft script for Night One. Added placeholder images.

define v = Character("Valeria")
define e = Character("Unknown", color = "#800000") #maroon
define d = Character("Darren")
define a = Character("Advisor")

# define screen effects
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define long_flash = Fade(0.5, 0.0, 2.0, color="#fff")
define shake = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=1)

# The game starts here.
label start:

    # define and instantiates protagonists' stats
    python:
        protag_stats = main_stats(50,50,50)

    # debug scene selection
    menu:
        "Go to Scene: "

        "Advisor Meeting":
            jump advisor

        "Night 0":
            jump night0

        "Debug Test":
            jump test_space

    # The opening scene is Valeria’s memory of her conversation  with her advisor, but she’s actually in her apartment. Until she makes the contract, her Morality and Friendship stay neutral and her actions don’t affect the stats. This section simply sets up the plot.
    label advisor:

    scene background with dissolve
    show valeria

    v "...Could you repeat that sir?"

    a "Miss Jimenez, I’ve told you many times that you should go to tutoring. It’s free and doesn’t interfere with your schedule. All you have to do is ask."

    v "I don’t need tutoring."

    "The advisor takes off his glasses and sighs. He’s clearly tired of hearing the same responses time and time again."

    a "Valeria, listen to me. You’re failing three of your required courses. Your finals are coming up as well, and I’m afraid that if this continues you won’t qualify for your scholarship anymore."

    v "What? I’ll have to drop out if that happens!"

    "The advisor’s lips are pressed into a thin line, and he nods grimly."

    # The memory is over and Valeria is at her desk in her apartment.

    # Night Zero

    # The phone pops up with a message, so the following dialogue is through text (format pasted from the premade messaging system found in the design document. The rest of that system will have to be pasted into The Death Contract game.)
    label night0:

    scene background2 with fade

    hide valeria

    "Later that night"

    call phone_start

    call message_start("Unknown", "Hello there.")
    call message_start("Unknown", "Many college students are in your situation, you know. It’s easy to fall when you’re alone and away from home. It feels a bit like the world’s against you, doesn’t it?")

    call reply_message("Who is this?")

    # Label names here are placeholders

    call screen phone_reply("I think you’ve got the wrong number.","label1","What do you mean by interested?","label2")

    label label1:
        call phone_after_menu
        call message_start("me", "I think you’ve got the wrong number.")
        call message("Unknown", "Do I, Valeria?")
        jump aftermenu

    label label2:
        call phone_after_menu
        call message_start ("me", "What do you mean by interested?")
        call message("Unknown", "I'm glad you asked, Valeria.")
        jump aftermenu

    label aftermenu:
        call reply_message("How do you know my name??")
        call message ("Unknown", "Go ahead and summon me, Valeria. All you have to do is call.")

    call phone_end

    "They text a number. It’s bolded and underlined, just asking to be called."

    show valeria

    v "I don’t get it, how do they know my name? I don’t have this number saved. Could it be someone from my class?"

    # Two choices
    # Choice 1
    menu:
        "Block the number":
                v "If it’s someone from one of my classes, they’re probably pranking me. Somehow they found out about my scholarship situation. Well, I’m not gonna play the fool."
                "It’s not worth it. I block the number and put it out of my mind. Now... what am I going to do about my scholarship? I could call my parents... Ah, nevermind."
                jump game_over
    # The game abruptly ends here and goes back to the start. The Entity would presumably move on as they never made a contract with her in this case.

    # Choice 2
        "Call the number":
            v "I might as well see what they’re about?"

    "The phone rings for a second, then a second more before the call is picked up. It’s silent, like the other person is waiting for me to speak first."

    v "...Hello? This is Valeria Jimenez."

    v "You’re not just messing with me, right?"

    # The Entity appears in person. Valeria has a shocked expression. We could also consider adding in animations, like a screen shake to indicate shock.
    with shake
    with flash

    show valeria

    show valeria:
        linear 0.25 xalign 0.9

    show entity:
        xalign -0.8 yalign 1.0

    e "Don’t be scared. I’m the entity you spoke with on the phone."

    v "How the hell did you get in here?"

    e "I’m here to offer you a solution, Valeria."

    v "I don’t need your help!"

    e "You’re on the verge of losing your scholarship, right? If you tell your parents, you’ll lose all their support, won’t you?"

    v "What?"

    e "You can’t even vent to your best friend. It’s not like he would understand. His professors love him, and he’s able to afford this school. Unlike you."

    v "Leave Darren out of this. And I could afford it if I took out a loan!"

    e "Don’t kid yourself. Make a deal with me."

    # Two Choices
    menu:
        "Accept":
            jump accept_deal
        "Refuse":
            jump refuse_deal

    # Choice 1
    label accept_deal:
    v "I’ll bite. What’s this deal you’re talking about?"
    e "You made the right choice."

    #Choice 2
    label refuse_deal:
    v "I’m telling you that I don’t need your help."
    e "With no one to rely on, aren’t you desperate to solve this situation? I could help you if you let me."

    # Both choices end up here.

    e "All you have to do is sign this contract. I’m an entity with great powers. Helping you keep your scholarship and pass your finals can be done with a snap of my fingers. But I’d like something in return."

    v "Which is?"

    e "Your best friend, Darren Romero was it? His future seems pretty bright. I’d like for you to dim it down."

    v "What is that supposed to mean?"

    e "I’ll contact you, and you’ll know. Do we have a deal?"

    v "What about if I can’t do what you ask?"

    e "Then I get your soul."

    # Inner thoughts

    v "*Am I making a deal with a demon here? I could lose my life... but I’m desperate.*"

    # This seems like a part where she definitively accepts or refuses, as the last choice was railroaded back to the same explaination

    v "Alright then, I accept."

    e "Grasp my hand and repeat after me: I, Valeria Jimenez, formally accept the terms of the Death Contract."

    v "I, Valeria Jimenez, formally accept the terms of the Death Contract."

    with long_flash

    # Everything goes dark. End scene.
    $renpy.pause(1)
    scene black with fade

    jump endgame

#################### TEST AREA BELOW ########################

    label test_space:

    #Testing stat box
    show screen stat_box(protag_stats)
    pause
    hide screen stat_box

    #Testing phone conversation

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

    label game_over:
        scene game_over with fade
        ""

    label endgame:
    # This ends the game.

    return
