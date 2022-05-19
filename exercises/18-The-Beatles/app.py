# Your code here!!
def sing():
    cancion = ''

    for i in range(1,13):
        if i == 5:
            cancion = cancion + 'whisper words of wisdom, '
        elif i == 11:
            cancion = cancion + 'there will be an answer, '
        elif i == 12:
            cancion = cancion + 'let it be'
        else:
            cancion = cancion +'let it be, '
    return cancion

print(sing())