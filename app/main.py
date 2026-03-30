# gegeben das Würfelspiel ist gestartet,
# wenn ich einen Wurf auslöse,
# dann muss das Ergebnis eine Ganzzahl zwischen 1 und 6 (inklusiv) sein



# gegeben ich führe eine sehr hohe Anzahl an Würfen durch,
# wenn ich die Ergebnisse analysiere,
# dann sollte jede Zahl (1-6) annähernd gleich oft vorkommen (Gleichverteilung).



# gegeben ich habe gerade gewürfelt,
# wenn das Ergebnis angezeigt wird,
# dann werde ich sofort gefragt, ob ich erneut würfeln möchte.

from DiceGameEngine import DiceGameEngine
# from DiceStatistik import DiceStatistik 


def start_game():
    engine = DiceGameEngine(sides=6)
    while True:
        choice = input("Drücke [N], um zu würfeln, [Q] zum Beenden, [S] zum Anzeigen der Statistiken ...")
        match choice.lower():
            case "n":
                result = engine.roll()
                print(f"Du hast eine {result} gewürfelt!")
            case "s":
                distribution = engine.stats.get_distribution()
                print("Aktuelle Verteilung:")
                for side, freq in distribution.items():
                    print(f"{side}: {freq:.2%}")
                print("Häufigkeit der Ergebnisse:")
                for side, count in engine.stats.counts.items():
                    print(f"{side}: {count} mal")
            case "q":
                print("Danke fürs Spielen! Auf Wiedersehen!")
                break
            case _:
                print("Ungültige Eingabe. Bitte versuche es erneut.")

if __name__ == "__main__":
    start_game()

    

    
