Zadanie 1.

Program do zadania uruchamia się następująco:

python3 zad1.py <in

gdzie, in to plik zawierający polecenia przekazywane na standardowe wejście. Fromat pliku wejściowego
powinien być zgodny z poleceniem, to znaczy pierwsza linia to liczba instrukcji, następnie w każdej
następnej linii instrukcja z parametrami (lub bez).
Przykładowy input:

21
insert 10 9
insert 2 3
insert 2 5
insert 19 27
insert 6 7
print
top
pop
print
pop
print
priority 6 4
print
pop
print
pop
pop
pop
print
insert 1 1
print

Złożoność instrukcji:

insert x p - wstawia do struktury wartość x o priorytecie p. Struktura wstawia nowy element na koniec 
listy, po czym przestawia go tak, aby kolejka została zachowana względem priorytetu. W tym celu element
jest przesuwany wyżej (w górę kopca), aż znajdzie się na właściwym miejscu. Ponieważ samo przesuwanie
w góre ma stałą złożność, a liczba takich przeunięć jest rzędu wysokości kopca, to złożność procedury
jest O(log(n)).

empty - struktura przetrzymuje pole informujące o jej rozmiarze. Jeśli queue.size == 0, to empty drukuje
1, w przeciwnym razie 0. Czas dostępu do elementu size jest stały i niezależny od n, stąd złożoność 
operacji jest O(1), co oczywiście jest również O(log(n)).

top - pobiera wartość klucza o najwyższym priorytecie. Jest to równoważne z pobranie wartości z 
pierwszego elementu z kolejki (id=0). Dostęp do elementu w kolejce jest stały, stąd złożoność top to 
również O(1).

pop - poza wypisanie wartości jak top, usuwa również dany element z kolejki. Konieczne jest zatem 
naprawienie własności kolejki. W tym celu wywoływana jest procedura heapify, która przechodzi cały
kopiec kierując się w dół. Naprawienie właności na danym poziomie (wybranie minimum z 3 wartości i
poprawne ustawienie) ma stałą złożoność. Procedura heapify wywołuje się rekurencyjnie na całej 
wysokości kopca, stąd złożoność jest rzędu O(h) = O(log(n)).

priority x p - zmienia priorytet na większy p dla klucza x. Procedura po zmianie priorytetu musi
podobnie jak insert naprawić kopiec, przesuwając element w górę. Stąd złożność procedury jest rzędu
wysokości h kopca, czyli O(h) = O(log(n)).

print (nie wymagane O(log(n)))- drukuje wszystkie elementy kolejki. Iterując po całej kolejce ma 
złożoność O(n).

