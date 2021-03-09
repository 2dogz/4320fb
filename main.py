# HARD CODED START AND STOP VALUES, PYTHON INDEX STARTS AT 0
start = 1
stop = 101

# HARD CODED DIVISIBLE VALUES, ABLE TO CHANGE NUMBERS MUCH FASTER
divisibleByA = 3
divisibleByB = 5

#Loops over numbers 1-100
for x in range(start,stop):
    #modulo operator is useful to check if a variable is divisible by another, if the remainder of the modulo operation is 0, the number is divisible.
    if x % divisibleByA == 0 and x % divisibleByB == 0:
        # IF LOOP VAR DIVISIBLE BY 3 AND 5 PRINT FIZZBUZZ
        print('{} fizzbuzz'.format(x))
    else:
        if x % divisibleByA == 0:
            # IF LOOP VAR DIVISIBLE BY 3 PRINT FIZZ
            print('{} fizz'.format(x))
        elif x % divisibleByB == 0:
            # IF LOOP VAR DIVISIBLE BY 3 PRINT BUZZ
            print('{} buzz'.format(x))
        else:
            # IF LOOP VAR IS NOT DIVISIBLE BY 3 OR 5 OR BOTH PRINT THE LOOP VARIABLE
            print(x)
