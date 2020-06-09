Zadanie 3.

W zadaniu 3. korzystam z kolejki z zadania 1 do implementacji algorytmów Prima i Krsukala. Program
wyznaczy minimalne drzewa rozpinające MST dla podanego grafu.
Przykładowe uruchomienie:

Prim:
python3 zad3.py -p <in

Kruskal:
python3 zad3.py -k <in

Przykładowy input:

8
16
5 6 0.35
5 8 0.37
6 8 0.28
1 8 0.16
2 6 0.32
1 5 0.38
3 4 0.17
2 8 0.19
1 3 0.26
2 3 0.36
2 4 0.29
3 8 0.34
7 3 0.4
4 7 0.52
7 1 0.58
7 5 0.93

Pierwsza linia to liczba wierzchołków, druga to liczba krawędzi, pozostałe to definicje krawędzi.

UWAGA: ponownie wierzchołki muszą być numerowane 1,2,...,n.

Algorytm Prima:
Podobnie jak Dijkstra korzysta z listy sąsiedztwa, wierzchołki trzyma w kolejce i przechodzi po 
sąsiadach. Jeśli algorytm znajdzie lepszą krawędź (u,v) prowadzącą do wierzchołka v, to wierzchołek
v otrzyma rodzica u.

Algorytm Kruskala:
Tutaj w kolejce trzymane są krawędzie, priorytetem jest ich waga. Dodatkowo konieczna była
implementacja zbiorów, z której korzysta podany algorytm w celu sprawdzenia czy dany wierzchołek
był odwiedzony.

Na standarowym wyjściu zostaną wypisane kolejno:

1) u v w
oznaczające krawędzie (u,v) o wadze w, użyte do budowy drzewa MST

2) waga całego drzewa
