#%% Assignment 1: Append .Jr. to the current full_name variable which will result in Erling Haaland Jr.
first_name = "Erling"
last_name  = "Haaland"

full_name  = first_name + last_name
print(full_name)

#%%
full_name_new = f"{first_name} {last_name} .Jr"
print(full_name_new)

# %% Assignment 2: Replace the first name of Erling Haaland (Erling) to only the abbreviation of his first hame. This should result in: E. Haaland Jr.
first_letter = first_name[0]
full_name_newer = f"{first_letter}. {last_name} .Jr"
print(full_name_newer)

# %% Assignment 3: Create a variable called nationality with the value "Norway". Use this variable to create the string (sentence) "E. Haaland .Jr - Nationality: Norway". Print out the sentence.
nationality = "Norway"
sentence = f"{full_name_newer} - Nationality: {nationality}"
print(sentence)
# %%
