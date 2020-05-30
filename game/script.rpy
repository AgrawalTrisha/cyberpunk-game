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
define newbie = Character("Kona")


# The game starts here.

label start:

    $ talkedToHacker = False
    $ talkedToSpy = False
    $ talkedToWeapTech = False
    $ talkedToSniper = False
    $ talkedToNewbie = False
    $ talkedToLeader = False

# EXPOSITION START
    "The year is 3158. Androids join humans on the streets and in the workforce. Disease has been near eradicated and world hunger is barely an issue anymore."
    "The enemy of the people is instead one of the oldest known to man: the government."
    "In order to restore power to the people, a resistance has formed to fight the standing administration. You are part of that organization."
    "Known simply as \"the Rebellion\", your organization is underground, made up of a network of factions across the country."
    "Your faction is the first and founding one, aptly named the \"First Squadron\"."
    "You were working abroad trying to find allies across the sea. Now that you've returned, you realize things have gone downhill."
    "You're in Bronx's office, the leader of Squadron 1, listening to him recount the team's last mission."
# EXPOSITION END

# BRONX EXPOSITION START
    scene bg room

    show leader neutral

    "Bronx shifts around in his seat."
    leader "This mission was called Operation Backwater. Our target was Flint Maddox, current Secretary of Defense."
    leader "The objective was to gather information on a thumbrive that was supposed to be in his home."
    leader "The opportunity to steal the drive arose when we got word he'd be hosting a gala. That drive was supposed to have vital information that could change everything for the Rebellion."
    leader "It was supposed to be in Oran Jege's office. Jege is Maddox's resident 'computer specialist', but that's just codeword for hacker."
    leader "When we infiltrated Maddox's gala, it wasn't there and we left empty-handed."
    jump initial_conversation_menu
# BRONX EXPOSITION END
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
        "newbie" if talkedToNewbie == False:
            $ talkedToNewbie = True
            jump newbie_first_conversation
        "leader" if talkedToLeader == False:
            $ talkedToLeader = True
            jump leader_first_conversation
        "mission briefing" if talkedToHacker and talkedToLeader and talkedToNewbie and talkedToSniper and talkedToSpy and talkedToWeapTech:
            jump mission_briefing

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
            jump hacker_do_you_want_help

label how_did_you_get_back_there:
    jump placeholder

label hacker_do_you_want_help:
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

# NEWBIE INITIAL CONVERSATION START
label newbie_first_conversation:
    "description of the room"
    menu:
        newbie "hey whats up mc?"
        "just wanted to see what you're up to":
            menu:
                newbie "oh, just thinking about the last mission, it didn't go how i expected"
                "it didnt go how anyone expected":
                    "they laugh but it sounds bitter"
                    newbie "it really didnt. can i tell you something"
                    mc "always"
                    newbie "the mission failing kind of feels like my fault, like what happened during it was because of me and now we lost the thumbdrive"
                    jump newbie_what_happened_on_the_mission
                "want to talk about it?":
                    newbie "yeah actually, i feel kinda bad about it, i think its my fault it failed so bad"
                    jump newbie_what_happened_on_the_mission
        "how you been?":
            menu:
                newbie "ive been better, the mission was kind of a mess and its been making me a mess too"
                "want to talk about it?":
                    newbie "yeah actually, i feel kinda bad about it, i think its my fault it failed so bad"
                    jump newbie_what_happened_on_the_mission
                "it didn't go how anyone expected":
                    "they laugh but it sounds bitter"
                    newbie "it really didnt. can i tell you something"
                    mc "always"
                    newbie "the mission failing kind of feels like my fault, like what happened during it was because of me and now we lost the thumbdrive"
                    jump newbie_what_happened_on_the_mission

label newbie_what_happened_on_the_mission:
    newbie "well, me and weap tech were supposed to get into the target's hacker's office right? hacker was leading us there by looking through the security cameras"
    newbie "we were supposed to be in and out as spy was distracting the govt hacker meaning the hallway was supposed to be empty, but someone was there"
    mc "who was there?"
    "they look uncomfortable"
    menu:
        newbie "it was the targets daughter, i knew we werent supposed to be seen, the only showing their face was supposed to be spy, but i didnt know what else to do, so i spoke to her"
        "why did you speak to her":
            newbie "i thought i could distract her? it didnt really work out that way, she distracted me more than anything, i had to be pulled away by weap tech"
            jump did_you_get_anything_out_of_her
        "was she on to you?":
            newbie "no, it didn't seem like it"
            jump did_you_get_anything_out_of_her

label did_you_get_anything_out_of_her:
    mc "did you get anything out of her?"
    newbie "nothing other than she's annoyed with her dad right now, she doesnt seem like a fan of the guy"
    menu:
        newbie "i would have gotten more info i swear, but by that time weap tech yanked me down the hall and leader was giving the call to pull out"
        "it doesnt sound like you ruined the mission":
            newbie "oh, thank you, but im still not sure, ill never make the same mistake though, i wont let this team down"
            jump youre_awfully_determined
        "did you see anything else?":
            newbie "the office seemed empty, but we couldnt go in because the daughter was there\nthere sounded like there were people arguing nearby too, i heard someone yelling as we were bolting"
            mc "could you hear what about?"
            newbie "no, but if i had to guess, someone was getting yelled at\nif only i had been paying better attention, then i wouldve gotten the drive, or at least better info"
            jump youre_awfully_determined

label youre_awfully_determined:
    mc "you're awfully determined"
    menu:
        newbie "anything to take down the tyrants they call the government around here"
        "it seems like you don't like the govt":
            newbie "no, too many people have suffered because of them, if i can make this place just a little bit more just, ill have done my job"
            mc "you're in the right place if that's your goal"
            jump youre_in_the_right_place_if_thats
        "you're in the right place if that's your goal":
            jump youre_in_the_right_place_if_thats

label youre_in_the_right_place_if_thats:
    newbie "no place id rather be! id do anything for this team\nyou really cheered me up mc! thanks, im gonna go to the kitchen for a bite if you want to come"
    mc "i'm alright, thanks though"
    newbie "your loss then! see you later"
    mc "see you later"
    jump initial_conversation_menu
# NEWBIE INITIAL CONVERSATION END

# LEADER INITIAL CONVERSATION START
label leader_first_conversation:
    "description of the room"
    menu:
        leader "how can i help you"
        "wanted to speak with you":
            leader "what about?"
            mc "what can you tell me about that night leader?"
            jump leader_what_can_you_tell_me_about
        "what are you looking at?":
            menu:
                leader "im going over a report of the mission, we'll be having a meeting later as a team"
                "what about?":
                    leader "what about?"
                    mc "what can you tell me about that night leader?"
                    jump leader_what_can_you_tell_me_about
                "have you figured anything out about that night?":
                    menu:
                        leader "no, nothing new, it doesnt make sense how it could have gone that badly, they must have known we'd be there"
                        "so you're sure there's a mole?":
                            leader "100 sure, we were too careful in our plans, i dont plan missions that go sideways that easily"
                            mc "what can you tell me about that night leader?"
                            jump leader_what_can_you_tell_me_about
                        "what can you tell me about that night?":
                            jump leader_what_can_you_tell_me_about


label leader_what_can_you_tell_me_about:
    leader "hacker and i were in a van offsite, the woods surrounding the property to be exact, theres a road hidden but still close enough to the building for hacker to be able to hack in"
    mc "what were you doing?"
    menu:
        leader "i was piloting the drone that hacker designed and weap tech built, i like having an eye on the team during high-stake missions like those"
        "what did you see?":
            leader "mostly guards changing their shifts, it was good to get a list of government affiliated people from the guests though"
            jump would_you_say_everyone_did_their_jobs
        "where did things go sideways?":
            leader "id say the turning point was when spy lost their visual on the target's hacker, they ran off and went god knows where"
            leader "but at the same time, hacker got kicked out of the system just minutes before, so maybe that should have been our first warning"
            jump would_you_say_everyone_did_their_jobs

label would_you_say_everyone_did_their_jobs:
    mc "would you say everyone did their jobs well?"
    leader "well for the most part yes"
    leader "i am a little annoyed by newbie however, they werent supposed to engage with anyone at the party especially not the daughter of the target that we're meant to steal from, i may have to speak to them later"
    mc "its a shame we lost the thumbdrive"
    menu:
        leader "yes...it is a shame...the thumbdrive would have been groundbreaking for the organization"
        "are you okay?":
            leader "yes, just thinking about something, dont worry about it"
            leader "anyway, i should finish going through these reports, ill see you at the meeting"
            mc "okay have fun"
            jump initial_conversation_menu
        "it looks like something's on your mind":
            leader "theres always a lot on the mind of a rebellion leader, speaking of, i should finish going through these reports, ill see you at the meeting"
            mc "okay have fun"
            jump initial_conversation_menu
# LEADER INITIAL CONVERSATION END

# MISSION BRIEFING START
label mission_briefing:
    "in the war room, everyone is there"
    "leader is talking abt what they could do from here"
    leader "did you get any info that we can use spy?"
    spy "nothing we didnt already know"
    leader "hacker?"
    hacker "we were able to get a better idea of who is involved with govt affairs, it was more public figures than we thought"
    weaptech "you mean like celebrities?"
    hacker "yeah, we knew about some, but there were so many more guests than we expected"
    sniper "you are referring to the target's daughter"
    hacker "well, i suppose, she wasnt supposed to be at her fathers house at all this month"
    leader "speaking of, ill take this time to remind the team that we have assigned jobs for a reason, i give you tasks that fit you, so stick to them"
    "theres an awkward pause"
    newbie "i was just trying to help"
    leader "i know that and everyone here appreciates that-"
    sniper "i did not appreciate it"
    "weap tech hits sniper"
    hacker "yeah, he has a point, youre new newbie, but that doesnt mean we dont have a system to things"
    spy "well hey now everybody, newbie was only trying to help, we've all made mistakes on missions before"
    sniper "i do not"
    "weap tech hits him again"
    leader "that's true, but no one has deliberately disobeyed directions before, it wont happen again"
    newbie "youre right, it wont, im sorry for messing up like that"
    hacker "whyd you even make conversation with her for so long? you could have made up an excuse and left or something"
    newbie "um"
    weaptech "yeah, it seemed like she wanted to speak with you for some reason"
    spy "i hope youre not suggesting something"
    weaptech "no no! just saying"
    sniper "do you know the daughter newbie?"
    newbie "no! of course not, ive never met her before"
    spy "newbie is not friends with anyone from the government, right newbie?"
    newbie "no, no im not"
    spy "so there you go, id appreciate it if you would stop throwing accusations like that of my friend"
    weaptech "newbie is our friend too spy"
    leader "and no one is accusing anyone of anything"
    "leader avoids your gaze when he says that"
    leader "this meeting was to establish the groundwork for where we go next"
    leader "i was banking on whatever we gleaned from the last mission to provide direction for the next, but because we didnt learn much, we'll have to find something else to do"
    leader "i'll call another meeting when i have a plan, get some rest for now"
    "the meeting ends"
# MISSION BRIEFING END

label second_conversation_menu:
    $ talkedToHacker2 = False
    $ talkedToSpy2 = False
    $ talkedToWeapTech2 = False
    $ talkedToSniper2 = False
    $ talkedToNewbie2 = False
    $ talkedToLeader2 = False
    $ numPeopleTalkedTo = 0

    menu:
        "you get to speak with three people"
        "hacker" if talkedToHacker2 == False and numPeopleTalkedTo < 3:
            $ talkedToHacker2 = True
            $ numPeopleTalkedTo += 1
            jump hacker_second_conversation
        "spy" if talkedToSpy2 == False and numPeopleTalkedTo < 3:
            $ talkedToSpy2 = True
            $ numPeopleTalkedTo += 1
            jump spy_second_conversation
        "weapon tech" if talkedToWeapTech2 == False and numPeopleTalkedTo < 3:
            $ talkedToWeapTech2 = True
            $ numPeopleTalkedTo += 1
            jump trishaPlaceholder
        "sniper" if talkedToSniper2 == False and numPeopleTalkedTo < 3:
            $ talkedToSniper2 = True
            $ numPeopleTalkedTo += 1
            jump trishaPlaceholder
        "newbie" if talkedToNewbie2 == False and numPeopleTalkedTo < 3:
            $ talkedToNewbie2 = True
            $ numPeopleTalkedTo += 1
            jump trishaPlaceholder
        "leader" if talkedToLeader2 == False and numPeopleTalkedTo < 3:
            $ talkedToLeader2 = True
            $ numPeopleTalkedTo += 1
            jump trishaPlaceholder
        "fight in workshop" if numPeopleTalkedTo == 3:
            jump trishaPlaceholder

# HACKER SECOND CONVERSATION START
label hacker_second_conversation:
    "you get to the hackers room and you can hear voices"
    hacker "yeah i know, its not the best"
    "..."
    hacker "i didnt know it would happen! i made it nearly foolproof-"
    "..."
    hacker "you cant blame this on me, i did everything i could to help"
    "..."
    hacker "yeah, yeah i-"
    "she turns around and sees you there in the doorway, startled"
    hacker "i-i gotta go mom, talk to you later"
    "she hangs up and looks at you awkwardly"
    "that was my mom, she was chewing me out because her recipe folder got deleted again, even though i helped her save it into like three different places"
    mc "that's rough"
    hacker "yeah haha"
    menu:
        hacker "...that meeting went kind of weird huh? i hope we can find a way to recover from losing the thumbdrive"
        "leader will think of something":
            hacker "yeah, hes smart, but ive actually had an idea for a while"
            hacker "ive been meaning to bring it up to him, but i havent had a chance to"
            mc "what's your idea?"
            hacker "tsk tsk! thats for me to know and everyone else to find out!"
            menu:
                hacker "tsk tsk! thats for me to know and everyone else to find out!"
                "you seem excited about the idea":
                    hacker "yeah, usually i just provide the tech backup, so it feels nice to do something more!"
                    mc "tech backup is super important still"
                    hacker "yeah but still! anyway im gonna go take a nap"
                    jump i_saw_those_redbulls_under
                "have you been having caffeine again?":
                    hacker "maybe...only natural sources though, tea does wonders for the body\nshe doesnt sound convincing\nim gonna go take a nap now"
                    jump i_saw_those_redbulls_under
        "what was even supposed to be on that drive?":
            hacker "no one really knows, but anything would be helpful, we can find a way to use whatever we get from the govt against them\nthe target was the president's old college buddy and current secretary of defense, so he runs in powerful circles"
            mc "how did we know the drive existed?"
            menu:
                hacker "oh uh, i found mentions of it in emails between him and the president"
                "emails? i thought govt officials werent supposed to use them anymore, i thought it was all via direct holo link?":
                    hacker "uh...yeah! i meant i found it mentioned by some people on a mission a couple months back"
                    mc "what people?"
                    hacker "i dont remember, it was so long ago\nanyway, i gotta take a nap, all this mission talk is tiring me out"
                    mc "uh okay"
                    "she disappears among the shelves and suddenly you hear a \"thump!\" and quiet snoring, it doesnt sound faked"
                    jump second_conversation_menu
                "that was a lucky find":
                    hacker "sure was haha, well, i gotta take a nap, too much mission talk you know?"
                    mc "uh okay"
                    "she disappears among the shelves and suddenly you hear a \"thump!\" and quiet snoring, it doesnt sound faked"
                    jump second_conversation_menu

label i_saw_those_redbulls_under:
    mc "how? i saw those redbulls under your desk"
    hacker "oops, i thought i hid those better, i can feel the caffeine crash coming though, i probably have about twenty seconds before i pass out"
    mc "uh, yeah go take a nap"
    hacker "bye!"
    "she disappears among the shelves and you can only hope she hit something soft before you hear heavy snoring"
    jump second_conversation_menu
# HACKER SECOND CONVERSATION END

# SPY SECOND CONVERSATION START
label spy_second_conversation:
    menu:
        "spys room is empty his journal is on his desk"
        "go find spy":
            "you walk out of the wardrobe wander around, hearing a groan and thump from the kitchen as you pass it"
            "peeking in, you find spy surrounded by salines on the table"
            mc "why are you surrounded by crushed saltines?"
            spy "oh! mc! you scared me, i was building a house of cards, or- er, crackers i suppose"
            menu:
                spy "i was bored if you couldnt tell"
                "could i ask you about your journal?":
                    spy "sure what about it?"
                    mc "whats in it?"
                    spy "just doodles, some venting that i dont feel comfortable sharing with people, that sort of thing\nmy dad used to do the same thing so i think i got it from him"
                    jump i_dont_know_much_about_families
                "so whered you get your journal?":
                    "he looks surprised but answers"
                    spy "well you know it was my dads, he left it to me when i moved away"
                    jump i_dont_know_much_about_families
        "open his journal":
            "creeping in, you reach his desk"
            "you open the journal to the first page which has written property of emson s penned on it"
            menu:
                "it seems like most of the front pages is writing and the back pages are drawings"
                "look at writings":
                    "they seem to be daily entries, he wrote more on somedays and less on others\nthe biggest entries seem to be mission days"
                    "today we broke into a govt lab. i didnt like it very much because we had to smash a bunch of samples, i think they were dna. im not sure, but i didnt like the mess. it cheered me up to remember this was govt property. i got glass in one of my shoes though."
                    "today was SUPER FUN!! we saw HORSES!!! like actual, not lab produced, naturally born horses!! i didnt know they came in those colors naturally too. i asked leader if we could take one back to the base, but he said no."
                    "yesterday sniper hit me during a mission. it hurt a lot, but i dont think he realized he used so much force, because when i fell, his eyes suddenly got wide and his mouth opened all big like a dumb old fish. though that might have been because a bomb went off."
                    "it looks like the last entry was after the failed mission"
                    "things didnt go well today. we didnt complete the objective, and now i think we're a little stuck. we all tried really hard, but im not sure where we'll go from here. im so sick of fighting all for us to have nowhere to go to lick our wounds. i can tell leader is stressed. he has to know that the govt is getting closer to us each day, but i wonder if hes just deluding himself."
                    "you hear a voice behind you"
                    spy "what are you doing!"
                    jump spy_turn_around
                "look at drawings":
                    "the first couple are absent scribbles, you can imagine emson scrawling in the journal during meetings with bronx droning in the back"
                    "others look like drawings of the others, side profiles that also were made during debriefs"
                    "some look like they were drawn by others, a cartoon of hacker seems to be self portrait"
                    "the more you go on, the better the drawings get, eventually they turn into sceneries of places you recognize from old missions as well as maps of places the team has infiltrated"
                    "the latest mission's building is in here"
                    "it looks like its a typical map of the three story building, just like what leader showed diagrams of in the war room"
                    "whats different is a map of an unrecorded floor that seems to be the basement, theres enough detail for it to suggest someones been there before, but this is spy's journal? when had he been to the basement of the target's home?"
                    jump trishaPlaceholder

label spy_turn_around:
    jump trishaPlaceholder

label i_dont_know_much_about_families:
    mc "i dont know much about peoples families here"
    "he shrugs"
    spy "some people are more comfortable talking about their families than others. it doesnt hurt to ask though in my opinion"
    mc "i suppose youre right"
    spy "well, i gotta clean up these crackers, leader will have my head if i dont"
    mc "bye bye"
    jump second_conversation_menu
# SPY SECOND CONVERSATION END

label placeholder:
    "has not been written"

label trishaPlaceholder:
    "code it trish!"