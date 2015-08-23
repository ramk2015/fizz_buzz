import sys
count = 1
try: 
    if sys.argv[1] > 0:
        upper=sys.argv[1]
except IndexError: 
    upper = raw_input ("enter number to do fizz buzz till ")
try:
    int(upper)
except ValueError:
    print "Dude...numeric inputs only"
    upper = raw_input ("enter number to do fizz buzz till ")
try:
    int(upper)
    print ("Fizz buzz counting up to {}".format(upper)) 
    while count <=int(upper):
        if count % 3 == 0 and count % 5 == 0:
            print "fizz buzz"
        elif count % 3 == 0:
            print "fizz"
        elif count % 5 == 0:
            print "buzz"
        else: print count
        count += 1
    print "done"
except ValueError:
    print "what part of numeric do you not understand...Bye"

