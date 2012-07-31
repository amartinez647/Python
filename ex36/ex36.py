from sys import exit

def pink_room():
    print "Here's the pink room. Do you like it?"

    next = raw_input("> ")
    if "Yes" in next:
        print "Awesome!"

    elif "No" in next:
        print "Bummer!"
        exit(0)
    else:
        dead("Goodbye!")
        
        
def purple_room():
    print "Here's the purple room. Do you like it?"

    next = raw_input("> ")
    if "Yes" in next:
        print "Awesome!"

    elif "No" in next:
        print "Bummer!"
        exit(0)
    else:
        dead("Goodbye!")
        
        
def blue_room():
    print "Here's the blue room. Do you like it?"

    next = raw_input("> ")
    if "Yes" in next:
        print "Awesome!"

    elif "No" in next:
        print "Bummer!"
        exit(0)
    else:
        dead("Goodbye!")


def dead(why):
    print why, "Goodbye!"
    exit(0)
    
def start():
    print "What is your favorite color? Pink, purple or blue?"

    next = raw_input("> ")

    if next == "pink" or "Pink":
        pink_room()
    elif next == "purple" or "Purple":
        purple_room()
    elif next == "blue" or "Blue":
        blue_room()
    else:
        dead("You seriously need color in your life.")
        
        
start()