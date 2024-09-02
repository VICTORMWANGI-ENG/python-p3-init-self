#!/usr/bin/env python3

class Dog:
     
    def __init__(self, name,breed='Mutt'):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self
