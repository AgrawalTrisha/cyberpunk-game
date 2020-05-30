# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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
    scene bg war room
    show leader neutral

    "Bronx shifts around in his seat."
    leader "This mission was called Operation Backwater. Our target was Flint Maddox, current Secretary of Defense."
    leader "The objective was to gather information on a thumbrive that was supposed to be in his home."
    leader "The opportunity to steal the drive arose when we got word he'd be hosting a gala. That drive was supposed to have vital information that could change everything for the Rebellion."
    leader "It was supposed to be in Oran Jege's office. Jege is Maddox's resident 'computer specialist', but that's just codeword for hacker."
    leader "When we infiltrated Maddox's gala, it wasn't there and we left empty-handed."
    mc "What does this have to do with me?"
    leader "I've suspected for a while, but I think there's a mole in the First Squadron."
    "You look at him sharply."
    mc "A mole?"
    show leader serious
    leader "Yes. I won't go into the whole history, but there's been too many coincidences. I'm sure of it and as this team's leader, I need to protect them."
    leader "Even if it's from themselves."
    mc "Who could it be?"
    leader "Anyone in the First. This squadron has the highest clearance of all the Rebellion, so the mole can do some real damage."
    "Meet the members."
    scene bg black
    show hacker happy
    "Lilea the Hacker" "Computer expert, inventor, caffiene addict"
    show spy happy
    "Emson the Spy" "Charmer, socialite, excellent conversationalist"
    show weaptech happy
    "Erix the Weapons Technician" "Inventor, mechanic, proud guardian of 40+ pistols"
    show sniper neutral
    "Elio the Sniper" "Trained marksmen, soldier, tall drink of water"
    show newbie happy
    "Kona the Newbie" "Jack of all trades, first line of defense, unofficial team toddler"
    show leader neutral
    "Bronx the Leader" "Veteran, strategist, unofficial team dad"
    jump initial_conversation_menu
# BRONX EXPOSITION END

label initial_conversation_menu:
    scene bg war room
    menu:
        "Who do you want to talk to?"
        "Lilea" if talkedToHacker == False:
            $ talkedToHacker = True
            jump hacker_first_conversation
        "Emson" if talkedToSpy == False:
            $ talkedToSpy = True
            jump spy_first_conversation
        "Erix" if talkedToWeapTech == False:
            $ talkedToWeapTech = True
            jump weaptech_first_conversation
        "Elio" if talkedToSniper == False:
            $ talkedToSniper = True
            jump sniper_first_conversation
        "Kona" if talkedToNewbie == False:
            $ talkedToNewbie = True
            jump newbie_first_conversation
        "Bronx" if talkedToLeader == False:
            $ talkedToLeader = True
            jump leader_first_conversation
        "Mission Briefing" if talkedToHacker and talkedToLeader and talkedToNewbie and talkedToSniper and talkedToSpy and talkedToWeapTech:
            jump mission_briefing

# HACKER INITIAL CONVERSATION START
label hacker_first_conversation:
    scene bg hacker room
    menu:
        "The room is dark, metal shelves creating a maze you can't imagine navigating. The bare walls make the clutter stand out more."
        "Cardboard boxes and stray papers line the shelves. You can see wires sticking out of random stacks."
        "A desk is on the far side of the room with a computer sitting idle."
        "Find Lilea.":
            "Listening closely, you can hear noises. It sounds like it's coming from inside the shelf maze."
            "You walk into the maze, following the mysterious noises. The source seems to be coming from a shelf pressed against a wall."
            show hacker neutral
            menu:
                "You don't know how, but Lilea is trapped in between the shelf and wall."
                "What are you doing?":
                    show hacker surprised
                    "She startles, craning her neck to look at you."
                    menu:
                        hacker "I'm trying to find something I dropped. Thought I could find it, but it's kinda dark back here."
                        "Thats the problem here?":
                        show hacker confused
                            "Lilea looks at you."
                            jump hacker_do_you_want_help
                        "Do you want help?":
                            jump hacker_do_you_want_help
                "How did you get back there?":
                    jump how_did_you_get_back_there
        "Snoop around.":
            "When you get close to the desk, the walls talk."
            "Voice" "Who's there?"
            "You whip around."
            menu:
                show hacker neutral
                "You can see a figure behind a shelf."
                "Who are you?":
                    "Voice" "You sound familiar... do I know you? I'm Lilea!"
                    "Oh, there she is."
                    mc "It's me."
                    jump its_me
                "It's me.":
                    jump its_me

label its_me:
    show hacker happy
    hacker "Oh mc! It's good you're there. I may or may not be stuck."
    "You notice now that the figure is contorted in between the shelf and a wall."
    menu:
        "Poor Lilea."
        "How did you get back there?":
            jump how_did_you_get_back_there
        "Do you want help?":
            jump hacker_do_you_want_help

label how_did_you_get_back_there:
    show hacker neutral
    hacker "Uh, I'm not sure."
    jump hacker_do_you_want_help

label hacker_do_you_want_help:
    show hacker neutral
    hacker "I could use some light. Go get my flashlight under my desk."
    "Her desk is messy, with lots of folders, wires, and drawings spread across it."
    "Belatedly, you notice there are at least three working monitors, with several smashed ones in the corner of the room."
    "You see the flashlight under the desk, along with a stray sock."
    hacker "Nice! Could you shine the light over me?"
    "You click on the flashlight, illuminating Lilea."
    show hacker happy
    hacker "Thanks, now I see it."
    mc "What did you lose?"
    "She extracts herself from the shelf, knocking over several boxes. In the process, even more wires and papers fall out of the boxes."
    hacker "My stress ball! I chucked it at the wall last night, you know... after Backwater."
    mc "Ah, I see."
    hacker "Yeah, it was kind of a mess."
    mc "What were you doing during Backwater, Lilea?"
    show hacker neutral
    hacker "My job was to be the eyes basically. Bronx and I were in a van offsite."
    menu:
        hacker "He was working a drone I designed last month, and i was inside Maddox's security system."
        "Did you see anything important?":
            hacker "Like anything wrong? Not really, though the plan did go sideways pretty quickly."
            mc "How?"
            hacker "Well, everything was doing their jobs to the letter except Kona."
            hacker "I was monitoring the team, and I saw her chatting up the target's daughter, Andrea, as if she didn't have somewhere to be."
            hacker "She must have gotten spotted and was trying to get away, if only they were more careful."
            mc "Was Kona alone?"
            hacker "No, she was a part of the inside team with Erix and Emson."
            mc "Maybe I should go talk to them."
            jump maybe_i_should_go_talk_to_them
        "Was everything going well?":
            hacker "Yeah it was, up until I lost my eyes that is."
            hacker "Jege must have realized I was in the system and booted me out. I think that was when things were over for us."
            mc "How could they have known?"
            hacker "I have no clue. I was so thorough. Maybe the inside team got caught."
            mc "Who was the inside team?"
            menu:
                hacker "That would be Kona, Emson, and Erix. After I lost my eyes I had no way of watching them, but there were a lot of close calls before that happened."
                "What kind of close calls?":
                    hacker " know Kona got spotted at one point. She was supposed to be sneaking with Erix, but for some reason she was talking with Maddox's daughter, Andrea!"
                    hacker "No clue what she was thinking."
                    hacker "Erix was supposed to be back up for Kona, to make sure the drive got picked up perfectly. You can tell they didn't exactly pull that off."
                    hacker "It wasn't long afterward before Bronx called the mission off."
                    jump im_sure_newbie_has_their_own_side_to_the_story
                "Maybe I should go talk to them.":
                    jump maybe_i_should_go_talk_to_them

label maybe_i_should_go_talk_to_them:
    show hacker happy
    hacker "Oh, if you're going to yell at her, there's no point. It won't solve anything."
    jump im_sure_newbie_has_their_own_side_to_the_story

label im_sure_newbie_has_their_own_side_to_the_story:
    mc "I'm sure Kona has her own side to the story."
    hacker "Right. Well, now that I have my stress ball, I can get back to stressing! I've got some schematics to look at."
    hacker "Without that thumbdrive, we lost a lot of valuable information. Gotta be double on top of everything!"
    mc "Well, bye."
    jump initial_conversation_menu
# HACKER INITIAL CONVERSATION END

# SPY INITIAL CONVERSATION START
label spy_first_conversation:
    scene bg spy room
    show spy neutral
    "The room reminds you of a thrift store. There's racks upon racks of clothes lining the walls, with additional dressers stacked in any free space."
    "A wall of mannequins wearing different length and style wigs. You don't understand the organization of the clothes, but you see a T-Rex costume hanging next to a floorlength prom dress."
    "There's a desk with a mirror propped on it tucked into the corner. Makeup and a journal cover the surface. The makeup seems to be half regular and half special effects."
    "Emson is lying on a feinting couch with his eyes closed."
    "He hears you approach and sits up."
    menu:
        spy "Hey! What's up?"
        "Nothing really. What're you doing?":
            "His eyes drift to his journal and he shrugs."
            menu:
                spy "Just decompressing. I was writing for a bit, but it was nothing big."
                "It looks pretty important. It's on real paper.":
                    "Only things that people don't want shared are written on paper. It's too easy to get your personal holo hacked if youre not careful."
                    "The Rebellion uses paper for mission plans, weapon and device designs, and other secret info."
                    menu:
                        spy "Oh yeah, it's just some personal stuff. That was my dad's journal so..."
                        "Oh, I'm sorry for prying.":
                            spy "No worries! I admit it is pretty weird for someone to be using an actual journal nowadays. This is just really sentimental to me."
                            menu:
                                spy "Is there something I can do for you?"
                                "What did you do during Backwater, Emson?":
                                    jump spy_what_did_you_do_on_the_mission
                                "Backwater didn't go well, did it?":
                                    jump the_mission_didnt_go_well
                        "Are those drawings?":
                            "You can see what looks like doodles and sketches on a page sticking out of the journal."
                            spy "Oh, yeah. They're small."
                            mc "What of?"
                            menu:
                                spy "Uh, people mostly. Sometimes places we go to."
                                "Who?":
                                    "He gets shy."
                                    menu:
                                        spy "The team..."
                                        "How sweet, you love us.":
                                            spy "Of course I do. You're my family."
                                            menu:
                                                spy "Speaking of, why'd you waltz into my room like an annoying little sibling?"
                                                "What did you do during Backwater, Emson?":
                                                    jump spy_what_did_you_do_on_the_mission
                                                "Backwater didn't go well, did it?":
                                                    jump the_mission_didnt_go_well
                                        "We better not look ugly.":
                                            spy "Not more ugly than you all are usually."
                                            menu:
                                                spy "Say, as much as I love being interrogated, did you need something?"
                                                "What did you do during Backwater, Emson?":
                                                    jump spy_what_did_you_do_on_the_mission
                                                "Backwater didn't go well, did it?":
                                                    jump the_mission_didnt_go_well
                                "What places?":
                                    menu:
                                        "Mainly places we go to on missions. Sometimes, I draw maps to study so i don't get lost. Also some of the places we see are so gorgeous, it'd be a crime not to."
                                        "Did you draw a map of Maddox's estate?":
                                            menu:
                                                spy "I did, as tragic as Backwater was."
                                                "What did you do during Backwater, Emson?":
                                                    jump spy_what_did_you_do_on_the_mission
                                                "Backwater didn't go well, did it?":
                                                    jump the_mission_didnt_go_well
                                        "I bet they're really good. You have an eye for gorgeous things.":
                                            "Well of course. Beauty knows beauty."
                                            menu:
                                                spy "Oh, did you need something? You did come in here for something right?"
                                                "What did you do during Backwater, Emson?":
                                                    jump spy_what_did_you_do_on_the_mission
                                                "Backwater didn't go well, did it?":
                                                    jump the_mission_didnt_go_well
                "You got a crush? Writing in your diary to them?":
                    spy "What! No! There's no one."
                    mc "Riiiiight."
                    "He blushes."
                    menu:
                        spy "I mean it, but never mind. What did you come to me for?"
                        "What did you do during Backwater, Emson?":
                            jump spy_what_did_you_do_on_the_mission
                        "Backwater didn't go well, did it?":
                            jump the_mission_didnt_go_well
        "I wanted to ask how Backwater went. I heard it was bad.":
            spy "Yeah. It wasn't as smooth as it could've been."
            mc "What did you do during Backwater, Emson?"
            jump spy_what_did_you_do_on_the_mission

label spy_what_did_you_do_on_the_mission:
    spy "I was the distraction. It's kinda my thing, ya know?"
    spy "I was supposed to keep Maddox's lapdog out of their office."
    jump lapdog

label lapdog:
    mc "Lapdog?"
    spy "Yeah, their resident tech guy, Jege. Hard to call him a hacker when he doesn't hold a candle to ours, heh."
    mc "Did you get to them?"
    spy "Yeah, I did."
    menu:
        spy "We were chatting for a bit when he suddenly got real agitated and ran away. I guess he figured out something was up. Probably was wearing an earpiece."
        "Did he say anything?":
            menu:
                spy "Nothing that made sense. Only 'no, get out of there! You were supposed to stay out of there.'"
                "That's weird.":
                    spy "Yup, but what do you expect from rats? Good thing Bronx gave the order to abort the mission soon afterward."
                    jump you_really_hate_the_government
                "Do you know what he was talking about?":
                    spy "No, not at all. Government rats rarely make sense."
                    jump you_really_hate_the_government
        "What did you do afterwards?":
            spy "I was going to radio in to Bronx, but then someone else came to talk to me."
            mc "who came to talk to you?"
            spy "Ah, just some government jerk. Low-level riff-raff is all. Didn't say anything useful. Bronx gave the order for us to abort like ten minutes after that anyway."
            jump you_really_hate_the_government

label you_really_hate_the_government:
    mc "You really hate the government don't you?"
    "His face gets stony."
    spy "They're not my favorite people, no."
    spy "Hey, I love talking—that's why I'm so good at my job—but I think I need some me time. Backwater kind of tired me out."
    mc "Oh, see you then."
    jump initial_conversation_menu

label the_mission_didnt_go_well:
    spy "No. No, it didn't."
    spy "I mean, it could've been a lot worse, but it could've been a lot better."
    mc "How could it have been worse?"
    spy "We didn't lose anyone this time."
    "You look at Emson awkwardly."
    spy "Sorry, that was grim. Hard not to be in this line of work sometimes."
    spy "I had to deal with Maddox's lapdog and I get grouchy when I have to socialize with rats."
    jump lapdog
# SPY INITIAL CONVERSATION END

# WEAPON TECH INITIAL CONVERSATION START
label weaptech_first_conversation:
    "The room is cluttered, but the organized kind of cluttered. Tables line the walls, covered with scraps, diagrams, and schematics."
    "The largest table is in the middle of the workshop. Even more weapon schematics are on the walls."
    "Half-made weapons, drones, and other contraptions are scattered on the various tables."
    menu:
        "There's a figure bent over the middle table. It's Erix."
        "Approach the table.":
            "You notice they're working on an explosive. When you walk to the other side of the them, Erix sees you."
            menu:
                weaptech "Hey! What's up?"
                "Just wanted to talk. You busy?":
                    "Erix wipes their hands on a rag."
                    weaptech "Nope, what do you need?"
                    mc "What did you do on the mission, Erix?"
                    jump weaptech_what_did_you_do_on_the_mission
                "Uh, is that a bomb?":
                    weaptech "Yup! Good thing you didn't scare me. One wrong move and this room is fire and rubble."
                    "You eye the bomb carefully."
                    mc "Is that for a mission?"
                    weaptech "Oh no, not anything in particular. It just never hurts to have an explosive around!"
                    mc "Right. Well, I just wanted to chat."
                    weaptech "Sure, what about?"
                    mc "What did you do on the mission, Erix?"
                    jump weaptech_what_did_you_do_on_the_mission
        "Hey. What're you working on?":
            "Erix jolts suddenly, startled."
            weaptech "No no no!"
            "They throw whatever was in their hands across the room and drag you out the door to the hallway."
            mc "Why are we out here?"
            "They press you to the ground and curl up on top of you, not answering."
            "..."
            "After a minute, they get up and peek in the doorway."
            menu:
                weaptech "Well, I was working on an explosive. Guess it wasnt a good one."
                "That was a bomb?":
                    weaptech "It was supposed to be. No idea why it didn't blow—not that I'm complaining. What brings you to my shop?"
                    mc "Just wanted to talk. You busy?"
                    weaptech "Nope, what do you need?"
                    mc "What did you do on the mission, Erix?"
                    jump weaptech_what_did_you_do_on_the_mission
                "Was going into the hallway really supposed to save us from an explosion?":
                    "They drag you into the room again and plop down in their seat."
                    weaptech "I mean, it's better than nothing right? What brought you to my shop though?"
                    mc "Just wanted to talk. You busy?"
                    weaptech "Nope, what do you need?"
                    mc "What did you do on the mission, Erix?"
                    jump weaptech_what_did_you_do_on_the_mission

label weaptech_what_did_you_do_on_the_mission:
    weaptech "I was meant to be Kona's backup. She's talented, but still fresh. I'm probably the most skilled in combat after Elio and Kona."
    weaptech "Together we were meant to find Maddox's hacker's office. Jege was supposed to have it there."
    mc "Was it not there?"
    weaptech "No, it wasn't. We broke in not long after Emson started speaking with Jege."
    mc "Everything worked out though? Besides the missing drive?"
    menu:
        weaptech "Well, not quite. The daughter of the target—Andrea, I think her name was? She actually spotted us. I'm not surprised we ran into someone, but I'm shocked it was her."
        "Why?":
            weaptech "There weren't any guards in that area, the most important corner of the building. Jege's office, Maddox's office, and even an entire vault were in that hallway."
            mc "How did you get away?"
            weaptech "Well, I made up some excuse and dragged Kona away. Good timing too, Bronx told us to get out almost immediately after."
            weaptech "I could have sworn I heard someone yelling at someone else as we ran. Sounded angry, but I didn't care. I just wanted to get out in one piece."
            jump they_stand_and_grab_a_pistol
        "What did you do?":
            menu: 
                weaptech "Well, by the time I noticed, Kona had struck up conversation with the woman. I swear, that girl spends so much time with Emson. She's really taking after the goober."
                "So they were talking?":
                    weaptech "Like they were old friends. Would've expected the daughter to immediately pull the alarm, but no, she never did."
                    weaptech "Bronx told us to get out of there right when I pulled Kona away."
                    mc "That's odd that they clicked so well."
                    weaptech "You're telling me. It was just in time too. I heard voices yelling as we ran—sounded like someone was getting chewed out."
                    jump they_stand_and_grab_a_pistol
                "How did you get away?":
                    weaptech "Well, I made up some excuse and dragged Kona away. Good timing too, Bronx told us to get out almost immediately after."
                    weaptech "I could have sworn I heard someone yelling at someone else as we ran. Sounded angry, but I didn't care. I just wanted to get out in one piece."
                    jump they_stand_and_grab_a_pistol

label they_stand_and_grab_a_pistol:
    "They stand and grab a pistol off the table, inspecting it carefully."
    menu:
        weaptech "You like 'em? This is my baby, Ace!"
        "Your baby?":
            weaptech "Yup! Built him myself!"
            jump this_bad_boy_packs
        "Why is it called Ace?":
            weaptech "Ace is a 'he', not an 'it'. Be nice. I don't know why he's called Ace. Just felt right."
            weaptech "I love my baby more than anything! Oh, but don't tell Elio, yeah? It'll be our little secret."
            mc "I guess?"
            jump this_bad_boy_packs

label this_bad_boy_packs:
    weaptech "Hehe, this bad boy packs more punch than a whole cannon! I was gonna test him after I finished the bomb, but oh well. Wanna come watch?"
    mc "You know, I'm good."
    weaptech "Well, your loss. If you want, you can hang around here more, but I'm gonna go now, see you!"
    mc "See you."
    jump initial_conversation_menu
# WEAPON TECH INITIAL CONVERSATION END

# SNIPER INITIAL CONVERSATION START
label sniper_first_conversation:
    "In this room, weapons cover the wall, including all manner of guns, knives, and blunt objects. There's a table with dismantled gun parts pushed against the far wall."
    "Ammo boxes are stacked underneath the table. Everything is so sterile, it reminds you of a twisted hospital."
    "A man is sitting criss-cross on the floor, polishing a dismantled rifle. It's Elio."
    menu:
        "He doesn't look up when you enter."
        "What're you doing?":
            menu:
                sniper "I'm cleaning my rifle."
                "How often do you do that?":
                    menu:
                        sniper "Before and after every mission, and at least once a day."
                        "Wow, that's a lot.":
                            sniper "It's what is necessary for the safety of myself and the people around me... or at least the people who aren't on the other side of the muzzle."
                            "There's a pause."
                            sniper "Why did you come to me?"
                            jump sniper_what_did_you_do_on_the_mission
                        "Explains why you're so good at it.":
                            sniper "I have lots of experience, yes."
                            "There's a pause."
                            sniper "Why did you come to me?"
                            jump sniper_what_did_you_do_on_the_mission
                "You look scary like that.":
                    sniper "I've been told that before."
                    sniper "Why did you come to me?"
                    jump sniper_what_did_you_do_on_the_mission
        "Hi Elio.":
            "He turns around."
            menu:
                sniper "Hello."
                "That's a big rifle.":
                    sniper "It does its job."
                    "There's a pause."
                    sniper "Why did you come to me?"
                    jump sniper_what_did_you_do_on_the_mission
                "Is this a bad time?":
                    sniper "No, I can spare time. Why did you come here?"
                    jump sniper_what_did_you_do_on_the_mission

label sniper_what_did_you_do_on_the_mission:
    mc "I wanted to ask about Backwater."
    "He looks at you."
    mc "What did you do during Backwater, Elio?"
    sniper "my job was to provide cover and visual for the group"
    menu:
        sniper "My job was to provide cover and visual for the group. I was stationed in the hills adjacent to Maddox's home with a clear view of the front and back entrances."
        "What did you see there?":
            menu:
                sniper "I saw people entering the front entrance in the beginning of the evening and not much movement from the back entrance."
                "Who was entering the front?":
                    sniper "Regular visitors, low-level government officials, and the like."
                    mc "Did you see anyone else in the front of the property?"
                    menu:
                        sniper "In fact, yes. Part of the way through the night, I saw a single guard stand outside by the outskirts of the property."
                        "What was the guard doing?":
                            sniper "I saw him loiter around for a while. It about five minutes, before staring into the woods surrounding the property. He suddenly turned around and stalked back to the building."
                            jump thats_really_weird
                        "Was he not supposed to be there?":
                            sniper "Usually the guards are in teams of two. I get the feeling he wasn't meant to be there."
                            sniper "He stood by the woods for a short amount of time before suddenly stalking back to the building."
                            jump thats_really_weird
                "What was happening at the back entrance?":
                    sniper "It seemed that was the main entrance for catering and security. I saw food being carried in and guards changing shifts through that door."
                    mc "Was there anything you saw that was different?"
                    jump was_there_anything_you_that_was_different
        "Did everything look good?":
            menu:
                sniper "Yes, there was no suspicious activity besides what was to be expected of the situation."
                "What was expected of the situation?":
                    sniper "The guest list was to be made up of people wrapped up in government secrets. Everyone there was complicit in their crimes."
                    mc "So nothing stuck out to you?"
                    sniper "I suppose something did, now that you remind me."
                    menu:
                        sniper "Part of the way through the night, I saw a single guard stand outside by the outskirts of the property. It was by the woods."
                        "What was the guard doing?":
                            sniper "I saw him loiter around for a while. It about five minutes, before staring into the woods surrounding the property. He suddenly turned around and stalked back to the building."
                            jump thats_really_weird
                        "Was he not supposed to be there?":
                            sniper "Usually the guards are in teams of two. I get the feeling he wasn't meant to be there."
                            sniper "He stood by the woods for a short amount of time before suddenly stalking back to the building."
                            jump thats_really_weird
                "Was there anything you saw that was different?":
                    jump was_there_anything_you_that_was_different

label was_there_anything_you_that_was_different:
    menu:
        sniper "Different? I suppose there was something that was unexpected, but not overtly suspicious. Part of the way through the night, I saw a single guard stand outside by the outskirts of the property. It was by the woods."
        "What was the guard doing?":
            sniper "I saw him loiter around for a while. It about five minutes, before staring into the woods surrounding the property. He suddenly turned around and stalked back to the building."
            jump thats_really_weird
        "Was he not supposed to be there?":
            sniper "Usually the guards are in teams of two. I get the feeling he wasn't meant to be there."
            sniper "He stood by the woods for a short amount of time before suddenly stalking back to the building."
            jump thats_really_weird

label thats_really_weird:
    mc "That's really weird."
    sniper "I don't typically use that word, but yes. I suppose it was weird."
    "He looks down at the weapon on the floor in front of him."
    sniper "I would like to continue cleaning my rifle."
    mc "Oh yeah, bye."
    jump initial_conversation_menu
# SNIPER INITIAL CONVERSATION END

# NEWBIE INITIAL CONVERSATION START
label newbie_first_conversation:
    "You enter a bedroom, plain and discreet. It looks like whoever lives here hasn't been here long enough to decorate."
    "The only signs of a person inhabiting the space is the bed and the walls. The sheets are slightly rumpled and the walls have things on one wall."
    "There's a poster of the president with a mustache scribbled on it with black marker, a target in the shape of a person, and a picture of the First Squadron on top of hill taken by Emson."
    "When you look closer, it looks like there's holes in the target, like someone was throwing knives at it. There are holes in the wall behind it too."
    "There's a woman laying on the ground by the bed. It's Kona."
    menu:
        newbie "Hi! What's up?"
        "Just wanted to see what you're up to.":
            menu:
                newbie "Oh, just thinking about Backwater. It didn't go how I expected."
                "It didn't go how anyone expected.":
                    "She laughs, but it sounds bitter."
                    newbie "No, it really didn't."
                    "A pause."
                    newbie "Can I tell you something?"
                    mc "Always."
                    newbie "Backwater failing kind of feels like my fault. Like, what happened during it was because of me and now we lost the thumbdrive."
                    jump newbie_what_happened_on_the_mission
                "Want to talk about it?":
                    newbie "Yeah, actually. I feel kinda bad about it. I think it's my fault it failed so bad."
                    jump newbie_what_happened_on_the_mission
        "How you been?":
            menu:
                newbie "I've been better. Backwater was kind of a mess and it's been making me a mess too."
                "Want to talk about it?":
                    newbie "Yeah, actually. I feel kinda bad about it. I think it's my fault it failed so bad."
                    jump newbie_what_happened_on_the_mission
                "It didn't go how anyone expected.":
                    "She laughs, but it sounds bitter."
                    newbie "No, it really didn't."
                    "A pause."
                    newbie "Can I tell you something?"
                    mc "Always."
                    newbie "Backwater failing kind of feels like my fault. Like, what happened during it was because of me and now we lost the thumbdrive."
                    jump newbie_what_happened_on_the_mission

label newbie_what_happened_on_the_mission:
    newbie "Well, Erix and I were supposed to get into Jege's office, right? Lilea was leading us there by looking through the security cameras."
    newbie "We were supposed to be in and out as Emson was distracting Jege. That meant the hallway was supposed to be empty, but someone was there."
    mc "Who was there?"
    "Kona looks uncomfortable."
    menu:
        newbie "It was Maddox's daughter. Her name's Andrea. I knew we weren't supposed to be seen. The only one of us showing our face was supposed to be Emson, but I didn't know what else to do, so i spoke to her."
        "Why did you speak to her?":
            newbie "I thought I could distract her. It didn't really work out that way. She distracted me more than anything. I had to be pulled away by Erix."
            jump did_you_get_anything_out_of_her
        "Was she on to you?":
            newbie "No, it didn't seem like it."
            jump did_you_get_anything_out_of_her

label did_you_get_anything_out_of_her:
    mc "Did you get anything out of her?"
    newbie "Nothing other than she's annoyed with her dad right now. She doesn't seem like a fan of the guy."
    menu:
        newbie "I would have gotten more info, I swear! By that time, Erix yanked me down the hall and Bronx was giving the call to pull out."
        "It doesn't sound like you ruined the mission.":
            newbie "Oh, thank you, but I'm still not sure. I'll never make the same mistake though. I wont let this team down."
            jump youre_awfully_determined
        "Did you see anything else?":
            newbie "The office seemed empty, but we couldn't look around for long because Andrea was there. There sounded like there were people arguing nearby too. I heard someone yelling as we were bolting."
            mc "Could you hear what about?"
            newbie "No, but if I had to guess, someone was getting yelled at. If only I had been paying better attention. Then I would've gotten the drive, or at least better info."
            jump youre_awfully_determined

label youre_awfully_determined:
    mc "You're awfully determined."
    menu:
        newbie "Anything to take down the tyrants they call the government around here."
        "It seems like you don't like the government.":
            newbie "No. Too many people have suffered because of them. If I can make this place just a little bit more just, I'll have done my job."
            mc "You're in the right place if that's your goal."
            jump youre_in_the_right_place_if_thats
        "You're in the right place if that's your goal.":
            jump youre_in_the_right_place_if_thats

label youre_in_the_right_place_if_thats:
    newbie "No place I'd rather be! I'd do anything for this team. You really cheered me up! Thanks, I'm gonna go to the kitchen for a bite if you want to come."
    mc "I'm alright. Thanks, though."
    newbie "Your loss then! See you later."
    mc "See you later."
    jump initial_conversation_menu
# NEWBIE INITIAL CONVERSATION END

# LEADER INITIAL CONVERSATION START
label leader_first_conversation:
    "The room is bare, except for a piece of paper taped high up on the wall, almost to the ceiling. It looks like \"THE WAR ROOM\" is written with crayon on the paper."
    "There's a long conference table in the center of the room, eight seats pushed in. Bronx is sitting at the end, files spread out before him. He looks up when you enter."
    menu:
        leader "How can I help you?"
        "Wanted to speak with you.":
            leader "What about?"
            mc "What can you tell me about Backwater, Bronx?"
            jump leader_what_can_you_tell_me_about
        "What are you looking at?":
            menu:
                leader "I'm going over a report of the events that happened at Backwater. We'll be having a meeting later as a team."
                "What about?":
                    leader "Where we go after the last mission. Speaking of, what did you come in here for? Did you have a question?"
                    mc "What can you tell me about Backwater, Bronx?"
                    jump leader_what_can_you_tell_me_about
                "have you figured anything out about that night?":
                    menu:
                        leader "No, nothing new. It doesn't make sense how it could have gone that badly. They must have known we'd be there."
                        "So you're sure there's a mole?":
                            leader "100 percent sure. We were too careful in our plans. I don't plan missions that go sideways that easily."
                            mc "What can you tell me about Backwater, Bronx?"
                            jump leader_what_can_you_tell_me_about
                        "What can you tell me about Backwater, Bronx?":
                            jump leader_what_can_you_tell_me_about


label leader_what_can_you_tell_me_about:
    leader "Lilea and I were in a van offsite. The woods surrounding the property to be exact. There's a road hidden but still close enough to Maddox's house for Lilea to be able to hack in."
    mc "What were you doing?"
    menu:
        leader "I was piloting the drone that Lilea designed and Erix built. I like having an eye on the team during high-stake missions like Backwater."
        "What did you see?":
            leader "Mostly guards changing their shifts. It was good to get a list of government affiliated people from the guests though. We can use who we saw there too compile a list of enemies."
            jump would_you_say_everyone_did_their_jobs
        "Where did things go sideways?":
            leader "I'd say the turning point was when Emson lost their visual on Maddox's hacker, Jege. They ran off and went God knows where."
            leader "But at the same time, Lilea got kicked out of the system just minutes before, so maybe that should have been our first warning."
            jump would_you_say_everyone_did_their_jobs

label would_you_say_everyone_did_their_jobs:
    mc "Would you say everyone did their jobs well?"
    leader "Well, for the most part, yes."
    leader "I am a little annoyed by Kona however. She wasn't supposed to engage with anyone at the party. Especially not the daughter of the target that we're meant to steal from. I may have to speak to her later."
    mc "It's a shame we lost the thumbdrive."
    leader "Yes..."
    leader "It is a shame..."
    menu:
        leader "The thumbdrive would have been groundbreaking for the Rebellion."
        "Are you okay?":
            leader "Yes, just thinking about something. Don't worry about it."
            leader "Anyway, I should finish going through these reports. I'll see you at the meeting."
            mc "Okay, have fun."
            jump initial_conversation_menu
        "It looks like something's on your mind.":
            leader "There's always a lot on the mind of a rebellion leader. Speaking of, I should finish going through these reports. I'll see you at the meeting."
            mc "Okay, have fun."
            jump initial_conversation_menu
# LEADER INITIAL CONVERSATION END

# MISSION BRIEFING START
label mission_briefing:
    "You got a message from Bronx asking for your presence in the War Room. When you enter, everyone is there. Bronx is talking about what the team could do from moving foreward."
    leader "Did you get any info that we can use Emson?"
    spy "Nothing we didn't already know."
    leader "Lilea?"
    hacker "We were able to get a better idea of who is involved with government affairs. There were more public figures than we thought."
    weaptech "You mean like celebrities?"
    hacker "Yeah. We knew about some, but there were so many more guests than we expected."
    sniper "You are referring to Maddox's daughter."
    hacker "Well, I suppose. She wasn't supposed to be at her father's house at all this month."
    leader "Speaking of, I'll take this time to remind the team that we have assigned jobs for a reason. I give you tasks that fit you, so please stick to them."
    "There's an awkward pause."
    newbie "I was just trying to help."
    leader "I know that, and everyone here appreciates that-"
    sniper "I did not appreciate it."
    "Erix gives Elio a nasty look."
    hacker "Yeah, he has a point. You're new Kona, but that doesn't mean we don't have a system for things."
    spy "Well hey now everybody. Kona was only trying to help. We've all made mistakes on missions before."
    sniper "I have not."
    "Erix glares at him again."
    leader "That's true, but no one has deliberately disobeyed directions before. It won't happen again."
    newbie "You're right. It won't. I'm sorry for messing up like that."
    hacker "Why'd you even make conversation with her for so long? You could have made up an excuse and left or something."
    newbie "Um."
    weaptech "Yeah. It seemed like she wanted to speak with you for some reason."
    spy "I hope you're not suggesting something."
    weaptech "No no! Just saying."
    sniper "Do you know Maddox's daughter, Kona?"
    newbie "No! Of course not! I've never met her before."
    spy "Kona is not friends with any of our enemies. Right, Kona?"
    newbie "No, no. I'm not"
    spy "So there you go, I'd appreciate it if you would stop throwing accusations like that at my friend."
    weaptech "Kona is our friend too, Em."
    leader "And no one is accusing anyone of anything."
    "Bronx avoids your gaze when he says that."
    leader "This meeting was to establish the groundwork for where we go next. I was banking on whatever we gleaned from Backwater to provide direction for the next, but because we didn't learn much, we'll have to find something else to do."
    leader "I'll call another meeting when I have a plan. Get some rest for the time being."
    "With that dismissal, everyone files out of the room."
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
        "You have time to talk to three people after the mission briefing."
        "Lilea." if talkedToHacker2 == False and numPeopleTalkedTo < 3:
            $ talkedToHacker2 = True
            $ numPeopleTalkedTo += 1
            jump hacker_second_conversation
        "Emson." if talkedToSpy2 == False and numPeopleTalkedTo < 3:
            $ talkedToSpy2 = True
            $ numPeopleTalkedTo += 1
            jump spy_second_conversation
        "Erix." if talkedToWeapTech2 == False and numPeopleTalkedTo < 3:
            $ talkedToWeapTech2 = True
            $ numPeopleTalkedTo += 1
            jump weaptech_second_conversation
        "Elio." if talkedToSniper2 == False and numPeopleTalkedTo < 3:
            $ talkedToSniper2 = True
            $ numPeopleTalkedTo += 1
            jump sniper_second_conversation
        "Kona." if talkedToNewbie2 == False and numPeopleTalkedTo < 3:
            $ talkedToNewbie2 = True
            $ numPeopleTalkedTo += 1
            jump newbie_second_conversation
        "Bronx." if talkedToLeader2 == False and numPeopleTalkedTo < 3:
            $ talkedToLeader2 = True
            $ numPeopleTalkedTo += 1
            jump leader_second_conversation
        "What's that noise?" if numPeopleTalkedTo == 3:
            jump fight_in_workshop

# HACKER SECOND CONVERSATION START
label hacker_second_conversation:
    "You get to Lilea's room and you can hear Lilea's voice. You stand in the doorway. It sounds like she's on the phone."
    hacker "Yeah, I know. It's not the best."
    "..."
    hacker "I didn't know it would happen! I made it nearly foolproof—"
    "..."
    hacker "You can't blame this on me. I did everything I could to help."
    "..."
    hacker "Yeah, yeah. I—"
    "She turns around and sees you there in the doorway, and she looks startled."
    hacker "I—I gotta go, Mom. Talk to you later."
    "She hangs up and looks at you awkwardly."
    "That was my mom. She was chewing me out because her recipe folder got deleted again, even though I helped her save it into like three different places on her hard drive."
    mc "That's rough."
    hacker "Yeah, haha..."
    menu:
        hacker "That meeting went kind of weird, huh? I hope we can find a way to recover from losing the thumbdrive."
        "Bronx will think of something.":
            hacker "Yeah, he's smart. But, I've actually had an idea for a while."
            hacker "I've been meaning to bring it up to him, but I haven't had a chance to."
            mc "What's your idea?"
            hacker "Tsk tsk! That's for me to know and everyone else to find out!"
            menu:
                hacker "Except for Bronx I guess, since I'll be telling him directly... but you get the point!"
                "You seem excited about the idea.":
                    hacker "Yeah. Usually I just provide the tech backup, so it feels nice to do something more!"
                    mc "Tech backup is super important."
                    hacker "Yeah, but still! Anyway, I'm gonna go take a nap."
                    jump i_saw_those_redbulls_under
                "Have you been having caffeine again?":
                    hacker "Maybe..."
                    hacker "Only natural sources though, tea does wonders for the body!"
                    "She doesn't sound convincing."
                    hacker "I'm gonna go take a nap now."
                    jump i_saw_those_redbulls_under
        "What was even supposed to be on that drive?":
            hacker "No one really knows, but anything would be helpful. We can find a way to use whatever we get from the government against them."
            hacker "Maddox was the president's old college buddy and is the current Secretary of Defense, so he runs in powerful circles."
            mc "How did we know the drive existed?"
            menu:
                hacker "Oh uh, I found mentions of it in emails between him and the president."
                "Emails?":
                    mc "I thought government officials weren't supposed to use them anymore. I thought it was all via direct holo link?"
                    hacker "Uh..."
                    hacker "Yeah! I meant I found it mentioned by some people on a mission a couple months back."
                    mc "What people?"
                    hacker "I don't remember. It was so long ago."
                    hacker "Anyway, I gotta take a nap. All this mission talk is tiring me out."
                    mc "Uh, okay."
                    "She disappears somewhere into the depths of her office. A moment later, you hear soft snoring."
                    jump second_conversation_menu
                "That was a lucky find.":
                    hacker "Sure was."
                    "She laughs."
                    hacker "Well, I gotta take a nap. Too much mission talk, you know?"
                    mc "Uh, okay."
                    "She disappears somewhere into the depths of her office. A moment later, you hear soft snoring."
                    jump second_conversation_menu

label i_saw_those_redbulls_under:
    mc "How? I saw those Redbulls under your desk."
    hacker "Oops, I thought I hid those better. I can feel the caffeine crash coming though. I probably have about twenty seconds before I pass out."
    mc "Uh, yeah. Go take a nap."
    hacker "Bye!"
    "She disappears somewhere into the depths of her office. A moment later, you hear soft snoring."
    jump second_conversation_menu
# HACKER SECOND CONVERSATION END

# SPY SECOND CONVERSATION START
label spy_second_conversation:
    menu:
        "When you enter Emson's room, it's empty. His journal is on his desk."
        "Go find Emson.":
            "You walk out of his room and wander around, hearing a groan and thump from the war room as you pass it."
            "Peeking in, you find Emson surrounded by saltines on the table."
            mc "Why are you surrounded by crushed saltines?"
            spy "Oh! You scared me. I was building a house of cards. Or—er, crackers, I suppose."
            menu:
                spy "I was bored if you couldn't tell."
                "Could I ask about your journal?":
                    spy "Sure. What about it?"
                    mc "What's in it?"
                    spy "Just doodles. Some venting that I don't feel comfortable sharing with people. That sort of thing."
                    spy "My dad used to do the same thing so I think I got it from him."
                    jump i_dont_know_much_about_families
                "So, where'd you get your journal?":
                    "He looks surprised, but answers anyway."
                    spy "Well, you know it was my dad's. He left it to me when I moved away."
                    jump i_dont_know_much_about_families
        "Open his journal.":
            "Creeping in, you reach his desk."
            "You open the journal to the first page, which has \"Property of Emson S.\" penned on it."
            menu:
                "It seems like most of the front pages is writing and the back pages are drawings."
                "Look at writings.":
                    "They seem to be daily entries. He wrote more on some days and less on others. The biggest entries seem to be mission days."
                    "\"Today we broke into a government lab. I didn't like it very much because we had to smash a bunch of samples. I think they were DNA. I'm not sure, but I didn't like the mess."
                    "It cheered me up to remember this was government property. I got glass in one of my shoes though.\""
                    "\"Today was SUPER FUN!! We saw HORSES!!! Like actual, not lab-produced, naturally-born horses!! I didn't know they came in those colors naturally either. I asked Bronx if we could take one back to the base, but he said no.\""
                    "\"Yesterday Elio hit me during a mission. It hurt a lot, but I don't think he realized he used so much force."
                    "When I fell, his eyes suddenly got wide and his mouth opened all big like a dumb old fish. Though that might have been because a bomb went off.\""
                    "It looks like the last entry was after Backwater."
                    "\"Things didn't go well today. We didn't complete the objective, and now I think we're a little stuck. We all tried really hard, but I'm not sure where we'll go from here."
                    "I'm so sick of fighting all for us to have nowhere to go to lick our wounds. I can tell Bronx is stressed. He has to know that the government is getting closer to us each day, but I wonder if he's just deluding himself.\""
                    "You hear Emson's footsteps behind you."
                    spy "What are you doing?"
                    jump spy_turn_around
                "Look at drawings.":
                    "The first couple are absent scribbles. You can imagine Emson scrawling in the journal during meetings with Bronx droning on in the background."
                    "Others look like drawings of the team, side profiles that also were made during debriefings."
                    "Some look like they were drawn by your teammates. A cartoon doodle of Lilea seems to be a self-portrait."
                    "The more you go on, the better the drawings get."
                    "Eventually they turn into sceneries of places you recognize from old missions as well as maps of places the team has infiltrated. The Backwater operation is in here."
                    "It looks like its a typical map of the three story home, just like what leader showed diagrams of in the war room."
                    "What's different is a map of an unrecorded floor that seems to be the basement. There's enough detail for it to suggest someone's been there before, but this is Emson's journal?"
                    "...When had he been to the basement of the Maddox family home?"
                    "The last drawing takes up two full pages. It looks like it was done by six different hands, each of the members."
                    "They're self portraits. Some are better than others, but all of them are holding hands. You wonder how they got Elio to draw himself. It was probably Erix's doing."
                    "There's an empty space on the far right with a sticky note pressed into the page.\">:D\""
                    "You hear Emson's footsteps behind you."
                    spy "What are you doing?"
                    jump spy_turn_around

label spy_turn_around:
    menu:
        spy "That's my journal."
        "I was just waiting for you.":
            spy "Waiting? That doesn't excuse going through my things."
            spy "...Please. Just go."
            "You don't meet his eyes."
            spy "And don't tell anyone about whatever you saw."
            jump second_conversation_menu
        "I'm sorry for looking at your journal.":
            spy "Yeah, well, that doesn't erase the fact that you did."
            spy "...Please. Just go."
            "You don't meet his eyes."
            spy "And don't tell anyone about whatever you saw."
            jump second_conversation_menu

label i_dont_know_much_about_families:
    mc "I don't know much about people's families here."
    "He shrugs."
    spy "Some people are more comfortable talking about their families than others. It doesn't hurt to ask, in my opinion."
    mc "I suppose you're right."
    spy "Well, I gotta clean up these crackers. Bronx will have my head if I don't."
    spy "Bye!"
    mc "Bye."
    jump second_conversation_menu
# SPY SECOND CONVERSATION END

# WEAPON TECH SECOND CONVERSATION START
label weaptech_second_conversation:
    "You find both Erix and Elio in the workshop, but they're on separate sides of the room. Erix smiles at you and calls you over."
    weaptech "Hey! Come look at this!"
    menu:
        "The table in front of them has metal parts strewn across it."
        "What is it?":
            weaptech "It's a rocket launcher! Or...I suppose it was. Elio found it in the woods and brought it to me to tinker with. Isn't he sweet?"
            mc "Very sweet."
            weaptech "Yup. He's secretly a romantic. It's actually super well made. Reminds me of my own designs."
            jump reminds_me_of_my_own_designs
        "How... impressive.":
            "You don't even know what it is silly! It's a deconstructed rocket launcher. It's awfully complex, I admit. Reminds me of my own designs."
            jump reminds_me_of_my_own_designs

label reminds_me_of_my_own_designs:
    mc "How does it remind you of your designs?"
    weaptech "Well, its construction is very well thought out. You can tell by the trigger lock. It doesn't interfere with the main combustion chamber at all, meaning there's no way it could misfire or jam. That's a common issue in these models."
    mc "What if it is your design?"
    weaptech "Oh no, that's not possible. My designs always have a signature. Look closely."
    "They heft up a rifle that was underneath the table."
    weaptech "See? There's a little insignia right there. It's a snake."
    "It is a snake, curled up in a circle right in the trigger grip."
    mc "Why sign your work? They could trace it back to you."
    weaptech "They could, but I'm not worried."
    "They smile, but it seems there's a deeper meaning than you understand."
    weaptech "Besides, when you make a masterpiece. It's hard not to take credit."
    mc "What if someone steals your designs?"
    weaptech "Well, that would mean someone gave someone my designs or a sample weapon."
    "They smile again."
    weaptech "I wouldn't worry about that."
    "They make their way to another table before busying themself with another weapon. Something under the table in front of you catches your eye."
    "There's a metal box and at first glance. It just seems to be discarded guns. You look up at Erix to ask them what it is, but they're gone."
    menu:
        "Elio is still in the room."
        "\"Hey, Elio? What's this?\"":
            "He turns around."
            sniper "Those are confiscated weapons from past missions. I believe that box is specifically from street gangs."
            "Looking closer, you notice an engraving in the trigger lock."
            "A single curled snake."
            "As soon as you notice it, Erix walks back into the room."
            weaptech "Wanna see Ace? I had to go check my bedroom for a piece, but I think I figured out how to make him lighter to carry!"
            mc "Maybe next time."
            weaptech "Oh, shame. Well, see you!"
            jump second_conversation_menu
        "Leave the box alone.":
            "You slide the box back under the table and stand up to go. As you do, Erix walks in."
            weaptech "Leaving so soon? I wanted to show you Ace. I checked my bedroom for a piece, and found something that could make his carrying weight lighter!"
            mc "Maybe next time."
            weaptech "Oh, shame. Well, see you!"
            jump second_conversation_menu
# WEAPON TECH SECOND CONVERSATION END

# SNIPER SECOND CONVERSATION START
label sniper_second_conversation:
    menu:
        "You find both Erix and Elio in the workshop, but they're on separate sides of the room. Elio is quietly cleaning a pistol. You recognize it as Ace."
        "I didn't know you could use a handgun.":
            menu:
                sniper "I can use all manner of firearms."
                "What about knives?":
                    sniper "Those as well. In order to most efficiently protect the team, I can use any object as a weapon."
                    mc "Even your hands?"
                    sniper "My hands were the first thing I trained."
                    jump wow_whered_you_learn
                "What's your favorite gun?":
                    sniper "Why would I have a favorite gun?"
                    mc "Well, you use them so often."
                    sniper "Does that mean you have a favorite fork?"
                    mc "Noted."
                    "He blinks, then sighs."
                    sniper "I have been using guns for a long time. I do not form bonds with them like Erix does. I've been using them for...I believe it would be twelve years now."
                    jump wow_whered_you_learn
        "Still cleaning your guns, huh?":
            sniper "Yes, I am."
            mc "What's your favorite gun?"
            sniper "Why would I have a favorite gun?"
            mc "Well, you use them so often."
            sniper "Does that mean you have a favorite fork?"
            mc "Noted."
            "He blinks, then sighs."
            sniper "I have been using guns for a long time. I do not form bonds with them like Erix does. I've been using them for...I believe it would be twelve years now."
            jump wow_whered_you_learn
label wow_whered_you_learn:
    mc "Wow. Where'd you learn?"
    sniper "A government mandated training school."
    mc "You worked for the government?"
    sniper "Yes, but I soon realized their true goals. They only value the destination, not the ones who get them there."
    sniper "I felt their values were damaging to individual character."
    mc "You seem to have a pretty strong character."
    sniper "I didn't always, and I'm not sure I do even now."
    "He looks down at the gun part in his hand."
    sniper "I owe a lot to Erix for all they've done to make me strong, but some days I feel weak."
    mc "How so?"
    sniper "I cannot forget my time with the government completely."
    "He looks uncomfortable."
    sniper "Forgive me. I know talking about it disturbs others."
    mc "You can talk. I don't mind."
    sniper "I'm afraid it disturbs me as well. I want to continue cleaning."
    mc "Oh, alright."
    "He turns his back to you."
    jump second_conversation_menu
# SNIPER SECOND CONVERSATION END

# NEWBIE SECOND CONVERSATION START
label newbie_second_conversation:
    "You enter Kona's room, but don't find her anywhere."
    menu:
        "You do see a holo on her bed, on and flashing with images."
        "Inspect holo.":
            menu:
                "You pick up the holo. A video is playing on it, muted."
                "Watch video.":
                    "It's hard to understand without subtitles, but you recognize the woman that's on the screen."
                    "It appears to be a documentary about Maddox's family, including his daughter, Andrea. In the video, she's walking down the steps of the same home your team infiltrated, smiling brightly."
                    "The footage quickly flips to her in a government building, looking stern and cold."
                    jump newbie_hear_footsteps_from_hallway
                "Unmute video.":
                    "You unmute the video and recognize the woman on the screen."
                    "It appears to be a documentary about Maddox's family, including his daughter, Andrea. In the video, she's walking down the steps of the same home your team infiltrated, smiling brightly."
                    "\"—by all, Andrea Maddox charms the hearts of every politician she meets. Not many can say they've heard a negative thing about her, besides the fact she hasn't followed in her father's footsteps.\""
                    "The footage quickly flips to her in a government building looking stern and cold."
                    "\"Notorious for her adversion to the political scene, Andrea rarely steps foot in her father's office for anything besides a friendly lunch. However, she has been known to share her opinions on recent developments in cybernetics firms such as—\""
                    jump newbie_hear_footsteps_from_hallway
        "Search for Kona.":
            "You take a peek in her bathroom, wondering if she could be there. Not a second later, Kona walks in with a water bottle in hand."
            newbie "Oh, hi. What're you doing here?"
            "Her eyes fall to her bed where the holo lays, still on. She darts down to shut it off."
            "You pretend you never noticed it."
            jump newbie_i_was_looking_for_you

label newbie_hear_footsteps_from_hallway:
    menu:
        "From the hallway, you hear footsteps."
        "Drop the holo.":
            "You drop the holo like it burned you, quickly stepping away from the bed. Kona walks in a second later, water bottle in hand."
            newbie "Oh, hi. What're you doing here?"
            "Her eyes drift down to her holo and she stiffens, snatching it up and switching it off."
            jump newbie_i_was_looking_for_you
        "Look up.":
            "Kona walks in a second later, water bottle in hand."
            newbie "Oh, hi. What're you doing here?"
            menu:
                "Her eyes drift down to her holo and she stiffens, snatching it up and switching it off."
                "What are you watching?":
                    newbie "Oh, I just wanted to get to know Maddox's family. It probably would've been smarter to do that before the mission, but better late than never right?"
                    mc "Right."
                    "Kona looks uncomfortable."
                    newbie "Why are you in my room?"
                    jump newbie_i_was_looking_for_you
                "You seem to want to get to know this woman.":
                    newbie "No! No, I just want to know who I might be dealing with, you know since she saw my face in all..."
                    mc "Right."
                    "Kona looks uncomfortable."
                    newbie "Why are you in my room?"
                    jump newbie_i_was_looking_for_you

label newbie_i_was_looking_for_you:
    mc "I was looking for you."
    menu:
        newbie "Uh, then how can I help you?"
        "I think Bronx was a little harsh.":
            newbie "Oh...he didn't say anything incorrect though."
            mc "Maybe, but Andrea could be useful."
            newbie "How so?"
            mc "She's bound to know things."
            newbie "I—I don't know if I'm comfortable using someone like that."
            mc "You don't know her though."
            "She doesn't say anything for a bit."
            newbie "Could you get out of my room, please? I'd like to be alone."
            mc "Oh. Goodbye then?"
            jump second_conversation_menu
        "Tell me about why you joined the rebellion.":
            newbie "I wanted to do good. My family has been taken advantage of by the government since I was little. I want to make life better for them."
            mc "I know you can do it."
            newbie "Yeah, I don't know how long after the mistake I made during Backwater. I shouldn't have spoken to Andrea."
            mc "Maybe, but Andrea could be useful."
            newbie "How so?"
            mc "She's bound to know things."
            newbie "I—I don't know if I'm comfortable using someone like that."
            mc "You don't know her though."
            "She doesn't say anything for a bit."
            newbie "Could you get out of my room, please? I'd like to be alone."
            mc "Oh. Goodbye then?"
            jump second_conversation_menu
# NEWBIE SECOND CONVERSATION END

# LEADER SECOND CONVERSATION START
label leader_second_conversation:
    "Everyone leaves the war room, but you return to talk to Bronx. He's not there, but Emson is. You don't know when he got here, but he's passed out, head to tabletop. Saltine crumbs surround him."
    "You notice the drone Bronx was flying by his seat under the table. It's connected to a laptop, where he was reviewing the recording he made. Eyeing Emson, you don't think he'll be waking up anytime soon."
    "It looks like it was edited to be the most important parts. The whole thing is mostly the top of Maddox's house. It's flying high enough to not be audible or visible."
    menu:
        "Speaking of audio, the drone didn't record sound, so the video is silent."
        "What's that moving?":
            "Looking closer, it's a man. A guard."
            "He's walking to the edge of the property and just standing there. The camera zooms in so close you can see his shoulders shaking from the cold."
            "He stands there for a minute, and because it's zoomed in so close you can see something fall from his hand before he turns around and walks back to the property."
            "The video zooms out to catch him walking away, but then refocuses on the ground he was standing on before he left. You can tell Bronx was looking for the thing he dropped."
            "After a second, the drone flies off in the direction you know the van was in and the video ends."
            "That's an odd ending."
            jump second_conversation_menu
        "Where is everyone?":
            "Looking closely, you can see the hills Elio was postitioned on. The drone keeps turning back to a certain section of the hill line, so you guess he's in that area."
            "You can see Emson enter the house early on in the night, walking in with the rest of the guests."
            "Erix and Kona are sneaking in through a window long after Emson gets to talking with Jege."
            "The guards seem to be going along with their shifts, changing every ten minutes and patroling the lawn of the home."
            "Everything moves like clockwork, except for one. A single guard moves to the far edge of the property."
            "He's walking to the edge of the woods and just standing there. The camera zooms in so close you can see his shoulders shaking from the cold."
            "He stands there for a minute, and because it's zoomed in so close you can see something fall from his hand before he turns around and walks back to the property."
            "The video zooms out to catch him walking away, but then refocuses on the ground he was standing on before he left. You can tell Bronx was looking for the thing he dropped."
            "After a second, the drone flies off in the direction you know the van was in and the video ends."
            "That's an odd ending."
            jump second_conversation_menu
# LEADER SECOND CONVERSATION END

# FIGHT START
label fight_in_workshop:
    "You hear yelling coming from the workshop."
    "Walking in, you see Erix, Elio, Lilea, and Bronx standing around the main table."
    weaptech "The fact of the matter is we don't have the drive! There's nothing we can do about it!"
    hacker "We could go back for it! There's nothing stopping us from running the mission again, we could just—"
    sniper "It's too risky. You know we never hit the same place twice."
    leader "Elio is right. We can't risk being caught when we barely made it out the first time."
    hacker "That's an exaggeration. We were fine—"
    leader "No, Lilea! I won't risk this team for a drive I—"
    "He stops suddenly."
    "The other three think he stopped for some other reason, but you can tell it's because he almost said something he didn't mean to."
    "Erix looks around and sees you in the doorway. They give you a smile."
    weaptech "Oh, hey. Sorry if we disturbed you. We were just talking."
    "You get the feeling that was a dismissal."
    "Lilea sighs and brushes past you, Bronx following a second after he collects himself."
    "When you look at Erix, they're turned around and fiddling with a scrap of metal at another bench."
    "Elio just stands there looking at the table."
# FIGHT END

label third_conversation_menu:
    $ talkedToHacker3 = False
    $ talkedToSpy3 = False
    $ talkedToWeapTech3 = False
    $ talkedToSniper3 = False
    $ talkedToNewbie3 = False
    $ talkedToLeader3 = False
    $ hackerTippedOff = False
    $ numPeopleTalkedTo = 0

    menu:
        "You have time to talk to three people after the mission briefing."
        "Lilea." if talkedToHacker3 == False and numPeopleTalkedTo < 3:
            $ talkedToHacker3 = True
            $ numPeopleTalkedTo += 1
            jump hacker_third_conversation
        "Emson." if talkedToSpy3 == False and numPeopleTalkedTo < 3:
            $ talkedToSpy3 = True
            $ numPeopleTalkedTo += 1
            jump spy_third_conversation
        "Erix." if talkedToWeapTech3 == False and numPeopleTalkedTo < 3:
            $ talkedToWeapTech3 = True
            $ numPeopleTalkedTo += 1
            jump weaptech_third_conversation
        "Elio." if talkedToSniper3 == False and numPeopleTalkedTo < 3:
            $ talkedToSniper3 = True
            $ numPeopleTalkedTo += 1
            jump sniper_third_conversation
        "Kona." if talkedToNewbie3 == False and numPeopleTalkedTo < 3:
            $ talkedToNewbie3 = True
            $ numPeopleTalkedTo += 1
            jump newbie_third_conversation
        "Bronx." if talkedToLeader3 == False and numPeopleTalkedTo < 3:
            $ talkedToLeader3 = True
            $ numPeopleTalkedTo += 1
            jump leader_third_conversation
        "You're out of time." if numPeopleTalkedTo == 3 and hackerTippedOff:
            jump mole_finds_you
        "You're out of time." if numPeopleTalkedTo == 3 and hackerTippedOff == False:
            jump time_to_choose

# HACKER THIRD CONVERSATION START
label hacker_third_conversation:
    "You walk into Lilea's room, calling her name. You get no answer."
    menu:
        "On her desk, you see folders spread open and abandoned. A shelf nearby also looks disturbed, papers knocked out of a box and laying on the ground."
        "Pick up folders on the desk":
            "You make your way to her desk in hopes of tidying it up for her. The papers are mostly sciencey stuff you don't understand, but some look like chat logs."
            "user403: Why didn't they get the drive\nuser983: i told you, its not my fault\nuser983: i did everything i could to make sure they got it"
            "user403: You still failed\nuser403: How are you going to install the program now?\nuser403: That thumbdrive was supposed to be your scapegoat so you could download the program without them suspecting you"
            "user983: relax relax im trying to convince them to go back for it\nuser403: Don't bother, I had one of my guards drop the drive on the edge of the property and it's not there now"
            "user983: are you saying its in the base?\nuser403: That's exactly what I'm saying\nuser403: now find it and install it\nuser983: I'm going"
            hacker "What are you doing at my desk?"
            "You turn around and see Lilea there."
            mc "I was just cleaning it up a little."
            hacker "I didn't ask you to do that. Please go."
            "You drop the papers and make your way out."
            jump third_conversation_menu
        "Pick up papers on the floor":
            "You crouch down to gather the papers and see they're mostly computer things you dont understand. Some of them look to be chat logs though."
            "user403: Why didn't they get the drive\nuser983: i told you, its not my fault\nuser983: i did everything i could to make sure they got it"
            "user403: You still failed\nuser403: How are you going to install the program now?\nuser403: That thumbdrive was supposed to be your scapegoat so you could download the program without them suspecting you"
            "user983: relax relax im trying to convince them to go back for it\nuser403: Don't bother, I had one of my guards drop the drive on the edge of the property and it's not there now"
            "user983: are you saying its in the base?\nuser403: That's exactly what I'm saying\nuser403: now find it and install it\nuser983: I'm going"
            hacker "What are you doing at my desk?"
            "You turn around and see Lilea there."
            mc "These papers were on the ground. I was picking them up."
            hacker "Oh haha. Yeah, there's a lot of mess here. I print every file on my computer. No back up like paper, huh?"
            "It seems wasteful and unnecessary to you, but then again you're not the computer guy. She walks forward to collect them for you and you shuffle the paper you were reading under some stray calculations."
            mc "Yeah, I don't know anything about these."
            hacker "Sometimes they don't make sense to me! Anyway, I should probably clean up my desk too. Hehe, see you!"
            mc "See you, Lilea."
            jump third_conversation_menu
# HACKER THIRD CONVERSATION END

# SPY THIRD CONVERSATION START
label spy_third_conversation:
    "You find Emson going through his outfits."
    menu:
        spy "Oh, hello there. I'm just organizing my clothes. Want to help?"
        "Sure.":
            "He smiled and hands you a disguise."
            spy "Fold this and place this on the far table. Do the same with this entire pile."
            "You begin to work, Emson humming quietly."
            jump spy_why_do_you_hate_the_government
        "I actually wanted to ask you something that was bothering me.":
            "His face gets nervous, before he plasters on a smile. Ever the charmer."
            spy "Yeah, of course. What's on your mind?"
            jump spy_why_do_you_hate_the_government

label spy_why_do_you_hate_the_government:
    mc "Why do you hate the government?"
    "He pauses and looks at you carefully. He lets out a heavy sigh and sits down on the fainting couch."
    spy "You want to know that bad, huh? Well, I guess I'll tell you if you're that curious."
    "He gathers himself for a second, then begins speaking."
    spy "My mom used to work for the government. I'm talking high level access kind of work. She was at the top of the cybernetics division and knew everything about what they were doing. You wouldn't believe how much money is pooled into just that branch alone."
    mc "What exactly is cybernetics?"
    spy "It's basically putting a computer in a person, be it to make them smarter, stronger, or sneakier. Well, my mom thought it was all to improve people who were hurt, people who lost limbs or have any sort of disability."
    spy "Turns out that wasn't what the government was doing the research for."
    mc "They wanted to make soldiers."
    spy "Exactly. I don't have to explain how bad that could be for us. When my mom found out, she tried to tell the people. She got into a car crash a week later."
    mc "It wasn't actually a car crash, was it?"
    spy "No, it wasn't. Because of them, I lost my best friend. I'm going to do everything in my power to tell the people what my mom couldn't. I won't rest until they know the truth."
    mc "We're here to help you."
    spy "Thank you. I know I can trust my family. I know I can trust you."
    "He looks down at the garment he's folding."
    spy "You can go if you want. It was nice to have some company, but I kinda want to cry."
    mc "I'll leave you be."
    jump third_conversation_menu
# SPY THIRD CONVERSATION END

# WEAPONS TECH THIRD CONVERSATION START
label weaptech_third_conversation:
    "Erix is standing in their workshop, silently moving boxes around. When you get close enough, they look up and offer a small smile."
    menu:
        weaptech "Good timing. I was wanting to talk to you."
        "What did you want to talk about?":
            jump you_think_they_were_stolen
        "I was too.":
            weaptech "Oh. I'm sure what you want to say is important, but I really need to tell you this. Can I go first?"
            mc "Go ahead."
            jump you_think_they_were_stolen

label you_think_they_were_stolen:
    weaptech "Well, I've been thinking about my designs..."
    weaptech "I've been thinking about if someone stole them."
    mc "You think they were stolen?"
    weaptech "No, they weren't."
    "They gesture to a box they just moved."
    weaptech "All my designs have a snake insignia."
    "They point to a curled snake stamped on a revolver."
    weaptech "This is a box of confiscated weapons. Whatever Elio or Kona or whomever finds during missions. They collect them for me to tinker with and this box is all from a street gang, the Rattlesnakes."
    mc "The Rattlesnakes?"
    weaptech "Yeah, stupid name. I know, but they were my old gang."
    mc "You were in a street gang?"
    weaptech "Yeah. Before I joined the rebellion, I worked with them to stay alive. It's where I met Elio."
    mc "Elio?"
    weaptech "Yeah, but that's his story to tell. I just wanted to be honest with you. Elio already knows, but I was gonna tell the rest of the team at our next mission."
    weaptech "I just ran into you first and can tell you wouldn't judge me too hard."
    mc "No one will think of you differently."
    weaptech "Oh, thank you. Well, I gotta upcycle a machine gun Lilea found in a dumpster last week. Thanks for being understanding."
    mc "Anytime."
    jump third_conversation_menu
# WEAPONS TECH THIRD CONVERSATION END

# SNIPER THIRD CONVERSATION START
label sniper_third_conversation:
    "Elio stands at a table in the workshop silently. Erix is by themself, working on something you can't see."
    "When you approach him, Elio's head snaps up."
    sniper "I want to be honest."
    mc "Are you being dishonest?"
    "He considers the question."
    menu:
        sniper "I believe I'm lying by omission. I would like to share my past with you."
        "I'm listening.":
            jump sniper_tells_you_his_past
        "You don't have to.":
            "He shakes his head."
            sniper "No, this is a part of me I would like you to know."
            mc "Alright."
            jump sniper_tells_you_his_past

label sniper_tells_you_his_past:
    sniper "Before I came to the rebellion, I was part of a steet gang. They were called the Rattlesnakes. It was there that I met Erix."
    mc "Erix?"
    sniper "Yes, but that's not my story to tell."
    mc "Why were you in a gang?"
    sniper "Working for the government was not kind. They taught me how to be a weapon."
    mc "A weapon?"
    sniper "Yes, and it was the gang who taught me how to be a person."
    sniper "I'm glad I left though, because it was this team who taught me how to be a family."
    mc "Thank you for telling me."
    sniper "Don't thank me. It was a selfish action. The guilt was making me feel bad and I knew telling you the truth would stop the feeling."
    mc "It's okay, buddy."
    sniper "Buddy? I don't like that name."
    "He pauses and checks his watch."
    sniper "This is usually the time I clean my scopes. I can't be late."
    mc "Bye?"
    "He doesn't respond."
    jump third_conversation_menu
# SNIPER THIRD CONVERSATION END

# NEWBIE THIRD CONVERSATION START
label newbie_third_conversation:
    "You find Kona standing in her room with a bowl of cereal. You don't know where she got the cereal, or why she's standing. She nods in greeting when you look at her."
    mc "I need you to explain your thing with Andrea."
    newbie "I don't know her if that's what you think. That time was our first meeting."
    "She sets her bowl down on her bed precariously."
    menu:
        newbie "She was nice to me, okay?"
        "What do you mean 'nice'?":
            newbie "I thought she would be mean. She's the daughter of Flint Maddox for goodness' sakes! I was expecting to be dead the second I looked at her, but no. She just made conversation with me."
            jump so_you_just_want_a_friend
        "Are people usually not nice to you?":
            newbie "I mean, I have had trouble with making connections with people in the past. Besides the First Squadron, Andrea was the nicest stranger I've ever spoken to."
            jump so_you_just_want_a_friend

label so_you_just_want_a_friend:
    mc "So... you just want a friend?"
    newbie "No! I mean, yeah, I like friends... but you make it sound like I don't have any. She just wasn't what I expected."
    newbie "I've been looking her up, and she's nothing like the rest of those government types. In fact, she seems to hate the government!"
    mc "That sounds too good to be true."
    newbie "Maybe, but I trust her. I've just met her, but I trust her. I think she could be a strong ally if we talk to her."
    mc "Bronx might consider it."
    newbie "I'm gonna ask him about it. I feel it. Andrea could really help!"
    mc "You better be making the right choice."
    newbie "I am! I bet my life on this woman!"
    "She grabs you in a tight hug for a moment, and then races out the door."
    jump third_conversation_menu
# NEWBIE THIRD CONVERSATION END

# LEADER THIRD CONVERSATION START
label leader_third_conversation:
    "You find Bronx in the hallway outside the war room. He seems frozen at the door."
    mc "Bronx?"
    menu:
        leader "I need to tell you something mc."
        "Is everything okay?":
            jump i_have_the_thumbdrive
        "Why are you standing here alone?":
            jump i_have_the_thumbdrive

label i_have_the_thumbdrive:
    leader "I have the thumbdrive."
    mc "You do? Why didn't you tell us?"
    leader "It seemed... off. I found it in the woods."
    mc "The woods?"
    leader "Yes, just inside the property. I saw a guard drop something with my drone during the mission, and it seemed so off I had to investigate."
    leader "I went to where he was standing right outside the woods and there it was. The drive was just lying there in the dirt. I didn't tell anyone because it didn't seem right... almost like they wanted us to find it."
    leader "I thought it might be a trap."
    mc "You think the mole set it up."
    leader "Think about it. One of the few missions we don't get info on, suddenly the objective gets left for us as we retreat? It's too suspicious."
    mc "Why don't you look at the drive?"
    leader "What if it has a tracking software on it? If this is from the enemy, we can't trust it."
    leader "I need time to think. Keep investigating."
    jump third_conversation_menu
# LEADER THIRD CONVERSATION END

# MOLE TIPPED OFF ENDING START
label mole_finds_you:
    "You walk through the hallway and as you pass by Lilea, she stops you."
    hacker "Hey uh, Bronx said he was calling a meeting? He sounded serious. He said to meet him in Erix's workshop."
    mc "Oh, gotcha."
    "You walk to the workshop together, but when you enter, the room is empty. You turn around to ask her where everyone is and see a flash of green as she lunges at you."
    "Your vision goes black."
    "..."
    "Consciousness comes back slowly and the first thing you notice is the cold ground."
    "You're lying on the war room floor next to Erix and Emson. They're out cold and have their hands restrained behind them like you."
    "Above you, Elio and Kona are being held by two men in black armor each. Both are struggling, also restrained, and near growling."
    "Bronx is sat in a chair, face frozen in an impassive mask. His hands are free but he is every bit the prisoner the others are. Lilea stands against the far wall, frowning."
    "From the doorway, you hear a voice."
    "Voice" "Ah, you woke up earlier than I thought you would."
    "The man behind you is also wearing armor, but he doesn't have a weapon. You recognize him as Flint Maddox."
    "Maddox" "I wanted to personally apprehend the people who invaded my home, even if the mission was planned out by Lilea and I here ourselves."
    "Lilea looks the other direction."
    "Maddox" "She contacted me after she realized you were onto her and I couldn't leave my little spy to get caught now could I?"
    "Maddox" "We were originally going to wait before we raided your base, but plans change I suppose. I was worried because you almost didn't get the drive I had Jege cook up for you, the First Squadron would slip away."
    "He smiles coldly."
    "Maddox" "Anyway, I'm please to announce none of you will be seeing anything but four brick walls for a long, long time."
    return
# MOLE TIPPED OFF ENDING END

# TURN IN THE MOLE ENDING START
label time_to_choose:
    "You walk through the hallway and as you pass by Lilea, she stops you."
    hacker "Hey uh, Bronx said he was calling a meeting? He sounded serious. He said to meet him in the war room."
    "Oh, thank you Lilea."
    "She smiles and together, you both walk to the meeting."
    "When you make it to the war room, Bronx is there. Everyone is gathered around the table again and Bronx's face says it all."
    leader "We're out of time. What have you come up with?"
    spy "What's Bronx talking about?"
    hacker "Are you up to something sneaky?"
    mc "What do you mean 'we're out of time'?"
    leader "I've gotten word from an ally that the nearest government outpost is on the move and they're headed here. I've already set up the mobilization process, but we have no more than half an hour to clear this up."
    leader "Now, who is the mole?"
    "The room bursts into outrage and confusion."
    weaptech "A mole?"
    newbie "You're saying you think one of us is a spy?"
    menu:
        "Bronx is looking at you. It's time to choose."
        "It's Lilea.":
            "Lilea freezes."
            hacker "What... how? I—"
            leader "Is it true, Lilea? Are you a spy for the government?"
            "She stiffens, then suddenly bolts for the door."
            "Elio is faster though. He grabs her by the sholders, pushing her down into a seat. He stands behind her silently."
            spy "Are you serious? Are you actually a snitch?"
            weaptech "Lea... why?"
            hacker "It's not as simple as 'good' or 'bad'. Sometimes there's a gray area, you know."
            newbie "What's worth it enough to make you switch sides completely?"
            hacker "Family."
            sniper "Are we not also your family?"
            leader "It doesn't matter now. We have to go. Elio, Kona, restrain her. We're going to the safe house. There, Lilea will have no contact with technology of any kind."
            leader "Get your go bags. You have five minutes."
            "As they pass Lilea, the team lets their eyes linger on her."
            "After getting your bag, you meet up with the team. Lilea's hands are pulled behind her with rope. Everyone avoids looking at her."
            "In the next fifteen minutes, government officers flood the halls, clearing rooms and searching for your team, but you are long gone."
            return
        "It's Emson.":
            "His jaw drops."
            spy "Me? You think I'm with those rats? How? Everything I do is for the rebellion!"
            leader "You're certain it's Emson? I trust you, but we need to be 100 percent sure before we deal with this."
            spy "Deal with me?"
            "You look at everyones faces, trying to put the pieces together in your head, but a face is missing."
            jump whos_missing
        "It's Erix.":
            weaptech "You think I'm a mole?"
            sniper "Be careful in who you accuse of betrayal. Erix is the most honest person in this room—"
            weaptech "No, I can speak for myself. You do not think that I'd betray you all like that. You are all my family."
            leader "You're certain it's Erix? I trust you, but we need to be 100 percent sure before we deal with this."
            "Elip slips his hand into Erix's."
            "You look at everyones faces, trying to put the pieces together in your head, but a face is missing."
            jump whos_missing
        "It's Elio.":
            sniper "How could I be a mole? I risk my life for this team daily. I would die for everyone here."
            "Everyone looks uncomfortable, except for Erix. They look murderous."
            leader "You're certain it's Elio? I trust you, but we need to be 100 percent sure before we deal with this."
            "Elio straightens his spine, like he's preparing for an attack."
            "You look at everyones faces, trying to put the pieces together in your head, but a face is missing."
            jump whos_missing
        "It's Kona.":
            newbie "What? No, no! Is this because of Andrea? No, she''s not anything to me. I just met her once I—"
            spy "It's alright, Kona. It's okay."
            leader "You're certain it's Kona? I trust you, but we need to be 100 percent sure before we deal with this."
            "Kona's face goes pale"
            "You look at everyones faces, trying to put the pieces together in your head, but a face is missing."
            jump whos_missing
        "It's Bronx":
            "His face tightens and he shoots to his feet."
            leader "Me? You think it's me? I gave you how long and this is what you come up with?"
            leader "I was the one who GAVE you this mission. If I were the mole, why would I let you know a mole exists?"
            leader "Don't you have anything else?"
            "You look at everyones faces, trying to put the pieces together in your head, but a face is missing."
            jump whos_missing

label whos_missing:
    newbie "Hey, where'd Lilea go?"
    "Bronx and you make eye contact. His gaze is sharp. 'It's Lilea.'"
    "Immediately, everyone in the room takes off down the hallway to search for the missing woman. Everyone branches in different directions. You run for her room."
    "She's not there, but one of her monitors is on. It shows a pop up: \"MESSAGE SENT\". You don't have to guess who the message was for."
    "You dart out of the room to find someone to warn, running for the war room. When you push the door open, you're greeted by the image of Erix and Emson knocked out on the ground, their hands are pulled behind their backs with rope."
    "Elio and Kona are being held by two men in black armor each. Both are struggling, also restrained, and near growling."
    "Bronx is sat in a chair, face frozen in an impassive mask. His hands are free but he is every bit the prisoner the others are. Lilea stands against the far wall, frowning. Behind you, you hear a voice."
    "Voice" "Ah, the last one. I'm glad we didn't have to look too hard."
    "The man behind you is also wearing armor, but he doesn't have a weapon. You recognize him as Flint Maddox."
    "Maddox" "I wanted to personally apprehend the people who invaded my home, even if the mission was planned out by Lilea and I here ourselves."
    "Lilea looks the other way as hands grab your arms from behind you."
    "Maddox" "Well, thank you mc, for making such a big mistake. It's because of you suspecting the wrong person that the real mole was able to alert us of your base's exact position."
    "Maddox" "I was worried because you almost didn't get the drive I had Jege cook up for you, the First Squadron would slip away."
    "He smiles coldly."
    "Maddox" "Anyway, I'm please to announce none of you will be seeing anything but four brick walls for a long, long time."
    return
# TURN IN THE MOLE ENDING END