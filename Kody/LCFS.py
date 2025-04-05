import random
from tabulate import tabulate  # Biblioteka do wyświetlania tabel w czytelny sposób

def lcfs():
    # Pobranie ilości procesów od użytkownika
    liczba_procesow = int(input("Podaj liczbę procesów: "))

    # Losowanie danych dla procesów
    procesy = []
    for i in range(liczba_procesow):
        #czas_przybycia = random.randint(0, 25) # Losowy czas przybycia
        #czas_wykonania = random.randint(1, 25) # Losowy czas wykonania
        print(f"\nWprowadź dane dla procesu P{i + 1}: ")
        czas_przybycia = int(input("  Czas przybycia: "))
        czas_wykonania = int(input("  Czas wykonania: "))
        procesy.append({"id": i + 1, "czas_przybycia": czas_przybycia, "czas_wykonania": czas_wykonania})

    # Wyświetlenie tabeli procesów przed rozpoczęciem symulacji
    print("\nTabela procesów przed rozpoczęciem symulacji:")
    print(tabulate(
        [(f"P{p['id']}", p['czas_przybycia'], p['czas_wykonania']) for p in procesy],
        headers=["PID", "Czas przybycia", "Czas wykonania"],
        tablefmt="grid"
    ))

    # Inicjalizacja zmiennych
    czas_biezacy = 0  # Aktualny czas symulacji
    suma_czas_wyjscia = 0  # Suma czasów wyjścia procesów
    suma_czas_realizacji = 0  # Suma czasów realizacji procesów
    suma_czas_oczekiwania = 0  # Suma czasów oczekiwania procesów

    kolejka = []  # Stos do przechowywania procesów zgodnie z zasadą LCFS
    wyniki = []  # Lista wyników do wyświetlenia

    # Sortowanie procesów według czasu przybycia (dla prawidłowej symulacji)
    procesy.sort(key=lambda x: x["czas_przybycia"])

    # Pętla symulacyjna, działa dopóki są procesy do obsłużenia
    while procesy or kolejka:
        # Dodanie do kolejki procesów, które dotarły w bieżącym czasie
        while procesy and procesy[0]["czas_przybycia"] <= czas_biezacy:
            kolejka.append(procesy.pop(0))

        if kolejka:
            # Pobranie ostatniego procesu ze stosu (zasada LCFS)
            proces = kolejka.pop()

            czas_przybycia = proces["czas_przybycia"]
            czas_wykonania = proces["czas_wykonania"]

            # Obliczanie metryk dla procesu
            czas_wyjscia = czas_biezacy + czas_wykonania
            czas_realizacji = czas_wyjscia - czas_przybycia
            czas_oczekiwania = czas_realizacji - czas_wykonania

            # Aktualizacja sum dla średnich czasów
            suma_czas_wyjscia += czas_wyjscia
            suma_czas_realizacji += czas_realizacji
            suma_czas_oczekiwania += czas_oczekiwania

            # Dodanie wyników dla bieżącego procesu
            wyniki.append((
                f"P{proces['id']}", czas_przybycia, czas_wykonania, czas_wyjscia, czas_realizacji, czas_oczekiwania
            ))

            # Aktualizacja bieżącego czasu symulacji
            czas_biezacy = czas_wyjscia
        else:
            # Jeśli kolejka jest pusta, przechodzimy do następnej jednostki czasu
            czas_biezacy += 1

    # Wyświetlenie tabeli wyników
    print("\nKolejność wykonywania procesów (LCFS):")
    print(tabulate(
        wyniki,
        headers=[
            "PID", "Czas przybycia", "Czas wykonania", "Czas wyjścia", "Czas realizacji", "Czas oczekiwania"
        ],
        tablefmt="grid"
    ))

    # Obliczanie średnich czasów dla wszystkich procesów
    sredni_czas_wyjscia = suma_czas_wyjscia / liczba_procesow
    sredni_czas_realizacji = suma_czas_realizacji / liczba_procesow
    sredni_czas_oczekiwania = suma_czas_oczekiwania / liczba_procesow

    # Wyświetlenie średnich czasów
    print("\nŚrednie czasy:")
    print(f"Średni czas wyjścia: {sredni_czas_wyjscia:.2f}")
    print(f"Średni czas realizacji: {sredni_czas_realizacji:.2f}")
    print(f"Średni czas oczekiwania: {sredni_czas_oczekiwania:.2f}")

# Uruchomienie funkcji
if __name__ == "__main__":
    lcfs()
