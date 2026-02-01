import pandas as pd

lastname = ['Amah','Didak','Dbldas','Oumar']
firstname = ['Kwaa','Ollah','Dalas','Assane']
age =  [25,35,45,34]
job = ['SWE','DE','SA','DA']
city = ['NYC','SF','London','Chicago']

df = pd.DataFrame({
    'Firstname':firstname,
    'Lastname':lastname,
    'Age':age,
    'Job':job,
    'City':city})
print(df)
print("=======================================")

# Sort customers by age
print("DataFrame sorted by age")
df_sorted = df.sort_values(by = 'Age',ascending=True)
print(df_sorted)