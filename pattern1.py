def pattern(n=5):
    for i in range(n):
        for j in range(i+1):
            print("* ",end=' ')
        print()

    for k in range(n*2):
        print('*  *')
    return

pattern(13)
