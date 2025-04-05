import random
from tabulate import tabulate

# Funkcja generująca dane dla procesów
def generuj_procesy(liczba_procesow):
    # Losowanie danych dla procesów
    procesy = []
    for i in range(liczba_procesow):
        #czas_przybycia = random.randint(0, 25) # Losowy czas przybycia
        #czas_wykonania = random.randint(1, 25) # Losowy czas wykonania
        print(f"\nWprowadź dane dla procesu P{i + 1}: ")
        czas_przybycia = int(input("  Czas przybycia: "))
        czas_wykonania = int(input("  Czas wykonania: "))
        procesy.append({"id": i + 1, "czas_przybycia": czas_przybycia, "czas_wykonania": czas_wykonania})
    return procesy

# Funkcja obliczajaca wyniki dla algorytmów FCFS i LCFS
def oblicz_wyniki(procesy, sortowanie_desc=False):
    # Sortowanie procesów według czasu przybycia (FCFS - domyślne, LCFS - przy sortowaniu malejącym)
    procesy.sort(key=lambda x: (x["czas_przybycia"], x["id"]))
    # Inicjalizacja zmiennych
    czas_biezacy = 0
    suma_czas_wyjscia = 0
    suma_czas_realizacji = 0
    suma_czas_oczekiwania = 0
    kolejka = []  # Kolejka procesów do przetworzenia
    wyniki = []  # Lista wyników dla kazdego procesu

    while procesy or kolejka:
        # Dodawanie procesów do kolejki, jeśli ich czas przybycia <= aktualny czas
        while procesy and procesy[0]["czas_przybycia"] <= czas_biezacy:
            kolejka.append(procesy.pop(0))

        # Sortowanie kolejki zgodnie z algorytmem (rosnąco/malejąco po czasie przybycia)
        if sortowanie_desc:
            kolejka.sort(key=lambda x: (-x["czas_przybycia"], -x["id"]))
        else:
            kolejka.sort(key=lambda x: (x["czas_przybycia"], x["id"]))

        if kolejka:
            # Pobranie pierwszego procesu z kolejki
            proces = kolejka.pop(0)
            czas_przybycia = proces["czas_przybycia"]
            czas_wykonania = proces["czas_wykonania"]

            # Aktualizacja czasu, jeśli proces przybył po aktualnym czasie
            if czas_przybycia > czas_biezacy:
                czas_biezacy = czas_przybycia

            # Obliczenie statystyk
            czas_wyjscia = czas_biezacy + czas_wykonania
            czas_realizacji = czas_wyjscia - czas_przybycia
            czas_oczekiwania = czas_realizacji - czas_wykonania

            # Obliczenie sum czasów do obliczenia średnich czasów
            suma_czas_wyjscia += czas_wyjscia
            suma_czas_realizacji += czas_realizacji
            suma_czas_oczekiwania += czas_oczekiwania

            # Dodanie wyników procesu do listy wyników
            wyniki.append((f"P{proces['id']}", czas_przybycia, czas_wykonania, czas_wyjscia, czas_realizacji, czas_oczekiwania))

            # Aktualizacja bieżącego czasu
            czas_biezacy = czas_wyjscia
        else:
            # Jeśli kolejka jest pusta, przesuwamy czas do następnego procesu
            czas_biezacy = procesy[0]["czas_przybycia"]

    # Obliczanie średnich czasów
    sredni_czas_wyjscia = suma_czas_wyjscia / len(wyniki)
    sredni_czas_realizacji = suma_czas_realizacji / len(wyniki)
    sredni_czas_oczekiwania = suma_czas_oczekiwania / len(wyniki)

    return wyniki, sredni_czas_wyjscia, sredni_czas_realizacji, sredni_czas_oczekiwania

# Funkcja drukująca wyniki w formie tabeli
def drukuj_wyniki(algorytm, wyniki, srednie):
    print(f"\nKolejność wykonywania procesów ({algorytm}):")
    print(tabulate(
        wyniki,
        headers=["Proces", "Czas przybycia", "Czas wykonania", "Czas wyjścia", "Czas realizacji", "Czas oczekiwania"],
        tablefmt="grid"
    ))

    print("\nŚrednie czasy:")
    print(f"Średni czas oczekiwania: {srednie[2]:.2f}")
    print(f"Średni czas realizacji: {srednie[1]:.2f}")
    print(f"Średni czas wyjścia: {srednie[0]:.2f}")

def main():
    # Pobranie ilości procesów od użytkownika
    liczba_procesow = int(input("Podaj liczbę procesów: "))
    #liczba_procesow = 10

    # Generowanie procesów
    procesy = generuj_procesy(liczba_procesow)

    print("\nTabela procesów przed sortowaniem:")
    print(tabulate(
        [(f"P{p['id']}", p['czas_przybycia'], p['czas_wykonania']) for p in procesy],
        headers=["Proces", "Czas przybycia", "Czas wykonania"],
        tablefmt="grid"
    ))

    # Obliczenie wyników
    wyniki_fcfs, sredni_fcfs_wyjscia, sredni_fcfs_realizacji, sredni_fcfs_oczekiwania = oblicz_wyniki(procesy.copy())
    wyniki_lcfs, sredni_lcfs_wyjscia, sredni_lcfs_realizacji, sredni_lcfs_oczekiwania = oblicz_wyniki(procesy.copy(),
                                                                                                      sortowanie_desc=True)
    # Wyświetlenie wyników
    drukuj_wyniki("FCFS", wyniki_fcfs, (sredni_fcfs_wyjscia, sredni_fcfs_realizacji, sredni_fcfs_oczekiwania))
    drukuj_wyniki("LCFS", wyniki_lcfs, (sredni_lcfs_wyjscia, sredni_lcfs_realizacji, sredni_lcfs_oczekiwania))
# Uruchomienie programu
if __name__ == "__main__":
    main()
