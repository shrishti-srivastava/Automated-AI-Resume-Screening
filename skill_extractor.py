import pandas as pd

class SkillExtractor:

    def __init__(self):
        # 1. Load your skills dataset
        df = pd.read_csv("data/skills.csv")
        
        # 2. Force all column headers to be stripped of spaces and lowercase
        df.columns = df.columns.str.strip().str.lower()
        
        # 3. Safe extraction from the normalized 'skills' header
        self.skills = df["skill"].tolist()

    def extract_skills(self, text):
        found = []
        for skill in self.skills:
            if skill.lower() in text.lower():
                found.append(skill)
        return found