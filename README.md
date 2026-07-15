# eFootball Tactical Matchup & Counter Engine

An interactive Command Line Interface (CLI) application built from scratch in Python. This engine serves as a tactical decision-making assistant for eFootball Mobile team playstyles, decoupling structural gaame rules using clean Object-Oriented Programming (OOP) principles.

## Why This Project?

Many web and backend projects rely heavily on database wrappers (CRUD apps) or basic API calls to do the heavy lifting. This project was engineered to solve a core logical problem locally:

- Game rules, strengths, and vulnerabilities are stored in an external configuration layer (`tactics.json`). The Python logic doesn't hardcode any specific matchup rules. Changing the JSON completely shifts the engine's behavior without modifying source code.
- **OOP Domain Modeling:** Raw JSON dictionary data is parsed and instantiated into strict, typed memory objects (`Playstyle`) rather than being passed around as raw string variables or dictionaries.
- **Interactive Flow Control:** Features a dual-loop CLI design, offering a seamless navigation system that dynamically handles user queries without reloading static resources from disk.

## Tech Stack & Concepts

- **Language:** Python 3
- **Data Format:** JSON (JavaScript Object Notation)
- **Programming Paradigm:** Object-Oriented Programming (OOP)
- **Architecture Pattern:** Decoupled Data/Execution

## Directory Structure

```text
counter-engine/
|
|--- data/
|    |--- tactics.json
|
|--- src/
|    |--- engine.py
|    |--- models.py
|
|--- .antigravity.md
|--- .gitignore
|--- README.md
|--- main.py
```

## Run the application

python main.py

## Usuage Example

#### EFOOTBALL COUNTER ENGINE

Available Playstyles:

- Quick Counter
- Possession Game
- Long Ball Counter
- Out Wide
- Long Ball

---

Enter opponent playstyle (or 'exit' to quit): Out Wide
Processing opponent playstyle: Out Wide

--- OUT WIDE OPTIONS ---

1. View Playstyle Description
2. View Who This Style Counters (Strengths)
3. View Who Counters This Style (Vulnerabilities)
4. Back to Main Menu
   Select an option (1-4): 3

[Recommended Counters] To exploit Out Wide, use:
-> Quick Counter: High defensive line with aggressive passing...
-> Long Ball: Direct, bypass-midfield playstyle...
