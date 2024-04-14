# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    define l = Character(_("Lyra"),color="#c8ffc8")
    define lm = Character("Voice in Lyra's Mind",color="#0fd2a1")
    define V = Character("Vex",color="#ef7575")
    define k = Character("Kael",color="#b76e64")
    define T = Character("Townsfolk",color="#0fda0f")
    define m = Character("Minion of Nightfall",color="#111711")
    define st = Character("Sir Tristan",color="#4a4c4a")
    define Sp = Character("Sparrow",color="#b064e0")
    define el = Character("Eclipse Lord",color="#ffffff")

    image  Vex happy = "images/Vex happy.png"
    image  Vex normal = "images/Vex normal.png"
    image  Vex talk = "images/Vex talk.png"
    image Sparrow happy = "Sparrow happy.png"
    image Sparrow normal = "Sparrow normal.png"
    image Sparrow talk = "Sparrow talk.png"
    image EL = "EL.png"

    $ tristanThere = False
    $ VexTere = True
    $ SparrowTere = True
# The game starts here.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "11 - Juniper Pokémon Lab.mp3" fadeout 1 
    scene store
    with fade
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lyra normal at right 
    with dissolve

    # These display lines of dialogue.

    "In the heart of the Eternal City, where the whispers of history intertwined with the dance of shadows upon ancient cobblestones, there dwelled a healer named Lyra."

    l "Hold still, friend. This salve will soothe your wounds."

    show Vex happy at left 
    with dissolve
    V "Thank you, Lyra. Your remedies work wonders."

    "With lucious locks that seemed to sip from the darkness of the night."
    hide Vex happy
    l "Another long night awaits. But my duty calls"

    ".and eyes that shimmered like liquid silver under the moon's caress.."
    l "There's a certain comfort in its glow, isn't there"
    " Lyra was whispered to possess the magic of the old gods themselves"
    T "They say Lyra's touch can cure any ailment. She's blessed by the ancient ones, no doubt"

    scene city2
    with fade
    "On a night ripe with possibility and draped in mystery, fate decided to dance its whimsical waltz into Lyra's sanctuary."

    l "Who goes there? Are you in need of aid?"

    show kael sad at right
    with dissolve
    k  "Please... help me... I seek refuge from the darkness."

    "A wounded stranger, his presence heralded by the solemn symphony of his stumbling steps, stumbled through the threshold seeking solace and succor."

    menu:
        "What should Lyra do?"

        "Help the stranger":
            jump Help_Kael
        "Refuse to help the stranger, wary of his unknown intentions":
            jump Dont_Help_Kael
    

label Help_Kael:

    scene store
    with dissolve
    show lyra normal at left
    with dissolve
    show kael happy at right
    with dissolve
    l "Let me tend to your wounds. What happened to you?"

    "As Lyra delicately tended to the stranger’s injuries, her fingers tracing the contours of his wounds with a gentle reverence..."

    k "The Nightfall Syndicate... they... they did this to me."

    l "noticing the symbol on his flesh, alarmed The Syndicate? Here?"

    "..she uncovered a hidden symbol etched into his flesh—a mark of the forbidden cult known as the Nightfall Syndicate."

    k "pleading You must help me. They're spreading darkness throughout the city."

    " The revelation sent a shiver down her spine, for tales of the Syndicatess nefarious deeds had long haunted the whispers of the city's nocturnal alleys."
    l "I will do what I can. But you must tell me everything."

    "The stranger, now revealed to be named Kael, gazed at her with eyes brimming with desperation..."

    k "They've taken everything from us. Our freedom, our hope..."

    "...his voice a tremulous plea as he recounted the tyranny inflicted upon the city by the Syndicate's shadowy grasp"
    menu:
        "What should Lyra do?"

        "turn Kael over to the authorities, unwilling to involve herself in dangerous political affairs.":
            jump Turn_kael_over
        "agree to aid Kael, drawn by a desire to defy the oppressive darkness that loomed over the city":
            jump Dont_Turn_kael_over

label Dont_Help_Kael:
    play music "18 - Accumula Town.mp3" fadeout 1 
    show lyra sad  at left
    with dissolve
    show kael sad at right
    with dissolve
    k "Please, I need your help. I'm injured and I don't have anywhere else to go."

    l "I'm sorry, but I can't help you. It's too risky for me to get involved with someone I don't know."

    k "Please, I'm desperate. I won't cause any trouble, I just need somewhere to rest and heal."

    l "I understand, but I can't take that chance. I'm sorry."

    k "Nods sadly I see. Thank you for considering it, at least."

    l "I hope you find the help you need. Take care."

    hide Kael sad
    l "I can't shake this feeling of guilt, no matter how hard I try."

    show lyramind normal at right
    with dissolve

    lm "You did what you thought was right, Lyra. You couldn't have known what would happen."

    l "But what if I could have helped him? What if my fear and hesitation led to his death?"

    lm "It's natural to feel responsible, but you can't blame yourself for the actions of others. You acted out of caution, out of concern for your safety and the safety of others."

    l "Nods I know, but it doesn't make it any easier. I just can't shake this sense of regret."

    lm "Sometimes, the hardest decisions are the ones that haunt us the most. But you can't let this consume you. Learn from it, grow from it, and use it to guide your actions in the future"

    l "Takes a deep breath You're right. I have to find a way to move forward, to honor his memory and ensure that I never let fear cloud my judgment again."
    return

label Turn_kael_over:
    play music "03 - Sky Pillar.mp3" fadeout 1 
    show lyra sad  at left
    with dissolve
    show kael sad at right
    with dissolve
    l  "I'm sorry, Kael. I have to do this. It's... it's for the greater good."

    show kael angry at right
    with dissolve
    k "What? Lyra, you can't be serious. You're handing me over to them?"

    l "I can't explain it now, Kael. Just trust me, please."

    show tristan talk at left
    with dissolve
    hide lyra sad
    with dissolve
    m "Well, well, well. Look what we have here. Another traitor trying to save her friend."

    k "You're betraying everything we stand for, Lyra! How could you do this?"

    show lyra sad  at left
    with dissolve
    hide tristan talk
    with dissolve
    l "I have no choice! I have to think about the bigger picture!"
    hide kael angry
    with fade
    show tristan talk at right
    with dissolve
    m "Time's up, little girl. Hand him over."
    "Kael is forcefully taken away"
    return

label Dont_Turn_kael_over:
    show lyra happy at left
    with dissolve
    show kael happy at right
    with dissolve
    l "You are not alone, Kael. Together, we will face this darkness."

    play music "17 - Soaring Dreams.mp3" fadeout 1 
    scene street1

    show lyra happy at left
    show kael happy at right
    "As Lyra and Kael embarked on their mission to gather allies, they encountered a diverse array of characters, each with their own motivations and secrets."

    l  "We need allies if we're to stand any chance against the Syndicate. Together, we can bring light to the darkness that plagues our city."
    
    hide lyra happy
    show tristan happy at left 
    with dissolve
    
    st  "I may not be the most reputable of companions, but I seek redemption. My skills and connections are at your disposal."

    "A Disgraced Noble Seeking Redemption, named Sir Tristan, was once a respected member of the city’s elite until a scandal tarnished his reputation."

    k  "We'll need all the help we can get. Welcome, Tristan."
    
    hide kael happy
    show Sparrow happy at right
    with dissolve 
    
    Sp  "Well, well, what do we have here? A noble in need of a second chance? Count me in for the adventure."

    "A Cunning Thief with a Heart of Gold, known only as Sparrow, possesses a quick wit and a penchant for mischief."
    show lyra happy at left
    l "Your skills will be invaluable, Sparrow. Welcome to the cause."

    scene street2
    with fade
    show kael happy at right
    hide lyra happy
    with dissolve
    show Vex happy at left 
    with dissolve
    V "Ah, I've been expecting you. Your quest intrigues me, and I offer my assistance."

    "A Mysterious Sorcerer Shrouded in Secrets, known only as Vex, possesses a mastery of arcane arts that borders on the forbidden."

    k "What's your angle, sorcerer? Why join us?"

    V "Let's just say I have my reasons. And for now, our goals align"

    menu:
        "How will Lyra proceed?"

        "Lyra could trust in the strength of her companions, believing in the power of unity to overcome adversity.":
            $ tristanThere = True
            jump Allcompanions 
        "Lyra could forge alliances cautiously, wary of betrayal from those with hidden agendas.":
            jump moreMenu

label moreMenu:
    menu:
        "Accept Vex and Sparrow as Ally":
            $ tristanThere = False
            $ VexTere = True
            $ SparrowTere = True
            jump Allcompanions
        "Accept Vex and Tristan as Ally":
            $ tristanThere = True
            $ VexTere = True
            $ SparrowTere = False
            jump Allcompanions
        "Accept Sparrow and Tristan as Ally":
            $ tristanThere = True
            $ VexTere = False
            $ SparrowTere = True
            jump Allcompanions

label Allcompanions:
    play music "05 - Royal Unova.mp3" fadeout 1 
    scene city1
    with fade

    "With newfound allies by her side, Lyra felt a surge of determination coursing through her veins as they prepared for the final confrontation with the Nightfall Syndicate."
    if tristanThere:
        show tristan talk at left
        with dissolve
        st " Today, we make our stand against tyranny! No longer shall we cower in fear of the Nightfall Syndicate!"
        hide tristan talk
    if SparrowTere:
        show Sparrow talk at right
        with dissolve
        Sp " I've scouted their defenses. They won't know what hit 'em."
        hide Sparrow talk
    if VexTere: 
        show Vex talk at left
        with dissolve
        V  "My spells will shield us from harm. We shall not falter."

    show lyra talk at right
    with dissolve
    
    l " I can't thank you all enough for joining me in this fight. Together, we can bring justice to our city."
    "As they strategized their approach, Lyra’s heart swelled with gratitude for her newfound companions. Despite their differences, they had come together in a common cause, bound by a shared desire to see justice served and the oppressive grip of the Syndicate broken."

    scene street2
    with fade
    show lyra talk at right
    with dissolve
    l "Stay sharp, everyone. We're getting close."
    "With each step, Lyra couldn’t help but feel a sense of apprehension gnawing at her insides. But with her allies at her side, she knew that together, they stood a chance against the darkness that threatened to consume them all."

    scene throne
    with fade
    play music "03 - Sky Pillar.mp3" fadeout 1

    "Tension hung thick in the air as Lyra and her allies reached the inner sanctum. Before them stood the imposing figure of the Eclipse Lord, a dark aura swirling around him like a cloak of shadows."
    show EL at right
    with dissolve
    el "So, you dare to challenge me?"

    show lyra talk at left
    with dissolve
    l  "We do. We stand together against tyranny and oppression."

    "The time had come to confront their greatest adversary. Lyra could feel the weight of their collective resolve bolstering her own, lending her strength in the face of the looming threat."

    menu:
        "Confront alone":
            jump Confront_Alone
        "Confront with Allies":
            jump ConfrontWithAllies

label Confront_Alone:
    scene throne
    with fade
    play music "25 - Battle! (Elite Four).mp3" fadeout 1
    "Summoning every ounce of courage within her, Lyra stepped forward, her allies holding back at the entrance to the chamber."
    "With a majestic aura of determination, she strode toward the Eclipse Lord, her very presence a testament to the indomitable spirit of humanity."
    play sound "Aurora Veil.mp3"

    show lyra angry at left
    with dissolve
    l "Behold, Eclipse Lord! The light of justice shall pierce through the veil of your darkness!"

    play sound "Extrasensory.mp3"
    "As Lyra faced the Eclipse Lord alone, the chamber trembled with anticipation, the echoes of their clash resonating through the annals of time. "
    "With a wave of his hand, the Eclipse Lord unleashed a cataclysmic storm of shadows, seeking to engulf her in an abyss of despair."
    play sound "Extrasensory.mp3"

    show EL at right
    with dissolve
    el "Mortal, your defiance is futile! You stand no chance against the might of the eclipse!"

    "But Lyra, radiant with celestial grace, refused to yield. With a sublime flourish, she called upon the heavens themselves, weaving strands of pure light to counter the encroaching darkness."
    l "I am the harbinger of dawn, the guardian of hope! By the power of the cosmos, I shall vanquish your tyranny!"
    
    T"he clash of their powers ignited the very fabric of reality, each wave of energy unleashing a spectacle of cosmic magnitude." 
    "Lightning danced across the firmament, illuminating the chamber in a dazzling display of celestial fury."
    play sound "Bolt Strike.mp3"
    el "You dare defy me, mortal?! I am the sovereign of shadows, the harbinger of oblivion!"

    "But Lyra, resplendent in her valor, stood firm against the tempest. "
    "With a crescendo of divine energy, she unleashed a supernova of pure radiance, a beacon of transcendent brilliance that rent the darkness asunder."
    play sound "Happy Hour.mp3"
    l " Darkness may linger, but it shall never extinguish the eternal flame of hope!"

    scene city1
    with fade
    play music "07 - Per Aspera Ad Astra.mp3" fadeout 1
    "As the brilliance faded and the echoes of battle subsided, Lyra stood victorious, her form bathed in the ethereal glow of her triumph." 
    "With a serene smile, she ascended to the heavens, her spirit merging with the stars themselves as a testament to her sacrifice and valor."
    "And thus, the city rejoiced, for their champion had transcended mortal bounds, becoming a celestial beacon of hope for all eternity."

    return

label ConfrontWithAllies:
    scene throne
    with fade
    play music "06 - Battle! (Zinnia).mp3" fadeout 1
    "As Lyra and her allies advanced into the chamber to confront the Eclipse Lord, tension crackled in the air like lightning. The Eclipse Lord’s sinister laughter echoed off the walls as he welcomed their challenge, his dark presence looming over them like a specter of doom."
    show EL at right
    with dissolve
    el "Ah, the heroes arrive at last. How delightful! Let us dance, my darlings, in the shadows of despair!"
    "With a flourish of his hand, the Eclipse Lord unleashed a torrent of shadowy tendrils, snaking towards them with deadly intent."
    play sound "Extrasensory.mp3"
    "Lyra and her allies sprang into action, each drawing upon their unique skills in a desperate bid to fend off the onslaught."
    show lyra angry at left
    with dissolve
    l "Stand firm, my friends! Together, we shall overcome this darkness!"

    "As the battle reached its climax, Lyra and her allies fought bravely against the Eclipse Lord and his minions." 
    "Despite the overwhelming odds, they refused to yield, their determination shining brightly amidst the encroaching darkness."
    play sound "Happy Hour.mp3"
    if SparrowTere:
        hide EL
        show Sparrow talk at right
        with dissolve
        Sp "Keep 'em coming! I've got plenty more where that came from!"
        hide Sparrow talk
    if VexTere: 
        hide EL
        show Vex talk at right
        with dissolve
        V "Feel the wrath of the arcane, foul creatures of the night!"
        hide Vex talk

    hide Lyra angry
    with dissolve
    show kael angry at right

    k "For the people! For justice!"

    if tristanThere:
        "But amidst the chaos, a shadow fell upon their fellowship. Sir Tristan, once their ally, now stood apart, his eyes burning with betrayal."
        play sound "Bolt Strike.mp3"
        "With a swift motion, he turned his blade upon Lyra, his allegiance to the Eclipse Lord revealed."

        show tristan talk at left
        with dissolve
        st "You were fools to trust me! The Eclipse Lord's power is unmatched, and I shall rise with him to claim my rightful place!"

        "Before Lyra could react, Kael threw himself in front of her, taking the brunt of Sir Tristan's attack." 
        "With a cry of pain, he collapsed to the ground, his lifeblood staining the chamber floor."
        hide tristan talk
        hide kael angry
        show lyra sad at left
        with dissolve
        l "Kael!"

        "Lyra's heart shattered as she watched her dear friend fall, his sacrifice etched into her soul like a dagger."
        "In that moment, the weight of loss threatened to consume her, but from the depths of despair, a spark of determination ignited within her."
          
        l "Kael... No! I won't let your sacrifice be in vain! We will prevail, I swear it!"

        "Despite the betrayal and the sacrifice of their comrade, Lyra felt a surge of determination rising within her. "
        "With renewed resolve, she faced the Eclipse Lord, her voice ringing out with unwavering conviction."
        show lyra angry at left
        show EL at right
        with dissolve
        l "We can do this! Together, we are unstoppable!"

        play sound "Aurora Veil.mp3"
        "With a defiant cry, she poured every ounce of her strength into a final, devastating attack, her magic blazing bright as it collided with the darkness. "
        "In a blinding flash of light, the Eclipse Lord was vanquished, his malevolent presence dissipating into nothingness."
        

        l "We did it. We won."

        "As the echoes of battle faded away, Lyra and her allies stood victorious, their breaths coming in ragged gasps as they surveyed the aftermath of their victory." 
        "With a sense of relief and gratitude, Lyra turned to her companions, her heart overflowing with pride."

        show lyra happy at right
        with dissolve
        l "We did it, my friends. Against all odds, we prevailed."

        scene city1
        with fade
        play music "07 - Per Aspera Ad Astra.mp3" fadeout 1
        "With those words echoing in their hearts, Lyra and her remaining allies pressed on, their spirits unbroken even in the face of treachery and loss. "
        "Together, they fought with all their strength, their bond forged in the crucible of adversity."
        "In the end, it was their unity that proved victorious, as they stood tall against the darkness, their victory a testament to the power of courage, friendship, and the enduring spirit of those who dare to defy the shadows."
    
    else:
        "With each strike, each spell cast, they pushed back against the Eclipse Lord’s forces, inching closer to victory with every passing moment." 
        "As the Eclipse Lord’s defenses began to falter, Lyra felt a surge of hope welling up within her."

        show lyra normal at right
        with dissolve
        l "We can do this! Together, we are unstoppable!"

        "With a defiant cry, she poured every ounce of her strength into a final, devastating attack, her magic blazing bright as it collided with the darkness. "
        "In a blinding flash of light, the Eclipse Lord was vanquished, his malevolent presence dissipating into nothingness."

        l "We did it. We won."

        "As the echoes of battle faded away, Lyra and her allies stood victorious, their breaths coming in ragged gasps as they surveyed the aftermath of their victory." 
        "With a sense of relief and gratitude, Lyra turned to her companions, her heart overflowing with pride."

        show lyra happy at right
        with dissolve
        l "We did it, my friends. Against all odds, we prevailed."

        scene city1
        with fade
        play music "07 - Per Aspera Ad Astra.mp3" fadeout 1
        "Together, they returned to the city as heroes, their bravery celebrated by all who had been oppressed by the Eclipse Lord’s rule." 
        "And though their journey had come to an end, Lyra knew that their bond would endure, a shining beacon of hope in a world once shrouded in darkness."
        return

