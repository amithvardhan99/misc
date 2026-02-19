#!/usr/bin/env python
import sys
import warnings

from datetime import datetime


from crew import NewsScraper

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

"""
    Run the crew.
"""
"""
def run():
    
    inputs = {
        'topic': "Can you retrieve latest news on Trump's immigration crackdown?",
        'date': str(datetime.now().year)
    }

    try:
        NewsScraper().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
"""

def run():

    list_of_inputs = [
        
        {"topic": "Latest news on Anthropic's Claude", "date": str(datetime.now().year), "file_name": "anthropic"},
        
        {"topic": "How was Microsoft as an organisation performing compared to other tech giants like Google, Facebook etc.", "date": 2019, "file_name": "performance_of_organisations"},
        
        {"topic": "Flaws of Indian education system", "date": 2022, "file_name": "education"}

    ]

    try:
        NewsScraper().crew().kickoff_for_each(list_of_inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()