#%%
import requests
import pandas

endpoint = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"

response = requests.get(endpoint)

#%%
data = response.json()
# %%
data[0]['kenteken']
# %%
data_df = pandas.DataFrame(data)
# %%
data_df.query("eerste_kleur=='ZWART'")
# %%
