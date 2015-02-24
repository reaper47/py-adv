def air1_counter():

    dests=['Berlin','Paris','Vienna','Prague','United States']
    
    print "*%s sees a queue to the counter and decides to line up*" %first
    raw_input()
    print "*10 minutes later..."
    raw_input()
    print "'Welcome to %s's greatest aiport!'" %country
    # ADD PATHS HERE AS WRITTEN ON PAPER
    print "'Hey 'maam sup? So I  finally decided to travel.'"
    print "'Please hand me your check-in ticket.'"
    print "'What is that?'"
    print "*sigh* You are supposed to check-in at that terminal over there... Check-in is basically your flight ticket scanned by the machine.'"
    raw_input()
    print "'Oh...'"
    raw_input()
    print "'No worries though! I am here to help.'"
    print "'First things first, please show me your flight receipt.'"
    print "*Having no idea what a flight receipt is... you: *"
            
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
            
    def air1_causian(): ###
                
            
                
     

def airport1():
    print "*************************************************"
    print "                Diary of the Void:    "
    print "        Chapter 2 - The Airport of %s" %country
    print "*************************************************"  
    print "You arrive at %s's most majestic airport." %country
    print "The airport is so big, and majestic it scares you."
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
                             
