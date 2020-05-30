# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define hacker = Character("Lilea")
define mc = Character("You")
define leader = Character("Bronx")


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
            "spy":
                jump placeholder
            "weapons tech":
                jump placeholder
            "sniper":
                jump placeholder
            "newbie":
                jump placeholder
            "leader":
                jump placeholder

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
                    jump placeholder
        "snoop around":
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

label placeholder:
    "has not been written"

label maybe_i_should_go_talk_to_them:
    hacker "oh, if youre going to yell at them, theres no point, it wont solve anything"
    jump im_sure_newbie_has_their_own_side_to_the_story

label im_sure_newbie_has_their_own_side_to_the_story:
    mc "i'm sure newbie has their own side to the story"
    hacker "right, well, now that i have my stress ball i can get back to stressing!\ni've got some schematics to look at, without that thumbdrive, we lost a lot of valuable information, gotta be double on top of everything"
    mc "well bye"
    jump initial_conversation_menu
    