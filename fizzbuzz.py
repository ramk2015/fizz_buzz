n=100
count = 1
print ("Fizz buzz counting up to {}".format(n)) 
while count <=n:
    if count % 3 == 0 and count % 5 == 0:
        print "fizz buzz"
    elif count % 3 == 0:
        print "fizz"
    elif count % 5 == 0:
        print "buzz"
    else: print count
    count += 1
print "done"