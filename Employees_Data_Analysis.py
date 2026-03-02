
import pandas as pd

#1.
# Explore the data and load it into a Pandas DataFrame.
File=pd.read_excel('Employee Sample Data - A.xlsx')
df=pd.DataFrame(File)
print(df.head())

#2.
# Clean the data.

#Befor clreaning the data we have to know the information aboutv the data
df.info()

df.duplicated()

# Droped the last col because it has alot of null values
df=df.drop('Exit Date',axis=1)

# Then Drop the null value from the rest col
df.dropna(inplace=True)

#3.
# Modify the first 5 rows (input any values).
for x in df.head().index:
  for j in df.head().columns:
    df.loc[x,j]=input(f'inter a new value in row {x} column {j}  ')

#to show the results from 3
df.head()

#4.
# Print the row with the largest salary.
max=df.loc[df['Annual Salary'].idxmax()]
max

#5.
# Group the data by department and calculate both the average age and the average salary.
df.groupby('Department')[['Age','Annual Salary']].mean()

#6.
# Group the data by department+ethnicity, then find the maximum age ,minimum age, and median salary.
df.groupby(['Department','Ethnicity']).agg({
    'Age':['max','min'],
    'Annual Salary':'median'
})

# 7.
# Save your work in a new Excel file.
with pd.ExcelWriter('/content/Employee Sample Data - A.xlsx') as writer:
  df.to_excel(writer,sheet_name='Employee Sample Data New',index=False)