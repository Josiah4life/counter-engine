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

if __name__ == "__main__":
    print("Attempting to load configuration data layer...")
    tactics_data = load_tactics()
    
    if tactics_data:
        print("Success! Loaded playstyles:")
        for playstyle in tactics_data.get("playstyles", {}):
            print(f" - {playstyle}")