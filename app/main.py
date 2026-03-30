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
    engine = DiceGameEngine(sides=26)
    while True:
    
        input("Drücke Enter, um zu würfeln...")
        result = engine.roll()
        print(f"Du hast eine {result} gewürfelt!")
        cont = input("Möchtest du erneut würfeln? (j/n): ")
        if cont.lower() != 'j':
            break
    print("Danke fürs Spielen! Hier sind deine Statistiken:")
    print(engine.stats)


if __name__ == "__main__":
    start_game()

    

    
