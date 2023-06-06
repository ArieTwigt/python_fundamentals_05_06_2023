# Assignment 1 - Create a conditional statement that indicates if your name starts with an "A or not
#%%
name = "Arie"

first_letter = name[0].lower()


# %%
if first_letter == "a":
    print("Your name starts with an 'A'")
else:
    print("Your name does not start with an 'A'")


# Assignment 2 - Create a conditional statement that indicates if your name begins with a vowel.
# 
# %%

name = "Arie"
vowels = ['a', 'e', 'o', 'u', 'i', 'y']

first_letter = name[0].lower()

#%%
if first_letter in vowels:
    new_name = name.replace(name[0], "B")
else:
    new_name = name.replace(name[0], "A")

print(new_name)
# Assignment 3: Create a conditional statement that indicates if your age is between 18 and 68.
# %%
my_age = 40

if my_age > 18 and my_age < 68:
    print("Between 18 and 68")
# %%
if 18 < my_age < 68:
    print("Between 18 and 68")
# %%