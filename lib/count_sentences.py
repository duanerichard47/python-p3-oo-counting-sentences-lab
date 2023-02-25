#!/usr/bin/env python3

class MyString:

    def __init__(self, value = ""):
        self._value = value
        
    def get_value(self):
        return self._value

    def set_value(self, value):
        if type(value) == str:
            self._value = value
        else: 
            print('The value must be a string.')

    value = property(get_value, set_value)

    def is_sentence(self):
        return self.value.endswith(".")
        # self.value = value
        # self.value_to_list = [letter for letter in self.value]
        # print(self.value_to_list)
        # period = '.'
        # if period in self.value_to_list:
      
    def is_question(self):
        return self.value.endswith("?")
        # self.value = value
        # self.value_to_list = [letter for letter in self.value]
        # question_mark ='?'
        # if question_mark in self.value_to_list:
        #     return True
        # else:
        #     return False
         
    
    def is_exclamation(self):
        return self.value.endswith("!")
        # self.value = value
        # self.value_to_list = [letter for letter in self.value]
        # exclamation = "!"
        # last_index = len(self.value)-1
        # if exclamation == self.value_to_list[last_index]:
        #     return True
        # else:
        #     return False
         

    def count_sentences(self):
        if len(self.value) == 0:
            return 0
        else:
            splitted_value = self.value.replace('?', '.')
            splitted_value = splitted_value.replace('!', '.')
            splitted_value = splitted_value.split('. ')
            print(splitted_value)
            print(len(splitted_value))
            length = len(splitted_value)
            return length

        