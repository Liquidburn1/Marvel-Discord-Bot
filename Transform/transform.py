import pandas as pd
import json
from langchain_community.llms import Ollama
from utils.helperfunc import get_transformed_Data

ollama = Ollama(
    base_url='http://localhost:11434',
    model="llama3"
)


df=pd.read_csv('Cleaned_data.csv')

results=[]

for index, row in df.iterrows():
    print(index)
    name = row['name']
    description = row['description']
    data=get_transformed_Data(ollama,name,description)
    results.append({'id':row['id'],'name':name,'description':description,'strength':data['strength'],'agility':data['agility'],'superpower':data['superpower'],'lvl':0})
    
    

transformed_data=pd.DataFrame(results)

transformed_data.to_csv('./Transformed_data.csv',index=False)
