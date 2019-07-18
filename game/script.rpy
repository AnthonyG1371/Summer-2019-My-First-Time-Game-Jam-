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
    "Time for last-minute announcements. I quietly twirl my pencil with my fingers and glance at the clock. 3:59 PM."
    "Today’s combination of humidity and heat has somehow made its way into the classroom. The faint rumbling of the useless air conditioning competes with my professor for my attention."
    "All that tuition money, and the university still can’t be bothered to get a better air conditioner."
    "At least I’m here on scholarship."
    "A calendar reminder lights up my phone screen: ADVISOR MEETING IN TEN MINUTES."
    "Professor"  "Don’t forget, the final exam is coming up. If you have any questions, come to the study session that’s in a few days, or schedule an appointment with me."
    "My pencil twirling slows to a stop. Study session, huh?"
    "Well, I’ve made it this far into the year juggling a part-time and my classes. I’m sure I’ll be fine without the study session. I just wish I didn’t have to hear about finals ever again."
    "Professor"  "That’s it for today!"
    "An eruption of shuffling commences. I sling my backpack over my shoulder and rush out of the classroom."

    # Campus scene
    scene bg campus with dissolve
    show valeria neutral at center
    show darren neutral at offscreenright
    "The classroom was stuffy enough, but the moment I leave the building, the heat hits me with full force. My first instinct is to fan myself with my notebook, but it barely offers any comfort."
    label campus:
    d "Valeria!"
    "Despite the weather, it’s hard not to smile when I see Darren waiting for me beneath the shade of the tree next to the building."
    show valeria neutral at left with move
    show darren neutral at right with move
    v "Hey Darren! What’s up?"
    d "The usual. All of my classes are wrapping up and everyone’s talking about finals. I’m guessing it’s the same for you."
    d "Hey, if you need help with some of the classes we have together, maybe we could study – "
    menu:
        "Firmly decline":
            v "No thanks. I’ll be fine. I just have to do some review beforehand."
            d "Oh, okay! That’s good then."
        "Offer an ambivalent answer":
            v "Maybe? I’ve already got so much on my plate, I don’t know if I’ll have the time… "
            d "That’s alright! Just let me know if you’re free, and we can study together then."
    # Return to main route
    "My phone buzzes in my pocket, momentarily taking my mind off the stress of school."
    "It’s another calendar notification for my advisor meeting. THREE MINUTES, my phone declares."
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
    "Advisor" "I’d like to remind you once again that we do offer tutoring services for the classes you’re taking. Tutoring is free and doesn’t interfere with your schedule. All you have to do is ask."
    v "I don’t believe I need the tutoring, sir."
    "Advisor" "As you’ve told me before."
    "Advisor" "Valeria, listen to me. You’re failing three of your required courses. Your finals are coming up as well, and I’m afraid that if this continues you won’t qualify for your scholarship anymore."
    "I sit there, staring stupidly at the imperfect grooves etched into the surface of his wooden desk. Waiting for the news to hit me."
    "And then –"
    v "You’re kidding."
    "Everything I’d achieved in high school: top of the class, making my parents proud. Everything I’d achieved, hanging by a thread over a cliff."
    v "I – I knew I wasn’t doing well, but I didn’t know it was this bad. And now you’re telling me I’m about to drop out."
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
            "Where was I? Oh yeah, worrying about my scholarship. I could call my parents and tell them everything, but that might make things worse."
            "Whatever. I’ll deal with this somehow."
            jump game_over
    # The game abruptly ends here and goes back to the start. The Entity would presumably move on as they never made a contract with her in this case.

    # Choice 2
        "Call the number":
            v "I might as well see what they’re about?"

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
    v "A solution to what? You just came out of my phone! You expect me to just calmly hear you out?"
    e "Then let me explain. You need help, don’t you?"
    v "I don’t need your help!"
    e "You’re on the verge of losing your scholarship. If you tell your parents, you’ll lose all their support, won’t you?"
    e "You can’t even vent to your best friend. It’s not like he would understand. His professors love him, and he’s able to afford this school. Unlike you."
    v "Leave Darren out of this. And I could afford it if I took out a loan!"
    e "Don’t kid yourself. You’re trapped, and I’m your only way out."
    e "You saw me come out of your phone — I’m clearly capable of so much more. Helping you would be so simple. But beggars can’t be choosers, and I don’t work for free. If you want my help, I’d like something in return."
    v "Which is?"
    e "Your best friend, Darren Romero. His future seems bright. Don’t you deserve the same thing?"
    e "You were the star pupil in high school; now you can barely reach the top. Doesn’t it hurt to see Darren succeed while you fail? Why not… extinguish some of that brightness?"
    v "Why?"
    e "There’s no need to know why, my dear Valeria. All you need to know is that I can help."
    v "What am I supposed to do?"
    e "I’ll contact you, and you’ll know. Do we have a deal?"
    v "What about if I can’t do what you ask?"
    e "Then I get your soul."
    v "My soul? What is that supposed to mean?"
    e "You’re a smart person; I’m sure you know exactly what that entails. I’ll own your soul, your life. But that’s only if you fail."
    e "If you hold up your end of the bargain, I will solve all of your problems and you’ll never see me again."

    # Two Choices
    menu:
        "Refuse":
            jump refuse_deal
        "Accept":
            jump accept_deal

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
    "I blink. The entity has vanished, replaced by empty air. I stand there for a few minutes, wondering what in the world I’d just talked to, and whether or not it was telling the truth."
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
    "The next morning, I join Darren at our usual seats near the middle of the class. With finals coming up, the room is packed today with students scrambling to cram as much psychology knowledge into their brains as possible."
    d "Morning!"
    v "Who gave you the right to be such a morning person?"
    d "You’re awfully chipper."
    "Professor" "Now, we’ve gone over the psychodynamic and biological theories on personality. If you’ve read the assigned pages, you’d know that today we will be discussing behaviorist theories."
    "Oh no."
    v "I forgot to read it since I was so worried last night… "
    d "What were you so worried about?"
    v "… "
    "Professor" "According to behavioral psychology, personality is determined by the environment, which reinforces your personality in an eternal cycle. Can someone tell me what the issue with this theory is?"
    d "Well, this theory considers environment as the only factor in determining someone’s personality. But what about cognition? Someone’s thinking is just as important as the environment surrounding them. Like the choices you make are exactly that— choices. They can have unpredictable outcomes."
    "Professor" "Great job, Mr. Romero."
    "Student" "Know-it-all."

    # Two choices
    # Note: I intend to include a similar scenario but with a major dip/raise in stats later on, and this bit is some foreshadowing and showing how some students view Darren.

    menu:
        "Don't say anything":
            # Choice 1, minor loss of Morality and Friendship
            $stats.add_both(-1)
            "I don’t say anything. Darren’s my best friend, but he is a bit of a know-it-all. He answers every question he can to get on the good side of his professors, and often studies late into the night."
            "Darren seems disappointed that no one refuted the claim."
        "Defend Darren":
            # Choice 2, minor gain of Morality and Friendship
            $stats.add_both(1)
            "I turn around to glare at the person. They roll their eyes."
            "Student" "What? It’s true."
            v "At least he studies. What’s your grade in this class?"
            "The student seems pretty embarrassed."
            "Student" "I– you don’t need to know that!"
            "Darren smiles."
    # End of choices

    "The lecture continues, and Darren is busy organizing his color-coded notes as usual. It’s hard to follow since I didn’t do the reading. I figure I don’t need to write notes anyways."
    "I remember the conversation with my advisor and sink further down into my seat. By the time the lecture is over and I gather my things, the professor beckons toward me."
    "Professor" "Miss Jimenez, can I speak to you for a moment?"
    d "I’ll wait outside then."
    show darren neutral at offscreenright with move
    hide darren neutral
    "I stand by the professor’s desk and patiently wait as he chats with a few students who have questions about a future quiz."
    "Wait a second."
    "A quiz?"
    "Professor" "At the beginning of the semester you were doing very well in this class. You had high quiz scores and were clearly very studious. I know your friend, Mr. Romero is a good influence–"
    "I can’t understand why my professors, advisors, and parents always feel the need to bring up Darren. Back in high school it was never an issue, but now it feels like a competition I didn’t choose to be in."
    "He drones on for a moment about how well I was doing in his class before he gets a phone call."
    "Professor" "Ah, excuse me for a moment. This is important."
    "I’m left completely alone, waiting by his desk. The word quiz bounces around in my thoughts, increasing in volume. I didn’t even realize there was one until those students asked about it. And I desperately need to do well on it."
    "On the professor’s desk there’s a sheet on top that says Answer Key. For a moment I think that it would be incredibly easy to snap a quick picture. No one would know, and I could get a good score."
# Take a picture of the key (loss of Morality)
# Ignore it (no effect)
    menu:
        "Take a picture of the key":
            # Choice: Take a picture of the key
            $stats.add_morals(-2)
            "I nervously look around, making sure nobody sees. I slip the phone out of my pocket and fumble trying to open the camera app, but manage to take a clear image of the key."
            v "Got it."
        "Ignore it":
            # Choice: Ignore it
            "I don’t need to cheat to get a good score. Somehow, though I don’t know how, I’ll manage. The paper is easily seen by any student who might come up to the professor’s desk, however."
            # Ignore it (no effect)
            # Turn the paper over (small Morality gain)
            menu:
                "Ignore it":
                    # Choice: Ignore it
                    "Well, whatever. If someone else wants to cheat, that’s not my problem."
                "Turn the paper over":
                    # Choice: Turn the paper over
                    $stats.add_morals(2)
                    "I don’t want to cheat. I’m better than that, but I don’t want any other student to get the chance either. It’s an unfair advantage. I flip the paper over so the blank side is up."
    #Return to main route

    "The professor comes back in, a little embarrassed about having to leave in the middle of an important talk. He clears his throat."
    "Professor" "Sorry about that. Now, my point, Valeria, was that you’re capable of so much. Why is it that you’re failing my class? I heard you’ll even lose your scholarship. There are many resources to help you, your friend could tutor you for example-"

    # Interrupt and lash out.(Morality loss)
    # Stay quiet and agree.(Morality gain)
    menu:
        "Interrupt and lash out":
            # Choice: Interrupt and lash out
            $stats.add_morals(-1)
            v "I don’t care!"
            "The professor is taken aback, and he stops his speech abruptly."
            "Professor" "Excuse me?"
            v "Stop talking about Darren. I get it, he’s better than I am and smarter and a hard worker–"
            "Professor" "That’s not what I meant–"
            v "But that’s what it sounds like to me! If only you saw me in high school. Do you want to know how I got my scholarship? I was the valedictorian. That’s right. Darren was below me. Now all anyone seems to talk about is how much I apparently suck."
            "Professor" "Valeria, please."
            # Insult the professor and leave. (big Morality loss)
            # Calm down and leave. (small Morality gain)
            menu:
                "Insult the professor and leave":
                    # Choice: Insult the professor and leave.
                    $stats.add_morals(-3)
                    "I hold up a hand before the professor can get another word."
                    v "Just do me a favor and stop meddling in my life. I get it. Since your wife left you this summer you’ve just been looking for someone else to bother."
                    "The professor’s face is completely red, and he stutters."
                    "Professor" "Excuse me?"
                    v "I’ll tell you this, Professor. It won’t be me."
                    "I storm out of the room and try to calm myself down to face Darren, but I’m sure I’m scowling and my eyebrows are furrowed in the way he says is scary."
                "Calm down and leave":
                    # Choice: Calm down and leave
                    $stats.add_morals(1)
                    "I take a deep breath and close my eyes. The professor patiently waits for me to finish."
                    v  "I’m sorry. I’m going to go now."
                    "Professor" "…  Alright. Take care, Valeria."
        "Stay quiet and agree":
            # Choice: Stay quiet and agree
            $stats.add_morals(2)
            "I concentrate on my breathing and focus on that before I start getting riled up about the professor bringing up Darren. The professor goes on about all the student services which I am acutely aware of thanks to the incessant reminders from my advisor."
            v "I assure you that I’m well aware that tutoring is available. I just don’t want to go."
            "Professor" "Why is that? Your grades are slipping, and I think you could benefit from it."
            "Why is it? I think back to my high school valedictorian days, to the time where I barely studied for exams but passed anyways because I was smart and had common sense. My friends looked up to me, and my parents praised me. I never needed tutoring then."
            v "Alright Professor, I’ll look into it."
            "It’s not worth it to argue. I’m just wasting my time."
            "Professor" "Great! I’ll see you in class, have a good day now."
            v "You too."
    # Return to main route

    label campus2:
    scene bg campus with fade
    show valeria neutral at left
    show darren neutral at right
    "Darren is waiting for me outside the classroom, texting rapidly on his phone. He grins when he sees me. Even though I’m more than a little miffed at the professor’s talk, I still give him a little wave when I see him."
    d "Ready for lunch? There’s a cool new spot near campus I wanted to check out."

# Join Darren (Friendship increase slightly)
# Politely decline (Friendship decreases slightly)
    menu:
        "Politely Decline":
            $stats.add_friendship(-1)
            $join_lunch = False
            "After what the professor just said to me, I think the last thing I want to do right now is hang out with Darren."
            v "Sorry Darren, I think I wanna take this lunch alone."
            "Darren visibly deflates a little, but he shrugs."
            d "That’s okay. I just wanted to tell you something. I was gonna tell you yesterday, but you had your advisor meeting."
            scene bg restaurant with fade
        "Join Darren":
            # Choice: Join Darren
            $stats.add_friendship(1)
            $join_lunch = True
            "My stomach growls at the thought of food. I can’t wait to break into my lunch"
            v "Let’s go to the spot, I’m starving."
            "Darren took me to a part of campus that I never seen before. As we went around the corner, there greeted us was a large oak tree on a hill. The sunlight pierced through the leaves as the shade was accompanied by a light breeze. It was the perfect tree to have a picnic under."
            "We made our way up the hill and sat under the tree. I went through my bag to grab the chicken wrap I made this morning. I took a big bite to satisfy my hunger."
            v "Mmmh… so good."
            "Darren chuckled and reached for his lunch out of his bag and began to eat."
            v "So…   how did you find this place? Most of your classes are on the other side of campus."
            d "That’s true, but I came over here to set up some campaign posters."
            v "Campaign posters?"
            "Why would he need to put up campaign posters?"
            d "Oh yeah, I totally forgot that I didn’t tell you."
            "Tell me what?"
            d "I’m running for student council president!"
            v "Student council president?"
            "All of a sudden the memory of my late night conversation pops into my mind. Before I can even react my phone vibrates in my pocket. Still in shock I excuse myself for a moment to check it."

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
            d "Thanks! Actually, I was wondering if you want to join the campaign effort. You can help me by asking people to vote for me and handing out promotional materials, stuff like that."
            menu:
                "Accept":
                    # Choice: Accept
                    v "Yeah! I’d love to help."
                    d "Awesome! I know I won’t fail with you on board now."
                    "He holds up his hand for what I know he’s hoping will be the best high five ever."
                    menu:
                        "High-five him":
                            # Choice: High-five him
                            $stats.add_friendship(1)
                            "Of course I have to. It’s basically my duty."
                            "There’s that initial sting of impact, and then the satisfaction of a high-five well-done."
                            d "Now it’s virtually impossible for us to lose."
                        "Leave him hanging":
                            "I roll my eyes."
                            d "Aw, c’mon."
                            v "Let’s save that for if you win, yeah?"
                            "Darren sighs and lets his hand drop back to his side."
                            d "Fair point, I guess."
                "Decline":
                    # Choice: Decline
                    v "I’m not sure that’s such a good idea, I’d rather not."
                    d "Please? I’d seriously appreciate it if my best friend could help me with my campaign."
                    "I laugh nervously."
                    v "Don’t pull the best friend card on me."
                    d "Please?"
                    v "Okay! Fine, I’ll help you."
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
    "I’m not sure if this is the worst idea I’ve ever had or the perfect opportunity, but there’s nothing I can do now. I already told Darren I’d help him."

    # IF VALERIA ACCEPTS LUNCH OFFER:
    if join_lunch:
        "The rest of lunch passes by quickly with idle chatter and irrelevant conversation. I joke and laugh, gossip and tease, but it feels like I’m just going through the motions."
    # Return to main route
    else:
    # IF VALERIA DOESN’T ACCEPTS LUNCH OFFER:
        "I spend the rest of lunch alone, flipping through the psychology chapter I didn’t read. The words swim through my brain and refuse to stay anchored. For a good twenty minutes, I read and re-read whole sections before I give up in frustration."
    # Return to main route

    "I can’t stop thinking about the deal I made last night. That thing wants me to hurt Darren’s campaign, no doubt. Only then will it help me."
    "The only question is, what am I supposed to do?"

    # Library scene
    label library:
    scene bg library with fade
    "After lunch, I head towards the library. It’s not a bad place to start working on the problem of my grades."
    "Even though I can hardly understand what I’m reading, I’m trying my best to concentrate. For a moment, I wish Darren had come so that we could study together."
    "Or rather, so that I could rely on him. Maybe it was better that he didn’t come. Maybe I need to prove that I can do this on my own."
    "Darren’s not a bad person. He’s really not, but sometimes I listen to him speak and get irrationally angry, especially when we’re in class."
    "Like earlier today, when he answered the professor. He didn’t have to, someone else was bound to know the answer, but he liked showing off too much to resist the chance."
    "A cackle rips through the relative quiet. I glare in the direction of the source, but the students are busy examining a poster on the opposite wall."
    "The desired effect of my glare is lost entirely."
    "Student 1" "He looks ridiculous in that poster. He’s trying too hard to look smart."
    "Student 2" "You can’t deny that he’s smart though."
    "Student 1" "Maybe. He’s still a try-hard though. Look at that tie, it’s just asking to be made fun of."
    "I peer past them to see what they’re discussing."
    "It’s one of Darren’s campaign posters, depicting him in a formal suit with Vote for Darren! across the top."

    # Call out to the students
    # Ignore them
    menu:
        "Call out to the students":
            show valeria neutral
            # Choice: Call out to the students
            v "Hey! Are you guys talking about Darren Romero?"
            "Student 1" "Uh, yeah? Who else?"
            "Student 2" "I can’t believe you just had to go and badmouth someone you don’t even know personally."
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
                    "Talking about Darren like this is almost liberating, actually. The frustrations I’ve had bubbling in the pit of my stomach since the start of this year finally surface and I find relief."
                    # Return to main route
                "Defend Darren":
                    # Choice: Defend Darren
                    $stats.add_friendship(1)
                    v "I don’t like the way you’re talking about my best friend."
                    "The student rolls their eyes."
                    "Student 1" "It’s true, though. Can you blame me?"
                    v "Maybe I can. What you call a try-hard I call a hard worker, someone who’s organized and passionate about what they’re doing. You can think whatever you like of Darren, but he’ll succeed because of the effort he puts into everything."
                    "Student 1" "Still, it’s just a stupid school election. It’s a waste of energy to be putting so much effort in that."
                    "Student 2" "Hey, just drop it okay? I’m looking to study, not get in a fight. I’m sorry about this one, they have a big mouth."
                    v "That’s okay."
                    # Return to main route
        "Ignore them":
            # Choice: Ignore them (All the texting is within the ignore them choice but not in the join/defend them choice.)
            "That student’s laughing at him, but I don’t want to engage with them. I have better things to worry about."
            "My phone lights up with yet another notification, and I unlock the screen to check the text."
            call phone_start
            call message_start("Darren", "Hey V!")
            call message_start("Darren", "If you’re still in the library do you want me to come by?")
            call message_start("Darren", "Just in case you wanted some company, or a study buddy.")
            call reply_message("Um...")
            # Label names here are placeholders
            call screen phone_reply("Accept","labelAccept","Decline","labelDecline")

            # Choice: Accept (Friendship gain)
            label labelAccept:
            call phone_after_menu
            call message_start("me", "Yeah, I could use your help.")
            call message("Darren", "Then I’m on my way!")
            jump aftermenu2

            # Choice: Decline (Friendship loss)
            label labelDecline:
            call phone_after_menu
            call message_start("me", "No thanks, I don’t need any help.")
            call message("Darren", "Oh. Okay.")
            jump aftermenu2

            label aftermenu2:
            call reply_message("You know... I heard something interesting.")
            call message ("Darren", "What was it?")
            call screen phone_reply ("Tell him about the students", "labelTell", "Don’t tell him about the students", "labelDont")

            # Choice: Tell him about the students (Friendship gain)
            label labelTell:
            $stats.add_friendship(1)
            call phone_after_menu
            call message_start("me", "Some students here were making fun of your campaign poster.")
            call message("Darren", "Wow. I knew that tie was too much.")
            call reply_message ("Huh? It doesn’t bother you?")
            call message ("Darren", "I can’t say it doesn’t, but I’m gonna run into critics if I’m gonna be campaigning.")
            call message ("Darren", "Thanks for telling me though. I really appreciate it.")
            call reply_message ("No problem.")
            call reply_message ("")
            jump aftermenu3

            # Choice: Don’t tell him about the students (Friendship loss)
            label labelDont:
            call phone_after_menu
            call message_start("me", "Nevermind, I don’t think you need to know.")
            call message("Darren", "Huh? What kind of statement is that?")
            call message ("Darren", "What don’t I need to know?")
            call reply_message ("Nothing, I already said nevermind. Christ.")
            call message("Darren", "Fine. When did you get so testy?")
            call reply_message ("")
            jump aftermenu3

            label aftermenu3:
            call message_start ("me", "I got to go. Trying to focus here haha.")
            call phone_end
            "Darren doesn’t reply after that."
            # Return to main route

    "I return to studying. After a while I get the urge to throw the books, or better yet myself, out the window. My eyes are tired and everything’s distracting— my phone, the contract I have with the entity, the students chattering loudly instead of studying."
    "The words in the books still don't make much sense to me, so I figure it’s better to leave. My next class is starting soon anyways."

# Valeria’s Bedroom (night)
    label night2:
    scene bg bedroom night
    "I sit in my bedroom in silence. My phone screen is lit up, but I don’t have to energy to even mindlessly scroll through social media. I don’t want to speak to anyone as I mull over the terms of the contract with the entity."
    "I’m deep in thought when a figure appears in front of me, seemingly from thin air. Startled, I jump up from my seat."
    show valeria shocked at left with dissolve
    show entity neutral at right with dissolve
    v "What the hell?"
    e "Hello, Valeria. I did tell you I would contact you again, didn’t I?"
    hide valeria shocked
    show valeria neutral at left
    "Of course I didn’t forget. I still remember the text I received the second Darren told me about his campaign. I knew what this was about. The entity continues without waiting for my reply."
    e "In case it can’t be any clearer, I want you to ruin Darren’s campaign for student council president."
    v "Why? I mean I know we have a contract, but what do you get out of it?"
    e "I am an agent of mischief, Valeria. I thrive off the humiliation and suffering of human beings. When I have a chance, I appear to those who may help me. It’s a mutually beneficial relationship, of course, since I offer something in return."
    v "I consider the entity before me. It’s reminiscent of a human, except for the unnatural coloring of its eyes, it’s skin, the translucent clothing that doesn’t reveal any kind of solid form. I look away. There are forces in this world I can’t understand, even if it’s right in front of me."
    v "I don’t know if I can do this."
    e "Because he’s your friend? Or is it simply your own abilities getting in the way?"
    v "What? I’m not doubting my \"abilities\" I just..."
    "My voice falters."
    e "You don’t need any supernatural abilities to hurt someone else. Humans do it all the time. They break each other’s hearts, they make each other cry, they drive each other mad, all with a few words. That’s all it takes."
    "The entity says this with an unsettling smile."
    e "You’re more than capable, Valeria. It’s simple. You already agreed to help him with the campaign. Just choose to do the opposite."
    "I know I’m capable of it... but the real issue is whether I should or shouldn’t go this far. On the one hand, Darren is my best friend. Even if he wasn’t, it’s horrible to ruin someone’s hard work and what they’re passionate about."
    "On the other, I’m signing my soul away if I don’t do this and I should probably value my life above all else..."
    "Even above our friendship. Maybe even above my morality."
    v "...Tomorrow. I’ll see what I can do."
    e "Have a good night, Valeria."
    hide entity neutral with dissolve
    "I don’t think I’ll get any sleep."

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
