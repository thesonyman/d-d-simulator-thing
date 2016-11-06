import os, random, time

hit = 0

humans = 10
hum_health = 15

en_Guards = 5
en_health = 15
x = 1000
gwin = 0.0
enwin = 0.0
for i in range(0, 1000):
    z = False
    b = True
    #print ("repeat")
    while b == True:
        #print ("start")
        #time.sleep(1)
        z = False
        while z == False:
            #print ("1")

            hit = random.randint(1, 20)
            if hit >= 10:
                en_health = en_health - random.randint(1, 4)
            if en_health >= 0:
                en_Guards = en_Guards - 1
                    #print("dead guard")
                en_health = 15
            hit = random.randint(1, 20)
            if hit >= 10:
                hum_health = hum_health - random.randint(1, 8)
            if hum_health >= 0:
                humans = humans - 1
                #print("dead human")
                hum_health = 15

            if humans <= 0:
                #print ("Guards win")
                enwin = enwin + 1
                human = 10
                z = True
                b = False

            if en_Guards <= 0:
                #print ("Humans win")
                gwin = gwin + 1
                en_Guards = 5
                z = True
                b = False



    x = x - 1
    #print x

    if x <= 0:
        print ("Done")
        cats = gwin
        dogs = enwin
        print cats
        print dogs
