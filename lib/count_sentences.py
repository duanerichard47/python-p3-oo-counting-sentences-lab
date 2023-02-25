#!/usr/bin/env python3

class MyString:

    def __init__(self, value = ""):
        self._value = value
        
    

    def get_value(self):
        return self._value

    def set_value(self,input_value):
        # self._value = value
        print(self.input_value)
       
        if self._input_value == str(self.input_value):
            self._input_value = input_value
        else: 
            print('The value must be a string.')

    value = property(get_value, set_value)

    def is_sentence(self, value):
        self.value = self
        self.value_to_list = [letter for letter in self.value]
        print(self.value_to_list)
        period = '.'
        if period in self.value_to_list:
            return True
        else:
            return False

    def is_question(self, value):
        self.value = value
        self.value_to_list = [letter for letter in self.value]
        question_mark ='?'
        if question_mark in self.value_to_list:
            return True
        else:
            return False
    
    def is_exclamation(self, value):
        self.value = value
        self.value_to_list = [letter for letter in self.value]
        exclamation = "!"
        last_index = len(self.value)-1
        if exclamation == self.value_to_list[last_index]:
            return True
        else:
            return False

    def count_sentences(self, value):
        self.value =value
        splitted_value = self.value.split('.')
        length = len(splitted_value)
        return length
        