from DiceGameEngine import DiceGameEngine
from SaveManager import SaveManager


def main():
    engine = None

    while True:
        print("\nWelcome to the Dice Game!")
        print("[1] New Game")
        print("[2] Continue (Load Save)")
        print("[3] Show Statistics")
        print("[4] Roll Dice")
        print("[5] Save Game")
        print("[6] Quit without Saving")

        choice = input("\nSelect an option: ").strip()

        match choice:
            case "1":
                try:
                    s = int(input("How many sides? (default 6): ") or 6)
                    engine = DiceGameEngine(sides=s)
                    print(f"New game started with {s} sides.")
                    print(f"New game started! Rolling first dice: {engine.roll()}")
                except ValueError:
                    print("Invalid input. Defaulting to 6 sides.")
                    engine = DiceGameEngine(sides=6)

            case "2":
                saves = SaveManager.get_all_saves()
                if not saves:
                    print("No save files found in /saves directory.")
                    continue

                print("\nAvailable Saves:")
                for i, path in enumerate(saves, 1):
                    print(f"[{i}] {path.name}")

                try:
                    save_choice = int(input("Select file number (or 0 to cancel): "))
                    if save_choice == 0:
                        continue

                    selected_file = saves[save_choice - 1]
                    strat = SaveManager.get_strategy(selected_file.suffix)

                    engine = DiceGameEngine(storage_tool=strat)
                    if engine.load_from_file(selected_file):
                        print(f"Game loaded from {selected_file.name}")
                except (ValueError, IndexError):
                    print("Invalid selection.")

            case "3":
                if not engine:
                    print("No active game. Start a new one or load a save first.")
                else:
                    print(f"\nStatistics (Total Rolls: {engine.stats.rolls})")
                    dist = engine.stats.get_distribution()
                    for side, freq in dist.items():
                        if freq > 0:
                            print(f"Side {side}: {freq:.1%}")
                    counts = engine.stats.counts
                    for side, count in counts.items():
                        if count > 0:
                            print(f"Side {side}: {count} rolls")

            case "4":
                if not engine:
                    print("No active game. Start a new one or load a save first.")
                else:
                    result = engine.roll()
                    print(f"Rolled a {result}!")

            case "5":
                if not engine:
                    print("Nothing to save. Start a game first.")
                else:
                    fmt = (
                        input("Choose format (json/yaml/xml) [default: json]: ")
                        .lower()
                        .strip()
                        or "json"
                    )
                    strat = SaveManager.get_strategy(fmt)

                    if strat:
                        engine.storage_tool = strat
                        path = SaveManager.construct_filepath(fmt)
                        engine.finalize(path)
                    else:
                        print(" Unsupported format.")

            case "6":
                confirm = input("Are you sure you want to quit? (y/n): ").lower()
                if confirm == "y":
                    print("Goodbye!")
                    break

            case _:
                print("Invalid command. Please select 1-6.")


if __name__ == "__main__":
    main()
