﻿# The script of the game goes in this file.
# The Death Contract Script

# v0.001 alpha     Project skeleton. Created protag_stats class to keep track of variables.
# v0.002 alpha     Added the draft script for Night One. Added placeholder images.
# v0.010 alpha     Main menu and game resizing completed.
# v0.020           Added working script up to the end of day 2.
# v0.900           Completed 2 endings. Added simple credits.

#------------------------------------------------
# NOTES ON MORLITY AND FRIENDSHIP POINTS
# BOTH START AT 0
# CHANCES TO GAIN OR LOSE POINTS SHOW UP IN DAY 2
#
# ---Day 2
#-Lecture
#1: DEFEND DARREN OR DON'T SAY ANYTHING. +/- 1 TO BOTH
#2: TAKE A PHOTO OR IGNORE IT, THEN IGNORE IT OR FLIP IT OVER. +2/-2 OR +0 MORALITY
#3: LASH OUT AT THE PROFESSOR OR NOT. -1/+2 MORALITY
#  3.5 IF LASHING OUT AT THE PROFESSOR, INSULT THEM OR CALM DOWN. -3/+1 MORALITY
#4: JOIN DARREN FOR LUNCH OR NOT. +/- 1 TO FRIENDSHIP.
#5: HIGH FIVE DARREN OR NOT. +1/+0 TO FRIENDSHIP.
#6: THROW AWAY OR KEEP THE CAMPAIGN POSTERS. +/- 3 TO BOTH.
#7: IF NOT IGNORING THE STUDENTS IN THE LIBRARY, DEFEND DARREN OR INSULT HIM. +/-1 TO FRIENDSHIP
#8: TELL DARREN THE TRUTH OR NOT WHEN TEXTING AT NIGHT. +/- 1 TO FRIENDSHIP
#
#TOTAL POSSIBLE VALUES:
#1223 = 8 MORALITY -12133 = -10 MORALITY
#111311 = 8 FRIENDSHIP -110311 = -7 FRIENDSHIP
#-----------------------------------------------

# Things that may need to be worked on
# Credits
# Music
# Sound
# Scene Select
# 2nd campus background
# high school classroom background
# advisor, professor, and misc student sprites
# Extra Ending?

define v = Character("Valeria")
define d = Character("Darren")
define e = Character("Unknown", color = "#800000") #maroon

define friendship = 0
$morals = 0
define tester = False
$join_lunch = True

image bg classroom_gray = im.Grayscale("bg classroom.jpg")

# define screen effects
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define long_flash = Fade(0.5, 0.0, 2.0, color="#fff")
define shake = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=1)

    # define and instantiates protagonists' stats

# The game starts here.
label start:
    # define and instantiates protagonists' stats
    python:
        stats = main_stats()

    if not tester:
        jump begin

    # debug scene selection
    label debug_menu:
    menu:
        "Go to Scene: "

        "Start":
            jump begin

        "Day 1":
            menu:
                "Campus meeting with Darren":
                    jump campus
                "Advisor Meeting":
                    jump advisor
                "Night 1":
                    jump night1
                "Back":
                    jump debug_menu
        "Day 2":
            menu:
                "Start":
                    jump day2
                "Campus meeting for lunch":
                    jump campus2
                "Library Scene":
                    jump library
                "Night 2":
                    jump night2
                "Back":
                    jump debug_menu
        "Day 3":
            label menu_day3:
            menu:
                "Route 1: Low Friendship & Morality":
                    menu:
                        "Start":
                            jump route3_1
                        "Bedroom":
                            jump bedroom3_1
                        "Library":
                            jump library3_1
                        "Back":
                            jump menu_day3
                "Route 3: High Friendship & Morality":
                    menu:
                        "Start":
                            jump route3_3
                        "Bedroom":
                            jump bedroom3_3
                        "Library":
                            jump library3_3
                        "Back":
                            jump menu_day3
                "Back":
                    jump debug_menu
        "Day 4":
            menu:
                "Route 1: Low Friendship & Morality":
                    jump route4_1
                "Route 3: High Friendship & Morality":
                    jump route4_3
                "Back":
                    jump debug_menu
        "Debug":
            jump debug

# SCRIPT
    label begin:
    # Classroom scene
    scene bg classroom with fade
    #show valeria neutral with dissolve
    "Professor"  "And that’s the end of our unit… "
    "Time for last-minute announcements. I quietly twirl my pencil with my fingers and peek over at the clock. 3:59 PM."
    "Today’s combination of humidity and heat has somehow made its way into the classroom. The faint rumbling of the useless air conditioning competes with my professor for my attention."
    "All that tuition money, and the university {i}still{/i} can’t be bothered to get a better air conditioner."
    "At least I’m here on scholarship."
    "A calendar reminder lights up my phone screen: {w=0.5} {i}ADVISOR MEETING IN TEN MINUTES{/i}."
    "Professor"  "Don’t forget, the final exam is coming up. If you have any questions, come to the study session that’s in a few days, or schedule an appointment with me."
    "My pencil twirling slows to a stop. Study session, huh?"
    "Well, I’ve made it this far into the year juggling a part-time and my classes. I’m sure I’ll be fine without the study session. I just wish I didn’t have to hear about finals ever again."
    "Professor"  "That’s it for today!"
    "An eruption of shuffling commences. I sling my backpack over my shoulder and rush out of the classroom."

    # Campus scene
    scene bg campus with fade
    show valeria neutral at center with dissolve
    show darren happy at offscreenright
    "The moment I leave the building, the heat hits me with full force. My first instinct is to fan myself with my notebook, but it barely offers any comfort."
    label campus:
    d "Valeria!"
    "Despite the weather, it’s hard not to smile when I see Darren waiting for me beneath the shade of the tree next to the building."
    show valeria neutral at left with move
    hide valeria neutral
    show valeria happy at left
    show darren happy at right with ease
    v "Hey Darren! What’s up?"
    d "The usual. All of my classes are wrapping up and everyone’s talking about finals. I’m guessing it’s the same for you."
    d "Hey, if you need help with some of the classes we have together, we could study together. It’d be a lot more fun than studying alone."
    "As much as I love Darren, something about the way he said that makes my eye twitch."
    menu:
        "Firmly decline":
            v "No thanks. I’ll be fine. I just have to do some review beforehand."
            d "Oh, okay! That’s good then."
        "Offer an ambivalent answer":
            v "Maybe? I’ve already got so much on my plate, I don’t know if I’ll have the time… "
            d "That’s alright! Just let me know if you’re free. We can plan things out then."
    # Return to main route
    "My phone buzzes in my pocket, momentarily taking my mind off the stress of school."
    "It’s another calendar notification for my advisor meeting. {i}THREE MINUTES{/i}, my phone declares."
    "Right. Back to stressing about school."
    v "Sorry Darren, I gotta go and meet up with my advisor. Maybe I’ll catch you later?"
    d "Aw, and I was just about to tell you about – "
    "A smile spreads over his face, giving me the impression of a kid who’s already seen his Christmas gifts, but can’t tell anyone."
    d "Actually, it can wait ‘til tomorrow; I’ll tell you then. Good luck with everything!"
    "He gives me a cheery wave before vanishing among the hordes of students emptying out of the academic buildings."
    "I head the other way, towards my advisor’s office."

    # Office scene
    label advisor:
    scene bg office with fade
    #show valeria neutral with dissolve
    "Advisor"  "Valeria. I hope your day went well."
    "He nods at me in acknowledgement as I sink into the seat facing his desk. I search for a halfhearted grin to put on my face, but nothing sticks."
    "Between my advisor’s pestering and the ever-present reminders of my stress, I hate coming in here."
    "Advisor" "I’d like to remind you once again that we {i}do{/i} offer tutoring services for the classes you’re taking. Tutoring is free and doesn’t interfere with your schedule. All you have to do is ask."
    v "I don’t believe I need the tutoring, sir. I can manage on my own."
    "Advisor" "As you’ve told me before."
    "Advisor" "Valeria, listen to me. You’re failing three of your required courses. Your finals are coming up as well, and I’m afraid that if this continues you won’t qualify for your scholarship anymore."
    "I sit there, staring stupidly at the imperfect grooves etched into the surface of his wooden desk. Waiting for the news to hit me."
    "And then –"
    #show valeria shocked with dissolve
    #pause(3)
    #show valeria neutral with dissolve
    v "You’re kidding."
    "Everything I’d achieved in high school: top of the class, making my parents proud. Everything I’d achieved, hanging by a thread over a cliff."
    v "I – I knew I wasn’t doing well, but I didn’t know it was {i}this{/i} bad. And now you’re telling me I’m about to drop out."
    "Advisor" "Yes, well… you have resources at your disposal. I can only hope that you’ll realize it’s best to accept all the help you’re offered."
    "Advisor" "Please, choose wisely."

    #Valeria is at her desk in her apartment.
    label night1:
    scene bg desk with fade
    #show valeria neutral with dissolve
    "The sun dips below the skyline as I drum my fingers against my desk, contemplating the psychology textbook next to my laptop."
    "It’s been a few hours since I met with my advisor, and I still can’t believe it. I breezed through high school easily enough; how did I fail so miserably in college?"
    "I don’t even want to think about what my parents will say."
    "My phone lights up with a new text message. Relieved by the interruption, I pick it up."

    # The phone pops up with a message, so the following dialogue is through text (format pasted from the premade messaging system found in the design document. The rest of that system will have to be pasted into The Death Contract game.)
    #hide valeria neutral with dissolve
    call phone_start
    call message_start("Darren", "V, don’t forget the psychology reading tonight.")
    call message("Darren", "Just a reminder because you forgot last time!")
    call phone_end

    "I roll my eyes. Of course."
    "A twinge of guilt twists my stomach."
    "I really shouldn’t think like that. Darren means well. He’s concerned and wants to help out in any way he can."
    "I just wish he wasn’t… like {i}that{/i} sometimes."
    "The moment my phone screen goes dark, it lights up again with another text."
    v "Seriously, Darren? Aren’t you supposed to be busy studying?"
    "My grumbling falters as I read the new message."

    call phone_start
    call message_start("Unknown", "Hello.")
    call message("Unknown", "Many college students are in your situation, you know. It’s easy to fall when you’re alone and away from home. It feels a bit like the world’s against you, doesn’t it?")
    call message("Unknown", "I could offer you a solution, if you're interested.")
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
    call message ("Unknown", "You’re not asking the right questions. But if you really want to know… why don’t you find out?")
    call phone_end

    "An unfamiliar number pops up, bolded and underlined. Just waiting to be called."
    "I don’t get it — how do they know my name? Is it someone from school?"

    # Two choices
    menu:
        "Block the number":
            "If it’s someone from school, they’re probably pranking me. I don’t know how they found out about my situation but… well, I’m not gonna play along."
            "I block the number and put it out of my mind."
            "Where was I? Oh yeah, worrying about my scholarship. I could call my parents and tell them, but that might make things worse."
            "Whatever. I’ll deal with this somehow."
            jump game_over
    # The game abruptly ends here and goes back to the start. The Entity would presumably move on as they never made a contract with her in this case.

    # Choice 2
        "Call the number":
            "Might as well see what’s going on. And I can’t help it; I’m curious. Who is this person, and what do they want from me?"

    "The phone rings for a second, then a second more. I’m in the middle of wondering if I’m being pranked when the call finally picks up."
    "The other person remains silent, like they’re waiting for me to speak first."
    v "Hello? This is Valeria Jimenez."
    v "You’re not just messing with me, right?"
    scene bg desk
    # The Entity appears in person. Valeria has a shocked expression. We could also consider adding in animations, like a screen shake to indicate shock.
    with flash
    show entity neutral at center with dissolve
    #show valeria shocked at left
    #show entity neutral at right
    #with dissolve
    e "Hello, Valeria." with vpunch
    v "What the — "
    scene bg bedroom night
    show valeria shocked at left
    show entity neutral at right
    with dissolve
    e "Don’t be scared. I was the one texting you."
    v "How the hell did you get in here?"
    e "I’m here to offer you a solution, Valeria."
    v "A solution to what? You just came out of my {i}phone{/i}! You expect me to just calmly hear you out?"
    e "Then let me explain. You need help, don’t you?"
    show valeria angry at left with dissolve
    v "I don’t need your help!"
    e "You’re on the verge of losing your scholarship. If you tell your parents, you’ll lose all their support, won’t you?"
    e "You can’t even vent to your best friend. It’s not like he would understand. His professors love him, and he’s able to afford this school. Unlike you."
    v "Leave Darren out of this. And I could afford it if I took out a loan!"
    e "Don’t kid yourself. You’re trapped, and I’m your only way out."
    e "I’m clearly capable of more than even you can imagine. Helping you would be so simple. But beggars can’t be choosers, and I don’t work for free. If you want my help, I’d like something in return."
    v "Which is?"
    e "Your best friend, Darren Romero. His future seems bright. Don’t you deserve the same thing?"
    e "You were the star pupil in high school; now you can barely reach the top. Doesn’t it hurt to see Darren succeed while you fail? You could… extinguish some of that brightness."
    v "Why?"
    e "There’s no need to know {i}why{/i}, my dear Valeria. All {i}you{/i} need to know is that I can help."
    v "What am I supposed to do?"
    e "I’ll contact you, and you’ll know."
    v "What about if I can’t do what you ask?"
    e "Then I get your soul."
    v "My {i}soul{/i}? What is that supposed to mean?"
    e "You’re a smart person; I’m sure you know exactly what that entails. I’ll own your soul, your life. But that’s only if you fail."
    e "If you hold up your end of the bargain, I will solve all of your problems and you’ll never see me again."
    v "What else do you get out of this deal?"
    "It laughs, the sound every bit as shrill and raking as an unoiled iron gate swinging in the wind."
    e "I am an agent of mischief, dear Valeria. I thrive off the humiliation and suffering of human beings."
    e "When I have a chance, I appear to those who may help me. It’s a mutually beneficial relationship, of course, since I offer something in return."
    e "So, what will it be? Do we have a deal?"

    # Two Choices
    menu:
        "Accept":
            jump accept_deal
        "Refuse":
            jump refuse_deal

    # Choice 1
    label refuse_deal:
    v "No."
    "This entire situation is a mess, but I got myself into it. I’m the only one who can get myself out of it, too."
    "Not to mention the way this thing is talking about Darren… "
    "Despite the perfectly comfortable room temperature, I shiver."
    e "With no one else to rely on, aren’t you desperate?"
    v "I don’t know what it is you want from me… but you mentioned my friend. I won’t do anything to hurt him."
    v "I don’t care what you’re promising. I refuse."
    e "Very well. Goodbye, Valeria."
    "I blink. The entity has vanished, replaced by empty air."
    "I stand there for a few minutes, wondering what in the world I’d just talked to, and whether or not it was telling the truth."
    "In the end, I guess it doesn’t matter."
    jump game_over
    # The game ends here as Valeria refused the contract.

    # Choice 2
    label accept_deal:
    show valeria neutral at left with dissolve
    "I’m desperate. What else can I do? I dug myself into this hole, and now there’s a rope being lowered just for me."
    "All I have to do is avoid failure. Simple enough."
    v "Alright then, I accept."
    e "Wonderful. I knew you’d make the right decision."
    e "Grasp my hand and repeat after me: I, Valeria Jimenez, formally accept the terms of the Death Contract."
    v "I, Valeria Jimenez, formally accept the terms of the Death Contract."
    with long_flash
    # Everything goes dark. End scene.
    scene bg black with fade
    pause(3)

# Day 2
    label day2:
    # Classroom
    scene bg classroom
    show valeria neutral at left
    show darren neutral at right
    with fade
    "The next morning, I join Darren at our usual seats near the middle of the class."
    "With finals coming up, the room is packed today with students scrambling to cram as much psychology knowledge into their brains as possible."
    "The image of frantic students flipping through scattered notes is so jarringly normal, I almost forget the bizarre events of last night."
    d "Morning!"
    "Almost."
    v "Who gave you the right to be {i}such{/i} a morning person?"
    d "Well, you’re awfully chipper."
    "Professor" "Now, we’ve gone over the psychodynamic and biological theories on personality. If you’ve read the assigned pages, you’d know that today we will be discussing behaviorist theories."
    "Oh no."
    v "I forgot to read it since I was so worried last night… "
    d "What were you so worried about?"
    v "…"
    "Professor" "According to behavioral psychology, personality is determined by the environment, which reinforces your personality in an eternal cycle. Can someone tell me what the issue with this theory is?"
    "As expected, Darren is the first to raise his hand."
    "I sigh a little. He really doesn’t have to; someone else is bound to know the answer. Unfortunately, he likes showing off a bit too much to resist."
    d "Well, this theory considers environment as the only factor in determining someone’s personality. But what about cognition?"
    d "Someone’s thinking is just as important as the environment surrounding them. Like the choices you make are exactly that — choices. They can have unpredictable outcomes."
    "Professor" "Great job, Mr. Romero."
    "Student" "Know-it-all."
    "The person behind me mutters the insult underneath their breath, but I hear it all the same."
    "Though Darren doesn’t change his expression, I notice his shoulders slump ever so slightly."

    # Two choices
    # Note: I intend to include a similar scenario but with a major dip/raise in stats later on, and this bit is some foreshadowing and showing how some students view Darren.

    menu:
        "Don't say anything":
            # Choice 1, minor loss of Morality and Friendship
            #$stats.add_both(-1)
            $friendship += 1
            "Darren may be my best friend, but I’m not about to argue against the truth."
            "Out of the corner of my eye, I notice Darren glancing at me. He stays silent."
        "Defend Darren":
            # Choice 2, minor gain of Morality and Friendship
            #$stats.add_both(1)
            $friendship -= 1
            show valeria angry at left with dissolve
            "I turn around to glare at the person. They roll their eyes."
            "Student" "What? It’s true."
            v "At least he studies. What’s your grade in this class?"
            "Student" "I – you don’t need to know that!"
            show darren happy at right
            show darren neutral at right
            with dissolve
            "Darren stays silent, but a small smile appears on his face."
            show valeria neutral at left with dissolve
    # End of choices

    "The lecture continues. As usual, Darren studiously writes in and organizes his color-coded notes."
    "I didn’t do the reading, so the lecture doesn’t make a whole lot of sense to me. I frown at my binder full of nonexistent notes, remembering the conversation I had yesterday with my advisor."
    "Before long, class ends and I’m gathering my things, wondering what I should do before my next class."
    "Professor" "Miss Jimenez, can I speak to you for a moment?"
    d "I’ll wait outside."
    show darren neutral at offscreenright with ease
    hide darren neutral
    show valeria neutral at center with ease
    "I stand by the professor’s desk and patiently wait as he chats with a few students who have questions about a future quiz."
    "Wait a second."
    "A quiz?"
    "The professor turns to me expectantly."
    "Professor" "At the beginning of the semester you were doing very well in this class. You had high quiz scores and were clearly very studious. I know your friend, Mr. Romero is a good influence – "
    "I can’t understand why my professors, advisors, and parents always feel the need to bring up Darren. Back in high school it was never an issue, but now it feels like a competition I didn’t choose to be in."
    "The professor’s phone buzzes on his desk, breaking through his droning about how good I used to be."
    "Professor" "Ah, excuse me for a moment. This is important."
    "He leaves me alone in the classroom to take the call. Abrupt silence follows. Somehow, the absence of noise is even louder than he was."
    "Anxiety slowly fills the recesses of my mind, becoming a pool of sludge I’m fighting to stay afloat in. I hadn’t even realized there was a quiz. And I have to do well on it."
    "I chew on my bottom lip as I look down at the professor’s desk, desperate for a distraction."
    "Something catches my attention: a poorly-hidden sheet of paper with the word {i}ANSWER{/i} emblazoned across the top. Other sheets of paper cut off the rest of the title, but the next word starts with a K."
    "Answer Key… ?"
    "My heart freezes mid-beat in my chest. It would be so easy to snap a quick picture. No one would have to know."
# Take a photo (loss of Morality)
# Don't take a photo (no effect)
    menu:
        "Take a photo":
            # Choice: Take a picture of the key
            $stats.add_morals(-2)
            hide valeria neutral
            show valeria sad
            with dissolve
            "I nervously scan my surroundings just to reconfirm that I’m alone. I slip my phone out of my pocket."
            "For a moment, I think I hear the professor’s footsteps. I fumble with my camera app, swearing under my breath."
            v "Got it."
            hide valeria sad
            show valeria neutral
            with dissolve
        "Don't take a photo":
            # Choice: Ignore it
            "I can already hear my mother’s scolding, my father’s tone of disappointment. I’ve never cheated my entire school career, and I don’t think I’m about to start now."
            "An exhale escapes my lungs. Somehow, though I don’t know how, I’ll manage."
            "It would still be easy for anyone to see the answer key, though."
            # Ignore it (no effect)
            # Turn the paper over (small Morality gain)
            menu:
                "Ignore it":
                    # Choice: Ignore it
                    "I back away from the desk. If someone else wants to cheat, that’s not my problem."
                "Turn the paper over":
                    # Choice: Turn the paper over
                    $stats.add_morals(2)
                    "I don’t want to cheat. I’m better than that, but I don’t want any other student to get the chance either. It’s an unfair advantage."
                    "I flip the paper over so the blank side is up."
    #Return to main route

    "The professor comes back in, a little frazzled but once again calm and collected. He clears his throat."
    "Professor" "Sorry about that. Now, my point, Valeria, was that you’re capable of so much. Why is it that you’re failing my class? There are many resources to help you out, Darren could tutor you - "

    # Interrupt and lash out (Morality loss)
    # Stay calm (Morality gain)
    menu:
        "Interrupt and lash out":
            # Choice: Interrupt and lash out
            $stats.add_morals(-1)
            hide valeria neutral
            show valeria angry
            with dissolve
            v "I don’t care."
            "The professor stops talking abruptly."
            "Professor" "Excuse me?"
            v "Stop talking about Darren. I get it, he’s better than I am and smarter and a harder worker –"
            "Professor" "That’s not what I meant –"
            v "But that’s what it sounds like to me. Do you want to know how I got my scholarship? I was the valedictorian in high school."
            v "That’s right. Darren was below me. Now all anyone seems to talk about is how much I apparently suck."
            "Professor" "Valeria, please."
            # Insult the professor and leave (big Morality loss)
            # Calm down and leave (small Morality gain)
            menu:
                "Insult the professor and leave":
                    # Choice: Insult the professor and leave.
                    $stats.add_morals(-3)
                    "I hold up a hand before the professor can get in another word."
                    v "Just do me a favor and stop meddling in my life. I get it. Since your wife left you this summer, you’ve just been looking for someone else to bother."
                    "The professor’s face turns bright red at an alarming rate."
                    "Professor" "Excuse me?"
                    v "I’ll tell you this, Professor. It won’t be me."
                    "I storm away, leaving the speechless professor in my wake."
                    "I try to control my scowling before I leave the room. I don’t want Darren asking me what’s wrong."
                "Calm down and leave":
                    # Choice: Calm down and leave
                    $stats.add_morals(1)
                    hide valeria angry
                    show valeria neutral
                    with dissolve
                    "I take a deep breath and close my eyes. Okay, hold on. Maybe this isn’t the smartest move for me to take."
                    "The professor patiently waits for me to finish."
                    v  "I’m sorry. I’m going to go now."
                    "Professor" "… Alright. Take care, Valeria."
        "Stay calm":
            # Choice: Stay calm
            $stats.add_morals(2)
            "I concentrate on my breathing. Getting riled up over the professor mentioning Darren would be an ugly shade of jealousy to wear."
            "Professor" "Have you tried the tutoring services we offer?"
            v "I assure you that I’m well aware. I just don’t need them."
            "Professor" "Why is that? Your grades are slipping, and I think you could benefit from it."
            "I think back to my high school valedictorian days, to the time where I barely studied for exams but passed anyways. My friends looked up to me, and my parents praised me."
            "I never needed tutoring then."
            "Still, I relent, knowing that I’d be wasting my time if I tried arguing."
            v "Alright Professor, I’ll look into it."
            "It’s not worth it to argue. I’m just wasting my time."
            "Professor" "Great! I’ll see you in class, have a good day now."
            v "You too."
    # Return to main route

    label campus2:
    scene bg campus
    show valeria neutral at left
    show darren neutral at right
    with fade
    "I find Darren waiting outside, eyes glued to his phone and fingers rapidly texting away. The moment he hears the door open, he looks up and grins at me."
    "Even though I’m more than a little miffed at the professor’s talk, I give Darren a little wave."
    d "Ready for lunch? There’s a cool new spot near campus I wanted to check out."

# Politely decline (Friendship decreases slightly)
# Join Darren (Friendship increase slightly)
    menu:
        "Politely Decline":
            #$stats.add_friendship(-1)
            $friendship -= 1
            $join_lunch = False
            "After what the professor just said to me, I think the last thing I want to do right now is hang out with Darren."
            v "Sorry Darren, I think I wanna take this lunch alone."
            show darren sad at right with dissolve
            "Darren frowns a little, but he shrugs."
            show darren neutral at right with dissolve
            d "That’s okay. I just wanted to tell you something. I was gonna tell you yesterday, but you had your advisor meeting."
            # !!! not sure if this label works
            jump aftermenu2
        "Join Darren":
            # Choice: Join Darren
            #$stats.add_friendship(1)
            $friendship += 1
            $join_lunch = True
            "My stomach growls at the thought of food."
            v "Let’s go, I’m starving."
            "Darren leads me to a part of campus that I’ve never seen before. The picturesque sight of a large oak tree sitting on a hill greets us. Sunlight pierces through the foliage at just the right angle."
            show darren happy at right with dissolve
            show valeria happy at left with dissolve
            d "Nice, right?"
            v "Are you kidding? It’s perfect."
            "We flop down onto a shady part of the grass. I dig through my bag in search for the chicken wrap I made this morning. It’s hard to resist the urge to scarf the entire thing down, but I take a big bite anyway."
            v "Mmmh… so good."
            "Darren chuckles as he reaches for his own lunch."
            show valeria neutral at left with dissolve
            v "So… how did you find this place? Most of your classes are on the other side of campus."
            show darren neutral at right with dissolve
            d "That’s true, but I came over here to set up some posters."
            v "Posters?"
            "Why would he need to put up posters?"
            d "Oh yeah, I totally forgot that I didn’t tell you."
            "Tell me what?"
            "In the middle of my confusion, I recall what Darren hinted at yesterday before I went to meet with my advisor. He was about to tell me something then, but —"
    # Return to main route
    label aftermenu2:
        show darren happy at right with dissolve
        d "I’m running for student council president!"
        show valeria shocked at left with dissolve
        "Woah."
        "I guess I shouldn’t be surprised. Ever since he set foot on this campus, he’s been pretty involved with the student government."
        "Still, the news manages to catch me off-guard."
        "Before I can open my mouth to reply, my phone vibrates in my pocket. I excuse myself for a moment to check."

        hide valeria shocked
        hide darren happy
        with dissolve

        call phone_start
        call message_start("Unknown", "Remember what we talked about, Valeria?")
        call message("Unknown", "Now’s your chance.")
        call phone_end

        show valeria neutral at left
        show darren happy at right
        with dissolve

        "… Right."
        "Darren is still grinning, completely oblivious, waiting for my response."
        show valeria happy at left with dissolve
        "In an attempt to mask my rising anxiety, I plaster a fake smile on my face. I’m not sure if it’s more for his benefit or mine."
        v "That’s great news!"
        "I don’t know what else to say. All I can think of are the texts I just received."
        d "Thanks! Actually, I was wondering if you want to join the campaign effort."
        d "You can help me by asking people to vote for me and handing out promotional materials, stuff like that."
        menu:
            "Accept":
                # Choice: Accept
                v "Yeah! I’d love to help."
                d "Awesome! I know I won’t fail with you on board now."
                "He holds up his hand for what I know he’s hoping will be the best high five ever."
                menu:
                    "High-five him":
                        # Choice: High-five him (Minor friendship gain)
                        #$stats.add_friendship(1)
                        $friendship += 1
                        "Of course I have to. It’s basically my duty."
                        "There’s that initial sting of impact, and then the satisfaction of a high-five well-done."
                        d "Now it’s virtually impossible for us to lose."
                    "Leave him hanging":
                        show valeria neutral at left with dissolve
                        "I roll my eyes."
                        d "Aw, c’mon."
                        v "Let’s save that for {i}if{/i} you win, yeah?"
                        show darren sad at right with dissolve
                        "Darren sighs and lets his hand drop back to his side."
                        d "Fair point, I guess."
            "Decline":
                # Choice: Decline
                show valeria sad at left with dissolve
                "The thing that talked to me last night… it’s planning something, and I’m not sure if I like where it’s going."
                v "I’d rather not."
                show darren neutral at right with dissolve
                d "Please? I’d seriously appreciate it if my best friend could help me with my campaign."
                v "Don’t pull the best friend card on me."
                "My phone vibrates in my pocket again."
                hide valeria sad
                hide darren neutral
                with dissolve
                call phone_start
                call message_start("Unknown", "I do hope you haven’t forgotten.")
                call message("Unknown", "You have no choice.")
                call phone_end
                show valeria sad at left
                show darren sad at right
                with dissolve
                "…"
                d "Please?"
                "Like it said: I have no choice."
                "My fingers curl around my phone, gripping it so hard that my knuckles turn white. I hope Darren doesn’t notice."
                v "Okay, okay. Fine, I’ll help you."

    # Return to main route
    show valeria neutral at left
    show darren neutral at right
    with dissolve
    "I’m not sure if this is the worst idea I’ve ever had or the perfect opportunity, but there’s nothing I can do now."
    d "Actually, I think I have your first task at hand! You have some free time after lunch, right?"
    v "Yeah. What do you need?"
    "He pulls out a stack of large cards and hands me one. The card has {i}Vote for Darren Romero!{/i} emblazoned across the top, along with what looks like a website link."
    "I turn the card over. There’s a cherry lollipop taped to the back."
    v "Where does that link lead to?"
    d "It’s just a site I set up for the campaign! It’s got all of the information on what I have planned for the year should I be elected."
    d "It took around a day to get the whole thing working. It’s worth it, though."
    "A little excessive if you ask me, but I’m also not the one campaigning."
    d "Just go out to the campus courtyard and start handing these out. I’ve got to do something real quick, but I’ll come back and help you out."
    v "Sounds good to me."

    # IF VALERIA ACCEPTS LUNCH OFFER:
    if join_lunch:
        "The rest of lunch passes by quickly with idle chatter and irrelevant conversation. I joke and laugh, gossip and tease, but it feels like I’m just going through the motions."
    # Return to main route
    else:
    # IF VALERIA DOESN’T ACCEPTS LUNCH OFFER:
        scene bg restaurant with fade
        "I spend the rest of lunch alone, flipping through the psychology chapter I didn’t read. The words swim through my brain and refuse to stay anchored."
        "For twenty minutes, I read and re-read whole sections before I give up in frustration."
    # Return to main route

    "I can’t stop thinking about the deal I made last night. That thing wants me to hurt Darren’s campaign, no doubt. Only then will it help me."
    "The only question is, what am I supposed to do?"
    "At any rate, Darren gave me a task. I’ll have to deal with that first."
    jump pass_out_cards

image valeria neutral flip:
    "valeria neutral"
    xzoom -1.0

image valeria sad flip:
    "valeria sad"
    xzoom -1.0

image valeria angry flip:
    "valeria angry"
    xzoom -1.0

image valeria happy flip:
    "valeria happy"
    xzoom -1.0

image valeria shocked flip:
    "valeria shocked"
    xzoom -1.0
    linear 0.2 yoffset -50
    linear 0.2 yoffset 0

transform floor:
    ypos 1130

### omelette scripting starts here.
label pass_out_cards:
    scene bg campus with fade
    show valeria neutral at offscreenleft, floor
    pause 0.0
    show valeria neutral at left, floor with move
    "With my arms full of campaign materials, I enter the campus courtyard and start making my rounds."
    show valeria sad at center, floor with move
    "I don’t see Darren yet. Where is he?"
    show valeria happy at right, floor with move
    v "Vote Darren Romero for student council president!"
    show valeria neutral flip at center, floor with move
    "I approach a student and offer a card."
    show valeria happy flip
    v "Your support would mean a lot!"
    show valeria neutral flip
    "Student" "No thanks."
    show valeria sad flip
    "Maybe I should have taken a look at Darren’s website to know what else to say. But then again, I’d been hoping that Darren would take point."
    show valeria neutral flip
    "Desperate, I flip the card over to show the cherry lollipop taped to the back."
    show valeria happy flip
    v "There’s a free lollipop!"
    show valeria neutral flip
    "The student frowns."
    show valeria sad flip
    "Student" "I don’t like cherry."
    show valeria angry flip
    "I give up and move on."
    show valeria happy flip at left, floor with move
    v "Hey, vote for —"
    show valeria shocked flip
    "Student" "Can I just take the lollipop and give you back the card?"
    show valeria angry at center, floor with move
    "I turn away from them and approach a different gaggle of students. However, I’m met with the same infuriating indifference."
    show valeria neutral
    "Student" "I’m not voting. I’m exercising my right as an American citizen to not vote."
    show valeria sad
    v "You do know this isn’t a real political election, right?"
    show valeria neutral
    "Student" "Whatever, go read the Constitution or something."
    show valeria sad
    "I make eye contact with the next student, who’s already shaking their head. The frustration begins to well up inside of me."
    show valeria angry
    "This isn’t worth my time."
    show valeria shocked:
        linear 0.2 yoffset -50
        linear 0.2 yoffset 0
    "Student" "No thanks. I’m curious though: why isn’t Darren here himself?"
    show valeria angry:
        linear 0.2 yoffset 25
    v "Great question, buddy. Just take the card."
    show valeria angry:
        linear 0.2 yoffset 0
    pause 0.0
    show valeria angry at right, floor with move
    "I push the card into the student’s unwilling hands and walk off."
    show valeria sad
    "It’s actually a valid question, though. Darren told me he would meet up with me, but it’s been a good fifteen minutes and I haven’t seen him at all. It’s {i}his{/i} campaign."
    show valeria angry:
        xzoom -1.0
        linear 1.5 xalign 1.0
        pause 0.5
        block:
            xzoom 1.0
            linear 1.5 xalign 0.0
            pause 3.5
            xzoom -1.0
            linear 1.5 xalign 1.0
            pause 3.5
            repeat
    "I’m rapidly getting tired of the general apathy and uncomfortable summer heat I’m experiencing. I’m not even getting paid. I could be studying instead."
    # show valeria sad at right, floor with move
    show valeria sad:
        linear 0.5 xzoom -1.0
        linear 1.5 xalign 0.0
    "There’s still a decent stack of promotional cards left, but I don’t want to deal with them anymore."

    #Throw the rest away (Big Morality and Friendship loss)
    #Keep the rest to return to Darren (Big Morality and Friendship gain)
    menu:
        "Throw the rest away":
            $ friendship -= 3
            show valeria angry:
                linear 1.5 xalign 1.0
                linear 0.25 yoffset 50
                linear 0.25 yoffset 0
            "I chuck the remainder of the promotional cards into a trash bin, lollipops and all, and dust my hands off."
            # Return to main route
        "Keep the rest to return to Darren":
            $friendship += 3
            show valeria sad at center, floor with move
            "As annoyed as I am right now, I know Darren spent a lot of time and money on these cards. I’ll just stop promoting for now and hand them back to him later."
    show valeria neutral
    "Maybe if I manage to find him at all today, he’ll tell me face-to-face why he flaked on me."
    show valeria neutral at offscreenright, floor with move
    pause 0.25
    jump library

label library:
    scene bg library with fade
    show valeria neutral flip at offscreenright, floor
    pause 0.25
    "With that out of the way, I head towards the library. It’s not a bad place to start working on the problem of my grades."
    show valeria sad flip at right, floor with move
    "Even though I can hardly understand what I’m reading, I’m trying my best to concentrate. For a moment, I wish Darren had come so that we could study together."
    show valeria angry flip at center, floor with move
    "Or rather, so that I could rely on him. Maybe it was better that he didn’t come. Maybe I need to prove that I can do this on my own."
    show valeria angry flip at left, floor with move
    pause 0.25
    show valeria shocked flip
    "A cackle rips through the relative quiet."
    show valeria angry
    "I glare in the direction of the source, but the students are busy examining a poster on the opposite wall."
    show valeria neutral
    "The desired effect of my glare is lost entirely."
    show valeria sad
    "Student 1" "He looks ridiculous in that poster. He’s trying too hard to look smart."
    show valeria neutral
    "Student 2" "You can’t deny that he’s smart though."
    show valeria sad
    "Student 1" "Maybe. He’s still a try-hard though. Look at that tie, it’s just asking to be made fun of."
    show valeria neutral
    "I peer past them to see what they’re discussing."
    show valeria shocked:
        linear 0.2 yoffset -50
        linear 0.2 yoffset 0
    "It’s one of Darren’s campaign posters, depicting him in a formal suit with {i}Vote for Darren!{/i} across the top."
    show valeria sad
    "I’m reminded of the promotional cards I’d just handed out."
    show valeria angry
    "Without Darren’s help."
    menu:
        "Call out to the students":
            show valeria neutral at center, floor with move
            v "Hey! Are you guys talking about Darren Romero?"
            show valeria sad
            "Student 1" "Uh, yeah? Who else?"
            show valeria neutral
            "Student 2" "I can’t believe you just {i}had{/i} to go and badmouth someone you don’t even know personally."
            menu:
                "Join in":
                    $friendship -= 1
                    show valeria sad
                    "Honestly? I can’t blame them."
                    show valeria happy
                    v "He’s my friend and all, but you’re right about the tie."
                    show valeria neutral
                    "Student 1" "It’s like, you know this isn’t a real election right? It’s just some stupid school thing."
                    show valeria happy
                    v "That’s Darren though. He’s always going overboard."
                    show valeria sad
                    "The other student frowns at me."
                    show valeria angry
                    "Student 2" "Shouldn’t you be defending him if he’s your friend?"
                    show valeria angry flip
                    v "Maybe. But I won’t lie, he’s a try-hard. It’s even worse during class. You should see the way he sucks up to professors."
                    show valeria neutral flip
                    "They shrug, not saying much else as the first student and I make a few more jokes about Darren."
                    show valeria happy flip
                    "Talking about Darren like this is almost liberating, actually. The frustrations I’ve had bubbling in the pit of my stomach finally surface and I find relief."
                    show valeria neutral flip
                    "Eventually, we both get tired of joking around, so I return to my studying."
                "Defend Darren":
                    $friendship += 1
                    show valeria angry:
                        linear 0.25yoffset -50
                        linear 0.25yoffset 0
                    v "I don’t like the way you’re talking about my best friend."
                    show valeria sad
                    "Even though I’m still annoyed with Darren, there has to be a good reason for why he didn’t show up. I have to trust in him."
                    show valeria angry
                    "The student rolls their eyes."
                    show valeria neutral
                    "Student 1" "What I’m saying is true, though. Can you blame me?"
                    show valeria angry
                    v "Maybe I can. What you call a try-hard I call a hard worker, someone who’s organized and passionate about what they’re doing."
                    show valeria happy
                    v "You can think whatever you like of Darren, but he’ll succeed because of the effort he puts into everything."
                    show valeria angry
                    "Student 1" "Still, it’s just a stupid school election. It’s a waste of energy to be putting so much effort in that."
                    show valeria sad
                    "Student 2" "Hey, just drop it okay? I’m looking to study, not get in a fight. I’m sorry about this one, they have a big mouth."
                    show valeria neutral
                    v "That’s okay."
                    show valeria sad flip
                    "I’m not really looking to get into a fight either."
            show valeria sad flip at center, floor with move
        "Ignore them":
            show valeria neutral flip
            "That student’s laughing at him, but I don’t want to engage with them. I have better things to worry about."
            pause 0.05
            show valeria neutral flip at center, floor with move
    show valeria neutral flip
        # linear 0.5 yoffset 50
    "I open up my psychology textbook."
    show valeria sad flip
    "…"
    show valeria angry flip
    "…"
    show valeria angry flip:
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.1 xoffset 10
        linear 0.1 xoffset -10
        repeat
    "I’m suddenly overwhelmed with the urge to throw the book, or better yet myself, out the window."

    show valeria sad flip:
        linear 0.5 xoffset 0
    "I rub my eyes. Everything’s distracting me — my phone, the students whispering loudly in the corner. Darren’s absence, weighing down on mind."
    show valeria angry flip
    "The contract I have with my soul on the line…"
    show valeria sad flip
    "What am I going to do?"
    jump night2

label night2:
    scene bg bedroom night
    show valeria neutral at center, floor
    with fade
    "I sit in my bedroom in silence that night, watching the long shadows sprawled across my wall."
    show valeria sad
    "I can’t be bothered to answer the mountain of texts that have accrued throughout the day. I don’t even have to energy to mindlessly scroll through social media."
    show valeria shocked:
        linear 0.2 yoffset -50
        linear 0.2 yoffset 0
    "My phone lights up with yet another text."
    show valeria neutral:
        linear 0.5 xalign 0.25
    pause 0.75
    show valeria neutral flip
    call phone_start(pos='left')
    call message_start("Darren", "Hey V!")
    show valeria happy flip
    call message("Darren", "How did campaigning go?")
    show valeria angry flip
    call reply_message("…")
    call screen phone_reply("Tell him the truth","labelTruth","Lie","labelLie")
    return

label labelTruth:
    $friendship += 1
    call phone_after_menu
    call message_start("me", "Not very well.")
    show valeria sad flip
    call message("Darren", "What do you mean?")
    show valeria neutral flip
    call reply_message("Everyone I talked to didn’t seem to care, so I gave up.")
    show valeria sad flip
    call message("Darren", "Oh. Oh well.")
    show valeria neutral flip
    jump after_truth_lie

label labelLie:
    $friendship -= 1
    call phone_after_menu
    call message_start("me", "It went well.")
    show valeria sad flip
    call message("Darren", "Really?")
    show valeria neutral flip
    call reply_message("Yeah, I talked about what you were planning to do.")
    show valeria sad flip
    call reply_message("People seemed excited.")
    show valeria angry flip
    call message("Darren", "Right.")
    show valeria sad flip
    jump after_truth_lie

label after_truth_lie:
    show valeria neutral flip
    call message("Darren", "V… when I asked you how campaigning went, you just… sent ellipses.")
    show valeria sad flip
    call message("Darren", "You know how it is when I get anxious over messages.")
    show valeria neutral flip
    call message("Darren", "It feels like you’re irritated. Is everything okay?")
    show valeria sad flip
    call screen phone_reply("Point out his absence","labelAbsence","Brush it off","labelBrush")

label labelAbsence:
    call phone_after_menu
    call message_start("me", "Where were you this afternoon? It’s your campaign, and you weren’t even there.")
    show valeria angry flip
    call message("Darren", "I know, I’m sorry.")
    show valeria sad flip
    call message("Darren", "It was kind of on a short notice.")
    show valeria angry flip
    call reply_message("What was? Seriously, people were asking me about you.")
    show valeria sad flip
    call reply_message("What could you possibly have been busy with?")
    show valeria angry flip
    call message("Darren", "I can’t really tell you.")
    show valeria shocked flip
    call reply_message("Oh, you just wanted to get out of the sun, huh? It was hot as hell, so you made the right choice..")
    show valeria angry flip
    call message("Darren", "No, that’s not it.")
    show valeria sad flip
    call reply_message("What was it, then?")
    show valeria angry flip:
        linear 0.2 yoffset -50
        linear 0.2 yoffset 0
    call message("Darren", "I said, I can’t tell you.")
    show valeria shocked
    call reply_message("Alright, I see how it is.")
    show valeria angry
    call phone_end
    show valeria sad
    "I purse my lips in irritation. What’s he not telling me?"
    jump entity2

label labelBrush:
    call phone_after_menu
    call message_start("me", "Nothing.")
    show valeria neutral flip
    call message("Darren", "Are you sure?")
    show valeria sad flip
    call reply_message("Yeah. Just let me get back to work. I’m fine.")
    show valeria neutral flip
    call message("Darren", "Okay…")
    show valeria sad flip
    call phone_end
    show valeria angry flip
    "Whether it’s out of a sense of futility or weariness, Darren doesn’t text back."
    show valeria sad flip
    "Still, I can’t help but wonder why he never mentioned his absence today."

label entity2:
    "I’m deep in thought when a figure appears before me, seemingly out of thin air. I jump up from my seat."
    show valeria shocked:
        linear 0.2 yoffset -50
        parallel:
            linear 0.2 yoffset 0
        parallel:
            linear 0.2 xalign 0.0
        block:
            linear 0.05 xoffset 5
            linear 0.05 xoffset -5
            linear 0.1 xoffset 10
            linear 0.1 xoffset -10
            repeat
    show entity neutral at right with flash
    v "What the hell?"
    show valeria neutral flip at left, floor
    e "Hello, Valeria. I {i}did{/i} tell you I would contact you again, didn’t I?"
    show valeria angry flip
    v "Yeah, well, humans don’t usually just {i}appear{/i} out of thin air when they wanna talk to each other, so don’t blame me for getting a heart attack every time you do… {i}that{/i}."
    show valeria angry flip:
        linear 0.25 xoffset 25
        linear 0.25 xoffset 0
    "I gesture to the previously empty space the entity now occupies."
    show valeria neutral flip
    v "So… you want me to sabotage Darren’s campaign."
    show valeria sad flip
    e "Yes, I hope I made that abundantly clear."
    show valeria angry flip
    v "Oh trust me, it was {i}very{/i} clear."
    show valeria sad flip
    "I just… I just don’t know if I can do this."
    show valeria shocked flip
    "An unsettling smile crawls across the entity’s face."
    show valeria sad flip
    e "My dear, you don’t need any supernatural abilities to hurt someone else. Humans do it all the time. They break each other’s hearts, they make each other cry, they drive each other mad, all with a few words. That’s all it takes."
    show valeria angry flip
    v "What? I’m not doubting my {i}abilities{/i}, I just…"
    show valeria sad flip
    "My voice falters."
    show valeria neutral flip
    e "Ah, I see. Is it because he’s your friend?"
    show valeria sad flip
    "… Is he? I think back to earlier this afternoon, when he made a promise and didn’t keep it. And now he’s refusing to tell me why."
    show valeria angry flip
    e "Remember the conditions you agreed to. I will own your life and your soul should you fail."
    show valeria neutral flip
    e "You’re more than capable, Valeria. You already agreed to help him with the campaign. Just choose to do the opposite."
    show valeria sad flip
    v "…"
    show valeria angry flip
    v "Tomorrow. I’ll see what I can do."
    show valeria sad flip
    "The entity’s smile has not faded."
    show valeria neutral flip
    e "Have a good night, Valeria."
    show valeria shocked flip
    hide entity neutral with flash
    "I end up not sleeping at all."
    show valeria sad flip at center, floor with move
    "That gives me plenty of time to consider my situation."
    jump day_3

# Day Three

# General course of events regardless of route
# Scene 1: Going to class, conversation with Darren
# Scene 2: A conversation with the entity in the bedroom that either reinforces Valeria’s pride and actions, or causes her to fight against it
# Scene 3: Meeting Darren in the library to help him write his speech

label day_3:
    if friendship < 0:
        jump route3_1
    else:
        jump route3_3

# Route 1 Low Friendship, Low Morality
label route3_1:
    scene bg classroom_gray with fade
    show valeria sad at offscreenright, floor
    "Back in high school, Darren and I studied together a lot. He used to ask me for help since I was always scoring higher than him."
    show valeria sad at right with move
    "That made me feel… confident. Needed."
    show valeria angry at center with move
    "But now? I’m watching him breeze through life with his rich parents and good grades while I’m finding myself dead in the water."
    show valeria shocked at left with move
    "Everyone’s constantly rubbing in how Darren is such an excellent student and we should study together. He might offer to help me because we’re friends, but I know it’s also because he pities me."
    show valeria angry flip:
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.1 xoffset 10
        linear 0.1 xoffset -10
        repeat
    "I helped him get to where he is now. And I deserve more than I’m getting."

    # Classroom scene
    scene bg classroom
    show darren neutral at right, floor
    show valeria angry flip at offscreenright
    with fade
    show valeria angry flip at left, floor with move
    "When I head into literature class, I find Darren already seated, flipping through the assigned reading of {i}The Iliad{/i}."
    show valeria angry
    show darren sad
    "There’s little to no time to make small talk as the rest of the class filters in, followed by the professor."
    show darren neutral
    show valeria angry flip
    "Occasionally, I scowl in Darren’s direction."
    show valeria shocked
    "He doesn’t seem to notice, but that only fuels my anger."
    show valeria neutral
    show darren happy
    "Professor" "I hope you’re all prepared for our discussion today: the theme of betrayal!"
    show valeria angry
    "My ears burn. What a fitting topic."
    show darren neutral
    show valeria sad
    "Professor" "Now, there are multiple instances of betrayal throughout the poem…"
    show darren sad
    show valeria shocked flip
    "Darren nudges me, temporarily distracting me from the lecture at hand."
    show valeria neutral flip
    d "Hey Valeria, if you don’t mind… could you meet me in the library later? Elections aren’t until next week, but… I kind of want to get my speech out of the way."
    show valeria angry flip
    "The request comes out slow and hesitant, like he hasn’t forgotten the hostility I showed over text last night."

    menu:
        "Accept, with attitude":
            # Choice: Accept, with attitude
            show valeria angry flip:
                linear 0.2 xoffset 25
                linear 0.2 xoffset 0
            v "Shh. The professor’s lecturing on Achilles’ betrayal of Agamemnon. You should show some respect."
            show valeria shocked flip
            show darren angry
            d "Come on…"
            show valeria angry flip
            show darren neutral
            v "Fine, sure. Maybe I’ll suddenly be busy and won’t show up though. Just to keep you on your toes."
            show valeria angry
            show darren sad
            "Darren sighs, but he leaves me alone after that."
        "Offer an abivalent answer":
            show valeria flip sad
            show darren neutral
            v "Oh, I might be busy. Can’t say for sure."
            show valeria flip neutral
            show darren angry
            "Darren furrows his brow, clearly annoyed at my non-answer."
            show darren sad
            show valeria flip sad
            d "Fine. I’ll see you if you’re able?"
            show valeria angry
            v "Yup, whatever."
            # Return to main route
        "Decline":
            show darren neutral
            show valeria flip angry
            v "No. I’ve got better things to do."
            show darren angry
            show valeria neutral flip
            d "Are you still mad at me? I’m sorry, okay? I’ll give you a proper apology later, I just really need your help right now."
            show darren sad
            show valeria sad flip
            d "Please?"
            show valeria angry flip
            "Well… if I can find a way to ruin his speech, it would go a long way to saving my soul."
            show valeria sad flip
            show darren happy
            v "Maybe, then. I won’t make any promises."
            show valeria neutral
    show darren neutral
    "Professor" "… and there were probably times when you were all going, ‘Hey Achilles, stop being such an idiot already! There are bigger things to deal with than your ego!’"
    show valeria sad
    "Professor" "It’s incredible how pride can drive someone to such lengths. No wonder it’s considered a deadly sin."

    menu:
        "Raise hand":
            show valeria angry
            "I’m struck by the sudden need to defend Achilles and his decision. After all, he had a valid reason to refuse bowing down to Agamemnon."
            show valeria neutral
            "Professor" "Yes, what do you have to say?"
            show valeria angry
            show darren sad
            v "Isn’t it really harsh to judge Achilles and simply call him prideful?"
            show valeria neutral
            "Professor" "Go on."
            show valeria happy
            v "Well, Achilles has every right to stand up for himself. Agamemnon isn’t exactly the greatest of the bunch. Meanwhile, Achilles is the best warrior in the army."
            show valeria angry
            show darren angry
            "Darren jumps into the conversation, like he can no longer bear staying silent."
            show valeria neutral
            d "Still, it’s like the professor said: there are more important things going on. Achilles should put aside his pride. Lives are at stake."
            show valeria angry
            v "So you’re siding with Agamemnon? The man who shouldn’t be in charge in the first place? He is every bit as prideful as Achilles, but he never proves himself the same way Achilles does."
            show darren neutral
            show valeria neutral
            "Darren opens his mouth to reply, but he seems to be at a loss for words. He takes in a deep breath and closes his mouth, signaling an end to the conversation."
            show valeria angry
            "For what seems like the first time ever since we entered college, Darren doesn’t raise his hand again. Instead, he quietly contemplates the pages of his book."
        "Don't raise hand":
            show valeria sad
            "I can’t think of what to say. I never really was the type to participate in class, anyway."
            show valeria neutral
            show darren sad
            "The professor continues pushing us to examine the betrayal between Achilles and Agamemnon."
            show valeria shocked
            show darren neutral
            "Eventually, I come to my own conclusions. As the greatest warrior in the army, Achilles has every right to stand up for himself. Agamemnon never proves himself; he is beneath Achilles."
            show darren sad
            show valeria angry
            "For what seems like the first time ever since we entered college, Darren doesn’t raise his hand at all. Instead, he quietly contemplates the pages of his book."
    show valeria angry
    show darren neutral
    "I’m not sure if he’s absorbing anything that the professor is saying."
    jump bedroom3_1

label bedroom3_1:
    scene bg bedroom with fade
    show entity at offscreenright
    show valeria neutral at offscreenright, floor
    show valeria neutral at left, floor with ease
    "After class, I retreat to my dorm. I have some time to kill before I have to meet up with Darren at the library, and the less time I spend with Darren, the better."
    show entity neutral at right with flash
    e "Hello, Valeria."
    show valeria neutral flip
    "This time, the materialization out of thin air doesn’t faze me."
    show valeria angry flip
    v "What do you want {i}this{/i} time?"
    show valeria neutral flip
    e "Oh, nothing more than what you’re already supplying. You’re doing an excellent job."
    show valeria sad flip
    e "Despite all of the support you’ve given him, it seems our dear friend Darren isn’t so eager to return the favor, is he?"
    show valeria angry flip
    "I grit my teeth. It hurts, but it’s the unkind truth."
    show valeria shocked flip
    v "I’ve been helping him since high school, and {i}this{/i} is how he decides to thank me."
    show valeria angry flip
    e "Even {i}I’m{/i} appalled, and I’m a {i}demon{/i}. At the very least, I’m honest and I keep my promises."
    show valeria sad flip
    e "But now… you see? He clearly doesn’t need you. And now, the feeling is mutual."
    show valeria angry flip
    v "That son of a — "
    show valeria angry flip:
        linear 0.2 yoffset -50
        linear 0.2 yoffset 0
    pause 0.4
    show valeria angry flip at center, floor
    show entity:
        xpos 0.8
    with move
    "I get up mid-sentence and sling my backpack over my shoulder. The entity curls a shadowy hand around the back of my chair, watching me curiously."
    show valeria sad flip
    e "What will you do now?"
    show valeria angry flip at right with move
    "I stalk towards the door and grip the cool metal of the knob tightly."
    show valeria shocked:
        xzoom -1.0
    v "I’m going to ruin the rest of his life."
    show valeria angry at offscreenright with move
    jump library3_1

label library3_1:
    scene bg library
    show darren neutral at right
    with fade
    show valeria angry flip at offscreenleft
    show valeria angry flip at left with move
    "I enter the library in a haze of anger."
    show valeria shocked
    show darren sad
    "Darren gives me a halfhearted wave when he spots me, like he can perceive the anger that rolls off of me in an all-encompassing aura."
    show valeria neutral
    show darren neutral
    d "Hey, I wanted to apologize for yesterday — "

    menu:
        "Stop him":
            show valeria angry
            v "Save it."
            show valeria neutral
            show darren shocked
            d "Wh- What?"
            show valeria angry
            v "I said, {i}save it{/i}. I’m not interested in what you have to say anymore. I’m only here to fulfill a promise, nothing more."
            show darren angry
            "Darren furrows his brow and breaks eye contact from me. He doesn’t say anything for a very long time."
            show darren sad
            "Nevertheless, I pull out my laptop and start a new document."
            show valeria sad
            v "Let’s get this over with."
        "Listen to his apology":
            show darren sad
            d "I, uhm. This is embarrassing to admit, but I was getting anxious."
            show darren angry
            show valeria sad
            d "I thought about meeting all of those people and having to promote myself to them. And something inside me… {i}froze{/i}."
            show valeria neutral
            show darren sad
            d "I couldn’t move. I couldn’t do it."
            show darren neutral
            d "To be clear, this isn’t an excuse. I was supposed to be helping you. It’s just… an explanation. For why I wasn’t there when I should have been."
            show darren sad
            show valeria angry
            d "You’ve also been acting really weird these past few days. It feels like I hurt you somehow, and I don’t know what I did, but whatever I did, I just want to say…"
            show valeria sad
            d "I’m sorry."
    menu:
        "Ridicule him":
            show valeria angry:
                linear 0.2 yoffset -25
                linear 0.2 yoffset 0
            show darren shocked
            "I scoff."
            v "You were {i}scared{/i}? Don’t you know what you signed up for?"
            show darren shocked
            d "Yeah, but —"
            show darren sad
            v "You’re running for student body president. You should have known you were going to have to do this sort of thing."
            show darren angry
            show valeria sad
            v "The only way you’re gonna be able to build up support is if you promote yourself. Which you’re now telling me you’re scared to do."
            show valeria angry
            show darren shocked
            v "What will everyone think when they realize you’re just a coward?"
            show valeria neutral
            "Darren stares at me, mortified, with no words left to grasp at. Ignoring him, I pull out my laptop and open a new document."
            show valeria sad
            show darren angry
            v "Let’s get this over with. I don’t want to do this any more than you do, apparently."
        "Reject his apology":
            show valeria angry
            show darren shocked
            v "I don’t care."
            show darren sad
            show valeria neutral
            d "I’m sorry?"
            show valeria angry
            v "I don’t want your apology. It’s not fit for me to accept."
            show darren angry
            d "What — what do you want me to do? Grovel at your feet? How am I supposed to apologize further when I don’t know what else I did to you!"
            show darren shocked
            v "Maybe I would’ve accepted some grovelling before, but I don’t want it anymore. I’m here to do this one final thing for you, and after that, we’re finished."
            show darren angry
            "Darren narrows his eyes at me. Ignoring him, I pull out my laptop and start a new document."
            show valeria sad
            v "Let’s get this over with. I don’t want to do this any more than you do, apparently."
    jump route4_1

# Route 3 High Friendship, High Morality
label route3_3:
    scene bg classroom_gray with fade
    show valeria sad at offscreenright, floor
    "Back in high school, Darren and I studied together a lot. He used to ask me for help since I was always scoring higher than him."
    show valeria sad at right with move
    "That made me feel… confident. Needed."
    show valeria angry at center with move
    "We’ve switched places now. He’s soaring to higher heights than I’d ever reached. All I can do is look up."
    show valeria sad at left with move
    "Still… he’s trying to pull me up. He might have an insufferable know-it-all streak to him, but he’s a good person, through and through."
    show valeria sad flip
    "I’m still not sure why he flaked on me, but there has to be a reasonable explanation."
    show valeria sad flip at center with move
    "If I’ve realized anything from my success in high school and subsequent failure in college, it’s that people aren’t just what they appear to be."

    # Classroom scene
    scene bg classroom
    show darren neutral at right, floor
    show valeria sad flip at offscreenright
    with fade
    show valeria sad flip at left, floor with move
    "When I head into literature class, I find Darren already seated, flipping through the assigned reading of {i}The Iliad{/i}."
    show darren sad
    show valeria neutral
    "There’s little to no time to make small talk as the rest of the class filters in, followed by the professor."
    show darren neutral
    show valeria neutral flip
    "Occasionally, I try to establish eye contact with Darren, but he doesn’t seem to notice. Or he’s ignoring me. Did I hurt him with my texts last night?"
    show valeria sad
    "Wish I had telepathy."
    show valeria neutral
    "Professor" "I hope you’re all prepared for our discussion today: the theme of redemption!"
    show valeria shocked:
        linear 0.2 yoffset -50
        linear 0.2 yoffset 0
    "Right as I’m about to give up trying to communicate with Darren, he nudges me."
    show valeria neutral flip
    show darren happy
    d "Hey Valeria, if you don’t mind… could you meet me in the library later? Elections aren’t until next week, but… I kind of want to get my speech out of the way."
    show darren sad
    show valeria sad flip
    "The request comes out slow and hesitant, like he’s carefully trying to walk on eggshells without breaking them."

    menu:
        "Accept":
            show valeria neutral flip
            "If there’s any way to ensure Darren succeeds in winning the hearts of the student body, this would be it."
            show valeria sad flip
            "I’m ashamed of the fact that I accepted a deal to hurt him for my own gain. But maybe I can make up for what I did."
            show valeria happy flip
            v "You know what? I have a better idea."
            show darren neutral
            d "Like what?"
        "Decline":
            show valeria sad flip
            "By now, I’m wary about my role in assisting Darren’s campaign. Clearly this speech is another chance for me to sabotage his work."
            show darren neutral
            v "I… I don’t think that’s a good idea."
            show valeria neutral flip
            show darren sad
            d "Why?"
            show valeria sad flip
            "How can I explain the contract I made with a demonic entity in the most normal way possible? And how can I explain that I was ready to hurt him?"
            show valeria angry flip
            "I just don’t trust myself with the responsibility of helping him write that speech."
            show valeria sad flip
            "…"
            show darren neutral
            "Maybe I can spin this another way."

    show valeria neutral flip
    v "I think you can write the speech. I mean, obviously I’ll proofread and all that. But I think you can write the speech yourself."
    show darren shocked
    d "What?"
    show valeria happy flip
    v "Yeah! You can write well; I’ve seen your persuasive essays. You can practice your speech on me, but I think you can write it yourself."
    show darren sad
    show valeria neutral flip
    d "But what if I mess it up?"
    show valeria happy flip
    v "No way, just look at you! How can you mess it up? You’ve been passionate about making the campus a better place for students ever since we started attending classes here."
    show darren neutral
    v "I believe in you."
    show darren sad
    show valeria shocked:
        linear 0.2 yoffset -50
        linear 0.2 yoffset 0
    "Darren frowns at me, but I’m forced to shut up when the professor shoots a stern look in my direction."
    show valeria sad
    show darren neutral
    "Professor" "Now… there were probably times when you were all going, ‘Hey Achilles, stop being such an idiot already! There are bigger things to deal with than your ego!’"
    show valeria neutral
    "Professor" "And yet, he somehow redeemed himself in the end. How?"

    menu:
        "Raise hand":
            show valeria neutral:
                linear 0.25 yoffset -25
                linear 0.5 yoffset 0
                pause 1.5
                repeat
            show darren shocked
            "I’m struck by the sudden need to answer the question. After all, Achilles didn’t redeem himself without help."
            show darren shocked
            show valeria neutral at left
            "Professor" "Yes, what do you have to say?"
            show valeria happy
            v "I think a lot of that had to do with not just his actions, but also Patroclus’."
            show darren sad
            "Darren raises an eyebrow."
            show valeria neutral
            "Professor" "Go on."
            show valeria happy
            v "Patroclus’ actions open up that possibility of redemption. His death causes Achilles to do some unspeakable things, but in turn, I think Patroclus’ love redeemed Achilles."
            show darren neutral
            v "That’s all I wanted to say."
            show valeria neutral
            "Professor" "Interesting contribution! Anyone else want to add on?"
        "Don't raise hand":
            show valeria sad
            "I can’t think of what to say. I never really was the type to participate in class, anyway."
            show valeria neutral
            "The professor continues pushing us to examine Achilles and his love for Patroclus."
            show valeria sad
            "Eventually, I come to my own conclusions and write them down. Achilles doesn’t redeem himself without help. Patroclus’ actions open up that possibility of redemption."
    show valeria neutral
    show darren sad
    "For what seems like the first time ever since we entered college, Darren doesn’t raise his hand at all. Instead, he quietly contemplates the pages of his book."
    show darren neutral
    "Still, something tells me he’s listening."
    show valeria happy
    "We’re going to make this happen."
    jump bedroom3_3

# Valeria’s Bedroom
label bedroom3_3:
    scene bg bedroom with fade
    show entity at offscreenright
    show valeria neutral at offscreenright, floor
    show valeria sad at left, floor with ease
    "After class, I retreat to my dorm. I have some time to kill before I have to meet up with Darren at the library, and I might as well collect my thoughts alone."
    show entity neutral at right with flash
    e "Hello, Valeria."
    show valeria angry
    "This time, the materialization out of thin air doesn’t faze me."
    show valeria angry flip
    v "Hello."
    show valeria neutral flip
    e "I must say, I’m fairly disappointed in your progress. The election is coming up soon, and you’re no closer to destroying Darren’s prospects."
    show valeria sad flip
    e "Almost as if you refuse to."
    show valeria angry flip
    v "That’s my intention, yes."
    show valeria sad flip
    show entity:
        linear 1.5 xpos 0.5
    "The entity doesn’t immediately reply, but curls its shadowy fingers, one by one, around the back of my chair. I ignore the sudden chill the crawls along my shoulder."
    e "Let me remind you of the terms of our contract — "
    show valeria angry
    v "You don’t have to remind me. I still remember."
    show valeria sad
    show entity:
        linear 0.25 yoffset -15
        linear 0.5 yoffset 0
    "The entity snorts."
    e "You would give up your life — your {i}soul{/i} — for your friend?"
    show valeria angry
    v "What kind of friend would I be if I made him miserable instead?"
    show valeria sad
    "I get up and sling my backpack over my shoulder. The entity watches me curiously."
    show valeria neutral flip at right with move
    e "What will you do now?"
    show valeria neutral
    "I meet its unblinking stare before I open the door, smiling slightly."
    show valeria happy
    v "I’m gonna help my friend."
    show valeria happy flip at offscreenright with ease
    jump library3_3

# Library
label library3_3:
    scene bg library with fade
    show darren sad at right
    with fade
    show valeria happy flip at offscreenleft
    show valeria happy flip at left with move
    "I enter the library in a laser-focused mindset of determination."
    show darren neutral
    "Darren waves when he spots me, but his hand moves a little slower than usual. The movement is almost sheepish, like he has half a mind to shrink in his seat."
    show valeria neutral flip
    show darren sad
    d "Hey… I wanted to apologize. For yesterday, that is."
    show valeria sad flip
    "He pauses mid-thought, struggling with the words he wants to say. I patiently wait for him to continue."
    show valeria neutral flip
    d "The reason why I didn’t meet up with you was because… well, I was getting anxious."
    show darren neutral
    d "I thought about meeting all of those people and having to promote myself to them. And something inside me… {i}froze{/i}."
    show darren sad
    d "I couldn’t move. I couldn’t do it."
    show valeria sad flip
    d "To be clear, this isn’t an excuse. I was supposed to be helping you. It’s just… an explanation. For why I wasn’t there when I should have been."
    show valeria neutral flip
    show darren neutral
    d "And I know that hurt you. I don’t blame you."
    show darren sad
    d "I’m sorry."

    menu:
        "Ask why he didn't tell you":
            show valeria sad flip
            show darren neutral
            v "Darren, if you’d told me yesterday that you couldn’t do it, I would’ve understood. Why didn’t you?"
            show valeria neutral flip
            show darren happy
            "Darren lets out a hollow laugh."
            show darren neutral
            d "It’s so dumb now that I think about it, but I was just scared to tell you."
            show valeria happy flip
            v "That isn’t dumb."
            show darren happy
            d "Thanks."
        "Ask if he still wants to run":
            show valeria happy flip
            v "Thanks. The fact that you’re trusting me with this means a lot."
            show valeria neutral flip
            show darren neutral
            v "Not to put too fine a point on it, but running for student body president is all about promoting yourself. Do you still want to… ?"
            show darren sad
            "Darren sighs."
            show darren neutral
            d "Yeah. I really want to make a difference, you know?"
            show valeria happy flip
            d "I just need to get better at talking to people. And fast, if I want to start promoting myself before elections next week."
    show valeria neutral flip
    v "Well at any rate, I accept your apology. I won’t lie, I was definitely confused and hurt, but I’m glad you came to me."
    show darren happy
    show valeria happy flip
    v "For the record, I meant every word I said earlier. About believing in you. You should believe in yourself, too."
    show valeria neutral flip
    show darren sad
    d "Claiming that I believe in myself is one thing. Actually believing in myself is another."
    show darren neutral
    show valeria happy flip
    v "Then believe in me, because I believe in you."
    show darren happy at right
    "The corner of Darren’s mouth twitches upwards."
    show valeria neutral flip
    d "That’s a bit roundabout."
    show valeria happy flip
    v "Well, you gotta believe in someone, don’t you?"
    show valeria darren neutral
    v "I know you’re gonna do some great work as president, Darren."
    show darrne happy
    d "I hope so."
    show valeria neutral flip
    "I pull out my laptop and start a new document."
    show darren neutral
    v "Here. You dictate. I’ll write. Make this speech your own."
    show valeria happy flip
    v "And count me as your second-in-command this week. I’m gonna be right there beside you, making people realize you’d be the best president in the history of this college."
    show valeria neutral flip
    show darren happy
    d "… Thanks, Valeria. {w=1.0} For everything."
    jump route4_3

# Day Four (Election Day, a week later)
# General course of events regardless of route
# Scene 1: Darren gives his speech in the auditorium, then has a conversation with Valeria
label route4_1:
    # Route 1 Low Friendship, Low Morality
    scene bg auditorium with fade
    "Come Election Day, I join the crowds of students gathered to hear the candidates’ speeches."
    "Even after \"assisting\" Darren in writing the worst, most half-assed speech in the history of speeches, I have to wonder if he’s stubborn enough to make an appearance."
    "Student 1" "Did you notice? The ballots still have Darren’s name on it."
    "Student 2" "I never even saw him around campus. I saw all of the other candidates… but never him."
    "Student 1" "He’s still going to class, but he snapped at the first person who tried asking him. First time I think {i}anyone{/i} ever saw him angry."
    "Interesting. He’s been dutifully avoiding the classes we share."
    "A hush comes over the audience. One of the faculty members has walked on stage and approached the mic."
    "Faculty Member" "Good morning, everyone. Unfortunately, Darren Romero, who was previously running for student body president, has dropped out of the race. Please disregard his name on the ballot when voting."
    "The whispers in the audience increase in volume. As everyone gossips about this new development, my phone vibrates in my pocket."

    call phone_start
    call message_start("Unknown", "The terms of the contract have been met. You’ll get to keep your scholarship.")
    call message("Unknown", "Congratulations, Valeria Jimenez. It was a pleasure working with you.")
    call reply_message("The pleasure was all mine.")
    call phone_end

    "With my freedom finally confirmed, I begin walking away from the assembled students. Each step I take feels lighter than the last."
    "I’m never failing again."
    "Meanwhile, somewhere else on campus, Darren Romero’s failures have only just begun."
    jump end1

    # Route 3 High Friendship, High Morality
    label route4_3:
    scene bg auditorium with fade
    "Come Election Day, I join the crowds of students gathered to hear the candidates’ speeches."
    "This past week has simultaneously been the most stressful and the most rewarding week I’ve ever experienced."
    "Darren managed to write up a speech all on his own — and, in my humble opinion, it was one of the best speeches I’d ever heard, even after I had to sit through fifty of Darren’s speech recitations."
    "I eavesdrop on the students around me, trying to gauge their feelings and reactions."
    "Student 1" "Man, I’m tired. All of those speeches…"
    "Student 2" "Hey, last person’s coming up, though! You have anyone in mind yet?"
    "Student 1" "I’m leaning towards Darren."
    "Student 2" "Wow, decided already? He hasn’t even given his speech yet."
    "Student 1" "I know you’re just joking, but he came up to me the other day and recognized me. Knew that I’d been trying to push for more resources that help freshmen transition into college because of my younger sister."
    "Student 2" "He’s pretty friendly, isn’t he? I always assumed he was a teacher’s pet who only liked talking to the professors, but when I actually met him, he was surprisingly approachable."
    "Student 1" "Yeah! Not to mention he has a clear and concise plan for how he can help us as president. I really hope he wins."
    "I let out a sigh of relief. Glowing reviews, all around. Hopefully."
    "A hush comes over the audience. I spot Darren striding across the stage towards the mic."
    #show darren neutral at offscreenleft ---too fast
    show darren neutral at center with dissolve
    "He’s the very picture of confidence."
    d "Good morning, everyone! As you all know, I’m Darren Romero, and I’m running for student body president…"
    "Darren plunges into his speech. I know the words by heart, but something about the way he seems to make eye contact with everyone in the audience, something about the way his voice carries through…"
    "The exhilaration of being on a stage has transformed his words."
    "All around me, college students listen quietly, enraptured. Somehow, Darren has done the impossible."
    d "… And that’s why I believe I can be your next student body president. So vote for me, Darren Romero! Thank you!"
    "Everyone erupts into cheers, cheers that are much louder than any reception the other candidates have received."
    "I smile to myself. Suffice it to say, there’s no need to wait until the ballots get counted to know that Darren has won the vote."
    "Right on cue, my phone vibrates in my pocket. I’ve been waiting."
    hide darren neutral with dissolve

    call phone_start
    call message_start("Unknown", "The terms of the contract were not met. You will forfeit your scholarship, life, and soul to me.")
    call reply_message("I’m not scared of you.")
    call message("Unknown", "Then you’re a fool.")
    call message("Unknown", "Before I take over your pitiful existence, I would like to know why.")
    call reply_message("Guess it couldn’t hurt to explain why I decided to defy the wishes of an immortal demon, huh?")
    call message("Unknown", "You are wasting your time, my dear Valeria. I would talk, and talk fast.")
    call reply_message("He’s my friend. My soul isn’t worth anything without my friendship to Darren.")
    call message("Unknown", "You would truly have such a low opinion of yourself?")
    call reply_message("Your contract called for just one soul — mine.")
    call reply_message("But what happens when my soul is connected to another? And another? One connection for each friendship I have.")
    call reply_message("Unless I cut those ties, you won’t be receiving one soul. You’ll be receiving the pieces of many more.")
    call reply_message("Your contract was flawed from the start.")
    call message("Unknown", "…")
    call phone_end

    "Somewhere in the back of my mind, I swear I can hear a low, skin-crawling chuckle."
    call phone_start
    call message_start("Unknown", "You are an interesting human, Valeria Jimenez.")
    call message("Unknown", "Congratulations; you have tricked me. Not many can say the same.")
    call message("Unknown", "You are no longer bound to this faulty contract. Enjoy the rest of your life.")
    call phone_end

    "With my freedom finally confirmed, I begin walking away from the assembled students. Each step I take feels lighter than the last."
    "I’m still in danger of failing three classes, still in danger of losing my scholarship… but… "
    "From here, I can see Darren waving, beaming with pride and looking towards the future."
    "I still have my life. And I know I made the right choice."
    jump end3

#################### TEST AREA BELOW ########################
    jump endgame

    label test_space:

    #Testing stat box
    show screen stat_box(protag_stats)
    pause
    hide screen stat_box

    # These display lines of dialogue.

####################    End Cards    ########################

    label game_over:
        scene bg game over with fade
        pause
        jump endgame

    label end1:
        scene bg end1 with fade
        pause
        jump credits

    label end3:
        scene bg end3 with fade
        pause
        jump credits

    label extra_end:
        scene end5 with fade
        show valeria happy
        show darrent happy at left
        show entity neutral at right
        v "Welcome to the extra section!"
        d "So how was the game?"
        e "Placeholder text"

    label credits:
        show bg black with fade
        show bg credits1 with fade
        pause(3)
        show bg credits2 with fade
        pause(3)
        show bg credits3 with fade
        pause(3)
        show bg credits4 with fade
        pause(3)
        show bg credits5 with fade
        pause(3)
        show bg credits6 with fade
        pause(3)
        show bg credits7 with fade
        pause(5)

    label endgame:
    $stats.set_both(0)
    scene bg black with fade

    return
