#%%
try:
    with open("somethingelse.txt") as file:
        for line in file: 
            print(line)
except: 
    pass 


#%%

def say_hello_to_student():
    name = input("tell me your name: ")

    if name == "Pepe":
        raise ValueError("name should be a student's name, Pepe")
    
    print(f"Hello {name}")

