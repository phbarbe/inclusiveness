#récupération du CSV
import pandas as pd
import requests
url = "https://raw.githubusercontent.com/phbarbe/inclusiveness/main/Questionnaire.csv"
r = requests.get(url)

df_questionnaire = pd.read_csv(url, sep=";")
df_questionnaire.head()

#transforme le dataframe en dictionnaire

quiz = df_questionnaire.to_dict('index')
quiz

#Tire au sort 20 questions du questionnaire
import random

def obtenir_20_questions(quiz):
    if len(quiz) < 20:
        raise ValueError("La liste des questions doit contenir au moins 20 questions.")
    # Convert the dictionary keys to a list before sampling
    return random.sample(list(quiz.keys()), 20)  

# Obtenir 20 questions aléatoires
questions_aleatoires = obtenir_20_questions(quiz)

# Afficher les 20 questions aléatoires
for question_key in questions_aleatoires:
    print(quiz[question_key])  # Access the question details using the key

from fastapi import FastAPI
from typing import List, Dict
import random

app = FastAPI()

def obtenir_20_questions(quiz: Dict):
    if len(quiz) < 20:
        raise ValueError("La liste des questions doit contenir au moins 20 questions.")
    return random.sample(list(quiz.values()), 20)

@app.get("/questions/", response_model=List[Dict])
def lire_questions():
    try:
        questions = obtenir_20_questions(quiz)
        return questions
    except ValueError as e:
        return {"error": str(e)}


                