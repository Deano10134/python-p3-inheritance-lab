#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "Variables store data in memory",
            "Functions encapsulate reusable code blocks",
            "Classes define blueprints for objects",
            "Loops allow repeated execution of code",
            "Conditionals enable decision-making in programs",
            "Lists are ordered collections of items",
            "Dictionaries store key-value pairs",
            "Inheritance promotes code reusability",
        ]

    def teach(self):
        return random.choice(self.knowledge)
    
    def answer_question(self, question):
        answers = {
            "What is the capital of France?": "The capital of France is Paris.",
            "What is 2 + 2?": "2 + 2 equals 4.",
            "What is the boiling point of water?": "The boiling point of water is 100 degrees Celsius.",
            "Who wrote 'Romeo and Juliet'?": "William Shakespeare wrote 'Romeo and Juliet'.",
            "What is the largest planet in our solar system?": "The largest planet in our solar system is Jupiter."
        }
        return answers.get(question, "I'm not sure about that. Let me get back to you.")

