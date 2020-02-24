#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Dico:
    def __init__(self):
         self.keys = []
         self.values = []

    def get(self, key):
        return 0

    def pop(self, key):
        return 0

    def update(self, key, value):
        return 0

    def getCorr(self, key):
        for i in range(len(self.keys)):
            if(self.keys[i] == key):
                return self.values[i]
        return None

    def popCorr(self, key):
        ret = None
        for i in range(len(self.keys)):
            if(self.keys[i]== key):
                ret = self.values[i]
                del self.keys[i]
                del self.values[i]
                break
        return ret

    def updateCorr(self, key, value):
        for i in range(len(self.keys)):
            if(self.keys[i] == key):
                self.values[i] = value
        self.keys.append(key)
        self.values.append(value)