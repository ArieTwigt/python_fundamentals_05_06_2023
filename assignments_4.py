# Assignment 1: Assign a variable that holds the number of days until your next birthday
#%%
from datetime import date


#%% define the date to your next birthday
birthday_date = date(2024, 4, 1)

#%%
today_date = date.today()


# %%
days_difference = birthday_date - today_date
# %%
days_difference_int = days_difference.days


# %%
today_date.strftime("Vandaag is %A in het jaar %Y")

# Assignment 2

# %% Calculate the surface of a circle with a diameter of 10 (radius^ * pi)

#%%
from math import pi, pow


# %%
diameter = 10
radius = diameter / 2

size = pow(radius, 2) * pi
print(size)

# %%
