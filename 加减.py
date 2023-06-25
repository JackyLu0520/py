def plus():

    print((int(input('')) + int(input('+'))))

def minus():

    print((int(input('')) - int(input('-'))))

while 1:
    if (input('plus or minus?') == 'plus'):
        plus()
    else:
        minus()
