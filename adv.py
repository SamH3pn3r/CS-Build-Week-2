from util import Stack, Queue
# from credentials import TOKEN, TOKEN_2
import random
from ast import literal_eval
import requests
import json
import time
from dotenv import load_dotenv
import os
from world import World


load_dotenv()
tokens = os.getenv('TOKEN')


seed = random.randint(0, 217120)
random.seed(185393)

adv_endpoint = "https://lambda-treasure-hunt.herokuapp.com/api/adv"
bc_endpoint = "https://lambda-treasure-hunt.herokuapp.com/api/bc"
token = 'Token ' + tokens

headers = {
    'Authorization': token
}

headers_post = {
    'Authorization': token,
    'Content-type': 'application/json'
}

visited_rooms = {}

map_file = "map.txt"

world = World()

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

def init():
    r = requests.get(f'{adv_endpoint}/init/', headers=headers)
    data = r.json()
    # with open('current_rooms.txt', 'w') as f:
    #     f.write(json.dumps(data))
    # with open('rooms.txt', 'w') as f:
    #     f.write(json.dumps(data) + '\n')
    wait(data['cooldown'])
    print('Init: ', data)
    return data

def move(direction):
    data = {"direction": f"{direction}"}
    r = requests.post(f'{adv_endpoint}/move/', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    # with open('rooms.txt', 'a') as f:
    #     f.write(json.dumps(data_json) + '\n')
    wait(data_json['cooldown'])
    print('Move: ', data_json)
    # print("Current number of visited rooms: ", len(visited_rooms))
    # print('visted_rooms: ', visited_rooms)
    return data_json

def wise_explorer(direction, room_id):
    data = {"direction": f"{direction}", "room_id": f"{room_id}"}
    r = requests.post(f'{adv_endpoint}/move', data=json.dumps(data), headers=headers)
    data_json = r.json()
    # with open('rooms.txt', 'a') as f:
    #     f.write(json.dumps(data_json))
    print('Wise: ', data_json)
    wait(data_json['cooldown'])
    return data_json

def wait(cooldown):
    time.sleep(cooldown)

def take(name):
    r = requests.post(f'{adv_endpoint}/move', data=json.dumps(name), headers=headers)
    data_json = r.json()
    print('Take: ', data_json)
    wait(data_json['cooldown'])
    return data_json

def drop(name):
    r = requests.post(f'{adv_endpoint}/drop', data=json.dumps(name), headers=headers)
    data_json = r.json()
    print('drop: ', data_json)
    wait(data_json['cooldown'])
    return data_json

def sell(name, confirm="no"):
    data = {
        "name": f"{name}",
        "confirm": f"{confirm}"
    }
    r = requests.post(f'{adv_endpoint}/drop', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    print('Sell: ', data_json)
    wait(data_json['cooldown'])
    return data_json

def status():
    r = requests.post(f'{adv_endpoint}/status/', headers=headers_post)
    data_json = r.json()
    wait(data_json['cooldown'])
    print('Status: ', data_json)
    return data_json

def examine(name):
    data = {"name": f"{name}"}
    r = requests.post(f'{adv_endpoint}/examine', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    print("Examine: ", data_json)
    wait(data_json['cooldown'])
    return data_json

def wear(name):
    data = {"name": f"{name}"}
    r = requests.post(f'{adv_endpoint}/wear', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    print("Wear: ", data_json)
    wait(data_json['cooldown'])
    return data_json

def undress(name):
    data = {"name": f"{name}"}
    r = requests.post(f'{adv_endpoint}/undress', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    print("Undress: ", data_json)
    wait(data_json['cooldown'])
    return data_json

def change_name(name):
    data = {"name": f"{name}"}
    r = requests.post(f'{adv_endpoint}/change_name', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    print("Change name: ", data_json)
    wait(data_json['cooldown'])
    return data_json

def pray():
    r = requests.post(f'{adv_endpoint}/pray/', headers=headers_post)
    data = r.json()
    print('Pray: ', data)
    wait(data['cooldown'])
    return data

def fly(direction):
    data = {"direction": f"{direction}"}
    r = requests.post(f'{adv_endpoint}/fly', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    print("Fly: ", data_json)
    wait(data_json['cooldown'])
    return data_json

def dash(direction, num, next_rooms):
    data = {"direction": f"{direction}", "num_rooms": f"{num}", "next_room_ids": f"{next_rooms}"}
    r = requests.post(f'{adv_endpoint}/dash', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    print("Dash: ", data_json)
    wait(data_json['cooldown'])
    return data_json

def carry(name):
    data = {"name": f"{name}"}
    r = requests.post(f'{adv_endpoint}/carry', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    print("Carry: ", data_json)
    wait(data_json['cooldown'])
    return data_json

def receive():
    r = requests.post(f'{adv_endpoint}/receive/', headers=headers_post)
    data_json = r.json()
    print('Receive: ', data_json)
    wait(data_json['cooldown'])
    return data_json

def warp():
    r = requests.post(f'{adv_endpoint}/warp', headers=headers_post)
    data_json = r.json()
    print('Warp: ', data_json)
    wait(data_json['cooldown'])
    return data_json

def recall():
    r = requests.post(f'{adv_endpoint}/recall', headers=headers_post)
    data_json = r.json()
    print('Recall: ', data_json)
    wait(data_json['cooldown'])
    return data_json

def mine(new_proof):
    data = {"proof": f"{new_proof}"}
    r = requests.post(f'{bc_endpoint}/mine', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    print("Mine: ", data_json)
    wait(data_json['cooldown'])
    return data_json

def last_proof():
    r = requests.get(f'{bc_endpoint}/last_proof', headers=headers)
    data_json = r.json()
    print("Last proof: ", data_json)
    wait(data_json['cooldown'])
    return data_json

def get_balance():
    r = requests.get(f'{adv_endpoint}/get_balance', headers=headers)
    data_json = r.json()
    print('Get balance: ', data_json)
    wait(data_json['cooldown'])
    return data_json

def transmogrify(name):
    data = {"name": f"{name}"}
    r = requests.post(f'{adv_endpoint}/transmogrify', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    print('Transmogrify: ', data_json)
    wait(data_json['cooldown'])
    return data_json

def reverse(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    else:
        return 'e'

def new_entry(room, visited_rooms):
    visited_rooms[room['room_id']] = {}

    for exit_direction in room['exits']:
            visited_rooms[room['room_id']][exit_direction] = '?'

def bfs(current_room, visited_rooms):
    room = current_room
    q = Queue()
    q.enqueue([room['room_id']])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        last = path[-1]
        if last not in visited:
            visited.add(last)
            for exit_direction in visited_rooms[last]:
                if (visited_rooms[last][exit_direction] == '?'):
                    return path
                elif (visited_rooms[last][exit_direction] not in visited):
                    new_path = path + [visited_rooms[last][exit_direction]]
                    q.enqueue(new_path)
    return path

def traverse():
    previous_room = None
    current_room = init()
    print("init: ", current_room)

    while(len(visited_rooms) < 500):
        if current_room['room_id'] not in visited_rooms:
            new_entry(current_room, visited_rooms)

        exits = []
        for new_direction in visited_rooms[current_room['room_id']]:
            if (visited_rooms[current_room['room_id']][new_direction] == '?'):
                exits.append(new_direction)

        if (len(exits) == 0):
            path = bfs(current_room, visited_rooms)
            # tranlate room id to direction
            for id in path:
                for exit_direction in visited_rooms[current_room['room_id']]:
                    if (exit_direction in visited_rooms[current_room['room_id']]):
                        if (visited_rooms[current_room['room_id']][exit_direction] == id and current_room['room_id'] != id):
                            previous_room = current_room
                            current_room = move(exit_direction)
                            if (current_room['room_id'] not in visited_rooms):
                                new_entry(current_room, visited_rooms)
                            visited_rooms[previous_room['room_id']][exit_direction] = current_room['room_id']
                            visited_rooms[current_room['room_id']][reverse(exit_direction)] = previous_room['room_id']
        else:
            new_exit = random.choice(exits)
            previous_room = current_room
            current_room = move(new_exit)
            if (current_room['room_id'] not in visited_rooms):
                new_entry(current_room, visited_rooms)
            visited_rooms[previous_room['room_id']][new_exit] = current_room['room_id']
            visited_rooms[current_room['room_id']][reverse(new_exit)] = previous_room['room_id']


# if __name__ == "__main__":
    # traverse()
    # with open('room_directions.txt', 'w') as f:
    #     f.write(json.dumps(visited_rooms))