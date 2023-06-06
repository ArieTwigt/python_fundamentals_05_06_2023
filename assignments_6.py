# Assignment 1: Create a loop that removes the vowels 
# from the following names list: ['Jim', 'John', 'Marc', 'Danny', 'Peter'] . Add the results to a new list.

#%%
names_list = ['Jim', 'Arie',  'John', 'Marc', 'Danny', 'Peter']

vowels = ['a', 'e', 'o', 'u', 'i', 'y']

for name in names_list:
    print(f"Old name is: {name}")
    for letter in name.lower():
        if letter in vowels:
            name = name.replace(letter, "")
    
    print(f"New name is {name}")
    print("="*15)

        


# %%
# Assignment 2: Create a loop that prints the name of the day for the following 10 days

#%%
from datetime import date, timedelta

#%%
today_date = date.today()

# %%
for day_num in range(0, 10):
    new_date = today_date + timedelta(day_num + 1)

    new_day = new_date.strftime("%A")
    print(new_day)



# %%
