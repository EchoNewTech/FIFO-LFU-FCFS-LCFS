from collections import Counter
import random

def lfu(pages, num_frames):
    frames = []
    freq = Counter()  # Licznik częstotliwości
    trafienia_lfu = 0
    bledy_lfu = 0

    print("\nAlgorytm LFU:")
    for i, page in enumerate(pages):
        print(f"\nKrok {i + 1}: Wczytana strona: {page}")
        if page in frames:
            trafienia_lfu += 1
            freq[page] += 1
            print(f"  Trafienie! Strona {page} już w pamięci.")
        else:
            if len(frames) < num_frames:
                frames.append(page)
                print(f"  Dodano stronę {page} do pamięci.")
            else:
                # Znajdź stronę o najniższej częstotliwości
                lfu_page = min(frames, key=lambda p: freq[p])
                frames.remove(lfu_page)
                frames.append(page)
                print(f"  Usunięto stronę {lfu_page}, dodano stronę {page}.")
            bledy_lfu += 1
            freq[page] += 1

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

    print(f"\nWygenerowane strony: {pages}\n")
    # Oblicz wyniki dla LFU
    trafienia_lfu, bledy_lfu = lfu(pages, num_frames)
    wspolczynnik_lfu = wspolczynnik_trafien(trafienia_lfu, bledy_lfu)

    # Wyświetlanie wyników
    print("\n===== Podsumowanie wyników =====")
    print(f"Algorytm LFU:")
    print(f"Liczba błędów stron: {bledy_lfu}")
    print(f"Liczba trafień: {trafienia_lfu}")
    print(f"Współczynnik trafień: {wspolczynnik_lfu:.2f}%\n")

if __name__ == "__main__":
    user()