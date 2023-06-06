#%%
from datetime import datetime, date, timedelta

#%% huidige datum en tijd
datetime.now()

# %%
today_date = date.today()

# %%
next_birthday = date(2024,4,1) # define
# %%
days_difference = next_birthday - today_date
# %%
days_difference_int = days_difference.days
# %%
days_plus_50 = today_date + timedelta(days=50)
# %%
days_plus_50
# %%
today_date.strftime("%m")
# %%
