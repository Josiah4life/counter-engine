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
