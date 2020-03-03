import json
import ast

rooms = open('rooms.txt', 'r+')
# print(rooms.read())

room_directions = open('room_directions.txt', 'r+')
# print(room_directions.read())

room_directions = json.load(room_directions)
# rooms = json.load(rooms)

new_rooms = {}
counter = 0

for room in rooms:
    room = ast.literal_eval(room)

    for room_d in room_directions:
        if room_d not in new_rooms and int(room_d) == room['room_id']:
            print('exits: ', room_directions[room_d])
            new_rooms[room_d] = ([room['coordinates'], room_directions[room_d]])
            print('new_rooms length: ', len(new_rooms))

# print(new_rooms['0'])


with open('map.txt', 'w') as f:
    f.write(json.dumps(new_rooms, indent=4))

# print('new rooms:', new_rooms)

# for room in rooms:
#     room = ast.literal_eval(room)
#     print(room['room_id'])
#     print()
#     print(len(room))

# for room in rooms:
#     # print(room)
#     # room = json.load(room)
#     # print(room)
#     if room[counter] not in new_rooms and counter <= 500:
#         new_rooms[counter] = room
#         counter += 1
#         print("counter: ", counter)
#         print()
#         print(len(new_rooms))

# print(len(new_rooms))
# print(room_directions, '\n')
# for room in room_directions:
#     print('room: ', room)
#     for other_room in rooms:
#         other_room = ast.literal_eval(other_room)
#         if room not in new_rooms and int(room) == other_room['room_id']:
#             print(room_directions[room])
#             new_rooms[f"{room}"] = {}
#             new_rooms[f"{room}"] = [other_room['coordinates'], room_directions[room]]
#             print('new_rooms length: ', len(new_rooms))


# print(new_rooms)

# room_directions = json.load(room_directions)
# for room in rooms:
#     # for directions in room_directions:
#     for i in range(len(room_directions)):
#         if ()
#         direct = room_directions[str(i)]
#         new_room = json.loads(room)
#     print(new_room['room_id'], new_room['coordinates'], )
    
#     print()


