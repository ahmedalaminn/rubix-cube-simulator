from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)  # flask --app app.py --debug run <--- updates app when reloaded

@app.route("/")
def index():
    return render_template("index.html")

cube = [ # 0 for white, 1 for yellow, 2 for orange, 3 for green, 4 for red, 5 for blue 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 
            1, 1, 1, 1, 1, 1, 1, 1, 1, 
            2, 2, 2, 2, 2, 2, 2, 2, 2, 
            3, 3, 3, 3, 3, 3, 3, 3, 3, 
            4, 4, 4, 4, 4, 4, 4, 4, 4, 
            5, 5, 5, 5, 5, 5, 5, 5, 5
        ]

@app.route("/get_cube") # default cube
def get_cube():
    return jsonify(cube=cube)

# Functions for Buttons & Moves
def update_cube(move):
    global cube
    # Updates the cube based on the selected button
    if move == "Shuffle":
        shuffle()
    elif move == "Reset":
        cube = [ # 0 for white, 1 for yellow, 2 for orange, 3 for green, 4 for red, 5 for blue 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 
            1, 1, 1, 1, 1, 1, 1, 1, 1, 
            2, 2, 2, 2, 2, 2, 2, 2, 2, 
            3, 3, 3, 3, 3, 3, 3, 3, 3, 
            4, 4, 4, 4, 4, 4, 4, 4, 4, 
            5, 5, 5, 5, 5, 5, 5, 5, 5
        ]
    else:
        make_move(move)

def make_move(move):
    global cube
    if move == "U":
        cube[18:21], cube[27:30], cube[36:39], cube[45:48] = cube[27:30], cube[36:39], cube[45:48], cube[18:21]
    elif move == "U'":
        cube[18:21], cube[27:30], cube[36:39], cube[45:48] = cube[45:48], cube[18:21], cube[27:30], cube[36:39]
    elif move == "U^2":
        make_move("U")
        make_move("U")
    elif move == "D":
        cube[24:27], cube[33:36], cube[42:45], cube[51:54] = cube[51:54], cube[24:27], cube[33:36], cube[42:45]
    elif move == "D'":
        cube[24:27], cube[33:36], cube[42:45], cube[51:54] = cube[33:36], cube[42:45], cube[51:54], cube[24:27]
    elif move == "D^2":
        make_move("D")
        make_move("D")
    elif move == "L":
        cube[0:9:3], cube[27:36:3], cube[47:56:3], cube[9:18:3] = cube[47:56:3], cube[0:9:3], cube[9:18:3], cube[27:36:3]
    elif move == "L'":
        cube[0:9:3], cube[27:36:3], cube[47:56:3], cube[9:18:3] = cube[27:36:3], cube[9:18:3], cube[0:9:3], cube[47:56:3]
    elif move == "L^2":
        make_move("L")
        make_move("L")
    elif move == "R":
        cube[2:11:3], cube[29:38:3], cube[45:54:3], cube[11:20:3] = cube[29:38:3], cube[11:20:3], cube[2:11:3], cube[45:54:3]
    elif move == "R'":
        cube[2:11:3], cube[29:38:3], cube[45:54:3], cube[11:20:3] = cube[45:54:3], cube[2:11:3], cube[11:20:3], cube[29:38:3]
    elif move == "R^2":
        make_move("R")
        make_move("R")
    elif move == "F":
        cube[6:9], cube[20:29:3], cube[36:45:3], cube[9:12] = cube[20:29:3], cube[9:12], cube[6:9], cube[36:45:3]
    elif move == "F'": 
        cube[6:9], cube[20:29:3], cube[36:45:3], cube[9:12] = cube[36:45:3], cube[6:9], cube[9:12], cube[20:29:3]
    elif move == "F^2":
        make_move("F")
        make_move("F")
    elif move == "B": 
        cube[0:3], cube[18:27:3], cube[38:47:3], cube[15:18] = cube[38:47:3], cube[0:3], cube[15:18], cube[18:27:3]
    elif move == "B'":
        cube[0:3], cube[18:27:3], cube[38:47:3], cube[15:18] = cube[18:27:3], cube[15:18], cube[0:3], cube[38:47:3]
    elif move == "B^2": 
        make_move("F")
        make_move("F")

def shuffle():
    global cube
    moves = ["U", "U'", "U^2", "D", "D'", "D^2", "F", "F'", "F^2", "B", "B'", "B^2", "L", "L'", "L^2", "R", "R'", "R^2"]
    for _ in range(100):
        update_cube(random.choice(moves))

@app.route('/get_move', methods=['POST'])
def get_move():
    data = request.json
    move = data.get('move')
    update_cube(move)
    return jsonify(cube=cube)

if __name__ == "__main__":
    app.run(debug=True)
