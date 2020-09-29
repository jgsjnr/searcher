import os, time
def counting():
    x = 0
    cont = 10
    for x in range(11):
        print(x)
        x = ++x
        time.sleep(1)
        os.system('cls')
        if x == 10:
            break
    if x == 10:
        print('finished!')
