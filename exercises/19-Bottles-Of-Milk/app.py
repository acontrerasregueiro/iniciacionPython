def number_of_bottles():
    cancion = ''
    una_botella = '1 bottle of milk on the wall, 1 bottle of milk.'
    sinbotellas = 'No more bottles of milk on the wall, no more bottles of milk.Go to the store and buy some more, '
    for i in range(99,0,-1):
        #print(i)
        if i != 0 and i!=1:            
            cancion = cancion + str(i) + ' bottles of milk on the wall, '
        elif i==1:
            cancion = cancion + una_botella
        else:
            cancion = cancion + sinbotellas
    print(cancion)


number_of_bottles()