from src.engine import MatchupEngine

if __name__ == "__main__":
    print("Initializing the Counter Engine...")
    engine = MatchupEngine()
    
    opponent = "Quick Counter"
    print(f"\nEvaluating opponent playstyle: {opponent}")
    print("=" * 40)
    counters = engine.get_counter_strategies(opponent)
    
    if counters:
        print(f"Recommended counters to exploit {opponent}:")
        print("-" * 40)
        for counter_style in counters:
            counter_style.display_info()
            print("-" * 40)