# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define hacker = Character("Lilea")
define mc = Character("You")
define leader = Character("Bronx")
define spy = Character("Emson")
define weaptech = Character("Erix")
define sniper = Character("Elio")


# The game starts here.

label start:

    $ talkedToHacker = False
    $ talkedToSpy = False
    $ talkedToWeapTech = False
    $ talkedToSniper = False
    $ talkedToNewbie = False
    $ talkedToLeader = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    show leader neutral

    leader "youre part of an organization"
    leader "there was a failed mission not long ago that you werent a part of"
    mc "what happened on the mission"
    leader "explains how the mission went down"
    mc "what does this have to do with me?"
    leader "you gotta find the mole"
    mc "who could it be"
    leader "has to be someone on the mission, high clearance only"
    mc "who's high clearance"
    leader "character descriptions"
    jump initial_conversation_menu

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label initial_conversation_menu:
        menu:
            "who do you want to talk to?"
            "hacker" if talkedToHacker == False:
                $ talkedToHacker = True
                jump hacker_first_conversation
            "spy" if talkedToSpy == False:
                $ talkedToSpy = True
                jump spy_first_conversation
            "weapons tech" if talkedToWeapTech == False:
                $ talkedToWeapTech = True
                jump weaptech_first_conversation
            "sniper" if talkedToSniper == False:
                $ talkedToSniper = True
                jump sniper_first_conversation
            "newbie":
                jump trishaPlaceholder
            "leader":
                jump trishaPlaceholder

# HACKER INITIAL CONVERSATION START
label hacker_first_conversation:
    menu:
        "description of the hacker's room"
        "find hacker":
            "you hear noises from behind a shelf"
            "investigate"
            menu:
                "in between wall and shelf you find hacker trapped"
                "what are you doing?":
                    menu:
                        hacker "trying to find something i dropped, thought i could find it but its kinda dark back here"
                        "thats the problem here?":
                            "hacker looks confused"
                            jump hacker_do_you_want_help
                        "do you want help?":
                            jump hacker_do_you_want_help
                "how did you get back there?":
                    jump how_did_you_get_back_there
        "snoop around":
            "the walls are bare, mostly taken up by shelving for various nondescript boxes, peeking in you see stacks of papers and metal scraps\nthere's a desk against the far wall\ndesk is messy, with lots of folders, wires, and drawings spread across it\nthere are at least three working monitors, with several smashed ones in the corner\nwhen you get close to the desk, the walls talk"
            "Voice" "who's there?"
            "you whip around"
            menu:
                "its dark but you can see a figure behind a shelf"
                "who are you?":
                    "Voice" "you sound familiar, do i know you? i'm hacker"
                    "oh there she is"
                    jump its_me
                "its me":
                    jump its_me

label its_me:
    hacker "oh mc! its good youre there, i may or may not be stuck"
    "you notice now that the figure is contorted in between the shelf and a wall"
    menu:
        "its hacker!"
        "how did you get back there?":
            jump how_did_you_get_back_there
        "do you want help?":
            jump do_you_want_help

label how_did_you_get_back_there:
    jump placeholder

label do_you_want_help:
    mc "do you want help?"
    hacker "sure i could use some light go get my flashlight under my desk"
    "her desk is messy, with lots of folders, wires, and drawings spread across it\nthere are at least three working monitors, with several smashed ones in the corner\ntheflashlight is under the desk, along with a stray sock"
    "you give it back to her"
    hacker "nice could you shine the light over me"
    "you shine the light over her"
    hacker "thanks, found it"
    mc "what did you lose anyway"
    "she extracts herself from the shelf, knocking over several boxes\nin the process, even more wires and papers fall out of the boxes"
    hacker "my stress ball, i chucked it at the wall last night, you know...after the mission"
    mc "ah i see"
    hacker "yeah it was kind of a mess"
    mc "what were you doing on the mission hacker"
    menu:
        hacker "my job was to be the eyes basically\nme and the leader were in a van offsite, he ws working on a drone i designed last month, and i was inside the target's security system"
        "did you see anything important?":
            mc "did you see anything important?"
            hacker "like anything wrong? not really, though the plan did go sideways pretty quickly"
            mc "how?"
            hacker "well, everything was doing their jobs to the letter except newbie"
            hacker "i was monitoring the team, and i saw her chatting up the target's daughter as if she didn't have somewhere to be"
            hacker "she must have gotten spotted and was trying to get away, if only they were more careful"
            mc "was newbie alone?"
            hacker "no, they were apart of the inside team with weap tech and spy"
            mc "maybe i should go talk to them"
            jump maybe_i_should_go_talk_to_them
        "was everything going well?":
            hacker "yeah it was..."
            hacker "up until i lost my eyes that is"
            hacker "the target must have realized i was in the system and booted me out, i think that was when things were over for us"
            mc "how could they have known?"
            hacker "i have no clue, i was so thorough. maybe the inside team got caught"
            mc "who was the inside team?"
            menu:
                hacker "that would be newbie, spy, and weap tech\nafter i lost my eyes i had no way of watching them, but there were a lot of lcose calls before that happened"
                "what kind of close calls?":
                    hacker "i know newbie got spotted at one point, she was supposed to be sneaking with weap tech, but for some reason she was talking with the target's daughter! no clue what she was thinking\nweap tech was supposed to be back up for newbie, to make sure the drive got picked up perfectly, but you can tell they didn't exactly do that\nit wasnt long afterward before leader called the mission off"
                    jump im_sure_newbie_has_their_own_side_to_the_story
                "maybe i should go talk to them":
                    jump maybe_i_should_go_talk_to_them

label maybe_i_should_go_talk_to_them:
    hacker "oh, if youre going to yell at them, theres no point, it wont solve anything"
    jump im_sure_newbie_has_their_own_side_to_the_story

label im_sure_newbie_has_their_own_side_to_the_story:
    mc "i'm sure newbie has their own side to the story"
    hacker "right, well, now that i have my stress ball i can get back to stressing!\ni've got some schematics to look at, without that thumbdrive, we lost a lot of valuable information, gotta be double on top of everything"
    mc "well bye"
    jump initial_conversation_menu
# HACKER INITIAL CONVERSATION END

# SPY INITIAL CONVERSATION START
label spy_first_conversation:
    "description of spy room"
    "spy is there lying on fainting couch with his eyes closed, theres a journal on his desk"
    "he hears you approach and sits up"
    menu:
        spy "hey! whats up?"
        "nothing really, what're you doing?":
            "his eyes drift to his journal and he shrugs"
            menu:
                spy "just decompressing, i was writing for a bit but it was nothing big"
                "it looks pretty important, its on real paper":
                    "only things that people dont want shared are written on paper, its too easy to get your personal holo hacked if youre not careful"
                    "the org uses paper for mission plans, weapon/device designs, and other secret info"
                    menu:
                        spy "oh yeah, its just some personal stuff, that was my dad's journal so..."
                        "oh im sorry for prying":
                            spy "no worries, i admit it is pretty weird for someone to be using an actual journal nowadays, this is just really sentimental for me"
                            menu:
                                spy "is there something i can do for you?"
                                "what did you do on the mission spy?":
                                    jump spy_what_did_you_do_on_the_mission
                                "the mission didn't go well did it?":
                                    jump the_mission_didnt_go_well
                        "are those drawings?":
                            "you can see what looks like doodles and sketches on a page sticking out of the journal"
                            spy "oh yeah they're small"
                            mc "what of?"
                            menu:
                                spy "uh people mostly sometimes places we go to"
                                "who?":
                                    "he gets shy"
                                    menu:
                                        spy "the team"
                                        "how sweet, you love us":
                                            spy "of course i do, you're my family"
                                            menu:
                                                spy "speaking of, why'd you waltz into my room like an annoying little sibling"
                                                "what did you do on the mission spy?":
                                                    jump spy_what_did_you_do_on_the_mission
                                                "the mission didn't go well did it?":
                                                    jump the_mission_didnt_go_well
                                        "we better not look ugly":
                                            spy "not more ugly than you all are usually"
                                            menu:
                                                spy "say, as much as i love being interrogated, did you need something?"
                                                "what did you do on the mission spy?":
                                                    jump spy_what_did_you_do_on_the_mission
                                                "the mission didn't go well did it?":
                                                    jump the_mission_didnt_go_well
                                "what places?":
                                    menu:
                                        "mainly places we go to on missions, sometimes i draw maps to study so i don't get lost, also some of the places we see are so gorgeous itd be a crime not to"
                                        "did you draw a map of this mission?":
                                            menu:
                                                spy "i did, as tragic as it went"
                                                "what did you do on the mission spy?":
                                                    jump spy_what_did_you_do_on_the_mission
                                                "the mission didn't go well did it?":
                                                    jump the_mission_didnt_go_well
                                        "i bet they're really good, you have an eye for gorgeous things":
                                            "well of course, beauty knows beauty"
                                            menu:
                                                spy "oh, did you need something, you did come in here for smth right?"
                                                "what did you do on the mission spy?":
                                                    jump spy_what_did_you_do_on_the_mission
                                                "the mission didn't go well did it?":
                                                    jump the_mission_didnt_go_well
                "you got a crush? writing in your diary to them?":
                    spy "what! no! theres no one!"
                    mc "riiiiight"
                    "he blushes"
                    menu:
                        spy "i mean it, but never mind, what did you come to me for?"
                        "what did you do on the mission spy?":
                            jump spy_what_did_you_do_on_the_mission
                        "the mission didn't go well did it?":
                            jump the_mission_didnt_go_well
        "i wanted to ask how the mission went, i hear it was bad":
            spy "yeah it wasnt as smooth as it couldve been"
            mc "what did you do on the mission spy?"
            jump spy_what_did_you_do_on_the_mission

label spy_what_did_you_do_on_the_mission:
    spy "i was the distraction, its kinda my thing ya know"
    spy "i was supposed to keep the target's lapdog out of their office"
    jump lapdog

label lapdog:
    mc "lapdog?"
    spy "yeah, their resident tech guy, hard to call him a hacker when he doesnt hold a candle to ours heh"
    mc "did you get to them?"
    spy "yeah i did"
    menu:
        spy "we were chatting for a bit, when he suddenly got real agitated and ran away, i guess he figured out something was up, probably was wearing an earpiece"
        "did he say anything?":
            menu:
                spy "nothing that made sense, only: \"no, get out of there, you were supposed to stay out of there\""
                "thats weird":
                    spy "yup, but what do you expect from rats? good thing leader gave the order to abort the mission soon afterward"
                    jump you_really_hate_the_government
                "do you know what he was talking about?":
                    spy "no, not at all, government rats rarely make sense"
                    jump you_really_hate_the_government
        "what did you do afterwards?":
            spy "i was going to radio in to leader but then someone else came to talk to me"
            mc "who came to talk to you?"
            spy "ah, just some government jerk, low-level riff-raff is all, didn't say anything useful, leader gave the order for us to abort like ten minutes after that anyway"
            jump you_really_hate_the_government

label you_really_hate_the_government:
    mc "you really hate the government dont you?"
    "he gets stony"
    spy "they're not my favorite people no"
    spy "hey, i love talking, thats why im so good at my job, but i think i need some me time, the mission kind of tired me out"
    mc "oh see you then"
    jump initial_conversation_menu

label the_mission_didnt_go_well:
    spy "no, no it didn't"
    spy "i mean, it could've been a lot worse, but it could've been a lot worse"
    mc "how could it have been worse"
    spy "we didn't lose anyone this time"
    "you look at spy awkwardly"
    spy "sorry, that was grim, hard not to be in this line of work sometimes"
    spy "i had to deal with the target's lapdog and i get grouchy when i have to socialize with rats"
    jump lapdog
# SPY INITIAL CONVERSATION END

# WEAPON TECH INITIAL CONVERSATION START
label weaptech_first_conversation:
    "description of weapon room"
    menu:
        "there's a figure bent over a table in the middle of the room, it's the weap tech"
        "approach the table":
            "you notice they're working on an explosive, when you walk to the other side of the them, weap tech sees you"
            menu:
                weaptech "hey! what's up?"
                "just wanted to talk, you busy?":
                    weaptech "nope, what do you need?"
                    mc "what did you do on the mission weap tech?"
                    jump weaptech_what_did_you_do_on_the_mission
                "uh, is that a bomb?":
                    weaptech "yup! good thing you didnt scare me, one wrong move and this room is fire and rubble"
                    "you eye the bomb carefully"
                    mc "was that for a mission?"
                    weaptech "oh no, not anything in particular, it just never hurts to have an explosive around!"
                    mc "right well i just wanted to chat"
                    weaptech "oh nice! what about?"
                    mc "what did you do on the mission weaptech?"
                    jump weaptech_what_did_you_do_on_the_mission
        "hey what're you working on?":
            "they jolt suddenly, startled"
            weaptech "no no no!"
            "they throw what ever was in their hands across the room and drag you out the door to the hallway"
            mc "why are we out here?"
            "they press you to the ground and curl up on top of you, not answering"
            "after a minute, they get up and peek in the door"
            menu:
                weaptech "well i was working on an explosive, guess it wasnt a good one"
                "that was a bomb?":
                    weaptech "it was supposed to be, no idea why it didn't blow- not that im complaining\nwhat brings you to my shop?"
                    mc "just wanted to talk, you busy?"
                    weaptech "nope, what do you need?"
                    mc "what did you do on the mission weaptech?"
                    jump weaptech_what_did_you_do_on_the_mission
                "was going into the hallway really supposed to save us from an explosion?":
                    "they drag you into the room again and plop down in their seat"
                    weaptech "i mean, its better than nothing right? what brought you to my shop though?"
                    mc "just wanted to talk, you busy?"
                    weaptech "nope, what do you need?"
                    mc "what did you do on the mission weaptech?"
                    jump weaptech_what_did_you_do_on_the_mission

label weaptech_what_did_you_do_on_the_mission:
    weaptech "i was meant to be newbie's backup, they're talented, but still fresh,im probably the most skilled in combat after sniper and newbie\ntogether we were meant to find the target's hacker's office, where the thumbdrive was supposed to be"
    mc "was it not there?"
    weaptech "no, it wasnt, we broke in not long after spy started speaking with the target's hacker"
    mc "everything worked out though? besides the missing drive?"
    menu:
        weaptech "well, not quite, the daughter of the target actually spotted us, im not surprised we ran into someone, but im shocked it was her"
        "why?":
            weaptech "there werent any guards in the area, the most important corner of the building\nthe hacker's office, the target's office, and even an entire vault in that one hallway"
            mc "how did you get away?"
            weaptech "well, i made up some excuse and dragged newbie away, good timing too, leader told us to get out almost immediately after"
            weaptech "i could have sworn i heard someone yelling at someone else as we ran, sounded angry, but i didnt care, i just wanted to get out in one piece"
            jump they_stand_and_grab_a_pistol
        "what did you do?":
            menu: 
                weaptech "well by the time i noticed, newbie had struck up conversation with the daughter, i swear, that girl spends so much time with spy, she's taking after the goober"
                "so they were talking?":
                    weaptech "like they were old friends, wouldve expected the daughter to immediately pull the alarm, but no, she never did"
                    weaptech "leader told us to get out of there right when i pulled newbie away"
                    mc "thats odd that they clicked so well"
                    weaptech "youre telling me, it was just in time too, i heard voices yelling as we ran, sounded like someone was getting chewed out"
                    jump they_stand_and_grab_a_pistol
                "how did you get away?":
                    weaptech "well, i made up some excuse and dragged newbie away, good timing too, leader told us to get out almost immediately after"
                    weaptech "i could have sworn i heard someone yelling at someone else as we ran, sounded angry, but i didnt care, i just wanted to get out in one piece"
                    jump they_stand_and_grab_a_pistol

label they_stand_and_grab_a_pistol:
    "they stand and grab a pistol off the table, inspecting it carefully"
    menu:
        weaptech "you like em? this is my baby, ace!"
        "your baby?":
            weaptech "yup! built him myself!"
            jump this_bad_boy_packs
        "why is it called ace?":
            weaptech "ace is a he, not an it, be nice and i dont know, just felt right"
            weaptech "i love my baby more than anything! oh but dont tell sniper yeah? itll be our little secret"
            mc "i guess?"
            jump this_bad_boy_packs

label this_bad_boy_packs:
    weaptech "this bad boy packs more punch than a whole cannon, i was gonna test him after i finished the bomb, but oh well, wanna come watch?"
    mc "you know, i'm good"
    weaptech "well, your loss, if you want you can hang around here more, but im gonna go now, see you!"
    mc "see you"
    jump initial_conversation_menu
# WEAPON TECH INITIAL CONVERSATION END

# SNIPER INITIAL CONVERSATION START
label sniper_first_conversation:
    menu:
        "description of the snipers room"
        "what're you doing?":
            menu:
                sniper "i'm cleaning my rifle"
                "how often do you do that?":
                    menu:
                        sniper "before and after every mission, and at least once a day"
                        "wow, that's a lot":
                            sniper "its what is necessary for the safety of myself and the people around me...or at least the people who arent on the other side of the muzzle"
                            "there's a pause..."
                            sniper "why did you come to me"
                            jump sniper_what_did_you_do_on_the_mission
                        "explains why you're so good at it":
                            sniper "i have lots of experience yes"
                            "theres a pause..."
                            sniper "why did you come to me"
                            jump sniper_what_did_you_do_on_the_mission
                "you look scary like that":
                    sniper "i've been told that before"
                    sniper "why did you come to me"
                    jump sniper_what_did_you_do_on_the_mission
        "hi sniper":
            "he turns around"
            menu:
                sniper "hello"
                "that's a big rifle":
                    sniper "it does its job"
                    "there's a pause..."
                    sniper "why did you come to me"
                    jump sniper_what_did_you_do_on_the_mission
                "is this a bad time?":
                    sniper "no, i can spare time, why did you come here"
                    jump sniper_what_did_you_do_on_the_mission

label sniper_what_did_you_do_on_the_mission:
    mc "i wanted to ask about the last mission"
    sniper "he looks at mc"
    mc "what did you do on the last mission?"
    sniper "my job was to provide cover and visual for the group"
    menu:
        sniper "i was stationed in the hills adjacent to the target's building with a clear view of the front and back entrances"
        "what did you see there?":
            menu:
                sniper "i saw people entering the front entrance in the beginning of the evening and not much movement from the back entrance"
                "who was entering the front?":
                    sniper "regular visitors, low-level government officials, and the like"
                    mc "did you see anyone else in the front of the property?"
                    menu:
                        sniper "in fact yes, part of the way through the night, i saw a single guard stand outside by the outskirts of the property"
                        "what was the guard doing?":
                            sniper "i saw him loiter around for a while, about five minutes before staring into the woods surrounding the property\nthen he suddenly turned around and stalked back to the building"
                            jump thats_really_weird
                        "was he not supposed to be there?":
                            sniper "usually the guards are in teams of two, i get the feeling he wasnt meant to be there"
                            sniper "he stood by the woods for a short amount of time before suddenly stalking back to the building"
                            jump thats_really_weird
                "what was happening at the back entrance?":
                    sniper "it seemed that was the main entrance for catering and security\ni saw food being carried in and guards changing shifts through that door"
                    jump was_there_anything_you_that_was_different
        "did everything look good?":
            menu:
                sniper "yes, there was no suspicious activity besides what was to be expected of the situation"
                "what was expected of the sitation?":
                    sniper "the guest list was to be made up of people wrapped up in government secrets, everyone there was complacent in their crimes"
                    mc "so nothing stuck out to you?"
                    sniper "i suppose somethind did now that you remind me"
                    menu:
                        sniper "part of the way through the night, i saw a single guard stand outside by the outskirts of the property"
                        "what was the guard doing?":
                            sniper "i saw him loiter around for a while, about five minutes before staring into the woods surrounding the property\nthen he suddenly turned around and stalked back to the building"
                            jump thats_really_weird
                        "was he not supposed to be there?":
                            sniper "usually the guards are in teams of two, i get the feeling he wasnt meant to be there"
                            sniper "he stood by the woods for a short amount of time before suddenly stalking back to the building"
                            jump thats_really_weird
                "was there anything you that was different?":
                    jump was_there_anything_you_that_was_different

label was_there_anything_you_that_was_different:
    mc "was there anything you that was different?"
    menu:
        sniper "different? i suppose there was something that was unexpected, but not overtly suspicious\npart of the way through the night, i saw a single guard stand outside by the outskirts of the property"
        "what was the guard doing?":
            sniper "i saw him loiter around for a while, about five minutes before staring into the woods surrounding the property\nthen he suddenly turned around and stalked back to the building"
            jump thats_really_weird
        "was he not supposed to be there?":
            sniper "usually the guards are in teams of two, i get the feeling he wasnt meant to be there"
            sniper "he stood by the woods for a short amount of time before suddenly stalking back to the building"
            jump thats_really_weird

label thats_really_weird:
    mc "that's really weird"
    sniper "i dont use that word, but yes, i suppose it was weird"
    "he looks down at the weapon on the floor in front of him"
    sniper "i would like to continue cleaning my rifle"
    mc "oh yeah bye"
    jump initial_conversation_menu
# SNIPER INITIAL CONVERSATION END


label placeholder:
    "has not been written"

label trishaPlaceholder:
    "code it trish!"