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
    mc "What does this have to do with me?"
    leader "I've suspected for a while, but I think there's a mole in the First Squadron."
    "You look at him sharply."
    mc "A mole?"
    leader "Yes. I won't go into the whole history, but there's been too many coincidences. I'm sure of it and as this team's leader, I need to protect them."
    leader "Even if it's from themselves."
    mc "Who could it be?"
    leader "Anyone in the First. This squadron has the highest clearance of all the Rebellion, so the mole can do some real damage."
    "Meet the members."
    "Lilea, Hacker" "Computer expert, inventor, caffiene addict"
    "Emson, Spy" "Charmer, socialite, excellent conversationalist"
    "Erix, Weapons Technician"
    "Inventor, mechanic, proud guardian of 40+ pistols"
    "Elio, Sniper"
    "Trained marksmen, soldier, tall drink of water"
    "Kona, Newbie"
    "Jack of all trades, first line of defense, unofficial team toddler"
    "Bronx, Leader"
    "Veteran, strategist, unofficial team dad"
    jump initial_conversation_menu
# BRONX EXPOSITION END
    return

label initial_conversation_menu:
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
    menu:
        "The room is dark, metal shelves creating a maze you can't imagine navigating. The bare walls make the clutter stand out more."
        "Cardboard boxes and stray papers line the shelves. You can see wires sticking out of random stacks."
        "A desk is on the far side of the room with a computer sitting idle."
        "Find Lilea.":
            "Listening closely, you can hear noises. It sounds like it's coming from inside the shelf maze."
            "You walk into the maze, following the mysterious noises. The source seems to be coming from a shelf pressed against a wall."
            menu:
                "You don't know how, but Lilea is trapped in between the shelf and wall."
                "What are you doing?":
                    "She startles, craning her neck to look at you."
                    menu:
                        hacker "I'm trying to find something I dropped. Thought I could find it, but it's kinda dark back here."
                        "Thats the problem here?":
                            "Lilea looks at you, confused."
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
                "You can see a figure behind a shelf."
                "Who are you?":
                    "Voice" "You sound familiar... do I know you? I'm Lilea!"
                    "Oh, there she is."
                    mc "It's me."
                    jump its_me
                "It's me.":
                    jump its_me

label its_me:
    hacker "Oh mc! It's good you're there. I may or may not be stuck."
    "You notice now that the figure is contorted in between the shelf and a wall."
    menu:
        "Poor Lilea."
        "How did you get back there?":
            jump how_did_you_get_back_there
        "Do you want help?":
            jump hacker_do_you_want_help

label how_did_you_get_back_there:
    jump placeholder

label hacker_do_you_want_help:
    hacker "Sure! I could use some light. Go get my flashlight under my desk."
    "Her desk is messy, with lots of folders, wires, and drawings spread across it."
    "Belatedly, you notice there are at least three working monitors, with several smashed ones in the corner of the room."
    "Instead of a rolling chair, a lawn chair with a cold cup of coffee in the cupholder."
    "You see the flashlight under the desk, along with a stray sock."
    hacker "Nice! Could you shine the light over me?"
    "You click on the flashlight, illuminating Lilea."
    hacker "Thanks, now I see it."
    mc "What did you lose?"
    "She extracts herself from the shelf, knocking over several boxes. In the process, even more wires and papers fall out of the boxes."
    hacker "My stress ball! I chucked it at the wall last night, you know... after Backwater."
    mc "Ah, I see."
    hacker "Yeah, it was kind of a mess."
    mc "What were you doing during Backwater, Lilea?"
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
                    "Erix wipes her hands on a rag."
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