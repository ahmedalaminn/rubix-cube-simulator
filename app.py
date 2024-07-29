from flask import Flask, render_template, request, jsonify

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

@app.route('/get_move', methods=['POST'])
def get_move():
    data = request.json
    move = data.get('move')
    return jsonify(cube=update_cube(move))

def update_cube(move):
    # Updates the cube based on the move 
    return cube

if __name__ == "__main__":
    app.run(debug=True)
