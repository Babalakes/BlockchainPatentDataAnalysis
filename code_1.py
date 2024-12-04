import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_meta = pd.read_csv("uspatents_meta.csv", low_memory=False)
df_meta.patnum = pd.to_numeric(
    df_meta.patnum, errors='coerce', downcast='integer')
print(df_meta[["patnum", "grantdate", "appldate"]].head(5))

df_link = pd.read_csv("uspatents_gvkey_linking.csv", low_memory=False)
df_link.patnum = pd.to_numeric(
    df_link.patnum, errors='coerce', downcast='integer')
print(df_link[["patnum", "gvkey_numeric"]].head(5))

df_list = pd.read_csv("query_absBsm_USPT.csv", low_memory=False)
df_list.patentNumber = pd.to_numeric(
    df_list.patentNumber, errors='coerce', downcast='integer')
print(df_list.head(5))

df_UKlist = pd.read_csv("query_absDesc_Espace.csv", low_memory=False)
df_UKlist.familyNumber = pd.to_numeric(
    df_UKlist.familyNumber, errors='coerce', downcast='integer')
print(df_UKlist.head(5))


# Assuming 'filingDate' column contains dates in 'dd/mm/yyyy' format
df_list['filingDate'] = pd.to_datetime(
    df_list['filingDate'], format="%d/%m/%Y")

# Filter rows with 'filingDate' from 2010 to 2022
df_list = df_list[(df_list['filingDate'].dt.year > 2009) &
                  (df_list['filingDate'].dt.year <= 2022)]
print(len(df_list))
print(len(df_list.drop_duplicates(subset=["patentNumber"])))


# Assuming 'filingDate' column contains dates in 'dd/mm/yyyy' format
df_UKlist['filingDate'] = pd.to_datetime(
    df_UKlist['filingDate'], format="%d/%m/%Y")

# Filter rows with 'filingDate' from 2010 to 2022
df_UKlist = df_UKlist[(df_UKlist['filingDate'].dt.year > 2009) & (
    df_UKlist['filingDate'].dt.year <= 2022)]
print(len(df_UKlist))
print(len(df_UKlist.drop_duplicates(subset=["familyNumber"])))


# Assuming df_list contains your DataFrame with patent data

# Extract year and quarter from filingDate column
df_list['filingYear'] = df_list['filingDate'].dt.year
df_list['quarter'] = df_list['filingDate'].dt.quarter

# Group by year and quarter and count the number of patents
patents_per_quarter = df_list.groupby(
    ['filingYear', 'quarter']).size().reset_index(name='number_of_patents')

# Calculate percentage increase in patents for each quarter
patents_per_quarter['percentage_increase'] = patents_per_quarter.groupby(
    'filingYear')['number_of_patents'].pct_change() * 100

# Create a DataFrame with the correct structure
patents_data = {
    'filingYear': patents_per_quarter['filingYear'],
    'quarter': patents_per_quarter['quarter'],
    'number_of_patents': patents_per_quarter['number_of_patents'],
    'percentage_increase': patents_per_quarter['percentage_increase']
}
patents_per_quarter_df = pd.DataFrame(patents_data)

print(patents_per_quarter_df)


# Extract year and quarter from filingDate column
df_UKlist['filingYear'] = df_UKlist['filingDate'].dt.year
df_UKlist['quarter'] = df_UKlist['filingDate'].dt.quarter

# Group by year and quarter and count the number of UK patents
uk_patents_per_quarter = df_UKlist.groupby(
    ['filingYear', 'quarter']).size().reset_index(name='number_of_patents')

# Calculate percentage increase in UK patents for each quarter
uk_patents_per_quarter['percentage_increase'] = uk_patents_per_quarter.groupby(
    'filingYear')['number_of_patents'].pct_change() * 100

# Create a DataFrame with the correct structure
uk_patents_data = {
    'filingYear': uk_patents_per_quarter['filingYear'],
    'quarter': uk_patents_per_quarter['quarter'],
    'number_of_patents': uk_patents_per_quarter['number_of_patents'],
    'percentage_increase': uk_patents_per_quarter['percentage_increase']
}
uk_patents_per_quarter_df = pd.DataFrame(uk_patents_data)

print(uk_patents_per_quarter_df)


# Summing up the number of patents per year
patents_per_year = patents_per_quarter_df.groupby(
    'filingYear')['number_of_patents'].sum()
uk_patents_per_year = uk_patents_per_quarter_df.groupby(
    'filingYear')['number_of_patents'].sum()

# Bar chart for the number of US and UK patents
plt.figure(figsize=(10, 6))
plt.bar(patents_per_year.index, patents_per_year.values, color='blue', width=0.4)
plt.bar(uk_patents_per_year.index,
        uk_patents_per_year.values, color='red', width=0.4)
plt.legend(['US', 'UK'])
plt.xlabel('Year')
plt.ylabel('Number of Patents')
plt.title('Number of Patents Every Year')
plt.grid(True, linewidth=0.5)


# Line chart for percentage increase
# Interpolate NaN values in percentage_increase column
patents_per_quarter_df['percentage_increase'] = patents_per_quarter_df['percentage_increase'].interpolate()
uk_patents_per_quarter_df['percentage_increase'] = uk_patents_per_quarter_df['percentage_increase'].interpolate()

# Line chart for percentage increase
plt.figure(figsize=(10, 6))
plt.plot(patents_per_quarter_df['filingYear'] + (patents_per_quarter_df['quarter'] -
         1) / 4, patents_per_quarter_df['percentage_increase'], color='blue', marker='o')
plt.plot(uk_patents_per_quarter_df['filingYear'] + (uk_patents_per_quarter_df['quarter'] -
         1) / 4, uk_patents_per_quarter_df['percentage_increase'], color='red', marker='o')
plt.legend(['US', 'UK'])
plt.title('Percentage Increase of Patents Every Quarter')
plt.xlabel('Year')
plt.ylabel('Percentage Increase')

plt.xticks(ticks=patents_per_quarter_df['filingYear'] +
           0.5, labels=patents_per_quarter_df['filingYear'])
plt.grid()

plt.tight_layout()
plt.show()
