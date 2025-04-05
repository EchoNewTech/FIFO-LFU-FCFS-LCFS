from collections import Counter
import random

# Funkcja dla algorytmu FIFO
def fifo(pages, num_frames):
    frames = []
    trafienia_fifo = 0 # Licznik trafień
    bledy_fifo = 0 # Licznik błędów stron

    print("Algorytm FIFO:")
    for i, page in enumerate(pages):
        # Wyświetlenie aktualnego kroku i strony do wczytania
        print(f"\nKrok {i + 1}: Wczytana strona: {page}")
        if page in frames:
            # Trafienie - strona znajduje się już w pamięci
            trafienia_fifo += 1
            print(f"  Trafienie! Strona {page} już w pamięci.")
        else:
            # Błąd strony - trzeba dodać nową stronę do pamięci
            if len(frames) < num_frames:
                # Jeżeli jest miejsce w ramkach - dodajemy stronę
                frames.append(page)
                print(f"  Dodano stronę {page} do pamięci.")
            else:
                # Jeżeli nie ma miejsca w ramkach - usuwamy najstarszą stronę
                removed_page = frames.pop(0)
                frames.append(page)
                print(f"  Usunięto stronę {removed_page}, dodano stronę {page}.")
            bledy_fifo += 1
        # Wyświetlenie aktualnego stanu pamięci
        print(f"  Stan pamięci: {frames}")

    return trafienia_fifo, bledy_fifo

# Funkcja obliczająca współczynnik trafień
def wspolczynnik_trafien(trafienia, bledy):
    return (trafienia / (trafienia + bledy)) * 100

# Funkcja do generowania losowych stron
def generuj_strony(liczba_krokow, zakres_stron):
    return [random.randint(0, zakres_stron - 1) for _ in range(liczba_krokow)]

# Interakcja z użytkownikiem
def user():
    # Pobranie danych wejściowych od użytkownika
    #dl_sekwencji = int(input("Podaj długość sekwencji: "))
    #zakres_stron = int(input("Podaj zakres wartości stron (np dla 10 zakres od 0 do 9): "))
    #num_frames = int(input("Podaj liczbę ramek pamięci (rozmiar okna): "))
    # Ustalone dane wejściowe (ale dalej losowe) przed odpaleniem programu
    #dl_sekwencji = 25
    #zakres_stron = 10
    #num_frames = 11

    # Ustalone dane wejściowe przed odpaleniem (już nie losowe)
    pages = [1, 2, 3, 4, 1, 2, 3, 4]
    num_frames = 2

    # Generowanie losowych stron
    #pages = generuj_strony(dl_sekwencji, zakres_stron)

    # Oblicz wyniki dla FIFO
    trafienia_fifo, bledy_fifo = fifo(pages, num_frames)
    wspolczynnik_fifo = wspolczynnik_trafien(trafienia_fifo, bledy_fifo)

    print("\n===== Podsumowanie wyników =====")
    print(f"Algorytm FIFO:")
    print(f"Liczba błędów stron: {bledy_fifo}")
    print(f"Liczba trafień: {trafienia_fifo}")
    print(f"Współczynnik trafień: {wspolczynnik_fifo:.2f}%")

# Uruchomienie programu
user()
