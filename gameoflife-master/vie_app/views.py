from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

def init_game_of_life(request):
    dim = int(request.GET.get('dim', 10))
    grid = [[random.randint(0, 1) for _ in range(dim)] for _ in range(dim)]

    # Renvoyer la grille sous forme de JSON
    data = {'grid': grid, 'rows': dim, 'cols': dim}
    return JsonResponse(data)
    
def game_of_life(request):

    # Récupérer les paramètres de l'utilisateur
    rows = int(request.GET.get('rows', 10))
    cols = int(request.GET.get('cols', 10))
    generations = int(request.GET.get('generations', 10))

    # Initialiser la grille avec des cellules aléatoirement vivantes ou mortes
    grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

    # Renvoyer la grille sous forme de JSON
    data = {'grid': grid, 'rows': rows, 'cols': cols, 'generations': generations}
    return render(request, 'game_of_life.html', context=data)


@csrf_exempt
def update_game_of_life(request):
    # Récupérer la grille, les rangées et les colonnes depuis la requête JSON
    data = json.loads(request.body.decode('utf-8'))
    grid = data['grid']
    rows = int(data['rows'])
    cols = int(data['cols'])
    # Calculer la nouvelle génération du jeu de la vie
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbors = 0
            # Compter le nombre de voisins vivants
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if not (di == 0 and dj == 0):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                            neighbors += 1
            # Appliquer les règles du jeu de la vie
            if grid[i][j] == 1 and neighbors in [2, 3]:
                new_grid[i][j] = 1
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
    # Renvoyer la nouvelle grille sous forme de JSON
    data = {'grid': new_grid, 'rows': rows, 'cols': cols}
    return JsonResponse(data)
