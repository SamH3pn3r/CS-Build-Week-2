from util import Stack, Queue
# from credentials import TOKEN, TOKEN_2
import random
from ast import literal_eval
import requests
import json
import time

seed = random.randint(0, 217120)
random.seed(185393)

adv_endpoint = "https://lambda-treasure-hunt.herokuapp.com/api/adv"
bc_endpoint = "https://lambda-treasure-hunt.herokuapp.com/api/bc"
token = 'Token ' + "2112332c7e8196503ad70f3056c67ef490742170"

headers = {
    'Authorization': token
}

headers_post = {
    'Authorization': token,
    'Content-type': 'application/json'
}

visited_rooms = {}

def init():
    r = requests.get(f'{adv_endpoint}/init/', headers=headers)
    data = r.json()
    # with open('current_rooms.txt', 'w') as f:
    #     f.write(json.dumps(data))
    with open('rooms.txt', 'w') as f:
        f.write(json.dumps(data) + '\n')
    wait(data['cooldown'])
    print('Init: ', data)
    return data

def move(direction):
    data = {"direction": f"{direction}"}
    r = requests.post(f'{adv_endpoint}/move/', data=json.dumps(data), headers=headers_post)
    data_json = r.json()
    with open('rooms.txt', 'a') as f:
        f.write(json.dumps(data_json) + '\n')
    wait(data_json['cooldown'])
    print('Move: ', data_json)
    print("Current number of visited rooms: ", len(visited_rooms))
    print('visted_rooms: ', visited_rooms)
    return data_json

def wise_explorer(direction, room_id):
    data = {"direction": f"{direction}", "room_id": f"{room_id}"}
    r = requests.post(f'{adv_endpoint}/move', data=json.dumps(data), headers=headers)
    data_json = r.json()
    with open('rooms.txt', 'a') as f:
        f.write(json.dumps(data_json))
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

## FUNCTIONS TO PRINT THE MAP START ##
def load_graph(room_graph):
    print(room_graph)
    num_rooms = len(room_graph)
    rooms = [None] * num_rooms
    grid_size = 1
    for i in range(0, num_rooms):
        x = room_graph[i][0][0]
        grid_size = max(grid_size, room_graph[i][0][0], room_graph[i][0][1])
        self.rooms[i] = Room(f"Room {i}", f"({room_graph[i][0][0]},{room_graph[i][0][1]})",i, room_graph[i][0][0], room_graph[i][0][1])
    self.room_grid = []
    grid_size += 1
    self.grid_size = grid_size
    for i in range(0, grid_size):
        self.room_grid.append([None] * grid_size)
    for room_id in room_graph:
        room = self.rooms[room_id]
        self.room_grid[room.x][room.y] = room
        if 'n' in room_graph[room_id][1]:
            self.rooms[room_id].connect_rooms('n', self.rooms[room_graph[room_id][1]['n']])
        if 's' in room_graph[room_id][1]:
            self.rooms[room_id].connect_rooms('s', self.rooms[room_graph[room_id][1]['s']])
        if 'e' in room_graph[room_id][1]:
            self.rooms[room_id].connect_rooms('e', self.rooms[room_graph[room_id][1]['e']])
        if 'w' in room_graph[room_id][1]:
            self.rooms[room_id].connect_rooms('w', self.rooms[room_graph[room_id][1]['w']])
    self.starting_room = self.rooms[0]

def print_rooms():
    rotated_room_grid = []

    for i in range(0, len(self.room_grid)):
        rotated_room_grid.append([None] * len(self.room_grid))
    for i in range(len(self.room_grid)):
        for j in range(len(self.room_grid[0])):
            rotated_room_grid[len(self.room_grid[0]) - j - 1][i] = self.room_grid[i][j]
    print("#####")
    str = ""
    for row in rotated_room_grid:
        all_null = True
        for room in row:
            if room is not None:
                all_null = False
                break
        if all_null:
            continue
        # PRINT NORTH CONNECTION ROW
        str += "#"
        for room in row:
            if room is not None and room.n_to is not None:
                str += "  |  "
            else:
                str += "     "
        str += "#\n"
        # PRINT ROOM ROW
        str += "#"
        for room in row:
            if room is not None and room.w_to is not None:
                str += "-"
            else:
                str += " "
            if room is not None:
                str += f"{room.id}".zfill(3)
            else:
                str += "   "
            if room is not None and room.e_to is not None:
                str += "-"
            else:
                str += " "
        str += "#\n"
        # PRINT SOUTH CONNECTION ROW
        str += "#"
        for room in row:
            if room is not None and room.s_to is not None:
                str += "  |  "
            else:
                str += "     "
        str += "#\n"
    print(str)
    print("#####")

map_file = "rooms.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
load_graph(room_graph)

## FUNCTIONS TO PRINT THE MAP END ##

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


if __name__ == "__main__":
    # traverse()
    print_rooms()
    with open('room_directions.txt', 'w') as f:
        f.write(json.dumps(visited_rooms))