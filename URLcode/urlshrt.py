#First CodeClause Project
#URL Shortener
#pip install pyshorteners==1.0.1
#pip install pyperclip

import pyshorteners
url = input("Enter the URL: ")

#defining a function
def shorturl(url): #creating a function which takes input as the original url
    a = pyshorteners.Shortener() #creating object
    print(a.tinyurl.short(url))

#calling a function
shorturl(url)






