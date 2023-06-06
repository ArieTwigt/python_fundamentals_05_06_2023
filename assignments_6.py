# Assignment 1: Create a loop that removes the vowels 
# from the following names list: ['Jim', 'John', 'Marc', 'Danny', 'Peter'] . Add the results to a new list.

#%%
names_list = ['Jim', 'Arie',  'John', 'Marc', 'Danny', 'Peter']

vowels = ['a', 'e', 'o', 'u', 'i', 'y']

for name in names_list:
    print(f"Old name is: {name}")
    for letter in name:
        if letter.lower() in vowels:
            name = name.replace(letter, "")
    
    print(f"New name is {name}")
    print("="*15)

        


# %%
