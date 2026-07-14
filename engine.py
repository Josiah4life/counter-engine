import json

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

class Playstyle:
    def __init__(self, name, description, strengths, vulnerabilities):
        self.name = name
        self.description = description
        self.strengths = strengths
        self.vulnerabilities = vulnerabilities
    
    def display_info(self):
        print(f"Playstyle: {self.name}")
        print(f"Description: {self.description}")
        print(f"Strengths: {', '.join(self.strengths)}")
        print(f"Vulnerabilities: {', '.join(self.vulnerabilities)}")


if __name__ == "__main__":
    print("Attempting to load configuration data layer...")
    tactics_data = load_tactics()
    
    if tactics_data:
        print("Success! Loaded playstyles:")
        for playstyle in tactics_data.get("playstyles", {}).values():
            playstyle_details = Playstyle(**playstyle)
            playstyle_details.display_info()
            print("-" * 40)
            print("\n")