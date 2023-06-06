#%%
from math import pi, pow


diameter_list = [10, 20, 30, 40, 50]

for diameter in diameter_list:
    radius = diameter / 2

    size = pow(radius, 2) * pi
    print(size)



# %%
ages_list   = [17, 18, 58, 15, 35]
names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']
person_list = []

#%%
for count, value in enumerate(names_list):
    print(count + 1)
    print(value)
    print("="* 10)

# %%
