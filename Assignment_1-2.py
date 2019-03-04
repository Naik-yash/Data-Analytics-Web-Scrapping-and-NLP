from collections import Counter

# import numpy as np
import csv


def count_token(text):
    token_count = {}
    text.strip()
    list = text.split()
    list1 = []
    print(list[0:])
    for x in list:
        if len(x) > 1:
            list1.append(x)
        else:
            continue

    print(list1)
    for x in range(7):
        list1[x] = list1[x].lower()

    print(list1)

    token_count = Counter(list)

    token_count = ({x: text.count(x) for x in set(list)})

    return token_count

class Text_Analyzer(object):
    
    def __init__(self, input_file, output_file):
        
        # add your code
        self.input_file = input_file
        self.output_file = output_file
          
    def analyze(self):
        
        
        # add your code
        #Reading the Input file
        
        input_file = self.input_file
        output_file = self.output_file
        
        f = open(input_file, "r")                       
        # loop through all lines
        lines=[line for line in f]                     
        print (lines)

        #Concatenating into string
        sent_str = ""
        sent_str = ''.join(lines)
        print(sent_str)

        #calling the function "count_token" to get a token-count dictionary
        out_dict = count_token(sent_str)
        print(out_dict)

        #saving the dictionary into foo.csv with each key-value pair as a line delimited by comma
        with open(output_file,'w') as f:
            w = csv.writer(f, delimiter=",")
            w.writerows(out_dict.items()) 
if __name__ == "__main__":  
    
    # Test Question 1
    text='''Hello world!
        This is a hello world example !'''   
    print(count_token(text))
    
    # # The output of your text should be: 
    # {'this': 1, 'is': 1, 'example': 1, 'world!': 1, 'world': 1, 'hello': 2}
    
    # Test Question 2
    analyzer=Text_Analyzer("foo.txt", "foo.csv")
    vocabulary=analyzer.analyze()

            