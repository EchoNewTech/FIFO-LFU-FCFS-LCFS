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

# Funkcja dla algorytmu LFU
def lfu(pages, num_frames):
    frames = [] # Lista przechowująca strony w ramkach pamięci
    freq = Counter()  # Licznik częstotliwości
    trafienia_lfu = 0 #Licznik trafień
    bledy_lfu = 0 # Licznik błędów stron

    print("\nAlgorytm LFU:")
    for i, page in enumerate(pages):
        # Wyświetlanie aktualnego kroku i strony do wczytania
        print(f"\nKrok {i + 1}: Wczytana strona: {page}")
        if page in frames:
            # Trafienie – strona znajduje się w pamięci
            trafienia_lfu += 1
            freq[page] += 1
            print(f"  Trafienie! Strona {page} już w pamięci.")
        else:
            # Błąd strony – należy dodać nową stronę do pamięci
            if len(frames) < num_frames:
                frames.append(page)
                print(f"  Dodano stronę {page} do pamięci.")
            else:
                # Znalezienie strony o najniższej częstotliwości
                lfu_page = min(frames, key=lambda p: freq[p])
                frames.remove(lfu_page)
                frames.append(page)
                print(f"  Usunięto stronę {lfu_page}, dodano stronę {page}.")
            bledy_lfu += 1
            freq[page] += 1
        # Wyświetlanie aktualnego stanu pamięci i liczników częstotliwości
        print(f"  Stan pamięci: {frames}, Częstotliwości: {dict(freq)}")

    return trafienia_lfu, bledy_lfu

# Funkcja obliczająca współczynnik trafień
def wspolczynnik_trafien(trafienia, bledy):
    return (trafienia / (trafienia + bledy)) * 100

# Funkcja do generowania losowych stron
def generuj_strony(liczba_krokow, zakres_stron):
    return [random.randint(0, zakres_stron - 1) for _ in range(liczba_krokow)]

# Interakcja z użytkownikiem
def user():
    # Pobranie danych wejściowych od użytkownika
    dl_sekwencji = int(input("Podaj długość sekwencji: "))
    zakres_stron = int(input("Podaj zakres wartości stron (np dla 10 zakres od 0 do 9): "))
    num_frames = int(input("Podaj liczbę ramek pamięci (rozmiar okna): "))
    # Ustalone dane wejściowe (ale dalej losowe) przed odpaleniem programu
    #dl_sekwencji = 25
    #zakres_stron = 10
    #num_frames = 11

    # Ustalone dane wejściowe przed odpaleniem (już nie losowe)
    #pages = [7, 5, 3, 8, 3, 2, 2, 0, 2, 5, 6, 1, 0, 9, 4, 9, 4, 9, 1, 8, 0, 6, 4, 6, 5]
    #num_frames = 2

    # Generowanie losowych stron
    pages = generuj_strony(dl_sekwencji, zakres_stron)

    # Wyświetlenie wygenerowanej sekwencji
    print(f"\nWygenerowana sekwencja: {pages}\n")

    # Oblicz. wyniki dla FIFO
    trafienia_fifo, bledy_fifo = fifo(pages, num_frames)
    wspolczynnik_fifo = wspolczynnik_trafien(trafienia_fifo, bledy_fifo)

    # Oblicz. wyniki dla LFU
    trafienia_lfu, bledy_lfu = lfu(pages, num_frames)
    wspolczynnik_lfu = wspolczynnik_trafien(trafienia_lfu, bledy_lfu)

    # Wyświetlanie wyników
    print("\n===== Podsumowanie wyników =====")
    print(f"Algorytm LFU:")
    print(f"Liczba błędów stron: {bledy_lfu}")
    print(f"Liczba trafień: {trafienia_lfu}")
    print(f"Współczynnik trafień: {wspolczynnik_lfu:.2f}%\n")

    print(f"Algorytm FIFO:")
    print(f"Liczba błędów stron: {bledy_fifo}")
    print(f"Liczba trafień: {trafienia_fifo}")
    print(f"Współczynnik trafień: {wspolczynnik_fifo:.2f}%")

# Uruchomienie programu
user()
