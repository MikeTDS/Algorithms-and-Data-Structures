Zadanie 2.

W zadaniu drugim został zaimplementowany program realizujący algorytmy Dijkstry. Wykorzystuje on
kolejkę z zadania 1.

Przykładowe uruchomienie:

python3 zad2.py <in

gdzie in zawiera przykładowe dane wejściowe zgodne z poleceniem, to znaczy liczbę wierzchołków
n, krawędzi m, kolejno krawędzie (u,v,w), wierzchołek startowy. 
Przykładowy input:

3
4
1 2 8
1 3 5
2 3 1
3 2 2.9
1

UWAGA: wierzchołki muszą być numerowane kolejno 1,2,...,n.

Algorytm Dijkstry wykorzystuje listy sąsiedztwa, które generuje na podstawie inputu. W kolejce 
znajdują się wierzchołki, których priortet to odległość od początkowego wierzchołka (na początku
\infty). Alogrytm przechodzi po kolejnych sąsiadach korzystając ze strategii relaksacji krawędzi,
jednocześnie każdy wierzchołek trzyma swojego rodzica w celu odtworzenia ścieżek.

Po wczytaniu danych zostaną wyznaczone najkrótsze ścieżki i na standardowym wyjściu wyświetlone w
kolejnych liniach:

indeks_celu waga_całej_drogi

Na stderr będą wypisane:

1) całe ścieżki, zakładając że ściezka ma postać (v1, v2, ... ,vn) oraz waga krawędzi (vi, vi+1) 
to wi, gdzie v1 jest źródlem, a vn celem, to ścieżki będą mieć postać:

(v1)--w1--(v2)--w2--(v3)--...--(vn-1)--wn-1--(vn).

2) czas działania progamu w milisekundach.

