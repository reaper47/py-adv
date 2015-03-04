from sys import argv, exit

game, first, last, age, country = argv

def over(why):
    print why, "Good job %s %s!" %(first,last)
    exit(0)

def start():
    print "*************************************************"
    print "         Welcome to Diary of the Void:    "
    print "   Chapter 1 - Misfortunate Soul of the Abyss"
    print "*************************************************"     
    raw_input()
    print "%s, greetings!" %first
    raw_input()
    print "You are about to embark on an adventure..."       
    print "An adventure partially based on a true story..."
    raw_input()
    print "Let the journey begin...\n"
    raw_input()
       
    print "The year is 2012. You are home alone drinking beer on a friday night."
    print "The time?"
    raw_input()
    print "A quarter 'till midnight."
    raw_input()
    print "The alcohol's flowing full force through your blood. You begin feeling tipsy."
    print "You stand up from the couch in front of the television."
    print "But you fall back down, unable to stand up."
    raw_input()
    print "You've simply been drinking too much."
    raw_input()
    print "The last sip now has been drank. Stars start swirling around your head."
    print "You rotate your head around to follow the stars, and you suddenly fall asleep.."
    raw_input()
    print "BANG!"
    print "You let go of the beer bottle unconsciously."
    raw_input()
    print "It shatters into a million fragments upon impact."
    raw_input()
    print "You continue sleeping without knowledge of what happened...\n"
    raw_input()
    print "\n...Eleven hours later..."
    print "'Honey? What the hell happened?'"
    print "*You look at the shattered glass and at the beer bottles lying around*"
    print "'God dammit... What have I done again?'"
    print "'Look I was alone yesterday night 'cuz you were out with your friends."
    print "I had a god dammned rough day yesterday at work --'"
    raw_input()
    print "'Alcoholic'"
    print "'I am NOT an alcoholic, baby. It is YOU who did NOT invite me yesterday.'"
    print "'I'm sorry... I...'"
    print "'Anyways, I'll clean my mess up, and the day will go on ok?'"
    raw_input()
    print "While cleaning your mess up...\nSuddenly something popped through your mind."
    raw_input()
    print "'My love! I was cleaning up, and something popped through my head!'"
    print "'How about we take a week off, and travel together to a destination!!??'"
    print "'Honey! This is a brilliant idea, but... but who will take care of the child?'"
    print "*Damn I should have not drank yesterday in the living room."
    print "Bad influence to Robert*"
    print "'I... I seriously don't know...'"
    print "\n*Honey hugs %s and whispers*\n'Look %s, live the dream you've always dreamnt." % first
    print "You are 32 years old.\n'I think it would be time for you to fulfill it.'" % first
    print "\n*%s presses chin on honey's shoulder while hugging*" %first
    print "'But I want to go with.'"
    print "'Courage my love, but this time I can't. Remember I've got no vacation time left" 
    print "this year.\nAnd our child needs someone.'\n'Now, %s, please, Christmas" % first
    print "is coming soon. It would be nice to bring \nnice pictures to our child, Robert!" 
    print "'Ok... True.'"
    print "'Once we're in 2013, I'll take two weeks off so that you and I can travel somewhere."
    print "Trust me, go somewhere you've always dreamnt of going to!'"
    raw_input()
    print "Life is short %s, life is short." %first
    raw_input()
    print "\nFour days later, %s has chosen his destination, and prepared his luggage for the trip."
    print "You are now ready to leave."
    raw_input()
    print "Before leaving for a week..."
    raw_input()
    print "*The couple kisses one last time*"
    raw_input()
    print "You reach for the main door, what is your final decision?"
    
        
    while True:
        next = raw_input("> ")
        
        if "stay" in next: 
            over("You are too afraid and insecure  of leaving without your lover.\nYou hence stay home,", 
                 "and enjoy your life.")
                 
        if next == "leave":
            print "You feel afraid and anxious of travelling alone for the first time."
            print "But, something's driving you... an invisible force. Xenophobia's striking you," 
            print "yet you resist and push forth"
            raw_input()
            print "You leave the house, and drive to the airport."
            True 
            airport1()
            
        else:
            print "*I gotta decide something*"  
                 
start()
    
    
    
    
