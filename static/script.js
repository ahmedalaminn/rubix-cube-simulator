document.addEventListener("DOMContentLoaded", function() {
    fetchCube();
});

function fetchCube() {
    console.log("Fetching cube data...");
    fetch("/get_cube")
        .then(response => response.json())
        .then(data => {
            console.log("Fetched!")
        })
        .catch(error => console.error('Error fetching cube data:', error));
}
