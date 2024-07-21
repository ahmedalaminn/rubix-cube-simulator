from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route("/")

def index():
    return render_template("index.html")


class RubiksCube:
    def __init__(self):
        # 0 for white, 1 for yellow, 2 for orange, 3 for green, 4 for red, 5 for blue 
        # reference picture for each piece's index.
        self.cube = [
            0, 0, 0, 0, 0, 0, 0, 0, 0,  # White (top) face
            1, 1, 1, 1, 1, 1, 1, 1, 1,  # Yellow (bottom) face
            2, 2, 2, 2, 2, 2, 2, 2, 2,  # Orange (left) face
            3, 3, 3, 3, 3, 3, 3, 3, 3,  # Green (front) face
            4, 4, 4, 4, 4, 4, 4, 4, 4,  # Red (right) face
            5, 5, 5, 5, 5, 5, 5, 5, 5   # Blue (back) face
        ]

    def rotate(movement):
        # 18 possible rotations: 
            '''
            Up: U, U', U^2
            Down: D, D', D^2
            Left: L, L', L^2
            Right: R, R', R^2
            Front: F, F', F^2
            Back: B, B', B^2
            '''

    def reset():
        cube = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 
            1, 1, 1, 1, 1, 1, 1, 1, 1, 
            2, 2, 2, 2, 2, 2, 2, 2, 2, 
            3, 3, 3, 3, 3, 3, 3, 3, 3, 
            4, 4, 4, 4, 4, 4, 4, 4, 4, 
            5, 5, 5, 5, 5, 5, 5, 5, 5
         ]
    
        
