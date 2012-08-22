class Parent(object):

# function that will print
    def override(self): 
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent() # Has the Parent class
son = Child() # Has the Child class

dad.implicit() # Calls the Parent class with the implicit function
son.implicit() # Calls the Child class, but outputs the implicit function from the Parent class

dad.override() # Calls the Parent class with the override function
son.override() # Calls the Child class with the override function in the child class

dad.altered() # Calls the Parent class with the altered function
son.altered() # Calls the Child class with the altered function, but the child altered function has a super which outputs both the altered functions from the parent and child