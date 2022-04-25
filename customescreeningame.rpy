
# I copied code from this video to set the inventory button
#https://www.bing.com/videos/search?q=how+to+display+stats+on+renpy&ru=%2fvideos%2fsearch%3fq%3dhow%2bto%2bdisplay%2bstats%2bon%2brenpy%26go%3dSearch%26qs%3dds%26form%3dQBVDMH&view=detail&mid=334FB983930560F85D84334FB983930560F85D84&&FORM=VDRVRV
image merchant:
    "merchant.jpg"
    size(1280,850)
image villagebanchee:
    "villagebanchee.jpg"
    size(1280,720)
image store3:
    "store3.jpg"
    size(1280,720)
image mordor:
    "mordor.jpg"
    size(1280,720)
image forest4:
    "forest4.jpg"
    size(1280,720)
image woodinterior:
    "woodinterior.jpg"
    size(1280,720)
image decl:
    "decl.png"
    size(200, 337)
image queen: #https://pixabay.com/vectors/playing-card-queen-clubs-card-deck-161484/
    "queen.png"
    size(200,337)
image king:
    "king.png" #https://pixabay.com/vectors/playing-card-king-card-deck-deck-161492/
    size(200,337)
image jack:
    "jack.png" #https://pixabay.com/vectors/playing-card-knave-card-deck-deck-161493/
    size(200,337)
image joker:
    "joker.png"
    size(200,337) #https://pixabay.com/vectors/joker-card-recreation-games-poker-28361/
image snowing:
    "snowing.png"  #https://pixabay.com/vectors/snowflakes-snow-winter-ice-cold-2031353/
    animation
    yalign 0.0
    easeout 0.4 yalign 0.25
    easein 0.4 yalign 0.0
    easeout 0.6 yalign 0.25
    repeat
image banshee:
    "banshee.png"
    parallel:
        linear 1.0 xalign 0.0
        linear 1.0 xalign 1.0
        repeat
    parallel:
        linear 1.3 yalign 1.0
        linear 1.3 yalign 0.0
        repeat
            


    #xalign 0.0
    #linear 1.0 xalign 1.0
    #linear 1.0 xalign 0.0
    #repeat
    #xalign 0.0
    #linear 2.0 xalign 1.0


    #show banshee at right
    #with moveinright
    #hide banshee
    #with moveoutleft
    #show banshee
    #with moveintop
    #hide banshee
    #with moveoutbottom
    #repeat
