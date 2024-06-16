import json


#This 
def get_transformed_Data(ollama,name,description):
    
    #text="Im using langchain to call you, so just return a json format and no text around it, so I can easily pass it through my process. I have a hero's "+name+" and "+description+"here : Make sure they have proper attributes based on their name and description Example if its just a normal human make the attributes low. I need you to create an object of this character and based on the name and description add strenght out of 10 ,  agility out of 10 and superpower out of 10. Respond in a json format like this and make sure not to add any extra text otherwise it wont work, like no can I do anything else for you. Make sure the format looks like this exactly with only the numbers being changed :{ strength: 7,    agility: 5, superpower: 9,} This is the format the output should be and only this"
    text = f"""
    I'm using Langchain to call you, so just return a JSON format with no text around it, so I can easily pass it through my process. 
    I have a hero's name and description here: Name: {name} Description: {description}. 
    Make sure they have proper attributes based on their name and description. 
    For example, if it's just a normal human, make the attributes low. 
    I need you to create an object of this character and based on the name and description, add strength out of 10, agility out of 10, and superpower out of 10. 
    Respond in a JSON format like this and make sure not to add any extra text, otherwise it won't work. 
    The format should look exactly like this with only the numbers being changed:

    {{
        "strength": 7,
        "agility": 5,
        "superpower": 9
    }}

    Make sure the format is correct with all the necessary brackets and without any extra text.
    """
    data=ollama.invoke(text)
    print(data) 
    return json.loads(data)