document.addEventListener("DOMContentLoaded", function() {
    fetchCube();

    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            move = button.dataset.move;
            console.log(move);

            fetch('/get_move', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ move: move }) // converting move to json in order to have it sent
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                displayCube(data.cube);  
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
});

function fetchCube() {
    console.log("Fetching cube data...");
    fetch("/get_cube")
        .then(response => response.json())
        .then(data => {
            console.log("Fetched!");
            displayCube(data.cube);
        })
        .catch(error => console.error('Error fetching cube data:', error));
}


function displayCube(cube){
    const colors = ["white", "yellow", "orange", "green", "red", 'blue'];

    for (let i = 0; i < colors.length; i++){
        const faceGrid = document.getElementById(colors[i]);

        for (let j = 0; j < 9; j++){
            const cell = document.createElement('div');
            const index = i * 9 + j;
            cell.style.backgroundColor = colors[cube[index]];
            cell.style.border = '1px solid black';
            faceGrid.appendChild(cell);
        }
    }
    console.log("Displayed!");
}
