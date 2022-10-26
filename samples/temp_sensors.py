from firebase import firebase
from random import randrange, random
from time import sleep
import sys
import signal

def Exit_gracefully(signal, frame):
    print("\n>>>> Bye.\n")    
    sys.exit(0)

db_url = 'https://app-2022f-default-rtdb.firebaseio.com/'

fdb = firebase.FirebaseApplication(db_url, None)

def main():
    # fdb.delete('','/J101')
    while True:
        fdb.put('/P306', 'k1', randrange(10,40))
        fdb.put('/P306', 'k2', randrange(10,60))
        fdb.put('/J405', 'k1', randrange(10,40))
        fdb.put('/J405', 'k2', randrange(10,40))
        fdb.put('/J405', 'k3', randrange(10,60))
        fdb.put('/I102', 'k1', randrange(10,40))
        fdb.put('/I102', 'k2', randrange(10,40))
        sleep(2)

if __name__=="__main__":
    print("""
*********************************************
* Press CTRL+C to stop test data generation *
*********************************************
          """)
    signal.signal(signal.SIGINT, Exit_gracefully)
    main()