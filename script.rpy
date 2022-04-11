default strength = 0
default luck = 0
default intellect = 0
default money = 0
default daisy = 0
default lotion = 0
default coughDrop = 0
default earmuffs = 0
define jeff = Character("Jeff")
define merchant = Character("Merchant Molluck")
label start:
    scene forest1
    pause
    jeff "Hello detective. Thank you for meeting me. Your services have come highly recommended."
    $ you = renpy.input("What should I call you?")
    if you == "":
        jeff "I am just going to call you Peanut"
        $ you = Character("Peanut")

    jeff "Nice to put a name to the face, [you]"
    jeff"Look [you], the surrounding villages are in unrest. As the villages expand, the more upset the fifels have become..."
    you "What the heck is fifel?! I only assist in matters involving mosters, villians, and bad hygiene."
    jeff"My bad, yes, we call them fifel. They are big, ugly, and have been harrassing our villagers and hurting our expansion efforts!"
    menu:
        "What do you want from me Jeff?":
            jeff "Get rid of them by any means necessary!"
        "What is in it for me?":
            jeff "Riches upon riches upon riches."
    you "Alright, tell me where these falafels are"
    jeff "It..uh...its pronounced, Fi-fel-s sir..."
    you "Enough of these games, where are your problem areas?"
    jeff "Where arent the problem areas? May I suggest stopping by the marketplace to pick up supplies, here is a 7 bucks to get you started?"
    menu:
        "Go to the merchant first for supplies?":
            $ money += 7
            jump market
        "Why do I need to go to get supplies?":
            jeff "Look, with all of these fife...I mean monsters running around, you are going to need all the help you can get.
            here is 7 bucks to get you started"
            $ money += 7
            jump market

label market:
    scene merchant   #need to fix this picture or get a new one. adjust lines26
    pause
    merchant "Well hello stranger! What can I do for you on this brisk night?!"

    menu:
        "What do you have to offer?":
            merchant "I got all kind o' stuff, anything you need! I got some of those there personal care items for travellers such as yourself and some special enhancements to protect you from danger"
            jump sellitem
        "Have you seen any suspicious creatures lerking around?":
            merchant "Yes'um I seen some creatures, never bothered my they have. Some folks get spooked pretty easy in these parts, but I never had no trouble! You ask me, just leave em' alone they wont bother with ya."
            jump sellitem
label sellitem:
    merchant "So how about you take a look at what I got! What are you interested in?"
    menu:
        "Attributes (5)":
            jump attributes
        "Personal Items (1)":
            jump items
        "Not interested in buying anything":
            jump firstmonster
label attributes:
    if money >= 5:
        menu:
            "Strength":
                $ strength+= 1
                $ money= money - 5
                "Your strength has increased by one"
                #jump checkmoneyattribute
            "Intellect":
                $ intellect += 1
                $ money= money - 5
                "Your intellect has increased by one"
                #jump checkmoneyattribute
            "Luck":
                $ luck+= 1
                $ money = money - 5
                "Your luck has increased by one"
        call checkmoneyattribute
label items:
    if money > 0:
        menu:
            "Daisy":
                merchant "You never know when a daisy will come in hand, good choice sir"
                $ daisy+= 1
                $ money = money - 1
                "Your daisy inventory has increased."
                #jump checkmoneyitem
            "Cough Drop":
                merchant "You ever had a cough so bad you gone lost your voice box? Lemme tell you, nothins worse than a sore throat"
                $ coughDrop+= 1
                $ money = money - 1
                "Your cough drop inventory has increased by one"
                #jump checkmoneyitem
            "Lotion":
                merchant "Good, you look like you could use some lotion, no offense"
                $ lotion+= 1
                $ money = money - 1
                "Your lotion inventory has increased by one"
            "Ear Muffs":
                "I have been selling out of these lately for some reason"
                $ earmuffs += 1
                $ money = (money - 1)
                "Your ear muff inventory has increased by one"
        call checkmoneyitem
label checkmoneyattribute:
    if money < 5:
        "You do not have enough money to upgrade your attribute"
    jump sellitem
label checkmoneyitem:
    if money == 0:
        "You have abosolutely no money"
    jump sellitem
label firstmonster:
    scene forest1
    jeff "You are finally back! We must hurry over to the  village of Bandlewood. A banchee has been terroizing the citizens for two days now, they had to put ear muffs on to stop the constant screeching. The problem is that now the citizens keeping missing their alarm clocks for work because their ears are covered!"
    menu:
        "Thats odd behavior for a banchee.":
            jeff "I agree. Regardless, I can't have that think disrupting the citizens work lives. It needs to go"
        "Has anyone died?":
            jeff "No, no one has died. But they are all suffering from a terrible cold that set in right around when the banchee started harassing villagers"
    scene villagebanchee
    pause
    jeff "I think I hear it coming, put on some earmuffs if you got them!!!!!!!!"
    "Just like a bug flying past your ear, the screaming coming from over the hill grew louder and louder, vibrating [you]'s and Jeff's eardrums."
    show banshee
    pause
    "As you watched her fly past screaming, you noticed something. The banshee's voice was raw and cracked, it was grasping at its throat. Then it hit you."


    #show screen inventory


     #We have lived in peace for hundreds of years, but recently there has been unrest"

return


#ctrl + s = save
#shift + r = run game
