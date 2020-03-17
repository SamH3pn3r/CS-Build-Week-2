import json
import ast

rooms = open('rooms.txt', 'r+')
# print(rooms.read())

room_directions = open('room_directions.txt', 'r+')
# print(room_directions.read())

terrain = open('terrain.txt', 'r+')

room_directions = json.load(room_directions)
terrain = json.load(terrain)
# rooms = json.load(rooms)

new_rooms = {}
counter = 0

# for i in terrain:
#     x = terrain.get(f"{i}")

#     i = int(i)

#     print(i, x)
#     print(type(i))


for room in rooms:
    room = ast.literal_eval(room)

    for room_d in room_directions:
        room_d = int(room_d)
        print(room_d)
        print(type(room_d))
        print(type(room['room_id']))
        new_rooms = dict([(room_d, room['room_id'])])
        if room_d not in new_rooms and room_d == room['room_id']:
            new_rooms[room_d] = room['room_id']
            # , (room['room_id']) = ([room['terrain'], room_directions[room_d]])
            
            print('new_rooms length: ', len(new_rooms))

# with open('terrain.txt', 'w') as f:
#     f.write(json.dumps(new_rooms, indent=4))
