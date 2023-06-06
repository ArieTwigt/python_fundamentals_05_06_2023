#%%
age = 24


if age < 21: # als True
    print("Helaas geen alcohol")
else:
    print("Proost!🍻")

# %%

name = "Dirk"


guests_list = ["Jim", "James", "Arie"]

#%%
if name in guests_list:
    print("Welcome")
else:
    print("Your are not on the list")
    guests_list.append(name)


# %%
if "A" in name:
    print("Has an 'A'")
else:
    print("Has no 'A'")

# %%
donation_max = 100

donation_amount = 0

while donation_amount < donation_max:
    print(f"Current donation is {donation_amount}")
    print("Adding donation")
    donation_amount += 10
    print(f"New donation amount is {donation_amount}")


# %%
age = 101


if age < 21:
    print("Nee")
elif age > 100:
    print("Ook niet")
else:
    print("Ja")
# %%
