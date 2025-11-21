#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, string):
        self.knowledge.append(string)
    
    def ask_question(self, question):
        return f"Can you explain {question}?"
