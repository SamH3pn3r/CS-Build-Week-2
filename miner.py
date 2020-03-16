import hashlib
import requests
import time

from adv import wait
import sys

from uuid import uuid4

from timeit import default_timer as timer

import random

import json
from dotenv import load_dotenv
import os

load_dotenv()
tokens = os.getenv('TOKEN_2')

token = 'Token ' + tokens

headers = {
    'Authorization': token
}

headers_post = {
    'Authorization': token,
    'Content-type': 'application/json'
}


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    proof = random.randint(-217120, 217120)
    #  TODO: Your code here
    # get previous_hash
    # previous_hash = f"{last_proof}".encode()
    # previous_hash = hashlib.sha256(previous_hash).hexdigest()

    # keep searching until a proof is found
    while valid_proof(last_proof, proof) is False:
        proof += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_proof, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """

    # TODO: Your code here!
    # create guess and guess_hash
    guess = f"{last_proof}{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    # guess_hash = hash(last_proof, proof)
    
    # test if the first 6 numbers of the guess_hash match the last 6 numbers of last_hash
    return guess_hash[:6] == "000000"


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-treasure-hunt.herokuapp.com/api/bc"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof", headers=headers)
        data = r.json()
        print(data['proof'])
        new_proof = proof_of_work(data['proof'])
        print(new_proof)
        wait(data['cooldown'])

        post_data = {"proof": new_proof}

        r = requests.post(url=node + "/mine", json=post_data, headers=headers_post)
        data = r.json()
        print(data)
        if data.get('message') == "New Block Forged":
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
            wait(data['cooldown'])
        else:
            print(data.get('message'))
            wait(data['cooldown'])
