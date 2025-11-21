#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Class "User" in user.py is a class that represents a user.
    # Class "User" in user.py initializes with first and last name.
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
