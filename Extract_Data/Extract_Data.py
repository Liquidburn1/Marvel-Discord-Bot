import pandas as pd

#Add Extract_Data. before utils.helper_funcitons if running from main
from utils.helper_functions import get_100_characters,clean_data




#To get all the characters that have a description
df=pd.DataFrame()
i=0
while i <1564:
    df1=pd.DataFrame(get_100_characters(i))
    df=pd.concat([df,df1[['id','name','description']][(df1.description!='') & (df1.description!=' ')]],ignore_index=True)
   

    i+=100

    print(i)

# Apply the function to clean HTML tags 
df['name'] = df['name'].apply(clean_data)
df['description'] = df['description'].apply(clean_data)

df.to_csv('./Cleaned_data1.csv',index=False)



