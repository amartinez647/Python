from sys import exit



def right_tunnel():
    print "There is a herd of sheep blocking the road."
    print "Do you honk at the sheep, run over the sheep, or play with the sheep?"
    sheep_moved = False

    while True:
        next = raw_input("> ")

        if next == "run over":
            dead("How horrible!!")
        elif next == "honk" and not sheep_moved:
            print "The sheep baa really loud, but move out of the way."
            sheep_moved = True
            exit(0)
        elif next == "honk" and sheep_moved:
            dead("Well...maybe you should try something else genius!")
        elif next == "play":
            dead("Great! You live happily ever after with the sheep!")
        else:
            print "That's not an option!"


def middle_tunnel():
    print "You are starving and come across an apple tree."
    print "Do you keep driving or stop to eat some apples?"

    next = raw_input("> ")

    if "keep driving" in next:
        exit(0)
    elif "apples" in next:
        dead("Those were some good apples!")
    else:
        start()


def dead(why):
    print why, "Well...better luck next time!"
    exit(0)

def start():
    print "You are driving down a long windy road."
    print "You come to three tunnels."
    print "Do you choose to go through the one to the left, middle, or right?"

    next = raw_input("> ")

    if next == "right":
        right_tunnel()
    elif next == "middle":
        middle_tunnel()
    elif next == "left":
        dead("That tunnel drops you into a black hole!")
    else:
        dead("You only had three choices...left, middle or right!")


start()