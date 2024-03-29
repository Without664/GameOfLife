var gameOfLife = document.getElementById('game-of-life');
var rows = gameOfLife.dataset.rows;
var cols = gameOfLife.dataset.cols;
var generations = gameOfLife.dataset.generations;
var grid = JSON.parse(gameOfLife.dataset.grid);

console.log(gameOfLife.dataset)


var csrftoken = Cookies.get('csrftoken'); // récupérer le jeton CSRF


var updateUrl = gameOfLife.dataset.updateUrl;
// Afficher la grille initiale
showGrid(grid);
console.log(updateUrl);

// Récupérer la grille HTML générée par la fonction showGrid
var html = $('#html-grid').html();

// Afficher la grille initiale
$('#grid').html(html);


// Mettre à jour la grille avec AJAX
setInterval(function() {
$.ajax({
url: "/game_of_life/",
type: "POST",
data: JSON.stringify({'grid': grid, 'rows': rows, 'cols': cols , 'csrfmiddlewaretoken': csrftoken}),
contentType: "application/json",
success: function(data) {
  grid = data.grid;
  showGrid(grid);
},
beforeSend: function(xhr, settings) {
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
}
});
}, 1000);

// Fonction pour afficher la grille dans le div #grid
function showGrid(grid) {
var html = '';
for (var i = 0; i < rows; i++) {
for (var j = 0; j < cols; j++) {
  if (grid[i][j] == 1) {
    html += '<span class="cell alive"></span>';
  } else {
    html += '<span class="cell"></span>';
  }
}
html += '<br>';
}
console.log(html);
$('#grid').html(html);
}