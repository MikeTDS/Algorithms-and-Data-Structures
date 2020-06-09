Zadanie 4.

UWAGA: plik zad4.py zawiera również rozwiązanie zadania 5, które może trwać dłużej dla dużych danych
wejściowych. Wyniki dla zadania 5 to ostatnia linia na stdout i na stderr.

W zadaniu 4 należało zaimplenentować 3 strategie poruszania się po pełnym nieskierowanym grafie tak,
aby przejść wszystkie wierzchołki.

Przykładowe uruchomienie:

python3 zad4.py <in

Przykładowy input:

10
1 2 3.56203
1 3 4.39984
1 4 4.12466
1 5 3.29763
1 6 3.6549
1 7 4.89959
1 8 3.02486
1 9 4.60805
1 10 4.29293
2 3 3.70813
2 4 5.01083
2 5 3.41035
2 6 5.25675
2 7 4.42823
2 8 3.19501
2 9 4.13282
2 10 4.40296
3 4 2.78921
3 5 4.61959
3 6 4.22009
3 7 3.40022
3 8 4.14471
3 9 5.312
3 10 3.09458
4 5 4.79665
4 6 4.2721
4 7 4.89251
4 8 2.73759
4 9 4.65557
4 10 3.60273
5 6 4.96099
5 7 2.86003
5 8 5.32378
5 9 3.72808
5 10 3.47887
6 7 3.62111
6 8 3.27009
6 9 3.82494
6 10 2.87159
7 8 4.88424
7 9 4.85429
7 10 5.20363
8 9 2.93702
8 10 4.75347
9 10 4.27429

Założenia:
Losujemy wierzchołek startowy i chodzimy po krawędziach aż nie odwiedzimy wszystkich wierzchołków.

Strategia błądzenia losowego (Random walk):
Każda następna krawędź jest losowana z prawdopodobieństwem jednostajnym. W treści nie było informacji
na temat kilkukrotnego odwiedzenia tego samego wierzchołka, dlatego zakładam, że poruszając się wiemy,
które wierzchołki już odwiedzliśmy i tam nie wracamy. Zakładając, że takiej wiedzy nie mamy, dla 
przypadków dużych grafów złożoność rośnie bardzo znacząco.

Szukanie najniższej wagi (Weight walk):
Wierzchołek v jest wybierany z aktualnego u, jeśli waga krawędzi (u,v) jest najniższa spośród pozostałych
sąsiadów oraz v nie był jeszcze odwiedzony.

Korzystanie z drzew rozpinających (MST walk):
Algorytm Prima/Kruskala zwraca listę krawędzi, po których będziemy się poruszać. Startując w wierzchołka
startowego pokonujemy każdą krawędź 2 razy odwiedzając wszystkie wierzchołki.

Wyniki:

Kolejność algorytmów - Random walk, Weight walk, MST walk, Dynamic (zad5)

Na standardowym wyjściu zostaną wypisane:

k W M t

gdzie k = liczba króków, W = waga pokonanaje trasy, M = zużcie dodatkowej pamięci (opis dla każdego),
t = czas działania algorytmu.

Na standardowym wyjściu błędów zostanie wypisana trasa:
v1 v2 v3 ... vm 
bedące kolejno odwiedzonymi wierzchołkami.

Obserwacje:

Ogólne:
Po wykonaniu testów dla rozmiarów podanych w zadaniu 4 (i kilku innych) widać bardzo szybki wzrost 
zużycia pamięci wraz ze zwiększeniem rozmiaru danych. Wynika to z faktu, że dla n wierzchołków mamy 
((n*(n-1))/2) krawędzi, co daje złożoność  zużycia pamięci O(n^2). Co za tym idzie wczytywanie danych, 
tworzenie listy sąsiedztwa oraz pozostałe elementy preprocessinguzajmują zdecydowanie więcej czasu niż 
dla wartości mnijeszych. Przykładowo na moim urządzeniu niemożliwe było przeprowadzenie testów dla 
n = 500000, który daje 1.2499975 * 10^11 krawędzi. Dla n = 5000 program zużył już tyle pamięci, że 
wystąpił problem z przerwanie programu. Czas samego działania algorytmu jest również znacznie 
dłuższy dla większych przypadków, ponieważ dla niewielkiego wzrostu n, znaczący jest wzrost możliwych 
ścieżek, co za tym idzie zdecydowanie większy jest problem do rozwiązania.

Wyniki samych testów znajdują się w pliku TESTS.txt

Random walk:
Przykładowy output:

9 36.553639999999994 110 0.000186920166015625
7 10 6 2 1 5 8 9 3 4 

W tej strategii algorytm wykona zawsze n-1 kroków (bo wie gdzie już był). Na dodatkowe zużcie pamięci
składa się tutaj lista sąsiedztwa oraz lista odwiedzonych wierzchołków. Oznacza to, że nie jest to
algorytm kosztowny ani czasowo ani pamięciowo, natomiast wyznaczona ścieżka może być daleka od 
optymalnej.

Dodatkowo gdy nie zakładamy, że pamiętamy gdzie juz byliśmy:

Random walk:
Przykładowy output:

17 67.69453 110 0.00025177001953125 
4 8 10 7 5 8 6 2 5 7 1 6 8 9 1 4 1 3

Tutaj czas trawnia oraz długość ścieżki są większe. Będą tym większe różnice między podejściem 1 a 2,
im większe wybierzemy n.

Weight walk:
Przykładowy output:

9 28.63325 110 0.000152587890625
7 5 1 8 4 3 10 6 9 2  

Ponownie zostanie wykonane zawsze n-1 kroków. Tym razem jednak krawędzie są wybierane na ogół lepiej, 
bo szukamy zawsze najkrótszej krawędzi. Zużycie pamięci jest takie samo jak w przypadku wyżej,
czas działania również zbliżony. Rezulataty tego algorytmu będą odbiegać od optimum wraz ze wzrostem
wielkości grafu.

MST walk - Prim (użyty w programie):
Przykładowy output:

18 53.61503999999999 209 0.0007059574127197266
7 5 1 8 4 3 10 6 10 3 4 8 9 8 2 8 1 5 7 

Liczba kroków będzie zawsze równa 2*n-2, ponieważ każdą krawędź trzeba pokonać 2 razy. Stąd waga
wyznaczonego drzewa stanowi połowę wartości pokonanej ścieżki (distance). Zużycie pamięci jest wyższe,
ponieważ zarówno algorytm Prima jak i wyznaczający ścieżkę trzymają listy sąsiedztwa i odwiedzonych
wierzchołków / wygenerowanych krawędzi.

MST walk - Kruskal (dodatkowo):
Przykładowy output:

18 53.615039999999986 174 0.0019392967224121094
7 5 1 8 2 8 4 3 10 6 10 3 4 8 9 8 1 5 7

Podobnie jak w Primie liczba kroków i dystans są identyczne. Ścieżki różnią się kolejnością przechodzenia,
ponieważ Prim i Kruskal zwracają krawędzie w różnych kolejnościach. Zużycie pamięci w Kruskalu jest inne niż
Primie, ponieważ algorytm Kruskala nie korzysta z list sąsiedztwa ani odwiedzonych wierzchołków, natomiast
ze zbiorów wierzchołków.

Wnioski:

Zasadniczo najmniej korzystnym algorytmem okazuje się random walk, ze względu na częste słabe wyniki. W 
przypadku Weight walk można dostać bardzo dobre wyniki dla małych grafów. Wraz z wzrostem ich wielkości
jego korzystność spada. Można również dobrać odpowiednio taki przykład, że weight walk da bardzo słaby 
wynik dla małego grafu. Korzystanie z MST jest o tyle dobre, że większe dane nie wpływają niekorzystnie 
na jakość wyniku, natomiast zwiększają złożoność czasową i pamięciową. Dla danych większych zdarza się,
że trasa pokonana przez MST walk jest mniejsza niż ta pokonana przez Weight walk.

Zużycie pamięci zbadałem również przy pomocy narzędzia tracemalloc. Oto wyniki (w KB):
Random walk - 0.004523
Weight walk - 0.003256
MST walk - 0.009696
Dynamic - 0.963232

Rezultaty są zgodne z wcześniejszymi oraz zużycie pamięci podjeścia dynamicznego jest zdecyowanie 
większe niż dla pozostałych (opis niżej).

Zadanie 5.

Rozszerza zadanie 4 o dodatkowy algorytm bazujący na programowaniu dynamicznym. Funkcja kosztu (wagi 
danej trasy) jest wyliczana rekurencyjnie, to znaczy dla każdego sąsiada v wierzchołka u cost(u) jest
liczony:
	cost(u) = min(cost(v) + w(u,v))

Dla podanego grafu pełnego z wierzchołka startowego sprawdzamy n-1 sąsidadów. Na n-1 wierchołkach,
każdy wywołuje rekurencyjnie procedurę dla n-2 sąsiadów itd. Oznacza to, że złożoność takiego
podjeścia to (n-1)(n-2)(n-3)...(1) = O(n!), czyli bardzo wysoka.

5.1 Podejście niedynamiczne (nieakutalne)
Przykładowy output:

9 28.17078 200 5.427484512329102 s
4 3 10 6 7 5 2 1 8 9

Dodatkowe zużycie pamięci (lista kosztów, sąsiedztwa, ścieżka) jest większe niż w przypadku Kruskala,
memory peak największy oraz czas trawnia nieproporcjonalnie duży (ponad 5 sekund) względem poprzednich
rozwiązań. Wynik jednak jest najlepszym z dotychczas otrzymanych, ponieważ jest wynikiem sprawdzenia
wszystkich możliwych tras, czyli jest globalnym optimum.

5.2 Podejście dynamiczne (aktualne)
Przykładowy output:

9 28.17078 4692 0.12027478218078613
4 3 10 6 7 5 2 1 8 9

Dodatkowe zużycie pamięci wzrosło znacznie o listę kosztów obliczonych już tras. Dzięki zapisywaniu 
dotychczasowych wyników, czas działa spadł z ponad 5s do 0.12s, natomiast odbyło się to kosztem
pamięci. Memory peak jest wysoki, ponieważ koszty jedynie przybywają do tablicy i nic nie jest
po drodze zwalniane. Oba rozwiązania (5.1 i 5.2) dają tak samo dobre wyniki, czyli globalne minima.
Niezależnie od wyboru podejścia (5.1, 5.2) przeprowadzenie testów dla danych powyżej 15 zaczynało
trwać bardzo długo.
