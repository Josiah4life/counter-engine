import json
from src.models import Playstyle

def load_tactics(file_path="tactics.json"):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Check your file format syntax.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

class MatchupEngine:
    def __init__(self, file_path="data/tactics.json"):
        self.file_path = file_path
        self.playstyles = {}
        tactics = load_tactics(self.file_path)
        self._initialize_playstyles(tactics)
    
    def _initialize_playstyles(self, raw_data):
        if raw_data and "playstyles" in raw_data:
            # store each playstyle in the playstyles dictionary with playstyle name as key and Playstyle object as value.
            for key, value in raw_data["playstyles"].items():
                self.playstyles[key] = Playstyle(**value)
                
    def get_counter_strategies(self, opponent_style):
        formatted_style = opponent_style.title()
        if formatted_style not in self.playstyles:
            print(f"Error: Playstyle `{opponent_style}` (formatted as `{formatted_style}`) not found in the loaded tactics.")
            return None
        vulnerabilities = self.playstyles[formatted_style].vulnerabilities
        counter_objects = []
        for vuln in vulnerabilities:
            if vuln in self.playstyles:
                counter_objects.append(self.playstyles[vuln])
        return counter_objects