
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
def analyze_tf(arr):
    
    tf_idf=[]
    #normalizes the frequency of each word as: word frequency divided by the length of the document.
    #Save the result as an array named tf (i.e. term frequency)
    # add your code
    
    shape=np.shape(arr)
    
    print(shape)
    print(arr)
    #calculating the sum of rows
    rowsum=np.sum(arr, axis=1)
    print(rowsum)
    rowshape=np.shape(rowsum)
    print(rowshape)
    
    #normalizing the frequency of each word
    tf = arr.T/rowsum
    #transposing because the shapes are (4.8) and (4,0), so making it (8,4) and then dividing
    #print(tf)
    
    #chanfing it back to its original shape (4,8)
    tf=tf.T
    print(tf)
    #used for loop first but then i read it cant be used 
    #for x in range(0,4):
       # rowSum = 0
        #for y in range(0,8):
         #   rowSum += arr[x][y]
          #  y+=1
       # tf_idf2 = []
        #for z in range(0,8):
         #   tf_idf2.append(arr[x][z]/rowSum)
        #tf_idf.append(tf_idf2)
        #applx += 1
            
    #binarising the values to calculate the occurance in the documents and then adding 
    tf1=np.where(arr>0, 1, 0)
    print ("document frequency of a word in each document", np.sum(tf1, axis=0))
    
    
    #calculating tf_idf
    tf_idf=np.divide(tf,tf1)
    print("tf_idf",tf_idf)
    
    #finding where the top 3 values in each row are
    arr1=np.argsort(arr)
    print(arr1[:,::-1][:,0:3])
    return tf_idf

def analyze_cars():
    #reading file
    cars=pd.read_csv("/Users/yash/Downloads/cars.csv")
    
    #sorting dataframe in descending order and containing cylinders and mpg
    
    sort = cars.sort_values(by=['cylinders','mpg'], ascending=False)
    print(sort.head(3))
    
    #splitting the cars column but " " and selecting the brand name and storing it into a new column called brand
    cars["brand"]=cars.apply(lambda row: row["car"].split(" ")[0], axis=1)
    print(cars.head(3))
    
    #values by "cylinders" for each of these brands: "ford", "buick" and "honda"

    cars1= cars[cars.brand.isin(['ford','buick','honda'])]
    groupby=cars1.groupby("cylinders")
    #print(groupby.head(3))
    print(groupby["acceleration"].mean())
    print(groupby["acceleration"].min())
    print(groupby["acceleration"].max())
    
    #cross tab to show the average mpg of each brand and each clinder value. 
    print(pd.crosstab(index=cars.brand, columns=cars.cylinders, values=cars.mpg, aggfunc=np.average))






# best practice to test your class
# if yourcript is exported as a module,
# the following part is ignored
if __name__ == "__main__":
    arr=np.random.randint(0,3,(4,8))
    
    tf_idf=analyze_tf(arr)
    
    # Test Question 2
    analyze_cars()

