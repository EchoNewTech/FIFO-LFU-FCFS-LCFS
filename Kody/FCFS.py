import random
from tabulate import tabulate

def fcfs():
    # Pobranie ilości procesów od użytkownika
    liczba_procesow = int(input("Podaj liczbę procesów: "))

    # Losowanie danych dla procesów
    procesy = []
    for i in range(liczba_procesow):
        czas_przybycia = random.randint(0, 25) # Losowy czas przybycia
        czas_wykonania = random.randint(1, 25) # Losowy czas wykonania
        #print(f"\nWprowadź dane dla procesu P{i + 1}: ")
        #czas_przybycia = int(input("  Czas przybycia: "))
        #czas_wykonania = int(input("  Czas wykonania: "))
        procesy.append({"id": i + 1, "czas_przybycia": czas_przybycia, "czas_wykonania": czas_wykonania})

    # Wyświetlenie tabeli przed symulacją
    print("\nTabela procesów przed symulacją:")
    print(tabulate(
        [(f"P{p['id']}", p['czas_przybycia'], p['czas_wykonania']) for p in procesy],
        headers=["PID", "Czas przybycia", "Czas wykonania"],
        tablefmt="grid"
    ))

    # Sortowanie procesów wg czasu przybycia
    procesy.sort(key=lambda x: x["czas_przybycia"])

    # Inicjalizacja zmiennych czasu i statystyk
    czas_biezacy = 0
    suma_czas_wyjscia = 0
    suma_czas_realizacji = 0
    suma_czas_oczekiwania = 0
    kolejka = [] # Kolejka procesów do przetworzenia
    wyniki = [] # Lista wyników dla kazdego procesu

    # Symulacja wykonywania procesów w jednostce czasu
    while procesy or kolejka:
        # Dodawanie procesów do kolejki gotowych, gdy ich czas przybycia jest zgodny z bieżącym czasem
        while procesy and procesy[0]["czas_przybycia"] <= czas_biezacy:
            kolejka.append(procesy.pop(0))

        if kolejka:
            # Pobieramy pierwszy proces z kolejki
            proces = kolejka.pop(0)
            czas_przybycia = proces["czas_przybycia"]
            czas_wykonania = proces["czas_wykonania"]
            czas_wyjscia = czas_biezacy + czas_wykonania # Obliczenie czasu zakończenia procesu
            czas_realizacji = czas_wyjscia - czas_przybycia # Obliczenie czasu realizacji
            czas_oczekiwania = czas_realizacji - czas_wykonania # Obliczenie czasu oczekiwania

            # Aktualizacja sum czasów do analizy
            suma_czas_wyjscia += czas_wyjscia
            suma_czas_realizacji += czas_realizacji
            suma_czas_oczekiwania += czas_oczekiwania

            wyniki.append((f"P{proces['id']}", czas_przybycia, czas_wykonania, czas_wyjscia, czas_realizacji, czas_oczekiwania))

            czas_biezacy = czas_wyjscia # Aktualizacja czasu bieżącego
        else:
            # Jeżeli kolejka jest pusta, przechodzimy do następnej jednostki czasu
            czas_biezacy += 1

    # Wyświetlenie tabeli wyników
    print("\nKolejność wykonywania procesów (FCFS - symulacja):")
    print(tabulate(
        wyniki,
        headers=["PID", "Czas przybycia", "Czas wykonania", "Czas wyjścia", "Czas realizacji", "Czas oczekiwania"],
        tablefmt="grid"
    ))

    # Obliczanie średnich czasów
    sredni_czas_wyjscia = suma_czas_wyjscia / liczba_procesow
    sredni_czas_realizacji = suma_czas_realizacji / liczba_procesow
    sredni_czas_oczekiwania = suma_czas_oczekiwania / liczba_procesow

    print("\nŚrednie czasy:")
    print(f"Średni czas wyjścia: {sredni_czas_wyjscia:.2f}")
    print(f"Średni czas realizacji: {sredni_czas_realizacji:.2f}")
    print(f"Średni czas oczekiwania: {sredni_czas_oczekiwania:.2f}")

# Uruchomienie funkcji
if __name__ == "__main__":
    fcfs()
