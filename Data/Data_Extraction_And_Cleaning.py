#!/usr/bin/env python
# coding: utf-8

# # Data Extraction

# In[11]:


import urllib.request
from bs4 import BeautifulSoup

urllib.request.urlretrieve("https://www.geeksforgeeks.org/grep-command-in-unixlinux/?ref=leftbar-rightbar","Task3.txt")
file = open("Task3.txt", "r")
contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')
  
f = open("Task3.txt", "w")
  
# traverse paragraphs from soup
for data in soup.find_all("p"):
    sum = data.get_text()
    f.writelines(sum)
f.close()


# # Data Cleaning

# In[12]:


import string
import nltk
text = []
with open("Task3.txt","r") as f:
    text.append(f.read())


# In[20]:


#Remove Special Symbols
import re 
text = re.sub("[^A-Za-z0-9]+"," ",str(text))


# In[14]:


# Covert each word into lower
text = [word.lower() for word in text]


# In[15]:


#word tokenizer
from nltk.tokenize import word_tokenize
tokenized_docs = [word_tokenize(word) for word in text]


#Sentence tokenization
from nltk.tokenize import sent_tokenize
sent_token = [sent_tokenize(word) for word in text]


# In[16]:


#puntuation removal
import re
regex = re.compile('[%s]' % re.escape(string.punctuation)) 

tokenized_docs_no_punctuation = []

for review in tokenized_docs:
    new_review = []
    for token in review:
        new_token = regex.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
    
    tokenized_docs_no_punctuation.append(new_review)
    


# In[17]:


# Cleaning text of stopwords
from nltk.corpus import stopwords

tokenized_docs_no_stopwords = []

for doc in tokenized_docs_no_punctuation:
    new_term_vector = []
    for word in doc:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)
    
    tokenized_docs_no_stopwords.append(new_term_vector)


# In[18]:


from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

porter = PorterStemmer()
wordnet = WordNetLemmatizer()

preprocessed_docs = []

for doc in tokenized_docs_no_stopwords:
    final_doc = []
    for word in doc:
        #final_doc.append(porter.stem(word))
        final_doc.append(wordnet.lemmatize(word))
    
    preprocessed_docs.append(final_doc)
    


# # Save the data into Text File

# In[19]:


f = open("Task3.txt","w")
for word in preprocessed_docs:
    f.write(str(word))
f.close()

