default strength = 0
default luck = 0
default intellect = 0
default money = 0
default daisy = 0
default lotion = 0
default coughDrop = 0
default earmuffs = 0
default checkflower = 0
default checkmuff = 0
default village_roll = 0
default your_roll = 0
define jeff = Character("Jeff", image = "jeff", who_color = "#ffcc00", what_prefix = '"', what_suffix ='"')
image side jeff = "jeff"
define jeff2 = Character("Jeff", image = "bezos", who_color = "#ffcc00", what_prefix = '"', what_suffix ='"')
image side jeff2 = "bezos"
define merchant = Character("Merchant Molluck", image = "molluck", who_color = "#0020FF", what_prefix = '"', what_suffix ='"')
image side molluck= "molluck"
define goll = Character("Gollum", image = "minigol", who_color="#90554D", what_prefix = '"', what_suffix ='"') #https://www.pngaaa.com/download/2454929
image side goll = "minigol"
define villageB = Character("Bandlewood Villagers", color = "#10FF10", what_prefix = '"', what_suffix ='"')
define merchant2 = Character("Mistress Hilda", image = "faceold", color = "#ffa07a", what_prefix = '"', what_suffix ='"')
image side faceold = "faceold"
define creature = Character("Shrill", image = "monster1", who_color = "#2e8b57", what_prefix = '"', what_suffix = '"')
image side monster1 = "monster1"
define villageC = Character("Hermit Cove Citizens", color = "#FF00FF", what_prefix = '"', what_suffix ='"')
define frank = Character("Frank", image = "frank", color = "#50FF60", what_prefix = '"', what_suffix ='"')
image side frank = "frank"
define villageF = Character("Odenwald Villagers", color = "#FF5030",  what_prefix = '"', what_suffix ='"')
define fbride = Character("Bride of Frank", image = "bride", color = "#40FF70", what_prefix = '"', what_suffix ='"') #https://www.deviantart.com/chelseageter/art/The-Bride-561708053
image side fbride = "bride"
# how i learned about images https://www.bing.com/videos/search?q=image+over+background+ren+py&&view=detail&mid=BD9A6F2659E01DD72AE4BD9A6F2659E01DD72AE4&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dimage%2520over%2520background%2520ren%2520py%26qs%3Dn%26form%3DQBVDMH%26%3D%2525eManage%2520Your%2520Search%2520History%2525E%26sp%3D-1%26pq%3Dimage%2520over%2520background%2520ren%2520py%26sc%3D0-28%26sk%3D%26cvid%3DA6E3230776A241B782BDB9F3D375C8C3
#how i learned about side images https://www.bing.com/videos/search?q=side+inage+character+renpy&&view=detail&mid=7DD294B40EF2D27FB5747DD294B40EF2D27FB574&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dside%2Binage%2Bcharacter%2Brenpy%26go%3DSearch%26qs%3Dds%26form%3DQBVDMH
#all images for this game were downloaded from Pixabay
#Music by <a href="/users/zakharvalaha-22836301/?tab=audio&amp;utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=audio&amp;utm_content=33106">ZakharValaha</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=33106">Pixabay</a>
#Music by <a href="/users/jayalvarez66-24411567/?tab=audio&amp;utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=audio&amp;utm_content=11647">JayAlvarez66</a> from <a href="https://pixabay.com/music/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=11647">Pixabay</a>
#how I learned how to add music/soundeffects
#https://www.youtube.com/watch?v=H5J38QeGKtg
#title photo https://pixabay.com/illustrations/werewolf-giant-forest-tree-beast-6033047/
label start:
    scene forest2
    play sound "audio/price-of-freedom.MP3"
    pause
    jeff "Hello detective. Thank you for meeting me. Your services have come highly recommended."
    $ you = renpy.input("What should I call you?")
    if you == "":
        jeff "I am just going to call you Peanut"
        $ you = Character("Peanut")

    jeff "Nice to put a name to the face, [you]"
    jeff"Look [you], the surrounding villages are in unrest. As the villages expand, the more upset the Fifels have become..."
    you "What the heck is Fifel?! I only assist in matters involving mosters, villians, and bad hygiene."
    jeff"My bad, yes, we call them Fifel, they have been harrassing our villagers and hurting our expansion efforts!"
    menu:
        "What do you want from me Jeff?":
            jeff "Get rid of them by any means necessary!"
        "What is in it for me?":
            jeff "Riches upon riches upon riches."
    you "Alright, tell me where these Falafels are"
    jeff "It..uh...its pronounced, Fi-fel-s sir..."
    you "Enough of these games, let's get going."
    jeff "I suggest stopping by the marketplace to pick up supplies, here is 7 bucks to get you started."
    menu:
        "Go to the merchant first for supplies.":
            $ money += 7
            jump market
        "Why do I need to go to get supplies?":
            jeff "Look, with all of these fife...I mean monsters running around, you are going to need all the help you can get.
            here is 7 bucks to get you started"
            $ money += 7
            jump market
label market:
    scene merchant   #need to fix this picture or get a new one. adjust lines26
    with fade  #just added check if words
    pause
    show merchant at left
    merchant "Well hello stranger! What can I do for you on this brisk night?!"
    menu:
        "What do you have to offer?":
            merchant "I got all kind o' stuff, anything you need! I got some of those there personal care items and some special enhancements to protect you from danger. I recommend anything to protect from the cold and sooth any ailments you have."
            merchant "Lots o' people been catching colds around here. How about you take a look at my inventory."
            jump sellitem
        "Have you seen any suspicious creatures lurking around?":
            merchant "Yes'um I seen some creatures, never bothered me they have. Some folks get spooked pretty easy in these parts, but I never had no trouble! You ask me, just leave em' alone they won't bother with ya."
            merchant "So how about you take a look at what I got! What are you interested in? It was a rough winter, I recommend anything to protect from the cold and sooth any ailments you have"
            jump sellitem
label sellitem:
    menu:
        "Attributes (5)":
            call attributes
            #jump attributes
        "Personal Items (1)":
            #jump items
            call items
        "Not interested in buying anything":
            jump firstmonster
label attributes:
    if money >= 5:
        menu:
            "Strength":
                $ strength+= 1
                $ money= money - 5
                "Your strength has increased by one"
                #jump sellitem
            "Intellect":
                $ intellect += 1
                $ money= money - 5
                "Your intellect has increased by one"
                #jump sellitem
            "Luck":
                $ luck+= 1
                $ money = money - 5
                "Your luck has increased by one"
                #jump sellitem
    else:
        "You do not have enough money"
    jump sellitem
label items:
    if money > 0:
        menu:
            "Daisy":
                merchant "You never know when a daisy will come in handy, good choice sir"
                $ daisy+= 1
                $ money = money - 1
                "Your daisy inventory has increased."
                jump sellitem
            "Cough Drop":
                merchant "You ever had a cough so bad you gone lost your voice box? Lemme tell you, nothins worse than a sore throat"
                $ coughDrop+= 1
                $ money = money - 1
                "Your cough drop inventory has increased by one"
                jump sellitem
            "Lotion":
                merchant "Good, you look like you could use some lotion, no offense"
                $ lotion+= 1
                $ money = money - 1
                "Your lotion inventory has increased by one"
                jump sellitem
            "Ear Muffs":
                "I have been selling out of these lately for some reason"
                $ earmuffs += 1
                $ money = (money - 1)
                "Your ear muff inventory has increased by one"
                jump sellitem
    else:
        "You do not have any money."
        jump sellitem
#label checkmoneyattribute:
#    if money < 5:
#        "You do not have enough money to upgrade your attribute"
#    jump sellitem
#label checkmoneyitem:
#    if money == 0:
#        "You have absolutely no money"
#    jump sellitem
label firstmonster:
    scene forest2
    with fade # just added see if works
    jeff "You are finally back! We must hurry over to the  village of Bandlewood. A banshee has been terroizing the citizens for two days now, they had to put ear muffs on to stop the constant screeching. The problem is that now the citizens keep missing their alarm clocks for work because their ears are covered!"
    menu:
        "Thats odd behavior for a banshee.":
            jeff "I agree. Regardless, I can't have that think disrupting the citizens work lives. It needs to go"
        "Has anyone died?":
            jeff "No, no one has died. But they are all suffering from a terrible cold that set in right around when the banshee started harassing villagers"
    scene villagebanchee
    with dissolve #just added see if works
    pause
    jeff "I think I hear it coming, put on some earmuffs if you got them!!!!!!!!"
label muffmenue:
    menu:
        "Put on earmuffs":
            if earmuffs == 0:
                "You do not have any earmuffs!"
                "It's scream rocked your brain"
                $ strength -= 1
                "You lost one strength"
                jump contmonster1
            else:
                "Ah, got them on just in time!"
                $luck += 1
                "Your luck has increased 1"
                jump contmonster1
        "I like to live on the wild side":
            "It's scream rocked your brain"
            $ strength = strength - 1
            "You lost one strength"
            jump contmonster1
    call checkmuff
label checkmuff:
    if earmuffs == 0:
        "You do not have any earmuffs!"
        $ strength = strength - 1
        "You lost one strength"
        jump contmonster1
    else:
        "Ah, got them on just in time!"
        $luck += 1
        "Your luck has increased 1"
        jump contmonster1

label contmonster1:
    "Just like a bug flying past your ear, the screaming coming from over the hill grew louder and louder." #, vibrating [you]'s and Jeff's eardrums."
    show banshee #at right
    with hpunch
    #with moveinright
    #hide banshee
    #with moveoutleft
    pause
    "As you watched her fly past screaming, you noticed something. The banshee's voice was raw and cracked, it was grasping at its throat. Then it hit you."
    "The Banshee has a sore throat!"
label bansheeoptions:
    menu:
        "Give the Banshee a coughdrop":
            jump banoption1
        "Grab Banshee to recieve reward from villagers":
            jump village1
        "This is too much for me right now Jeff, we will have to come back with more supplies":
            "Unable to aid the villagers and rid the Banshee you lost all opportunity to increase attributes"
            jump after1
    #call checkcough
label banoption1:
    if coughDrop == 0:
        "You do not have any cough drops"
        jump bansheeoptions
    else:
        "The Banshee gave a sigh of relief, and gave a screech of thanks and flew out of the village peacefully"
        $ coughDrop= coughDrop - 1
        $ strength += 2
        $ luck+= 1
        $ money += 1
        "Your strength has increase 2, your luck has increased 1, and you found a dollar"
        jump after1
label village1:
    hide banshee
    villageB "Thank you kind [you] for capturing this creature. We have not had a good rest all week!"
    menu:
        "What will you do with the Banshee now?":
            villageB "Oh, we will make use of it. We will keep in confined in a cage and put her out in the fields so she can scare the crows away"
            you "That seems a little inhumane"
            villageB "Waste not want not. Here is a reward for your troubles"
            $ money+= 12
            "Feeling alittle dirty you take the money and leave"
            "Your money has increased 12"
            jump after1
label after1:
    scene forest1
    with fade
    pause
    jeff "Well that was interesting. I think you should gather more supplies before our next encounter. Here follow me I know just the place"
    jump market2
label market2:
    scene store3
    pause
    show lady2 with easeinright
    merchant2 "Who goes there? I may be old and weak, but my rifle is not!"
    hide lady2
    show lady with dissolve
    you "Hello, my name is [you], I know its late but I was hoping to purchase some goods from you."
    "[merchant2] opens the door"
    merchant2 "Well hello there [you]..."
    you "Uhhh..."
    merchant2 "Hmph. Well you're lucky to find me, there aren't many merchants around here anymore. Most closed up shop!"
    hide lady
    show ladysitting with dissolve
    menu:
        "Why is that?":
            merchant2 "Well [you], simply put they all went out of business, can't compete anymore. I myself have had this shop for 30 years, but only theives come here now - hence the gun."
            merchant2 "Are you the same [you] that was down in Bandlewood?"
            menu:
                "Yes I imprisoned a banshee":
                    merchant2 "Oh, oh, oh, poor Eleanor. You should be ashamed of yourself. She used to own a shop where she gave singing lessons until she was forced out."
                    show oldlady3 with dissolve
                    merchant2 "Purchase what you need to get out of my shop!"
                "Yes I helped a banshee":
                    merchant2 "Oh, thank goodness hon, what a good and kind thing to do. I don't know what all the fuss was about in the first place"
                "I ran away because I didnt purchase the proper equipment":
                    merchant2 "[you], my advice to you is keep you toolbelt filled hon. You never know what you will need out here. Why don't you get alittle lotion, it's been dryer than woodchips out here"
            jump sellitem1
        "I am a little in a hurry can I see your inventory?":
            jump sellitem1

label sellitem1:
    menu:
        "Attributes (5)":
            call attributes1
        "Personal Items (1)":
            call items1
        "Not interested in buying anything":
            merchant2 "Well hon, you be safe out there. I can feel in my bones something just isnt right"
            jump meetjeff
label attributes1:
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
        #call checkmoneyattribute1
    else:
        "Not enough money"
    jump sellitem1
label items1:
    if money > 0:
        menu:
            "Daisy":
                merchant2 "Oh, hon, what a good choice! This is my favorite flower"
                $ daisy+= 1
                $ money = money - 1
                "Your daisy inventory has increased."
                #jump checkmoneyitem
            "Cough Drop":
                merchant2 "People were sick in the town over! Say, you didnt just come from there did you hon?"
                $ coughDrop+= 1
                $ money = money - 1
                "Your cough drop inventory has increased by one"
                #jump checkmoneyitem
            "Lotion":
                merchant2 "I am nearly sold out of lotion, the weather has been so strange. It used to be so humid around here, but now its as dry as saw dust."
                $ lotion+= 1
                $ money = money - 1
                "Your lotion inventory has increased by one"
            "Ear Muffs":
                merchant2 "I gave most of these to [merchant], they might not do much good for you around these parts."
                $ earmuffs += 1
                $ money = (money - 1)
                "Your ear muff inventory has increased by one"
    else:
        "You do not have any money"
    jump sellitem1

label meetjeff:
    scene forest4 #https://pixabay.com/illustrations/haunted-horror-mansion-old-night-7082900/
    with fade
    jeff "I hope you have the supplies you needed, we will need all the help we can get. Down the road is the city Hermit Cove. Oddly, the city folk have been unable to leave their homes due to unprecedented snowfall"
    jeff "These poor folks are scared to leave their houses, no work, no deliveries, no nothing! We must investigate this, it has not snowed in Hermit Cove for over 200 years!"
    you "I told you before, I only deal in matters of monsters, villians and bad hygiene"
    jeff "There is a monster behind it all. I know it in my gut!"
    jump monster2

label monster2:
    scene lagoon3
    with fade
    pause
    show snowing
    jeff "You see [you], it just does not make sense. It's nearly 95 degrees out here and its snowing! On the flip side, I havnt seen snow in years!
    try to catch one on your tongue!"
    "Jeff nudges you to join him in childhood memories"
    menu:
        "This does not seem like normal snow.":
            "Jeff starts coughing, spitting, and wiping his tongue with his hands, holding back a wretch of nausia he says,"
            jeff "UGHHHH, this isnt snow!"
            "You both look up to see a creature itching insatiably, whirling all through the air was its dry skin flakes"
            jeff "I am going to be sick"
            jump creaturesighting
        "YOLO":
            "You both laugh and start to catch snowflakes on your tongues. To your dismay, its not melting - it is accumluating in your mouth!"
            "Jeff starts to yack like a cat with a furball. You both look up to see a creature itching insatiably, whirling all through the air was its dry skin flakes"
            jump creaturesighting
label creaturesighting:
    show reptile at right
    "The creature spots you and cowers behind a rock"
    "Jeff looks at the creature in discust, still spitting the dry flakes of skin out of his mouth"
    jeff "What are you waiting for? This vile thing has disrupted the lives of all of the poor citizens of Hermit Cove. Who know how many others got a mouthful of flakes because of this creature."
    jump creaturesolution
label creaturesolution:
    menu:
        "I will just give it some lotion!":
            jump lotion1
        "Trap the creature to surrender to citizens for a cash reward":
            "The creature groans in pain was you bind its limbs"
            jump citizenreward
        "I can't do this right now, I need some mouthwash":
            jump meetingup
label lotion1:
    if lotion == 0:
        "You do not have any lotion"
        jump creaturesolution
    elif lotion !=0:
        $lotion -= 1
        $money += 2
        $intellect += 1
        "Your intellect increased by 1 and money increased by 2"
        jump meetingup
    else:
        "The creature coos as it puts the lotion on its skin, the poor thing had deep scars from the itching." #yea I said it!
        creature "Helloosss, my namesss iss Shrilll. You sssaved my lifesss. Notss long agosss I livessss in peace with humanssssss. I sssoold my slimeess for chilrensss to playsss with."
        creature "Then I wasss banished fromssss my mud lagoonsss and lost slimesss. No slimesss no businesss and drysss skinsss. I am gratefullsss for the helpsss"
        $ intellect += 2
        menu:
            "I can help you find a lagoon and you can start your business again":
                jump newlagoon

            "You should get out of here before the angry citizens find you":
                "The creature scurries away"
                jump meetingup
label newlagoon:
    scene newswamp
    with fade
    pause
    show reptile
    creature "Yousss savessss my lifesssss, thanksss yousss."
    you "Good luck with your slime business"
    $ intellect += 2
    $ money += 1
    "You gained one intellect, and one dollar"
    jump meetingup
label citizenreward:
    villageC "Thank you [you], our town lost so much tourism revenues because of this creature! Now it can pay us back, shove it in one of the empty enclosures in the board walk zoo"
    $ money += 10
    "You take the money, starting to feel like a monster"
    "Money increased by 10"
     #We have lived in peace for hundreds of years, but recently there has been unrest"
label meetingup:
    scene forest3 #https://pixabay.com/illustrations/fantasy-background-haunted-dark-6396037/
    with fade
    jeff "I never want to see snow again. Did you need supplies?"
    jump meet
label meet:
    menu:
        "Go get supplies":
            jeff "Lucky for us there is a vending machine right here."
            show vend at right
            pause
            if money > 0:
                menu:
                    "Daisy":
                        $ daisy+= 1
                        $ money = money - 1
                        "Your daisy inventory has increased."
                            #jump checkmoneyitem
                    "Cough Drop":
                        $ coughDrop+= 1
                        $ money = money - 1
                        "Your cough drop inventory has increased by one"
                        #jump checkmoneyitem
                    "Lotion":
                        $ lotion+= 1
                        $ money = money - 1
                        "Your lotion inventory has increased by one"
                    "Ear Muffs":
                        $ earmuffs += 1
                        $ money = (money - 1)
                        "Your ear muff inventory has increased by one"
                jump meet
            else:
                "You do not have money for supplies."
                jump frank
        "Don't need any supplies":
            jump frank

    jeff "One of our last stops is in Odenwald. The locals have been too frieghtened to travel outside of their homes. Those who are brave enough to wonder out, are too spooked and shaken to be productive in work activities"
    menu:
        "What are they frightened of?":
            jeff "Well [you], if the rumors are true, there is a reanimated man walking about"
            jump frank
        "Lets go to Odenwald":
            jeff "Follow me [you]"
            jump frank
label frank:
    scene castle
    with fade
    pause
    jeff "It was created by a mad scientist. It is said that this creature will not rest until it finds its wife. Look, there it is!"
    show frankwalk with easeinleft
    jeff "Now is your chance, you can bag this one!"
    you "Shhh...he is saying something"
    "You listen intently"
    frank "Whaaaaaaee aaaaaaa ooooooooo, wheaaaa aaaeee yooooouuu"
    you "He sounds distressed, I can almost make out what he is saying"
    menu:
        "Try to talk to this creature":
            jump talkfrank
        "Bag and bring to villagers":
            jump meetvillage
label talkfrank:
    "You draw nearer to the creature, to your suprise his face is wet with tears, its giant hands are shaking"
    you "Are you okay?"
    "The creature stares suspiciously"
    frank "Aaaaahhhaa"
    "It reached for its face and snapped its jaw back in place"
    frank "Hello kind stranger, didn't mean to scare you. My jaw keeps getting unhinged. Please, will you help me?"
    menu:
        "What do you need help with?":
            frank "My-uh-my wife is..well she is missing. I am unsure if she is lost or taken by one of the mob villagers. We used to live peacefully amongst the villagers until we sparked a poweroutage and they turned against us."
        "Who and what are you!?":
            frank "Oh yes, I feel so rude. My name is Frank Stein, I live here in this castle with my Mad Father..uh..I mean God Father and my..my...my..wife"
            "Frank started blubbering"
            frank "She is missing. I am so worried for her, she does not know her way out of the castle, she could be anywhere."
    menu:
        "Help find wife?":
            you "I will help you. See here Frank? There are tracks leading west toward an open field."
            jump outhouse
        "Take to villagers for reward":
            you "Sorry Frank, I really need cash, so I am going to have to sell you to the villagers."
            jump meetvillage
label outhouse:
    scene castle1 #https://pixabay.com/illustrations/castle-moon-full-night-milky-way-6236609/
    with fade
    show outhouse1 at right
    show gas behind outhouse1 at right  #https://www.bing.com/videos/search?q=renpy+picture+behind&&view=detail&mid=BD9A6F2659E01DD72AE4BD9A6F2659E01DD72AE4&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Drenpy%2520picture%2520behind%26qs%3Dn%26form%3DQBVR%26%3D%2525eManage%2520Your%2520Search%2520History%2525E%26sp%3D-1%26pq%3Drenpy%2520picture%2520behind%26sc%3D0-20%26sk%3D%26cvid%3D893584A6299C4DE7A00902ACED20ADE4
    pause
    frank "Hooonnneeyyy *crack* honey is that you in there?"
    fbride "Oh Frank, darling, please don't come any closer. Oh I am so embarrassed. I don't want you to hear or smell this."
    frank "But I can help you through this dear, my first pass after being reanimated was very painful too...please let me help you."
    you "I might have exactly what you need."
label poop:
    menu:
        "Give Frank earmuffs to muffle sound":
            jump muffler
        "Give Frank a daisy to mask smell":
            jump flower
        "No items to give":
            frank "Oh well, thanks for all your help, I really appreciate it!"
            you "See ya!"
            jump lastmeeting
label muffler:
    if earmuffs == 0:
        "You do not have any earmuffs."
        jump poop
    elif earmuffs >= 1:
            if checkmuff >=1:
                "You already gave Frank this item."
                jump poop
            else:
                "This will save Mrs.Stein some embarrasment."
                $earmuffs = earmuffs - 1
                $checkmuff += 1
                $money += 5
                "Your Money has increased by 5."
                jump poop
label flower:
    if daisy == 0:
        "You do not have a daisy"
        jump poop
    elif daisy >= 1:
        if checkflower != 0:
            "You already gave Frank a flower"
            jump poop
        else:
            "This will help cover up the horrible smell"
            frank "Thank you [you], we are newly weds, she is still very shy."
            $strength += 2
            $intellect += 1
            $money += 2
            $checkflower += 1
            "Your Strength has increased 2, Intellect increased 1, money increased 1"
            jump poop
label meetvillage:
    scene cabininwoods
    with fade
    jump village
label village:
    scene woodinterior
    pause
    villageF "Thanks for bringing him in [you], here is some money for your troubles."
    $money += 15
    "Your money has increased by 15"
    villageF "We will pay you extra if you know the location of his wife."
    "You ponder how far you are willing to go for money, when you start to look around the lodge."
    "To your horror, you see Shrek staring back at you, mounted as a hunting trophy. Surely Frank will suffer the same fate"
    show plaque at truecenter
    show shrek1 at truecenter
    #pause
    you "What have I done?! How about a wager?"
    villageF "Go on..."
    you "A game of dice. If I win, give me back Frank. If you win, I will tell you where his bride is."
    villageF "You want to throw dice to get this Freak back?"
    menu:
        "Yes. Gamble to get Frank back (dice)":
            villageF "I hope you are feeling lucky [you]."
            #hide plaque
            #hide shrek
            jump roll
        "No. Good riddance":
            villageF "Oh well, we will find her eventually."
            you "Whatever, I'm out."
            jump lastmeeting
label roll:
    $village_roll = renpy.random.randint(1,6)
    if village_roll == 1:
        show dice1 at left
    elif village_roll == 2:
        show dice2 at left
    elif village_roll == 3:
        show dice3 at left
    elif village_roll == 4:
        show dice4 at left
    elif village_roll == 5:
        show dice5 at left
    elif village_roll == 6:
        show dice6 at left
        pause
    $your_roll = renpy.random.randint(1+luck, 6)
    if your_roll == 1:
        show dice1 at right
    if your_roll == 2:
        show dice2 at right
    if your_roll == 3:
        show dice3 at right
    if your_roll == 4:
        show dice4 at right
    if your_roll == 5:
        show dice5 at right
    if your_roll == 6:
        show dice6 at right
    "The villagers rolled [village_roll] and you rolled [your_roll]!!!"
    jump judgement
label judgement:
    if village_roll > your_roll:
        "You lost."
        hide shrek1
        show frank at truecenter
        "You tell the villagers where Frank's wife is, and the villagers grab their torches and pitchforks"
        "It was later reported that the mob of villagers died from methane inhalation before they reached the outhouse"
        jump lastmeeting
    elif village_roll == your_roll:
        villageF "We must play another match to determine the winner"
        jump roll
    else:
        villageF "Fine you win."
        $luck += 1
        "Your luck has increased one"
        frank "Never speak to me again."
        jump lastmeeting
label lastmeeting:
    scene darkbackround
    pause
    you "I am really tired of programming...I mean fighting monsters, are we almost done."
    jeff "Go to the marketplace and spend all the money but don't waste your money on any more items you won't need them where I am taking you."
    call lastmarket
label follow:
    jeff "Last stop."
    "Jeff smiles slyly."
    jeff "Follow me"
    jump mordor
label lastmarket:
    scene barren #https://pixabay.com/illustrations/forest-night-heaven-clouds-3494574/
    show gollum at center #https://www.pngaaa.com/detail/2454882
    menu:
        "You look familiar.":
            goll "No precious *gollum* *gollum*"
            goll "Master is expecting [you]sess."
            call sellitem2
        "I live under a rock.":
            goll "You have money in your nassty little pocketsess. Give Gollum precious" #ripped off LOTR books
            call sellitem2
label sellitem2:
    menu:
        "Attributes (5)":
            jump attributes2
        "Not interested":
            jump follow
label attributes2:
    if money >= 5:
        menu:
            "Strength":
                $ strength+= 1
                $ money= money - 5
                "Your strength has increased by one"
                jump sellitem2
            "Intellect":
                $ intellect += 1
                $ money= money - 5
                "Your intellect has increased by one"
                jump sellitem2
            "Luck":
                $ luck+= 1
                $ money = money - 5
                "Your luck has increased by one"
                jump sellitem2
    else:
        "You do not have enough money"
        jump follow
label mordor:
    scene mordor #https://pixabay.com/photos/lord-of-the-rings-fantasy-mordor-6761163/
    show bezos
    you "What is going on here Jeff?"
    jeff2 "Mwahahahahaha. Those stupid Fifels were getting in the way of my expansion!! I drove them all out of business one by one"
    you "Wait, what?!"
    jeff2 "Oh yes [you], the Banshee used to give singing lessons and owned an instrument store, Shrill was taking away from my slime kit sales, and Frank used to own a nuts and bolts shop."
    jeff2 "After I drove them all out of business, they refused to leave. I just needed bodies to fill my factories, but those dang monsters continued to interupt business operations."
    jeff2 "I needed you to drive them away. I am looking for a new business partner [you], what do you say?"
    menu:
        "I will fight tooth and nail before I help you.":
            jeff2 "Pfft. Fine! Have it your way! Let's fight! Pick your poison!"
            jump trials
        "All I want are riches, why not.":
            jump endingtwo
label trials:
    menu:
        "A battle of strength":
            jeff2 "Fisties it is!"
            jump fisty
        "A battle of the brain":
            you "I have a game for you. Three decks shuffled randomly. If you draw any royal cards I win!"
            jump braingame
        "Try your luck":
            you "Let's roll some dice for the win."
            jump rollz
label braingame:
    scene pokertable #https://pixabay.com/illustrations/casino-gambling-happiness-roulette-4815934/
    show deckl at right
    show deckl at truecenter
    show delk at left
    pause
    $pileOne = []
    $pileTwo = []
    $pileThree = []

    #def create_shuffled_deck():
    $deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4
    $shuffdeck = renpy.random.shuffle(deck)
        #return deck
    #def three_piles():
        #shuffdeck = create_shuffled_deck()
    $pileOne= shuffdeck[0:17]
    $pileTwo= shuffdeck[17:34]
    $pileThree = shuffdeck[34:53]
    $jeffwins = 0
    $youwin=0
    if pileOne[0] == "J" or pileOne[0] == "Q" or pileOne[0] == "K":
        $jeffwins += 1
        call pile1
    elif pileTwo[0] == "J" or pileTwo[0] == "Q" or pileTwo[0] == "K":
        $jeffwins += 1
        call pile2
    elif pileThree[0] == "J" or pileThree[0] == "Q" or pileThree[0] == "K":
        $jeffwins += 1
        call pile3
    else:
        $iwin += 1
    jump results
label results:
    if jeffwins != 0:
        jeff2 "Mwuahahaha I win!"
        jump endingtwo
    elif iwin != 0:
        jeff2 "Noooooooo!"
        jump endingone
label pile1:
    if pileone == "Q":
        show queen at left
    elif pilone == "K":
        show king at left
    elif pileone == "J":
        show jack at left
    else:
        show joker at left
return
label pile2:
    if piletwo == "Q":
        show queen at truecenter
    elif piletwo == "K":
        show king at truecenter
    elif piletwo == "J":
        show jack at truecenter
    else:
        show joker at truecenter
return
label pile3:
    if pilethree == "Q":
        show queen at right
    elif piletwo == "K":
        show king at right
    elif piletwo == "J":
        show jack at right
    else:
        show joker at right
return

label fisty:
    pass
label rollz:
    pass
label endingone:
    pass
label endingtwo:
    pass
return

#https://www.bing.com/videos/search?q=display+stats+in+renpy&&view=detail&mid=DDDE483394617542515ADDDE483394617542515A&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Ddisplay%2520stats%2520in%2520renpy%26qs%3Dn%26form%3DQBVR%26%3D%2525eManage%2520Your%2520Search%2520History%2525E%26sp%3D-1%26pq%3Ddisplay%2520stats%2520in%2520renpy%26sc%3D1-22%26sk%3D%26cvid%3D28DD3D7C3BB34B25BCE905EA1606FF83
#https://www.youtube.com/watch?v=4O3uqLpvnKE
#ctrl + s = save
#shift + r = run game
