import time
import random
import string

yes = string.ascii_letters + string.punctuation + string.digits + ' '

def printt(toprint):
    attempts = 0
    curr = random.choice(yes)
    for char in toprint:
        while True:
            e = random.choice(yes)
            curr = curr[:-1] + e
            print(curr)
            attempts += 1
            time.sleep(0.005)
            if e == char:
                curr += random.choice(yes)
                break
    print("Printed {} in {} attempts".format(toprint, attempts))

printt(input("cat program but slow \n> "))