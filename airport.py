def air1_counter():

    dests=['Berlin','Paris','Vienna','Prague','United States']
    
    print "*%s sees a queue to the counter and decides to line up*" %first
    raw_input()
    print "*10 minutes later...*"
    raw_input()
    print "'Welcome to %s's greatest aiport!'" %country
    print "*%s shivers*"
    ask = raw_input('> Ask something about: ")
    
    if "marriage" in ask:
        print "'Hey counter lady, I see a calm gold ring rimmed with gold. Are you married?'"
        print "'Yes, and to a wonderul man'"
        cntr_lady()
        
    elif "math" or "mathematics" in ask:
        print "'Hey sup. I've got a question for you. A question showing tireless endeavors of the human mind...'"
        print "'What is %3.0f?" % (352/2+42/3+60*5-448)
        print "'Lemme think a 'lil about it.'"
        ans = raw_input('What is the answer?: )
        print "'The answer's %3.0f!" %ans
        print "'Not the right answer counter lady...'"
        raw_input()
        print "'Answer's the answer to the ultimate question of life, the universe and everything.'"
        print "*Counter Lady stares at %s without showing any facial expression whatsoever*" %first
        print "'Must have been a good joke to you haha! Here's another one: '"
        print "'Develop a mathematical theory to build a functional model of the brain that is mathematically consistant and predicative rather than merely biologically inspired."
        raw_input()
        print "'Enough with this sir! I'm presently working, and not talking about stuff nerds say in bars.'"
        print "'Let's get going with the purpose of why you showed up to this airport.'"
        cntr_lady()
        
    elif "life" in ask:
        print "Hello counter lady! A simple analyses of your eyes tells me your soul is as pure as paradise. Correct me if I'm wrong.'"
        print "*Counter lady blushes*"
        raw_input()
        print "'Ya know I've always wondered deep down the power of life'"
        print "'What do you mean?'"
        print "'You see life is, but a holy grail for one to develop their full potential, push their inner boundaries, and create great stuff they'll be remembered for.'"
        print "'Uhm.... ok?'"
        print "'Developping one's full potential proves to be one of the most satisfactory experience ever.'"
        print "'What do you think of this, my lady?'" 
        raw_input()
        print "'Ok, lemme get this straight. ONE. I am not your lady and never will be; look at my wedding ring.'"
        print "'TWO. I know what you mean and WILL reflect on it.'"
        print "'But now is not time you see I am on my shift serving clients, and you are no exception.'"
        print "'I'm sorry to say, but I got no time for this... look at the queue behind you.'"
        raw_input()
        print "*%s peers quickly behind*"
        raw_input()
        print "'Awe s*** you are right.'"
        print "'Perfect. Then let's get down to business.'"
        cntr_lady()
        
    elif "hate" in ask:
        print "*You need to vent your anger off to someone for you cannot accept how huge the airport is*"
        print "'I hate you. You look great, and all with that hair and smile. But, I hate you you ugly little piece of ****.\nOh excuse me let me dress up sexy and work in an airport for a bunch of pervs look at how beautiful I am.\n*While raising your fist...* I no hate you; I despise you -'"
        print "*Counter lady presses on the concealed help button*"
        raw_input()
        print "*A bulky 6'3\" security guard arrives to counter lady's desk while %s continues to harass her*" % first
        raw_input()
        print "'You big fat son of a b*** what the f*** do you want'"
        print "*As you realise what you have just said to someone twice your meat*"
        raw_input()
        print "'Harassing workers at the airport is a violation of %s's Airport Security Law.'" % country
        print "'The law is the law, and you are expelled from this airport for the rest of 2012.'"
        raw_input()
        print "'HA! ME NO CARELESS THE WORLD WILL END ON DECEMBER 21st!'"
        print "*Bulky security guard grabs you by the neck and throws you out of the aiport's main entrance.*"
        print "'Go away, and never come back.'"
        over(Well damn... What have I done? How will I explain this to my love...)
        
    else:
        print "You determine not to ask about this; you decide to skip straight to the meat and bone of why you came to the airport."
        cntr_lady()   
        
    
    def cntr_lady():
        print "'Great! Anways, so I  finally decided to travel.'"
        print "'Please hand me your check-in ticket.'"
        print "'What is that?'"
        print "*sigh* You are supposed to check-in at that terminal over there... Check-in is basically your flight ticket scanned by the machine.'"
        raw_input()
        print "'Oh...'"
        raw_input()
        print "'No worries though! I am here to help.'"
        print "'First things first, please show me your flight receipt.'"
        print "Having no idea what a flight receipt is... you: "
            
        receipt = raw_input("> ")
            
        if receipt == "pull out a random receipt" or "show a random receipt" or "pull out a receipt" or "show a receipt":
            print "You show a random receipt to the clerk, thinking it'll do."
            print "*Counter lady laughs out loud*"
            print "The funny type you are haha! Unfortunately, this is not an airplane ticket receipt."
            raw_input()
            print "'Well, at least I tried...'"
            raw_input()
            print "'Ok so let's do this the old fashion way.'"
            print "'We can purchase a ticket on the spot.'"
            print "'I cannot guarantee seat and destination availability though.'"
            raw_input()
            print "'So what am I supposed to do...?'"
            print "'I gotta tell you this is my first time travelling...'"
            raw_input()
            print "'No problem!'"
            print "'Where would you wish to go?'"
               
            dest = raw_input("Choose your travel destination: ")
              
            if dest != ("Prague" or "Berlin" or "Paris" or "United States" or "Vienna"):
                print "'I'm sorry traveller, but no seats are available for this destination today'"
                print "'Oooohhh.... kkk. What flights are available today?'"
                print "'Lemme check'"
                raw_input()
                print "*The counter lady scans through the flight database for current available flights with empty seats...*"
                raw_input()
                print "'Ding!'"
                raw_input()
                print "'Today's flights: %s'" %dests
                print "'Now, choose your destination, and we shall begin transaction.'"
                
                fnl_dest = raw_input("> ")
                  
                if  "Vienna" in fnl_dest:
                    print "'I want to travel to Vienna!'"
                    print "'How long?'"
                        
                    long = raw_input("> ")
                      
                    if long == "one week" or "seven days":
                        print "'%s'" %long
                        print "'Perfect.\nTotal price is 1241$.'"
                        print "*%s performs transaction*" %first
                        print "'Transaction DONE!!! I BOUGHT MY FIRST PLANE TICKET EVER!!!'"
                        raw_input()
                        print "'Congratulations! Now, please hand me your passport...'"
                        print "*Counter lady grabs %s's passport, opens the first page, compares passport picture to real life*"
                        print "*As she hands back the passport to %s...* You look like a criminal, but whatever...'"
                        print "'Here is your flight ticket. Do not lose it. I repeat. DO NOT LOSE IT.'"
                        print "'Now, lets check-in your luggage...'"
                        print "%s hands over luggage, and counter lady scans it and sends sends it through the luggage dispatch.*"
                        raw_input()
                        print "'%s, %s %s. Everything's set, and you are ready to pass the security gate, and wait for your flight to %s!'" %(last, first, last, dest)
                        print "'Flight departs in three hours.'"
                        print "'Simply go where I'm pointing, and everything will go great!'"
                        raw_input()
                        print "'Ok cool thank you kind lady!'"
                        print "'I shall go before missing my flight!'"
                        raw_input()
                        print "'Alright, farewell traveller. Enjoy your trip to %s!'" %fnl_dest
                        vienna_terminal()
                    
                    else:
                    
                
                elif "Paris" in fnl_dest:
            
                elif "Berlin" in fnl_dest:
            
                elif "Prague" in fnl_dest:
            
                elif "United States" in fnl_dest:  
            
                else:     
                            
                        
                        
                    
        else:    #else receipt      
               
                

def airtrance1():
    
    airtrce_list=['some people','a security guard', 'a check-in counter','a tourist information center']
    
    print "Smiling with a heart pounding fast, %s is absolutely proud to have entered an airport.\n\nA big feat.\n" %first
    print "Luggage held tightly in hand, you begin looking around.\n"
    print "Something lingers your mind though."
    raw_input()
    print "'What am I supposed to do once inside an aiport?"
    raw_input()
    print "You've spotted a couple of things: \n%s" %airtrce_list
    raw_input()
    
    next = raw_input("'I have no idea what to do so I'll go with: ")
    
    if airtrce_list[0] in next:   #some people
        print "You spot a beautifully slim Caucasian dressed in blue.\nFrom afar, whe appears to have blue eyes and brown hair."
        raw_input()
        print "'!!!'\n"
        print "'She seems to be travelling alone.'\n"
        print "As you approach her..."
        raw_input()
        air1_causian()
        
    elif airtrce_list[1] in next:  #the security guard
        print "A security guard stands a couple dozen meters from you."
        print "You approach him.\n"
        print "'Greetings traveller! Welcome to %s's most majestic airport!'" %country
        raw_input()
        print "'Good morning sir, how does it work in here?\nIt is my first time travelling, and thus setting foot in an airport.'"
        print "\n'Take it easy traveller, life is full of mysteries.\nAnd there is a first to everyone.'"
        print "'As I can see, you are not familiar with how airports function.\nBasically, you see that line over there?'"
        raw_input()
        print "\n'Yeah, I do sir.'
        raw_input()       
        print "Ok good. Well, son, this is where the counter to check-in, and drop your luggage is.'"
        print "'Go on ahead traveller."
        raw_input()
        print "'Thank you officer, I appreciate your advice.'"
        raw_input()
        print "'Take care traveller! And do NOT forget to take it easy!"
        print "\nThanks... Bye!"
        air1_counter()   
        
    elif airtrce_list[2] in next:  #airline counter
        air1_counter()

            
    elif airtrce_list[3] in next:  #tourist information center
        print "You decide to approach the tourist information center."
        print "Two people lie behind the counter: a woman and a man."
            
        info=raw_input("To Whom do you ask? ")
            
        if info == "woman":
            print "'Greetings, and a warm welcome to %s's greatest airport!'\n" %country
            print "'Well hello there charming lady!'"
            print "'I am new here, and I have never travelled. Where do I begin?'"
            raw_input()
            print "'It's rather simple young man.'\n"
            print "'Basically, join the queue to your selected airline. The rest will fall to place like a feather settling onto the ground'"
            raw_input()
            print "'Quite poetic you are! I like it.'"
            print "'Anyways, thank you for the information! I shall go.'\n Farewell young lady!'"
            print "'Good day young man!'"
            air1_counter()
            
        else:
            print "'Sup traveller? Welcome to %s's majestic airport!'"  %country
            raw_input()
            print "'Hey, It's my first time travelling, and I am not too familiar of what I'm supposed to do. Can you guide me?'"
            raw_input()
            print "'Well, I can't hold your hand and guide you all the way through, but I cetainly can tell you what to do.'"
            print "'Basically, join that queue over there.'"
            raw_input()
            print "'Ok thanks.'"
            raw_input()
            print "'Oh, and make sure it is the right queue. That latter is your desired airline.'"
            raw_input()
            print "'Alright, thanks. Bye.'"
            print "'Wishes to you traveller! Goodbye.'"
            air1_counter()
            
    def air1_causian(): 
        print "You close your eyes as a giant gush of wind flows down your nose as you sniff the lustrous divine smells."
        print "Images of what might happened in her past flash through your mind..."
        print "As you bob your head slowly whilst still having eyes closed."
        print "You start to salivate."
        raw_input()
        print "The lady looks stops and looks at you."
        print "'Eeeewwwwww' says the divine white Caucasian."
        raw_input()
        print "You quickly fall back on Earth, and swallow the saliva."
        print "'Oh sorry sorry sorry ma'am. I was day dreaming."
        print "'I hope so."
        raw_input()
        print "'Hey uhm I'm uhm new to travelling, and it is my first time at an airport.'"
        print "'I'm lost on what I'm supposed to do. Well, kind of."
        raw_input()
        print "A couple seconds later...\n"
        print "'I'll forget that I've seen a total stranger salivate as he day dreams.'"
        print "'Agreed. I'll help you.'"
        print "'Basically you see those counters and queues over there?'"
        raw_input()
        print "'Yeah I see them.'"
        raw_input()
        print "'Well, you simply gotta go to your desired airline to check-in.'"
        print "'The rest will fall into place.'"
        raw_input()
        print "'Cool thanks! By the way, are you an experienced traveller of the seven seas?'"
        raw_input()
        print "'Indeed I am!'"
        raw_input()
        print "*You now feel weirdly excited for some reason*"
        print "'Cool! Anyways, I shall go.'"
        print "'Farewell young lady!'"
        raw_input()
        print "'Anytime! Farewell, newb.'"
        raw_input()
        print "You take one last look at her to imprint her physcial divinity to your mind."
        print "You then walk towards the next big step..."
        air1_counter()
                       
def airport1():
    print '*' * (61-12)
    print "                Diary of the Void:    "
    print "        Chapter 2 - From Ignorance to Salvation" 
    print '*' * (61-12)  
    print "You arrive at %s's most majestic airport." %country
    print "The airport is so big, and grandiose it scares you."
    print "Upon arrival at the main entrance, what shall you do?"
     
    while True 
    next = raw_input("> ")
    
        if next == "leave": 
            over("'This is simply too huge for me.. I will lose myself inside the airport, and someone will kidnap me.'\n%s returns home, and lives his live without pushing through %s's limits." %(first, first))
            True
        
        elif next == "enter":
            print "Adrenaline rushes through your veins as you anxiously enter the huge glorious airport entrance gates, not knowing what lies behind."
            True
            airtrance1()
            
        else:
            print "*%s gazes at the airport's exterieur architecture.*" %first
            print "'Man, this airport architecture has to be some of the best I've seen... majestic, yet scary at the same time. A true art!'"
            print "*shrugs*"
            print "'Ok, I gotta choose what I want to do."                           
