#Loops over numbers 1-100
for x in range(1,101):
    #modulo operator is useful to check if a variable is divisable by another, if the remainder of the modulo operation is 0, the number is divisable.
    if x % 3 == 0 and x % 5 == 0:
        # IF LOOP VAR DIVISABLE BY 3 AND 5 PRINT FIZZBUZZ
        print('{} fizzbuzz'.format(x))
    else:
        if x % 3 == 0:
            # IF LOOP VAR DIVISABLE BY 3 PRINT FIZZ
            print('{} fizz'.format(x))
        elif x % 5 == 0:
            # IF LOOP VAR DIVISABLE BY 3 PRINT BUZZ
            print('{} buzz'.format(x))
        else:
            # IF LOOP VAR IS NOT DIVISABLE BY 3 OR 5 OR BOTH PRINT THE LOOP VARIABLE
            print(x)
