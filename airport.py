def dest():
    if fnl_dest == "Vienna":
        vienna()
    elif fnl_dest == "Berlin":
        berlin()
    elif fnl_dest == "Prague":
        prague()
    elif fnl_dest == "United States":
        san_francisco()
    elif fnl_dest == "Paris":
        paris()
        
        
def tml():
    
    raw_input()
    print "The security gate went surprisingly smoothly without a beep,"
    print "and you were surprised that nothing went wrong."
    print "\n"
    print "Once this was over, you found the airport terminal"
    print "for %s." % fnl_dest
    print "Finding it was surprisingly smooth as well for"
    print "the terminal television screens proved to be useful."
    raw_input()
    print "You sit down at a random seat, and think of what"
    print "to do because you have 2 hours and a half to kill."
    print "What do you want to do?"
    
    do = raw_input("> ")
    
    if "eat" in do:
        print "You close your eyes. Seconds later, "
        print "an intense smell of BBQ fried chicken dipped in"
        print "vegetable oil lights of an are of your brain.\n"
        print "Your eyes open as your robotically stand up"
        print "and fast-walk to where the smell comes from."
        print "Turns out to be a resaurant selling junk food."
        print "\n"
        print "You cannot resist the temptation and decide to"
        print "order an extra large french fries with 2 chicken breasts."
        print "The cost?"
        raw_input()
        print "43 credits."
        raw_input()
        print "'Hell how can this be soooo expensive. Look I'm poor you know...'"
        print "'My dear client, you ordered 2 chicken breasts, and one extra"
        print "large french fries. Individual chicken breast price is 17 credits,"
        print "an extra large french fries is 6 credits, and the rest is tax.'"
        raw_input()
        print "'Ok then. Then explain to me why this is so goddamn expensive.'"
        print "'That's because you are at an airport. Prices at airports are inflated.'"
        print "'Fine... I get it now.'"
        raw_input()
        print "After the transaction you happily eat your order while"
        print "your stomach stopped growling and working full-force.\n"
        print "You go sit back down to the same spot, and wait for your flight."
        dest()
        
    elif do == "wait":
        print "You decide to wait on your seat until flight time."
        print "Nothing special happens as you watch the wall clock rotate."
        dest()
    
    
    elif "sleep" in do:
        print "Time flows by way too slowly, and you had a long day."
        print "You close your eyes, and fall into deep sleep."
        print "The announcer calls passengers to board the plane."
        print "You remain asleep as you dream about %s." % fnl_dest
        print "You announcer calls your name."
        print "No buldge.\n"
        print "The airplane leaves. You wake up three hours later."
        over("You realize you missed your plane because you sleep,",
             "and feel stupid as you go back home...")
        
  
    else:
        print "You %s, then wait for your ride to glory."
        dest()
        

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
        print "'Hey counter lady, I see a calm gold ring rimmed 
        print "with gold. Are you married?'"
        print "'Yes, and to a wonderul man'"
        cntr_lady()
        
    elif "math" or "mathematics" in ask:
        print "'Hey sup. I've got a question for you. A question"
        print "showing tireless endeavors of the human mind...'"
        print "'What is %3.0f?" % (352/2+42/3+60*5-448)'"
        print "'Lemme think a 'lil about it.'"
        ans = raw_input('What is the answer?: )
        print "'The answer's %3.0f!" %ans
        print "'Not the right answer counter lady...'"
        raw_input()
        print "'Answer's the answer to the ultimate question of"
        print "life, the universe and everything.'"
        print "*Counter Lady stares at %s without showing any facial" %first
        print "expression whatsoever*" 
        print "'Must have been a good joke to you haha! Here's another one: '"
        print "'Develop a mathematical theory to build a functional"
        print "model of the brain that is mathematically consistant"
        print "and predicative rather than merely biologically inspired.'"
        raw_input()
        print "'Enough with this sir! I'm presently working, and not talking"
        print "about stuff nerds say in bars.'"
        print "'Let's get going with the purpose of why you showed up to this airport.'"
        cntr_lady()
        
    elif "life" in ask:
        print "Hello counter lady! A simple analyses of your eyes tells me your" 
        print "soul is as pure as paradise. Correct me if I'm wrong.'"
        print "*Counter lady blushes*"
        raw_input()
        print "'Ya know I've always wondered deep down the power of life'"
        print "'What do you mean?'"
        print "'You see life is, but a holy grail for one to develop their"
        print "full potential, push their inner boundaries,"
        print "and create great stuff they'll be remembered for.'"
        print "'Uhm.... ok?'"
        print "'Developping one's full potential proves to be one of" 
        print "the most satisfactory experience ever.'"
        print "'What do you think of this, my lady?'" 
        raw_input()
        print "'Ok, lemme get this straight. ONE. I am not your lady and never"
        print "will be; look at my wedding ring.'"
        print "'TWO. I know what you mean and WILL reflect on it.'"
        print "'But now is not time you see I am on my shift serving"
        print "clients, and you are no exception.'"
        print "'I'm sorry to say, but I got no time for this... look at the queue behind you.'"
        raw_input()
        print "*%s peers quickly behind*"
        raw_input()
        print "'Awe s*** you are right.'"
        print "'Perfect. Then let's get down to business.'"
        cntr_lady()
        
    elif "hate" in ask:
        print "*You need to vent your anger off to someone for you" 
        print "cannot accept how huge the airport is*"
        print "'I hate you. You look great, and all with that hair" 
        print "and smile. But, I hate you you ugly little piece of ****."
        print "Oh excuse me let me dress up sexy and work in an airport"
        print "for a bunch of pervs look at how beautiful I am."
        print "*While raising your fist...* I no hate you; I despise you -'"
        print "*Counter lady presses on the concealed help button*"
        raw_input()
        print "*A bulky 6'3\" security guard arrives to counter lady's" 
        print "desk while %s continues to harass her*" % first
        raw_input()
        print "'You big fat son of a b*** what the f*** do you want'"
        print "*As you realise what you have just said to someone twice your meat*"
        raw_input()
        print "'Harassing workers at the airport is a violation" 
        print "of %s's Airport Security Law.'" % country
        print "'The law is the law, and you are expelled from "
        print "this airport for the rest of 2012.'"
        raw_input()
        print "'HA! ME NO CARELESS THE WORLD WILL END ON DECEMBER 21st!'"
        print "*Bulky security guard grabs you by the neck and throws you" 
        print "out of the aiport's main entrance.*"
        print "'Go away, and never come back.'"
        over(Well damn... What have I done? How will I explain this to my love...)
        
    else:
        print "You determine not to ask about this; you decide to skip straight" 
        print "to the meat and bone of why you came to the airport."
        cntr_lady()   
       
    
    def cntr_lady():
        print "'Great! Anways, so I  finally decided to travel.'"
        print "'Please hand me your check-in ticket.'"
        print "'What is that?'"
        print "*sigh* You are supposed to check-in at that terminal over there... Check-in is" 
        print "basically your flight ticket scanned by the machine.'"
        raw_input()
        print "'Oh...'"
        raw_input()
        print "'No worries though! I am here to help.'"
        print "'First things first, please show me your flight receipt.'"
        print "Having no idea what a flight receipt is... you: "
            
        receipt = raw_input("> ")
            
        if receipt == "pull out a random receipt" or "show a random receipt" 
                      or "pull out a receipt" or "show a receipt" or "show receipt":
            print "You show a random receipt to the clerk, thinking it'll do."
            print "*Counter lady laughs out loud*"
            print "The funny type you are haha! Unfortunately," 
            print "this is not an airplane ticket receipt."
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
                print "*The counter lady scans through the flight database for" 
                print "current available flights with empty seats...*"
                raw_input()
                print "'Ding!'"
                raw_input()
                print "'Today's flights: %s'" %dests
                print "'Now, choose your destination, and we shall begin transaction.'"
                
                fnl_dest = raw_input("> ")
                  
                if  "Vienna" in fnl_dest:
                    print "'What good is there is see in Vienna?'"
                    raw_input()
                    print "'Vienna IS the capital of music, more specifically, classical music.'"
                    print "'Apart from that, there is the huge baroque Schonbrunn Palace, the totally majestic and"
                    print "the grandiose St. Stephen's Cathedral, and the Ringstrasse."
                    print "There is a lot to do in Vienna."
                    print "Although quite small in size relativement speaking, it packs a bunch."
                    print "And it has to be one of the world's cleanest cities. No kidding.'"
                    print "'Believe me, it is a great destination!'"
                    raw_input()
                    print "'I want to travel to Vienna!'"
                    print "'How long?'"
                                              
                    while True: 
                     
                        long = raw_input("> ")
                        
                        if long == "one week" or "seven days":
                            print "'%s'" %long
                            print "'Perfect.\nTotal price is 1241 credits.'"
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
                            True
                            tml()
                    
                        else:
                            print "'I'm sorry, but there are no flights for %s.'"
                            False                        
                    
                
                elif "Paris" in fnl_dest:
                    print "'What good is there to see in Paris?'"
                    raw_input()
                    print "'Paris is one of the world's top destinations. Expect tons of tourists."
                    print "This is not intended to be a bad thing."
                    print "Obviously, one absolutely has to check out the 301m-high Eiffel Tower from every angle."
                    print "The louvre proves to be one robust museum to go to. The world's most mysterious painting, the"
                    print "Mona Lisa, lies there and is a must to see."
                    print "Apart from that there is the Defense Headquarters, the Arche de Triomphe, the" 
                    print "Palace of Versailles, and many, man more."
                    print "Totally recommended!'"
                    raw_input()
                    print "'Wow! Sounds quite impressive!'"
                    print "'I totally want to travel there as my first destination!'"
                    raw_input()
                    print "'Perfect. Let's get down to business then.'"
                    print "'How long are you planning your trip?'"                   
                    
                    while True:
                    
                        long = raw_input("> ")
                        
                        if long == "one week" or "seven days":
                            print "'Perfect, now let's get things going."
                            print "Total price is 1342 credits.'"
                            raw_input()
                            print "%s pays Counter Lady with a debit card." %first
                            print "TRANSACTION STATUS: IN PROGRESS"
                            raw_input("3")
                            raw_input("2")
                            raw_input("1")
                            print "TRANSACTION STATUS: DONE."
                            raw_input()
                            print "'Congratualtions traveller!'"
                            raw_input()
                            print "'Uh, hey thanks kind counter lady.'"
                            raw_input()
                            print "'Ok good now hand me your passport.'"
                            print "Counter Lady checks the passport, and stamps a blanck page."
                            print "Counter Lady hands it back to %s." %first
                            raw_input()
                            print "'Good, now put your luggage right beside me to then dispatch it to the plane cargo.'"
                            print "'Basically, it's a check-in process.'"
                            print "%s carefully lies the luggage where demanded."
                            print "'Ok good now here is your ticket.'"
                            print "'This is no doubt your most precious possession until flight departure.'"
                            print "'Do not lose it. I repeat. DO NOT LOSE IT.'"
                            raw_input()
                            print "'Roger.'"
                            print "'So what's next?'"
                            raw_input()
                            print "'Yes, right. Simply go to pass the security gate over there.'"
                            print "'Once passed, simply go to the Paris Gate as indicated on the ticket and screen terminals.'"
                            print "'Flight departure is in three hours and a half.'"
                            raw_input()
                            print "'Alright! I should go. Farewell kind counter lady!'"
                            print "'Farewell traveller, and enjoy your trip!'"
                            True
                            tml()
                                                        
                        else:
                            print "'I'm sorry, but there are no flights for %s.'"
                            False 
                    
                                             
                elif "Berlin" in fnl_dest:
                    print "What good is there in Berlin?"
                    raw_input()
                    print "'Berlin. The city once destroyed by the war. Mostly rebuilt from scratch."
                    print "Berlin. The city that once has seen Hitler's rise and fall."
                    print "You will find countless historical museums as well as countless holocaust victims."
                    print "Whilst walking around town, you'll weep as its atmosphere engulfs you."
                    print "It a city like no ther. You will also discover The futuristic square with a huge television screen."
                    print "I recommend it.'"
                    raw_input()
                    print "'Alright, I wanna travel there!'"
                    print "'Perfect. Let's get down to business then.'"
                    print "'How long are you planning your trip?'"  
                    
                    long = raw_input("> ")
                    
                    while True:
                    
                        if long == "one week" or "seven days":
                            print "'Simply a week ma'am!'"
                            raw_input()
                            print "'Alright, perfect. Total's 1121 credits.'"
                            print "Counter lady hands the debit card machine to %s" % first
                            print "%s pays the total." % first
                            print "You hand back the debit card machine to the counter lady."
                            print "She gives you your airplane ticket."
                            raw_input()
                            print "'Alright, next up's the passport, please hand it to me for a second.'"
                            print "%s hands the passport to the counter lady." % first
                            print "Counter lady nods, looks at it, stamps a blank page, and hands it back to %s." % first
                            print "'Alright, next up's the luggage check-in. Please hand me your luggage.'"
                            print "You hand your luggage to her, and she puts it on the rolling carpet."
                            raw_input()
                            print "'Good! Everything's set. Now, simply pass the security gate, then"
                            print "go to the designated gate of your flight written on your travel ticket."
                            print "Flight departure is in 2 hours and a half.'"
                            raw_input()
                            print "'Well that was quite quick... I mean the process. I thought it"
                            print "would have taken around 1 hour or something to check-in.'"
                            print "'Anyways, if I understood correctly, I go up to that security guard then"
                            print "I go to the Berlin terminal, correct?'"
                            raw_input()
                            print "'Correct'"
                            print "'Well thank you kind counter lady! I appreciate your help.'"
                            raw_input()
                            print "'Good day counter lady, farewell!'"
                            print "'Take care, traveller! Make sure not to turn into a nazi!'"
                            True
                            tml()
                            
                        else:                        
                            print "'I'm sorry, but there are no flights for %s.'"
                            False 
                        
                        
                elif "Prague" in fnl_dest:
                    print "'Tell me about Prague, young one.'"
                    raw_input()
                    print "'One of the oldest cities in the world."
                    print "'I mean it has not been continuously bombarded during the"
                    print "second World War. Hence, it has retained its medieval architecture."
                    print "A truly spectacular city to be in. People love to party over there."
                    print "There's the Old Town Square where every day, people or bands come animate the crowds."
                    print "It is truly unique. Plus, there is this astronomical clock built a couple hundred years back.'"
                    print "'I totally recommend it.'"
                    raw_input()
                    print "'Whoah! Now you totally sold me! I really want to go there!'"
                    print "'You won't regret it! Now, let's get down to business then.'"
                    print "'How long are you planning your trip?'"                   
                                       
                    while True:
                        long = raw_input("> ")
                        if long == "one week" or "seven days":
                            print "'%s kind counter lady!'" % long
                            print "'Good. So the total's 1438 credits'"
                            print "Counter lady hands the debit card machine to %s" %first
                            print "Transaction has been successful, and %s hands it back to her."
                            raw_input()
                            print "'Alright, now hand your passport to me, and drop your luggage" 
                            peint "on the rolling carpet here.'"
                            print "You hand your passport to counter lady. While she checks stuff inside," 
                            print "you drop your luggage where demanded."
                            print "'Lucky you! Such a nice stamp this will be in your passport.'"
                            print "Counter lady presses a blank page in %s's passport." % first
                            print "She hands it back to her client."
                            raw_input()
                            print "'Alright, this is done, and the luggage is done.'"
                            print "'Ok, so what's next?'"
                            print "'Next step is to pass the security gates, and then go to the Prague terminal.'"
                            print "Counter lady gives a plane ticket to her client."
                            print "'This is your plane ticket. Do not lose it. I repeat. DO NOT LOSE IT.'"
                            print "'If ever you don't find the Prague terminal, simply check an terminal screen!'"
                            print "'Any questions?'"
                            raw_input()
                            print "'Actually, everything's clear to me!'"
                            print "'Glad to hear!'"
                            print "'Now, I should get going... Farewell kind counter lady!'"
                            print "'Take care traveller, and enjoy going back through time!'"
                            tml()  
                            
                        else:                        
                            print "'I'm sorry, but there are no flights for %s.'"
                            False                                        
                    
            
                elif "United States" in fnl_dest:  
                    print "'I pick the most powerful country in the world! Mwouhahahaha.'"
                    print "'Unfortunately, only San Francisco remains as a flight destination in the US today."
                    print "'Is that ok?'"
                    
                    ok = raw_input("> ")
                    
                    if ok == "yes":
                        print "'Ok perfect. Total's 846 credits'"
                        print "'Wow that's really cheap!'"
                        print "'Indeed, one of the lowest prices since 2010.'"
                        print "'Coincidence perhaps? Cuz you know... it's the end of the world soon.'"
                        print "'Haha yeah no kidding... Anyway, let's cut to the chase; I've got many other clients.'"
                        print "Counter lady hands the debit card machine to %s." % first
                        print "TRANSACTION STATUS: IN PROGRESS"
                        raw_input("3...")
                        raw_input("2...")
                        raw_input("1...")
                        print "TRANSACTION STATUS: DONE."
                        raw_input()
                        print "You hand the machine back to the beautiful counter lady."
                        print "She then gives you something."
                        print "'That's your plane ticket. You will find the time of departure as well"
                        print "as the terminal gate number. Do not throw it to the trash can. I repeat."
                        print "DO NOT THROW IT AWAY.'"
                        print "'Roger.'"
                        raw_input()
                        print "'Now hand me your passport, and while I check it, lay your luggage"
                        print "'down there on that automatic rolling carpet.'"
                        raw_input()
                        print "You do as she says. Whilst looking at your passport, she suddenly stamps an empty page."
                        print "She hands it back to you."
                        print "'Perfect, now all that's left to do is for you to pass security, go to the designated"
                        print "San Francisco flight terminal, and wait."
                        print "'Ok cool thanks, I understood everything of what I gotta do.'"
                        print "'Horray!'"
                        raw_input()
                        print "'Alright, I should get going. Farewell kind counter lady!'"
                        print "'Alright, goodye traveller! Please come back in one piece from the States!'"
                        tml()
                                                             
                    elif ok == "no":
                        cntr_lady()
                    
                           
                else:     
                    print "'I'm sorry, but there are no flights for %s.'"
                    False         
                        
                                           
        else:    #else receipt   
            print "I'm sorry my dear, but this is not what I am looking for.'"
            cntr_lady()   
               
                

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
        print "You spot a beautifully slim Caucasian dressed in blue."
        print "From afar, whe appears to have blue eyes and brown hair."
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
        print "'Good morning sir, how does it work in here?\nIt is my first time" 
        print "travelling, and thus setting foot in an airport.'"
        print "\n'Take it easy traveller, life is full of mysteries."
        print "And there is a first to everyone.'"
        print "'As I can see, you are not familiar with how airports function."
        print "Basically, you see that line over there?'"
        raw_input()
        print "\n'Yeah, I do sir.'
        raw_input()       
        print "Ok good. Well, son, this is where the counter to check-in,"
        print "and drop your luggage is.'"
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
            print "'Basically, join the queue to your selected airline. The rest will fall"
            print "to place like a feather settling onto the ground'"
            raw_input()
            print "'Quite poetic you are! I like it.'"
            print "'Anyways, thank you for the information! I shall go.'\n Farewell young lady!'"
            print "'Good day young man!'"
            air1_counter()
            
        else:
            print "'Sup traveller? Welcome to %s's majestic airport!'"  %country
            raw_input()
            print "'Hey, It's my first time travelling, and I am not too familiar of what"
            print "I'm supposed to do. Can you guide me?'"
            raw_input()
            print "'Well, I can't hold your hand and guide you all the way through," 
            print "but I cetainly can tell you what to do.'"
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
        print "You close your eyes as a giant gush of wind flows down your nose" 
        print "as you sniff the lustrous divine smells."
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
        print "'I'll forget that I've seen a total stranger salivate"
        print "as he day dreams.'"
        print "'Agreed. I'll help you.'"
        print "'Basically you see those counters and queues over there?'"
        raw_input()
        print "'Yeah I see them.'"
        raw_input()
        print "'Well, you simply gotta go to your desired airline to check-in,"
        print "and the rest will fall into place.'"
        raw_input()
        print "'Cool thanks! By the way, are you an experienced traveller 
        print "of the seven seas?'"
        raw_input()
        print "'Indeed I am!'"
        raw_input()
        print "*You now feel weirdly excited for some reason*"
        print "'Cool! Anyways, I shall go.'"
        print "'Farewell young lady!'"
        raw_input()
        print "'Anytime! Farewell, newb.'"
        raw_input()
        print "You take one last look at her to imprint her physcial 
        print "divinity to your mind."
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
            over("""
                  'This is simply too huge for me.. I will lose myself,
                  inside the airport, and someone will kidnap me.'\n%s, 
                 "returns home, and lives his live without pushing through, 
                 "%s's limits. """ %(first, first))
               
            True
        
        elif next == "enter":
            print "Adrenaline rushes through your veins as you anxiously enter the huge glorious"
            print "airport entrance gates, not knowing what lies behind."
            True
            airtrance1()
            
        else:
            print "*%s gazes at the airport's exterieur architecture.*" %first
            print "'Man, this airport architecture has to be some of the best I've seen..."
            print "majestic, yet scary at the same time. A true art!'"
            print "*shrugs*"
            print "'Ok, I gotta choose what I want to do."
                                       
