import requests
import numpy as np 
import csv 
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt 
def mpg_plot():
    cars= pd.read_csv('/Users/yash/Downloads/auto-mpg.csv')
    ctab=pd.crosstab(index=cars.model_year, columns=cars.origin, values=cars.mpg, aggfunc=np.mean)
    ctab.plot(kind='line', colormap='rainbow', \
    figsize=(8,5), title="avg mpg by origin over years").\
    legend(loc='center left', bbox_to_anchor=(1, 0.5));   
    plt.show()

def getReviews(movie_id):
    reviews=[]
    page_url="https://www.rottentomatoes.com/m/"+movie_id+"/reviews/?type=top_critics"
    page = requests.get(page_url)
    if page.status_code==200:
        pagesoup = BeautifulSoup(page.content, 'html.parser')  

#    filename = "movie.csv"
#    f= open("movie.csv","w")
#    headers= "reviewer, description, date, score\n"
#    f.write(headers)
#
#    critic_name = pagesoup.findAll("div",{"class":"col-sm-13 col-xs-24 col-sm-pull-4 critic_name"})
#    review = pagesoup.findAll("div",{"class":"the_review"})
#    date = pagesoup.findAll("div",{"class":"review_date subtle small"})
#    rating = pagesoup.findAll("div",{"class":"small subtle"})
#
#    with open("movie.csv", "w") as f:
#        writer=csv.writer(f, delimiter=',')
#        headers= "reviewer, description, date, score\n"
#        f.write(headers)
#        for x in range(0,(len(critic_name)+1)):   
#            c=critic_name[x].text.split("  ")[0]
#            r=review[x].text.replace(",",".")
#            d=date[x].text.replace(",","")
#            s=rating[x].text.split(" ")[-1].replace("/"," out of ")
#            f.write( c + "," + r + "," + d + "," + s + "\n")
    #i created a csv file excel output, creating a list too       
    divs=pagesoup.find_all("div",{"class":"row review_table_row"})
    for idx, div in enumerate(divs):
    
        name=None
        timestamp=None
        review=None
        rate=None
        
        criticname=div.select("a.unstyled.bold.articleLink")
        if criticname!=[]:
            name=criticname[0].get_text()
        
        date=div.select("div.review_date.subtle.small")
        if date!=[]:
            timestamp=date[0].get_text()
            
            
      
        desc=div.select("div.the_review")
        if desc!=[]:
            review=desc[0].get_text()
          
        
        score=div.select("div.review_desc div.small.subtle")
        if score!=[]:
            rate=score[0].get_text()[31:]
            
            
             
            
        reviews.append((name,timestamp,review,rate))
        
        
    return reviews
    
     

if __name__ == "__main__":
    mpg_plot()
    movie_id='finding_dory'
    reviews=getReviews(movie_id)
    print(reviews)