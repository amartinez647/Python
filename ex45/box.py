from random import randint

class Pyramid(object):

    def __init__(self, start):
        self.quips = [
            "Oh well...",
             "Does bad luck run in your family?",
             "Don't cry, it's just a game.",
             "Loser! Ha ha!"
        ]
        self.start = start

    def play(self):
        next_room_name = self.start

        while True:
            print "\n--------"
            room = getattr(self, next_room_name)
            next_room_name = room()


    def death(self):
        print self.quips[randint(0, len(self.quips)-2)]
        exit(1)

    def box_level_one(self):
        print "You are strolling through the forest when you come across a pyramid of boxes with envelopes in each one."
        print "The bottom of the pyramid has four small boxes." 
        print "The middle has three small boxes,"
        print "and the top has two small boxes."
        print "There are instructions there that say to pick one of the four boxes at the bottom and open the envelope inside."
        print "Your goal is to pick the right envelope to move you up to the next level of boxes."
        print "\n"
        print "Which one do you choose?"

        action = raw_input("> ")

        if action == "Box One":
            print "Inside the envelope there's a note that reads..."
            print "You lose!!! Better luck next time!"
            return 'death'

        elif action == "Box Two":
            print "Inside the envelope there's a note that reads..."
            print "You lose!!! My 3 year old can pick a better envelope than you!"
            return 'death'

        elif action == "Box Three":
            print "Inside the envelope there's a key with a note that reads..."
            print "You win!!! Please use this key to open one of three boxes from the next level up."
            return 'box_level_two'
            
        elif action == "Box Four":
            print "Inside the envelope there's a note that reads..."
            print "You lose!!! You have such horrible luck!"
            return 'death'

        else:
            print "You only have to pick a number from one to four! It's not that hard!"
            return 'box_level_one'
            
    def box_level_two(self):
        print "Which box are you going to open?"

        action = raw_input("> ")

        if action == "Box One":
            print "Inside the box is an envelope with a key and a note that reads..."
            print "Woo hoo!!! You get to move up to the next level!"
            print "If your luck continues, you will win the golden prize! But...it's a surprise!"
            return 'box_level_three'

        elif action == "Box Two":
            print "Inside the box is an envelope with a note that reads..."
            print "Sorry!!! Maybe you'll pick the right box in your next life! Ha ha!"
            return 'death'

        elif action == "Box Three":
            print "Inside the box is an envelope with a note that reads..."
            print "Bummer!!! You sure aren't good at this!"
            return 'death'

        else:
            print "You only have to pick a number from one to three! Geez!"
            return 'box_level_two'
            
    def box_level_three(self):
        print "Ok, the pressure is on!"
        print "Which box are you going to open? Box one or two?"

        action = raw_input("> ")
		
        if action == "Box One":
            print "Inside the box is an envelope with a note that reads..."
            print "You win the golden prize!!! But first, you must crack the code to completely unlock your prize."
            
            code = "%d%d%d" % (5,6,7)
            guess = raw_input("[keypad]> ")
            guesses = 0

            while guess != code and guesses < 2:
               print "BEEP!"
               guesses += 1
               guess = raw_input("[keypad]> ")
            
            if guess == code:
               print "You cracked the code!"
               print "A trip to see Justin Bieber in concert!!! OMG!!"
               print "Why do you look so disappointed? Did you think you were going to win a large sum of money? Bah ha ha!"
               exit(0)
            
            else:
               print "The lock beeps for the last time."
               print "What a shame! And the golden prize was pretty awesome!"
               return 'death'
               exit(0)

        elif action == "Box Two":
            print "Inside the box is an envelope with a note that reads..."
            print "You lose!! What a shame! And the golden prize was super awesome too!"
            exit(0)

        else:
            print "You only have to pick one or two! Come on!"
            return 'box_level_three'