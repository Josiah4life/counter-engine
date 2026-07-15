from src.engine import MatchupEngine

if __name__ == "__main__":
    print("Initializing the Counter Engine...")
    engine = MatchupEngine()
    
    while True:
        print("\n" + "=" * 40)
        print("         EFOOTBALL COUNTER ENGINE")
        print("=" * 40)
        
        print("\nAvailable Playstyles:")
        for style in engine.playstyles.keys():
            print(f" - {style}")
        print("=" * 40)
        
        user_input = input("\nEnter opponent playstyle (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the Counter Engine. Goodluck with your match!")
            break
        
        opponent_style = user_input.title()
        
        if opponent_style not in engine.playstyles:
            print(f"\nError: Playstyle '{user_input}' not found. Please try again.")
            continue
        
        selected_style = engine.playstyles[opponent_style]
        
        while True:
            print(f"\n--- {selected_style.name.upper()} OPTIONS ---")
            print("1. View Playstyle Description")
            print("2. View Who This Style Counters (Strengths)")
            print("3. View Who Counters This Style (Vulnerabilities)")
            print("4. Back to Main Menu")
            
            choice = input("Select an option (1-4): ").strip()
            if choice == "1":
                print(f"\n[Description]\n{selected_style.description}")
                
            elif choice == "2":
                print(f"\n[Strengths] {selected_style.name} is strong against:")
                for strength in selected_style.strengths:
                    print(f" -> {strength}")
                    
            elif choice == "3":
                print(f"\n[Recommended Counters] To exploit {selected_style.name}, use:")
                counters = engine.get_counter_strategies(selected_style.name)
                if counters:
                    for counter_style in counters:
                        print(f" -> {counter_style.name}: {counter_style.description}")
                else:
                    print(" No direct counters found.")
                    
            elif choice == "4":
                print(f"\nReturning to main playstyle list...")
                break # This breaks the inner loop, back to the main menu
                
            else:
                print("\nInvalid choice. Please enter a number from 1 to 4.")