# Assignment 1: Create a dictionary with an (imaginary) person with attributes like his name, age and hobb
#%% Imperatief programmeren
person = {}
person['name'] = "James"
person['age'] = 50
person['hobbies'] = ['tennis', 'gaming']

#%% Decleratief programmeren
person = {'name': 'James',
          'age':50, 
          'hobbies': ['tennis', 'gaming']}

# Assignment 2
#%% create the new and empty famility dict
family_dict = {}

# %% assign a name to the family
family_dict['name'] = "Jones"

# %% create the persons
person_2 = {}
person_2['name'] = "Mary"
person_2['age'] = 55
person_2['hobbies'] = ['cycling', 'boxing']

person_3 = {}
person_3['name'] = "Bobby"
person_3['age'] = 10
person_3['hobbies'] = ['gaming', 'fishing']

# add the persons to the family


# %% add a key, members, which is an empty list
family_dict['members'] = [person, person_2, person_3]



# %%
person_4 = {"name": "Baby",
            "age": 0,
            "hobbies": ["crying", "sleeping"]}
# %%
family_dict['members'].append(person_4)
# %%
