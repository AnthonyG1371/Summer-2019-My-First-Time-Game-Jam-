# The script of the game goes in this file.
# The Death Contract Script

# v0.001 alpha     Project skeleton. Created protag_stats class to keep track of variables.
# v0.002 alpha     Added the draft script for Night One. Added placeholder images.
# v0.010 alpha     Main menu and game resizing completed.
# v0.020           Added working script up to the end of day 2.

define v = Character("Valeria")
define e = Character("Unknown", color = "#800000") #maroon
define d = Character("Darren")
define a = Character("Advisor")

$join_lunch = True

# define screen effects
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define long_flash = Fade(0.5, 0.0, 2.0, color="#fff")
define shake = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=1)

# The game starts here.
label start:
    jump pass_out_cards
    # define and instantiates protagonists' stats
    python:
        stats = main_stats(0,0,0)

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

        "Debug Test":
            jump test_space

        "Debug":
            jump debug

# SCRIPT V2
    label begin:
    # Classroom scene
    scene bg classroom
    "Professor"  "And that’s the end of our unit… "
    "Time for last-minute announcements. I quietly twirl my pencil with my fingers and peek over at the clock. 3:59 PM."
    "Today’s combination of humidity and heat has somehow made its way into the classroom. The faint rumbling of the useless air conditioning competes with my professor for my attention."
    "All that tuition money, and the university {i}still{/i} can’t be bothered to get a better air conditioner."
    "At least I’m here on scholarship."
    "A calendar reminder lights up my phone screen: {i}ADVISOR MEETING IN TEN MINUTES{/i}."
    "Professor"  "Don’t forget, the final exam is coming up. If you have any questions, come to the study session that’s in a few days, or schedule an appointment with me."
    "My pencil twirling slows to a stop. Study session, huh?"
    "Well, I’ve made it this far into the year juggling a part-time and my classes. I’m sure I’ll be fine without the study session. I just wish I didn’t have to hear about finals ever again."
    "Professor"  "That’s it for today!"
    "An eruption of shuffling commences. I sling my backpack over my shoulder and rush out of the classroom."

    # Campus scene
    scene bg campus with dissolve
    show valeria neutral at center
    show darren neutral at offscreenright
    "The moment I leave the building, the heat hits me with full force. My first instinct is to fan myself with my notebook, but it barely offers any comfort."
    label campus:
    d "Valeria!"
    "Despite the weather, it’s hard not to smile when I see Darren waiting for me beneath the shade of the tree next to the building."
    show valeria neutral at left with move
    show darren neutral at right with move
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
    scene bg office with dissolve
    "Advisor"  "Valeria. I hope your day went well."
    "He nods at me in acknowledgement as I sink into the seat facing his desk. I search for a halfhearted grin to put on my face, but nothing sticks."
    "Between my advisor’s pestering and the ever-present reminders of my stress, I hate coming in here."
    "Advisor" "I’d like to remind you once again that we {i}do{/i} offer tutoring services for the classes you’re taking. Tutoring is free and doesn’t interfere with your schedule. All you have to do is ask."
    v "I don’t believe I need the tutoring, sir. I can manage on my own."
    "Advisor" "As you’ve told me before."
    "Advisor" "Valeria, listen to me. You’re failing three of your required courses. Your finals are coming up as well, and I’m afraid that if this continues you won’t qualify for your scholarship anymore."
    "I sit there, staring stupidly at the imperfect grooves etched into the surface of his wooden desk. Waiting for the news to hit me."
    "And then –"
    v "You’re kidding."
    "Everything I’d achieved in high school: top of the class, making my parents proud. Everything I’d achieved, hanging by a thread over a cliff."
    v "I – I knew I wasn’t doing well, but I didn’t know it was {i}this{/i} bad. And now you’re telling me I’m about to drop out."
    "Advisor" "Yes, well… you have resources at your disposal. I can only hope that you’ll realize it’s best to accept all the help you’re offered."
    "Advisor" "Please, choose wisely."

    #Valeria is at her desk in her apartment.
    label night1:
    scene bg desk with fade
    "The sun dips below the skyline as I drum my fingers against my desk, contemplating the psychology textbook next to my laptop."
    "It’s been a few hours since I met with my advisor, and I still can’t believe it. I breezed through high school easily enough; how did I fail so miserably in college?"
    "I don’t even want to think about what my parents will say."
    "My phone lights up with a new text message. Relieved by the interruption, I pick it up."

    # The phone pops up with a message, so the following dialogue is through text (format pasted from the premade messaging system found in the design document. The rest of that system will have to be pasted into The Death Contract game.)
    call phone_start
    call message_start("Darren", "V, don’t forget the psychology reading tonight.")
    call message_start("Darren", "Just a reminder because you forgot last time!")
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
    label debug:
    scene bg desk
    # The Entity appears in person. Valeria has a shocked expression. We could also consider adding in animations, like a screen shake to indicate shock.
    with flash
    show entity neutral at center
    e "Hello, Valeria." with vpunch
    v "What the — "
    e "Don’t be scared. I was the one texting you."
    v "How the hell did you get in here?"
    e "I’m here to offer you a solution, Valeria."
    v "A solution to what? You just came out of my {i}phone{/i}! You expect me to just calmly hear you out?"
    e "Then let me explain. You need help, don’t you?"
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
    scene bg classroom with fade
    show valeria neutral at left
    show darren neutral at right
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
            $stats.add_both(-1)
            "Darren may be my best friend, but I’m not about to argue against the truth."
            "Out of the corner of my eye, I notice Darren glancing at me. He stays silent."
        "Defend Darren":
            # Choice 2, minor gain of Morality and Friendship
            $stats.add_both(1)
            "I turn around to glare at the person. They roll their eyes."
            "Student" "What? It’s true."
            v "At least he studies. What’s your grade in this class?"
            "Student" "I – you don’t need to know that!"
            "Darren stays silent, but a small smile appears on his face."
    # End of choices

    "The lecture continues. As usual, Darren studiously writes in and organizes his color-coded notes."
    "I didn’t do the reading, so the lecture doesn’t make a whole lot of sense to me. I frown at my binder full of nonexistent notes, remembering the conversation I had yesterday with my advisor."
    "Before long, class ends and I’m gathering my things, wondering what I should do before my next class."
    "Professor" "Miss Jimenez, can I speak to you for a moment?"
    d "I’ll wait outside."
    show darren neutral at offscreenright with move
    hide darren neutral
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
            "I nervously scan my surroundings just to reconfirm that I’m alone. I slip my phone out of my pocket."
            "For a moment, I think I hear the professor’s footsteps. I fumble with my camera app, swearing under my breath."
            v "Got it."
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
    scene bg campus with fade
    show valeria neutral at left
    show darren neutral at right
    "I find Darren waiting outside, eyes glued to his phone and fingers rapidly texting away. The moment he hears the door open, he looks up and grins at me."
    "Even though I’m more than a little miffed at the professor’s talk, I give Darren a little wave."
    d "Ready for lunch? There’s a cool new spot near campus I wanted to check out."

# Politely decline (Friendship decreases slightly)
# Join Darren (Friendship increase slightly)
    menu:
        "Politely Decline":
            $stats.add_friendship(-1)
            $join_lunch = False
            "After what the professor just said to me, I think the last thing I want to do right now is hang out with Darren."
            v "Sorry Darren, I think I wanna take this lunch alone."
            "Darren frowns a little, but he shrugs."
            d "That’s okay. I just wanted to tell you something. I was gonna tell you yesterday, but you had your advisor meeting."
            # !!! not sure if this label works
            jump aftermenu2
        "Join Darren":
            # Choice: Join Darren
            $stats.add_friendship(1)
            $join_lunch = True
            "My stomach growls at the thought of food."
            v "Let’s go, I’m starving."
            "Darren leads me to a part of campus that I’ve never seen before. The picturesque sight of a large oak tree sitting on a hill greets us. Sunlight pierces through the foliage at just the right angle."
            d "Nice, right?"
            v "Are you kidding? It’s perfect."
            "We flop down onto a shady part of the grass. I dig through my bag in search for the chicken wrap I made this morning. It’s hard to resist the urge to scarf the entire thing down, but I take a big bite anyway."
            v "Mmmh… so good."
            "Darren chuckles as he reaches for his own lunch."
            v "So… how did you find this place? Most of your classes are on the other side of campus."
            d "That’s true, but I came over here to set up some posters."
            v "Posters?"
            "Why would he need to put up posters?"
            d "Oh yeah, I totally forgot that I didn’t tell you."
            "Tell me what?"
            "In the middle of my confusion, I recall what Darren hinted at yesterday before I went to meet with my advisor. He was about to tell me something then, but —"
    # Return to main route
    # !!! (same as above) not sure if this label works
    label aftermenu2:
        d "I’m running for student council president!"
        "Woah."
        "I guess I shouldn’t be surprised. Ever since he set foot on this campus, he’s been pretty involved with the student government."
        "Still, the news manages to catch me off-guard."
        "Before I can open my mouth to reply, my phone vibrates in my pocket. I excuse myself for a moment to check."

        hide valeria neutral
        hide darren neutral
        with dissolve

        call phone_start
        call message_start("Unknown", "Remember what we talked about, Valeria?")
        call message_start ("Unknown", "Now’s your chance.")
        call phone_end

        show valeria neutral at left
        show darren neutral at right
        with dissolve

        "… Right."
        "Darren is still grinning, completely oblivious, waiting for my response."
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
                        $stats.add_friendship(1)
                        "Of course I have to. It’s basically my duty."
                        "There’s that initial sting of impact, and then the satisfaction of a high-five well-done."
                        d "Now it’s virtually impossible for us to lose."
                    "Leave him hanging":
                        "I roll my eyes."
                        d "Aw, c’mon."
                        v "Let’s save that for {i}if{/i} you win, yeah?"
                        "Darren sighs and lets his hand drop back to his side."
                        d "Fair point, I guess."
            "Decline":
                # Choice: Decline
                "The thing that talked to me last night… it’s planning something, and I’m not sure if I like where it’s going."
                v "I’d rather not."
                d "Please? I’d seriously appreciate it if my best friend could help me with my campaign."
                v "Don’t pull the best friend card on me."
                "My phone vibrates in my pocket again."
                call phone_start
                call message_start("Unknown", "I do hope you haven’t forgotten.")
                call message_start("Unknown", "You have no choice.")
                call phone_end
                "…"
                d "Please?"
                "Like it said: I have no choice."
                "My fingers curl around my phone, gripping it so hard that my knuckles turn white. I hope Darren doesn’t notice."
                v "Okay, okay. Fine, I’ll help you."

    # Return to main route
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

label pass_out_cards:
    # omelette scripting starts here.
    ""
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
        pause 0.5
        linear 0.5 xzoom 1.0
        linear 1.5 xalign 1.0
        pause 0.5
        linear 0.5 xzoom -1.0
        linear 1.5 xalign 0.0
        repeat
    "I’m rapidly getting tired of the general apathy and uncomfortable summer heat I’m experiencing. I’m not even getting paid. I could be studying instead."
    # show valeria sad at right, floor with move
    show valeria sad at left with Move(1.5)
    "There’s still a decent stack of promotional cards left, but I don’t want to deal with them anymore."
    # !!! refer to red text in document, there is a choice for throwing the cards away or keeping them; put it here

    #Throw the rest away (Big Morality and Friendship loss)
    #Keep the rest to return to Darren (Big Morality and Friendship gain)
    menu:
        "Throw the rest away":
            $stats.add_both(-3)
            hide valeria neutral with dissolve
            show valeria angry with dissolve
            "I chuck the remainder of the promotional cards into a trash bin, lollipops and all, and dust my hands off."
            # Return to main route
        "Keep the rest to return to Darren":
            $statss.add_both(3)
            # Choice: Keep the rest to return to Darren
            "As annoyed as I am right now, I know Darren spent a lot of time and money on these cards. I’ll just stop promoting for now and hand them back to him later."
            # Return to main route

    "Maybe if I manage to find him at all today, he’ll tell me face-to-face why he flaked on me."


    # Library scene
    label library:
    scene bg library with fade
    "With that out of the way, I head towards the library. It’s not a bad place to start working on the problem of my grades."
    "Even though I can hardly understand what I’m reading, I’m trying my best to concentrate. For a moment, I wish Darren had come so that we could study together."
    "Or rather, so that I could rely on him. Maybe it was better that he didn’t come. Maybe I need to prove that I can do this on my own."
    "A cackle rips through the relative quiet. I glare in the direction of the source, but the students are busy examining a poster on the opposite wall."
    "The desired effect of my glare is lost entirely."
    "Student 1" "He looks ridiculous in that poster. He’s trying too hard to look smart."
    "Student 2" "You can’t deny that he’s smart though."
    "Student 1" "Maybe. He’s still a try-hard though. Look at that tie, it’s just asking to be made fun of."
    "I peer past them to see what they’re discussing."
    "It’s one of Darren’s campaign posters, depicting him in a formal suit with {i}Vote for Darren!{/i} across the top."
    "I’m reminded of the promotional cards I’d just handed out. Without Darren’s help."

    # Call out to the students
    # Ignore them
    menu:
        "Call out to the students":
            show valeria neutral
            # Choice: Call out to the students
            v "Hey! Are you guys talking about Darren Romero?"
            "Student 1" "Uh, yeah? Who else?"
            "Student 2" "I can’t believe you just {i}had{/i} to go and badmouth someone you don’t even know personally."
            # Join in (Friendship loss)
            # Defend Darren (Friendship gain)
            menu:
                "Join in":
                    # Choice: Join in
                    $stats.add_friendship(-1)
                    "Honestly? I can’t blame them."
                    v "He’s my friend and all, but you’re right about the tie."
                    "Student 1" "It’s like, you know this isn’t a real election right? It’s just some stupid school thing."
                    v "That’s Darren though. He’s always going overboard."
                    "The other student frowns at me."
                    "Student 2" "Shouldn’t you be defending him if he’s your friend?"
                    v "Maybe. But I won’t lie, he’s a try-hard. It’s even worse during class. You should see the way he sucks up to professors."
                    "They shrug, not saying much else as the first student and I make a few more jokes about Darren."
                    "Talking about Darren like this is almost liberating, actually. The frustrations I’ve had bubbling in the pit of my stomach finally surface and I find relief."
                    "Eventually, we both get tired of joking around, so I return to my studying."
                "Defend Darren":
                    # Choice: Defend Darren
                    $stats.add_friendship(1)
                    v "I don’t like the way you’re talking about my best friend."
                    "Even though I’m still annoyed with Darren, there has to be a good reason for why he didn’t show up. I have to trust in him."
                    "The student rolls their eyes."
                    "Student 1" "What I’m saying is true, though. Can you blame me?"
                    v "Maybe I can. What you call a try-hard I call a hard worker, someone who’s organized and passionate about what they’re doing."
                    v "You can think whatever you like of Darren, but he’ll succeed because of the effort he puts into everything."
                    "Student 1" "Still, it’s just a stupid school election. It’s a waste of energy to be putting so much effort in that."
                    "Student 2" "Hey, just drop it okay? I’m looking to study, not get in a fight. I’m sorry about this one, they have a big mouth."
                    v "That’s okay."
                    "I’m not really looking to get into a fight either."
        "Ignore them": # !!! double check to see if this choice works as intended
            "That student’s laughing at him, but I don’t want to engage with them. I have better things to worry about."

    # Return to main route
    "I open up my psychology textbook."
    "…"
    "…"
    "I’m suddenly overwhelmed with the urge to throw the book, or better yet myself, out the window."
    "I rub my eyes. Everything’s distracting me — my phone, the students whispering loudly in the corner. Darren’s absence, weighing down on mind."
    "The contract I have with my soul on the line…"
    "What am I going to do?"

# Valeria’s Bedroom (night)
    label night2:
    scene bg bedroom night
    "I sit in my bedroom in silence that night, watching the long shadows sprawled across my wall."
    "I can’t be bothered to answer the mountain of texts that have accrued throughout the day. I don’t even have to energy to mindlessly scroll through social media."
    "My phone lights up with yet another text."

    # !!!
    # Label names here are placeholders
    call phone_start

    call message_start("Darren", "Hey V!")
    call message_start("Darren", "How did campaigning go?")
    call reply_message("…")

    call screen phone_reply("Tell him the truth","labelTruth","Lie","labelLie")

    # Choice: Tell him the truth (Friendship Gain)
    label labelTruth:
    call phone_after_menu
    call message_start("me", "Not very well.")
    call message("Darren", "What do you mean?")
    call reply_message("Everyone I talked to didn’t seem to care, so I gave up.")
    call message("Darren", "Oh. Oh well.")

    jump after_truth_lie

    # Choice: Lie (Friendship Loss)
    label labelLie:
    call phone_after_menu
    call message_start("me", "It went well.")
    call message("Darren", "Really?")
    call reply_message("Yeah, I talked about what you were planning to do.")
    call reply_message("People seemed excited.")
    call message("Darren", "Right.")

    jump after_truth_lie

    label after_truth_lie:

    call message("Darren", "V… when I asked you how campaigning went, you just… sent ellipses.")
    call message("Darren", "You know how it is when I get anxious over messages.")
    call message("Darren", "It feels like you’re irritated. Is everything okay?")

    call screen phone_reply("Point out his absence","labelAbsence","Brush it off","labelBrush")

    # Choice: Point out his absence
    label labelAbsence:
    call phone_after_menu
    call message_start("me", "Where were you this afternoon? It’s your campaign, and you weren’t even there.")
    call message("Darren", "I know, I’m sorry.")
    call message("Darren", "It was kind of on a short notice.")
    call reply_message("What was? Seriously, people were asking me about you.")
    call reply_message("What could you possibly have been busy with?")
    call message("Darren", "I can’t really tell you.")
    call reply_message("Oh, you just wanted to get out of the sun, huh? It was hot as hell, so you made the right choice..")
    call message("Darren", "No, that’s not it.")
    call reply_message("What was it, then?")
    call message("Darren", "I said, I can’t tell you.")
    call reply_message("Alright, I see how it is.")

    call phone_end
    "I purse my lips in irritation. What’s he not telling me?"
    jump entity2
    # Return to main route

    # Choice: Brush it off
    label labelBrush:
    call phone_after_menu
    call message_start("me", "Nothing.")
    call message("Darren", "Are you sure?")
    call reply_message("Yeah. Just let me get back to work. I’m fine.")
    call message("Darren", "Okay…")

    call phone_end
    "Whether it’s out of a sense of futility or weariness, Darren doesn’t text back."
    "Still, I can’t help but wonder why he never mentioned his absence today."
    # Return to main route

    label entity2:
    "I’m deep in thought when a figure appears before me, seemingly out of thin air. I jump up from my seat."
    show valeria shocked at left with dissolve
    show entity neutral at right with dissolve
    v "What the hell?"
    e "Hello, Valeria. I {i}did{/i} tell you I would contact you again, didn’t I?"
    v "Yeah, well, humans don’t usually just {i}appear{/i} out of thin air when they wanna talk to each other, so don’t blame me for getting a heart attack every time you do… {i}that{/i}."
    hide valeria shocked
    show valeria neutral at left
    "I gesture to the previously empty space the entity now occupies."

    # !!!
    v "So… you want me to sabotage Darren’s campaign."
    e "Yes, I hope I made that abundantly clear."
    v "Oh trust me, it was {i}very{/i} clear. I just… I just don’t know if I can do this."
    "An unsettling smile crawls across the entity’s face."
    e "My dear, you don’t need any supernatural abilities to hurt someone else. Humans do it all the time. They break each other’s hearts, they make each other cry, they drive each other mad, all with a few words. That’s all it takes."
    v "What? I’m not doubting my {i}abilities{/i}, I just…"
    "My voice falters."
    e "Ah, I see. Is it because he’s your friend?"
    "… Is he? I think back to earlier this afternoon, when he made a promise and didn’t keep it. And now he’s refusing to tell me why."
    e "Remember the conditions you agreed to. I will own your life and your soul should you fail."
    e "You’re more than capable, Valeria. You already agreed to help him with the campaign. Just choose to do the opposite."
    v "…"
    v "Tomorrow. I’ll see what I can do."
    "The entity’s smile has not faded."
    e "Have a good night, Valeria."
    hide entity neutral with dissolve
    "I end up not sleeping at all."
    "That gives me plenty of time to consider my situation."

    scene bg black with fade
    pause(2)

# Day Three

#################### TEST AREA BELOW ########################
    jump endgame

    label test_space:

    #Testing stat box
    show screen stat_box(protag_stats)
    pause
    hide screen stat_box

    # These display lines of dialogue.

    "TEST VERSION. PLEASE IGNORE ANY LOGIC IN THIS."

    label game_over:
        scene game_over with fade
        ""

    label endgame:
    # This ends the game.

    return
