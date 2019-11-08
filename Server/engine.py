# RECOMMENDER ENGINE BASED ON CONTENT BASED RECOMMENDATION
# USING CONCEPT OF CONSINE SIMILARITY (COS(theta)) BETWEEN VECTORS

# -------------------IMPORTS---------------------
# IMPORT FOR DATA PRE-PROSSESING
import pandas as pd
import numpy as np

# IMPORT FOR ML ALGORITH
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# SCR IS IMPORTED TO GET USER HISTORY
import scr

# -------------DATA PRE-PROCESSING---------------

df = pd.read_csv("lappy.csv")

features = ['Screen Size','Cpu','Ram','Memory','Gpu','OpSys','Weight','Price_euros','RAM type']

# FUNCTION TO COMBINE ALL FEATURES AS A COLUMN
def combine_features(row):
    return str(row['Screen Size'])+" "+str(row['Cpu'])+" "+str(row['Ram'])+" "+str(row['Memory'])+" "+str(row['Gpu'])+" "+str(row['OpSys'])+" "+str(row['Weight'])+" "+str(row['Price_euros'])+" "+str(row['RAM type'])

for feature in features:
    df[feature] = df[feature].fillna('') #filling all NaNs with blank string

df["combined_features"] = df.apply(combine_features,axis=1)

# ------------FITTING DATA TO MODEL----------------

cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df["combined_features"]) 

cosine_sim = cosine_similarity(count_matrix)

# --------------PERFORM PREDICTION-----------------

# VARIABLES TO STORE PREDICTED RESULTS
cpu, ram, gpu, mem, price = [], [], [], [], []

def get_title_from_index(index):
    price.append(df[df.index == index].Price_euros.values[0])
    cpu.append(df[df.index == index].Cpu.values[0])
    gpu.append(df[df.index == index].Gpu.values[0])
    ram.append(df[df.index == index].Ram.values[0])
    mem.append(df[df.index == index].Memory.values[0])
    return df[df.index == index].Item_name.values

def get_index_from_title(title):
    return df[df.Item_name.str.contains(title)].index.values[0]

# PERFORM PREDICTION FOR USER HISTORY
lappy_user_likes = scr.lappy_user_likes
# lappy_user_likes = 'Alienware'
lappy_index = get_index_from_title(lappy_user_likes)

similar_lappy = list(enumerate(cosine_sim[lappy_index]))

sorted_similar_lappy = sorted(similar_lappy,key=lambda x:x[1],reverse=True)[1:]

# STORE TOP 6 RESULTS
i=0
res = []
for element in sorted_similar_lappy:
    e = (get_title_from_index(element[0]))
    res.append(e[0])
    i=i+1
    if i>5:
        break