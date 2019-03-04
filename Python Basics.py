Question: ## 1. Define a function to analyze the frequency of words in a string ##\n", " - Define a function named "count_token" which\n", " * has a string as an input \n", " * splits the string into a list of tokens by space. For example, "hello world" will be split into two tokens ['hello','world']\n", " * for the tokens, do the following in sequence:\n", " * strips all leading and trailing space of each token\n", " * removes a token if it contain no more than 1 character (use function len on each token, i.e. len(token)<=1)\n", " * converts all tokens into lower case\n", " * create a dictionary containing the count of every remaining token, e.g. {'is': 5, 'hello':1,...}\n", " * returns the dictionary as the output\n", " \n",
## 2. Define a class to analyze a collection of documents ##\n", " - Define a new class called "Text_Analyzer" which has the following:\n", " - two variables: input_file, output_file. Initialize them using the class constructor.\n", " - a function named "analyze" that:\n", " * reads all lines from input_file and concatenate them into a string\n", " * calls the function "count_token" to get a token-count dictionary \n", " * saves the dictionary into output_file with each key-value pair as a line delimited by comma (see "foo.csv" in Exercise 10.3 for examples).\n", " \n", 
## 3. Define a function to analyze a numpy array\n", " - Assume we have a array which contains term frequency of each document. Where each row is a document, each column is a word, and the value denotes the frequency of the word in the document. Define a function named "analyze_tf" which:\n", " * takes the array as an input\n", " * normalizes the frequency of each word as: word frequency divided by the length of the document. Save the result as an array named tf (i.e. term frequency)\n", " * calculates the document frequency (df) of each word, e.g. how many documents contain a specific word\n", " * calculates tf_idf array as: tf / df (tf divided by df). The reason is, if a word appears in most documents, it does not have the discriminative power and often is called a "stop" word. The inverse of df can downgrade the weight of such words.\n", " * for each document, find out the indexes of words with top 3 largest values in the tf_idf array. Print out these indexes.\n", " * return the tf_idf array.\n",
    


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

            
