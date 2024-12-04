# %% [markdown]
#
# Google Patent Search tool:
# ### 1. For US
# https://patents.google.com/?q=AB%3d(%22Blockchain%22)+OR+AB%3d(%22Cryptocurrency%22)+OR+AB%3d(%22bitcoin%22)+OR+AB%3d(%22consensus+mechanism%22)+OR+AB%3d(%22smart+contract%22)+OR+AB%3d(%22digital+asset%22)+OR+AB%3d(%22non-fungible+token%22)+OR+AB%3d(%22decentralized+finance%22)+OR+AB%3d(%22initial+coin+offering%22)+OR+AB%3d(%22decentralized+autonomous+organization%22)+OR+AB%3d(%22decentralized+application%22)+OR+AB%3d(%22Ethereum%22)+OR+AB%3d(%22Token+Standards%22)&country=US&before=priority:20230101&after=priority:20090101&dups=language
#
# ### 2. For China
# https://patents.google.com/?q=AB%253d%28%22Blockchain%22%29+OR+AB%253d%28%22Cryptocurrency%22%29+OR+AB%253d%28%22bitcoin%22%29+OR+AB%253d%28%22consensus+mechanism%22%29+OR+AB%253d%28%22smart+contract%22%29+OR+AB%253d%28%22digital+asset%22%29+OR+AB%253d%28%22non-fungible+token%22%29+OR+AB%253d%28%22decentralized+finance%22%29+OR+AB%253d%28%22initial+coin+offering%22%29+OR+AB%253d%28%22decentralized+autonomous+organization%22%29+OR+AB%253d%28%22decentralized+application%22%29+OR+AB%253d%28%22Ethereum%22%29+OR+AB%253d%28%22Token+Standards%22%29&country=CN&before=priority:20230101&after=priority:20090101&dups=language
#
# ### 3. For South Korea
# https://patents.google.com/?q=AB%253d%28%22Blockchain%22%29+OR+AB%253d%28%22Cryptocurrency%22%29+OR+AB%253d%28%22bitcoin%22%29+OR+AB%253d%28%22consensus+mechanism%22%29+OR+AB%253d%28%22smart+contract%22%29+OR+AB%253d%28%22digital+asset%22%29+OR+AB%253d%28%22non-fungible+token%22%29+OR+AB%253d%28%22decentralized+finance%22%29+OR+AB%253d%28%22initial+coin+offering%22%29+OR+AB%253d%28%22decentralized+autonomous+organization%22%29+OR+AB%253d%28%22decentralized+application%22%29+OR+AB%253d%28%22Ethereum%22%29+OR+AB%253d%28%22Token+Standards%22%29&country=KR&before=priority:20230101&after=priority:20090101&dups=language&num=100
#
# ### 4. For Japan
# https://patents.google.com/?q=AB%253d%28%22Blockchain%22%29+OR+AB%253d%28%22Cryptocurrency%22%29+OR+AB%253d%28%22bitcoin%22%29+OR+AB%253d%28%22consensus+mechanism%22%29+OR+AB%253d%28%22smart+contract%22%29+OR+AB%253d%28%22digital+asset%22%29+OR+AB%253d%28%22non-fungible+token%22%29+OR+AB%253d%28%22decentralized+finance%22%29+OR+AB%253d%28%22initial+coin+offering%22%29+OR+AB%253d%28%22decentralized+autonomous+organization%22%29+OR+AB%253d%28%22decentralized+application%22%29+OR+AB%253d%28%22Ethereum%22%29+OR+AB%253d%28%22Token+Standards%22%29&country=JP&before=priority:20230101&after=priority:20090101&dups=language&num=100
#
# ### 5. For UK
# https://patents.google.com/?q=AB%3d(%22Blockchain%22)+OR+AB%3d(%22Cryptocurrency%22)+OR+AB%3d(%22bitcoin%22)+OR+AB%3d(%22consensus+mechanism%22)+OR+AB%3d(%22smart+contract%22)+OR+AB%3d(%22digital+asset%22)+OR+AB%3d(%22non-fungible+token%22)+OR+AB%3d(%22decentralized+finance%22)+OR+AB%3d(%22initial+coin+offering%22)+OR+AB%3d(%22decentralized+autonomous+organization%22)+OR+AB%3d(%22decentralized+application%22)+OR+AB%3d(%22Ethereum%22)+OR+AB%3d(%22Token+Standards%22)&country=GB&before=priority:20230101&after=priority:20090101&num=100&dups=language
#
# | Type | Query |
# |---|---|
# | Search in the abstract | AB=("Blockchain") OR AB=("Cryptocurrency") OR AB=("bitcoin") OR AB=("consensus mechanism") OR AB=("smart contract") OR AB=("digital asset") OR AB=("non-fungible token") OR AB=("decentralized finance") OR AB=("initial coin offering") OR AB=("decentralized autonomous organization") OR AB=("decentralized application") OR AB=("Ethereum") OR AB=("Token Standards"); After: priority 2009-01-01; Before: priority 2023-01-01; Country: US;  |
#
# The patent database was queried by extracting specifics keywods from the patent's ABSTRACT
#
# Save the results "filingDate" and "id" into a csv file: "output.csv"

# %%
from statsmodels.tsa.stattools import adfuller
from time import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from datetime import datetime
from datetime import timedelta
from pandas.plotting import register_matplotlib_converters
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
register_matplotlib_converters()

# %%
# For the US
df_USlist = pd.read_csv("output.csv", index_col="priority_date", parse_dates=True,
                        low_memory=False, encoding="latin-1", date_format="%d/%m/%Y")
df_USlist.id = df_USlist.id.replace("US-", "", regex=True)
df_USlist.id = df_USlist.id.replace("-A1", "", regex=True)
df_USlist.id = df_USlist.id.replace("-B1", "", regex=True)
df_USlist.id = df_USlist.id.replace("-B2", "", regex=True)
df_USlist.id = pd.to_numeric(df_USlist.id, errors='coerce', downcast='integer')
print(df_USlist.head(5))

# %%
# For the UK
df_UKlist = pd.read_csv("gb_output.csv", index_col="priority_date", parse_dates=True,
                        low_memory=False, date_format="%d/%m/%Y", encoding="latin-1")
df_UKlist.id = df_UKlist.id.replace("GB-", "", regex=True)
df_UKlist.id = df_UKlist.id.replace("-A", "", regex=True)
df_UKlist.id = df_UKlist.id.replace("-D0", "", regex=True)
df_UKlist.id = pd.to_numeric(df_UKlist.id, errors='coerce', downcast='integer')
print(df_UKlist.head(5))


# %%
# For the CN
df_CNlist = pd.read_csv("cn_output.csv", index_col="priority_date", parse_dates=True,
                        low_memory=False, date_format="%d/%m/%Y", encoding="latin-1")
df_CNlist.id = df_CNlist.id.replace("CN-", "", regex=True)
df_CNlist.id = df_CNlist.id.replace("-A", "", regex=True)
df_CNlist.id = df_CNlist.id.replace("-B", "", regex=True)
df_CNlist.id = df_CNlist.id.replace("-U", "", regex=True)
df_CNlist.id = pd.to_numeric(df_CNlist.id, errors='coerce', downcast='integer')
print(df_CNlist.head(5))

# %%
# For the JP
df_JPlist = pd.read_csv("jp_output.csv", index_col="priority_date", parse_dates=True,
                        low_memory=False, date_format="%d/%m/%Y", encoding="latin-1")
df_JPlist.id = df_JPlist.id.replace("JP-", "", regex=True)
df_JPlist.id = df_JPlist.id.replace("JP-WO", "", regex=True)
df_JPlist.id = df_JPlist.id.replace("-A", "", regex=True)
df_JPlist.id = df_JPlist.id.replace("-A1", "", regex=True)
df_JPlist.id = df_JPlist.id.replace("-B1", "", regex=True)
df_JPlist.id = pd.to_numeric(df_JPlist.id, errors='coerce', downcast='integer')
print(df_JPlist.head(5))

# %%
# For the KR
df_KRlist = pd.read_csv("kr_output.csv", index_col="priority_date", parse_dates=True,
                        low_memory=False, date_format="%d/%m/%Y", encoding="latin-1")
df_KRlist.id = df_KRlist.id.replace("KR-", "", regex=True)
df_KRlist.id = df_KRlist.id.replace("-A", "", regex=True)
df_KRlist.id = df_KRlist.id.replace("-B1", "", regex=True)
df_KRlist.id = pd.to_numeric(df_KRlist.id, errors='coerce', downcast='integer')
print(df_KRlist.head(5))

# %%
# For the US
# Convert the index to datetime format (assuming 'priority_date' is the index)
df_USlist.index = pd.to_datetime(df_USlist.index, format="%d/%m/%Y")

# Filter rows with 'priority_date' from 2010 to 2022
mask = (df_USlist.index.year > 2009) & (df_USlist.index.year <= 2022)
df_USfiltered = df_USlist[mask].copy()

print(len(df_USfiltered))
print(len(df_USfiltered.drop_duplicates(subset=["id"])))

df_USpatents = df_USfiltered.drop_duplicates(subset=["id"])


# %%
# For the UK
# Convert the index to datetime format (assuming 'priority_date' is the index)
df_UKlist.index = pd.to_datetime(df_UKlist.index, format="%d/%m/%Y")

# Filter rows with 'priority_date' from 2010 to 2022
mask = (df_UKlist.index.year > 2009) & (df_UKlist.index.year <= 2022)
df_UKfiltered = df_UKlist[mask].copy()

print(len(df_UKfiltered))
print(len(df_UKfiltered.drop_duplicates(subset=["id"])))

df_UKpatents = df_UKfiltered.drop_duplicates(subset=["id"])

# %%
# For the CN
# Convert the index to datetime format (assuming 'priority_date' is the index)
df_CNlist.index = pd.to_datetime(df_CNlist.index, format="%d/%m/%Y")

# Filter rows with 'priority_date' from 2010 to 2022
mask = (df_CNlist.index.year > 2009) & (df_CNlist.index.year <= 2022)
df_CNfiltered = df_CNlist[mask].copy()

print(len(df_CNfiltered))
print(len(df_CNfiltered.drop_duplicates(subset=["id"])))

df_CNpatents = df_CNfiltered.drop_duplicates(subset=["id"])

# %%
# For the JP
# Convert the index to datetime format (assuming 'priority_date' is the index)
df_JPlist.index = pd.to_datetime(df_JPlist.index, format="%d/%m/%Y")

# Filter rows with 'priority_date' from 2010 to 2022
mask = (df_JPlist.index.year > 2009) & (df_JPlist.index.year <= 2022)
df_JPfiltered = df_JPlist[mask].copy()

print(len(df_JPfiltered))
print(len(df_JPfiltered.drop_duplicates(subset=["id"])))

df_JPpatents = df_JPfiltered.drop_duplicates(subset=["id"])

# %%
# For the KR
# Convert the index to datetime format (assuming 'priority_date' is the index)
df_KRlist.index = pd.to_datetime(df_KRlist.index, format="%d/%m/%Y")

# Filter rows with 'priority_date' from 2010 to 2022
mask = (df_KRlist.index.year > 2009) & (df_KRlist.index.year <= 2022)
df_KRfiltered = df_KRlist[mask].copy()

print(len(df_KRfiltered))
print(len(df_KRfiltered.drop_duplicates(subset=["id"])))

df_KRpatents = df_KRfiltered.drop_duplicates(subset=["id"])

# %% [markdown]
# ## Calculating Innovation Index
# Innovation Index = 1/patent age * Number of Citations  FCF= Forward Citation Frequency

# %%

current_date = datetime.date(datetime.now())
print(current_date)

df_USpatents['age'] = (
    current_date - df_USpatents.index.date).astype('timedelta64[D]')
df_UKpatents['age'] = (
    current_date - df_UKpatents.index.date).astype('timedelta64[D]')
df_CNpatents['age'] = (
    current_date - df_CNpatents.index.date).astype('timedelta64[D]')
df_JPpatents['age'] = (
    current_date - df_JPpatents.index.date).astype('timedelta64[D]')
df_KRpatents['age'] = (
    current_date - df_KRpatents.index.date).astype('timedelta64[D]')

# print results in years
df_USpatents['age'] = df_USpatents['age'] / np.timedelta64(1, 'Y')
df_UKpatents['age'] = df_UKpatents['age'] / np.timedelta64(1, 'Y')
df_CNpatents['age'] = df_CNpatents['age'] / np.timedelta64(1, 'Y')
df_JPpatents['age'] = df_JPpatents['age'] / np.timedelta64(1, 'Y')
df_KRpatents['age'] = df_KRpatents['age'] / np.timedelta64(1, 'Y')


# innovation_index = cite_number divided by age
df_USpatents['innovation_index'] = df_USpatents['cite_number'] / \
    df_USpatents['age']
df_UKpatents['innovation_index'] = df_UKpatents['cite_number'] / \
    df_UKpatents['age']
df_CNpatents['innovation_index'] = df_CNpatents['cite_number'] / \
    df_CNpatents['age']
df_JPpatents['innovation_index'] = df_JPpatents['cite_number'] / \
    df_JPpatents['age']
df_KRpatents['innovation_index'] = df_KRpatents['cite_number'] / \
    df_KRpatents['age']

print(df_USpatents.head(2))
print(df_UKpatents.head(2))
print(df_CNpatents.head(2))
print(df_JPpatents.head(2))
print(df_KRpatents.head(2))

# %%

# Assuming df_USpatents is your DataFrame
df_USpatents['priority_date'] = pd.to_datetime(
    df_USpatents.index)  # Convert 'priority_date' to datetime

# Group by month and year and count the number of patents
us_patents_per_month = df_USpatents.resample(
    'M').size().reset_index(name='number_of_patents')

# Sum of citations per month
us_patents_per_month['number_of_citations'] = df_USpatents.resample(
    'M')['cite_number'].sum().reset_index(name='number_of_citations')['number_of_citations']

# Calculate percentage increase in patents for each month
us_patents_per_month['percentage_increase'] = us_patents_per_month['number_of_patents'].pct_change() * \
    100

# Calculate the moving average
us_patents_per_month['moving_average'] = us_patents_per_month['number_of_patents'].rolling(
    window=3).mean()

# Calculate the mean of innovation_index for each month
us_patents_per_month['mean_innovation_index'] = df_USpatents.resample(
    'M')['innovation_index'].mean().reset_index(name='innovation_index')['innovation_index']

# Extract year and month
us_patents_per_month['year'] = us_patents_per_month['priority_date'].dt.year
us_patents_per_month['month'] = us_patents_per_month['priority_date'].dt.month

# Create the final DataFrame
us_patents_data = {
    'priority_date': us_patents_per_month['priority_date'],
    'number_of_patents': us_patents_per_month['number_of_patents'],
    'percentage_increase': us_patents_per_month['percentage_increase'],
    'number_of_citations': us_patents_per_month['number_of_citations'],
    'mean_innovation_index': us_patents_per_month['mean_innovation_index'],
    'year': us_patents_per_month['year'],
    'month': us_patents_per_month['month'],
    'moving_average': us_patents_per_month['moving_average']
}
us_patents_per_month_df = pd.DataFrame(us_patents_data)

print(us_patents_per_month_df)


# %%

# Assuming df_UKpatents is your DataFrame
# Convert 'priority_date' to datetime
df_UKpatents.index = pd.to_datetime(df_UKpatents.index, format="%d/%m/%Y")

# Group by month and year and count the number of patents
uk_patents_per_month = df_UKpatents.resample(
    'M').size().reset_index(name='number_of_patents')

# Sum of citations per month
uk_patents_per_month['number_of_citations'] = df_UKpatents.resample(
    'M')['cite_number'].sum().reset_index(name='number_of_citations')['number_of_citations']

# Calculate percentage increase in patents for each month
uk_patents_per_month['percentage_increase'] = uk_patents_per_month['number_of_patents'].pct_change() * \
    100

# Calculate the moving average
uk_patents_per_month['moving_average'] = uk_patents_per_month['number_of_patents'].rolling(
    window=3).mean()

# Calculate the mean of innovation_index for each month
uk_patents_per_month['mean_innovation_index'] = df_UKpatents.resample(
    'M')['innovation_index'].mean().reset_index(name='innovation_index')['innovation_index']

# Extract year and month
uk_patents_per_month['year'] = uk_patents_per_month['priority_date'].dt.year
uk_patents_per_month['month'] = uk_patents_per_month['priority_date'].dt.month

# Create the final DataFrame
uk_patents_data = {
    'priority_date': uk_patents_per_month['priority_date'],
    'number_of_patents': uk_patents_per_month['number_of_patents'],
    'percentage_increase': uk_patents_per_month['percentage_increase'],
    'number_of_citations': uk_patents_per_month['number_of_citations'],
    'mean_innovation_index': uk_patents_per_month['mean_innovation_index'],
    'year': uk_patents_per_month['year'],
    'month': uk_patents_per_month['month'],
    'moving_average': uk_patents_per_month['moving_average']
}
uk_patents_per_month_df = pd.DataFrame(uk_patents_data)

print(uk_patents_per_month_df)


# %%
# Assuming df_CNpatents is your DataFrame
# Convert 'priority_date' to datetime
df_CNpatents.index = pd.to_datetime(df_CNpatents.index, format="%d/%m/%Y")

# Group by month and year and count the number of patents
cn_patents_per_month = df_CNpatents.resample(
    'M').size().reset_index(name='number_of_patents')

# Sum of citations per month
cn_patents_per_month['number_of_citations'] = df_CNpatents.resample(
    'M')['cite_number'].sum().reset_index(name='number_of_citations')['number_of_citations']

# Calculate percentage increase in patents for each month
cn_patents_per_month['percentage_increase'] = cn_patents_per_month['number_of_patents'].pct_change() * \
    100

# Calculate the moving average
cn_patents_per_month['moving_average'] = cn_patents_per_month['number_of_patents'].rolling(
    window=3).mean()

# Calculate the mean of innovation_index for each month
cn_patents_per_month['mean_innovation_index'] = df_CNpatents.resample(
    'M')['innovation_index'].mean().reset_index(name='innovation_index')['innovation_index']

# Extract year and month
cn_patents_per_month['year'] = cn_patents_per_month['priority_date'].dt.year
cn_patents_per_month['month'] = cn_patents_per_month['priority_date'].dt.month

# Create the final DataFrame
cn_patents_data = {
    'priority_date': cn_patents_per_month['priority_date'],
    'number_of_patents': cn_patents_per_month['number_of_patents'],
    'percentage_increase': cn_patents_per_month['percentage_increase'],
    'number_of_citations': cn_patents_per_month['number_of_citations'],
    'mean_innovation_index': cn_patents_per_month['mean_innovation_index'],
    'year': cn_patents_per_month['year'],
    'month': cn_patents_per_month['month'],
    'moving_average': cn_patents_per_month['moving_average']
}
cn_patents_per_month_df = pd.DataFrame(cn_patents_data)

print(cn_patents_per_month_df)

# %%
# Assuming df_JPpatents is your DataFrame
# Convert 'priority_date' to datetime
df_JPpatents.index = pd.to_datetime(df_JPpatents.index, format="%d/%m/%Y")

# Group by month and year and count the number of patents
jp_patents_per_month = df_JPpatents.resample(
    'M').size().reset_index(name='number_of_patents')

# Sum of citations per month
jp_patents_per_month['number_of_citations'] = df_JPpatents.resample(
    'M')['cite_number'].sum().reset_index(name='number_of_citations')['number_of_citations']

# Calculate percentage increase in patents for each month
jp_patents_per_month['percentage_increase'] = jp_patents_per_month['number_of_patents'].pct_change() * \
    100

# Calculate the moving average
jp_patents_per_month['moving_average'] = jp_patents_per_month['number_of_patents'].rolling(
    window=3).mean()

# Calculate the mean of innovation_index for each month
jp_patents_per_month['mean_innovation_index'] = df_JPpatents.resample(
    'M')['innovation_index'].mean().reset_index(name='innovation_index')['innovation_index']

# Extract year and month
jp_patents_per_month['year'] = jp_patents_per_month['priority_date'].dt.year
jp_patents_per_month['month'] = jp_patents_per_month['priority_date'].dt.month

# Create the final DataFrame
jp_patents_data = {
    'priority_date': jp_patents_per_month['priority_date'],
    'number_of_patents': jp_patents_per_month['number_of_patents'],
    'percentage_increase': jp_patents_per_month['percentage_increase'],
    'number_of_citations': jp_patents_per_month['number_of_citations'],
    'mean_innovation_index': jp_patents_per_month['mean_innovation_index'],
    'year': jp_patents_per_month['year'],
    'month': jp_patents_per_month['month'],
    'moving_average': jp_patents_per_month['moving_average']
}
jp_patents_per_month_df = pd.DataFrame(jp_patents_data)

print(jp_patents_per_month_df)

# %%
# Assuming df_KRpatents is your DataFrame
# Convert 'priority_date' to datetime
df_KRpatents.index = pd.to_datetime(df_KRpatents.index, format="%d/%m/%Y")

# Group by month and year and count the number of patents
kr_patents_per_month = df_KRpatents.resample(
    'M').size().reset_index(name='number_of_patents')

# Sum of citations per month
kr_patents_per_month['number_of_citations'] = df_KRpatents.resample(
    'M')['cite_number'].sum().reset_index(name='number_of_citations')['number_of_citations']

# Calculate percentage increase in patents for each month
kr_patents_per_month['percentage_increase'] = kr_patents_per_month['number_of_patents'].pct_change() * \
    100

# Calculate the moving average
kr_patents_per_month['moving_average'] = kr_patents_per_month['number_of_patents'].rolling(
    window=3).mean()

# Calculate the mean of innovation_index for each month
kr_patents_per_month['mean_innovation_index'] = df_KRpatents.resample(
    'M')['innovation_index'].mean().reset_index(name='innovation_index')['innovation_index']

# Extract year and month
kr_patents_per_month['year'] = kr_patents_per_month['priority_date'].dt.year
kr_patents_per_month['month'] = kr_patents_per_month['priority_date'].dt.month

# Create the final DataFrame
kr_patents_data = {
    'priority_date': kr_patents_per_month['priority_date'],
    'number_of_patents': kr_patents_per_month['number_of_patents'],
    'percentage_increase': kr_patents_per_month['percentage_increase'],
    'number_of_citations': kr_patents_per_month['number_of_citations'],
    'mean_innovation_index': kr_patents_per_month['mean_innovation_index'],
    'year': kr_patents_per_month['year'],
    'month': kr_patents_per_month['month'],
    'moving_average': kr_patents_per_month['moving_average']
}
kr_patents_per_month_df = pd.DataFrame(kr_patents_data)

print(kr_patents_per_month_df)

# %%

print(us_patents_per_month_df.head(2))
print(uk_patents_per_month_df.head(2))
print(cn_patents_per_month_df.head(2))
print(jp_patents_per_month_df.head(2))
print(kr_patents_per_month_df.head(2))


# %%
# Create the bar plot using seaborn
plt.figure(figsize=(10, 6))
# plot barchart with x-axis as year, y-axis as number of patents
plt.bar(x='year', height='number_of_patents',
        data=us_patents_per_month_df, color='blue')
plt.bar(x='year', height='number_of_patents',
        data=uk_patents_per_month_df, color='red')
plt.bar(x='year', height='number_of_patents',
        data=cn_patents_per_month_df, color='green')
plt.bar(x='year', height='number_of_patents',
        data=jp_patents_per_month_df, color='yellow')
plt.bar(x='year', height='number_of_patents',
        data=kr_patents_per_month_df, color='orange')

# sns.barplot(x='year', y='number_of_patents', hue='month', data=us_patents_per_month)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of Patents')
plt.title('Number of Patents per Year with Monthly Data Points')
plt.legend(['US', 'UK', 'CN', 'JP', 'KR'])

# Show the plot
plt.show()

# %%
# Adding 'country' column to each dataframe
us_patents_per_month_df['country'] = 'US'
uk_patents_per_month_df['country'] = 'UK'
cn_patents_per_month_df['country'] = 'CN'
jp_patents_per_month_df['country'] = 'JP'
kr_patents_per_month_df['country'] = 'KR'

# Concatenate dataframes
combined_df = pd.concat([us_patents_per_month_df, uk_patents_per_month_df,
                        cn_patents_per_month_df, jp_patents_per_month_df, kr_patents_per_month_df])

# Create the grouped and bar plot with country as hue withouth using seaborn
plt.figure(figsize=(10, 6))
combined_df.groupby(['year', 'country'])['number_of_patents'].sum(
).unstack().plot(kind='bar', stacked=False)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of Patents')
plt.title('Number of Patents per Year')
plt.legend(title='Country')

# Show the plot
plt.show()

# %%

# Set up the figure and subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))

# Plot 1: Moving Average of patents per Month (Rolling Mean)
ax1 = axes[0, 0]
ax1.plot(us_patents_per_month_df['priority_date'],
         us_patents_per_month_df['moving_average'], color='blue')
ax1.plot(uk_patents_per_month_df['priority_date'],
         uk_patents_per_month_df['moving_average'], color='red')
ax1.plot(cn_patents_per_month_df['priority_date'],
         cn_patents_per_month_df['moving_average'], color='green')
ax1.plot(jp_patents_per_month_df['priority_date'],
         jp_patents_per_month_df['moving_average'], color='yellow')
ax1.plot(kr_patents_per_month_df['priority_date'],
         kr_patents_per_month_df['moving_average'], color='orange')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Patents')
ax1.set_title('Number of Patents Quarterly (Rolling Mean)')
ax1.legend(['US', 'UK', 'CN', 'JP', 'KR'])

# Plot 2: Percentage Increase in Patents per Month (Rolling Mean)
ax2 = axes[0, 1]
ax2.plot(us_patents_per_month_df['priority_date'],
         us_patents_per_month_df['percentage_increase'].rolling(3).mean(), color='blue')
ax2.plot(uk_patents_per_month_df['priority_date'],
         uk_patents_per_month_df['percentage_increase'].rolling(3).mean(), color='red')
ax2.plot(cn_patents_per_month_df['priority_date'],
         cn_patents_per_month_df['percentage_increase'].rolling(3).mean(), color='green')
ax2.plot(jp_patents_per_month_df['priority_date'],
         jp_patents_per_month_df['percentage_increase'].rolling(3).mean(), color='yellow')
ax2.plot(kr_patents_per_month_df['priority_date'],
         kr_patents_per_month_df['percentage_increase'].rolling(3).mean(), color='orange')
ax2.set_xlabel('Year')
ax2.set_ylabel('Percentage Increase in Patents')
ax2.set_title('Percentage Increase in Patents Quarterly (Rolling Mean)')
ax2.legend(['US', 'UK', 'CN', 'JP', 'KR'])

# Plot 3: Mean Innovation Index per Month (Rolling Mean)
ax3 = axes[1, 0]
ax3.plot(us_patents_per_month_df['priority_date'],
         us_patents_per_month_df['mean_innovation_index'].rolling(3).mean(), color='blue')
ax3.plot(uk_patents_per_month_df['priority_date'],
         uk_patents_per_month_df['mean_innovation_index'].rolling(3).mean(), color='red')
ax3.plot(cn_patents_per_month_df['priority_date'],
         cn_patents_per_month_df['mean_innovation_index'].rolling(3).mean(), color='green')
ax3.plot(jp_patents_per_month_df['priority_date'],
         jp_patents_per_month_df['mean_innovation_index'].rolling(3).mean(), color='yellow')
ax3.plot(kr_patents_per_month_df['priority_date'],
         kr_patents_per_month_df['mean_innovation_index'].rolling(3).mean(), color='orange')
ax3.set_xlabel('Year')
ax3.set_ylabel('Mean Innovation Index')
ax3.set_title('Mean Innovation Index Quarterly (Rolling Mean)')
ax3.legend(['US', 'UK', 'CN', 'JP', 'KR'])

# Plot 4: Number of Citations per Month (Rolling Mean)
ax4 = axes[1, 1]
ax4.plot(us_patents_per_month_df['priority_date'],
         us_patents_per_month_df['number_of_citations'].rolling(3).mean(), color='blue')
ax4.plot(uk_patents_per_month_df['priority_date'],
         uk_patents_per_month_df['number_of_citations'].rolling(3).mean(), color='red')
ax4.plot(cn_patents_per_month_df['priority_date'],
         cn_patents_per_month_df['number_of_citations'].rolling(3).mean(), color='green')
ax4.plot(jp_patents_per_month_df['priority_date'],
         jp_patents_per_month_df['number_of_citations'].rolling(3).mean(), color='yellow')
ax4.plot(kr_patents_per_month_df['priority_date'],
         kr_patents_per_month_df['number_of_citations'].rolling(3).mean(), color='orange')
ax4.set_xlabel('Year')
ax4.set_ylabel('Number of Citations')
ax4.set_title('Number of Citations Quarterly (Rolling Mean)')
ax4.legend(['US', 'UK', 'CN', 'JP', 'KR'])

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()


# %% [markdown]
# ## Company Analysis

# %%
# Get the number of patents per assignee
us_patents_per_assignee = df_USpatents.groupby(
    'assignee').size().reset_index(name='number_of_patents')
uk_patents_per_assignee = df_UKpatents.groupby(
    'assignee').size().reset_index(name='number_of_patents')

# Sort the values in descending order
us_patents_per_assignee = us_patents_per_assignee.sort_values(
    by='number_of_patents', ascending=False)
uk_patents_per_assignee = uk_patents_per_assignee.sort_values(
    by='number_of_patents', ascending=False)

# Get the top 10 assignees
us_top_10_assignees = us_patents_per_assignee.head(10)
uk_top_10_assignees = uk_patents_per_assignee.head(10)

print(us_top_10_assignees)
print(uk_top_10_assignees)


# %%
# Create the bar plot using seaborn
# Plot 1: US
plt.figure(figsize=(10, 6))
sns.barplot(x='number_of_patents', y='assignee', data=us_top_10_assignees)
plt.xlabel('Number of Patents')
plt.ylabel('Assignee')
plt.title('Top 10 Blockchain-Related Assignees in the US')
plt.show()

# Plot 2: UK
plt.figure(figsize=(10, 6))
sns.barplot(x='number_of_patents', y='assignee', data=uk_top_10_assignees)
plt.xlabel('Number of Patents')
plt.ylabel('Assignee')
plt.title('Top 10 Blockchain-Related Assignees in the UK')
plt.show()

# %%
# Create a line plot for top 10 assignees number of patents per month and year
# Set up the figure and subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15, 10))

# Plot 1: US
ax1 = axes[0]
for assignee in us_top_10_assignees['assignee']:
    # Get the number of patents per assignee
    us_patents_per_assignee_per_month = df_USpatents[df_USpatents['assignee'] == assignee].resample(
        'M').size().reset_index(name='number_of_patents')

    # Plot the line
    ax1.plot(us_patents_per_assignee_per_month['priority_date'],
             us_patents_per_assignee_per_month['number_of_patents'].rolling(6).mean(), label=assignee)

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Patents')
ax1.set_title('Number of Patents per Assignee per Month in the US')
ax1.legend()

# Plot 2: UK
ax2 = axes[1]
for assignee in uk_top_10_assignees['assignee']:
    # Get the number of patents per assignee
    uk_patents_per_assignee_per_month = df_UKpatents[df_UKpatents['assignee'] == assignee].resample(
        'M').size().reset_index(name='number_of_patents')

    # Plot the line
    ax2.plot(uk_patents_per_assignee_per_month['priority_date'],
             uk_patents_per_assignee_per_month['number_of_patents'].rolling(6).mean(), label=assignee)

ax2.set_xlabel('Year')
ax2.set_ylabel('Number of Patents')
ax2.set_title('Number of Patents per Assignee per Month in the UK')
ax2.legend()

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()


# %% [markdown]
# ## Company Cross border patent filing
#
# ### For Top 10 US Blockchain Company
# https://patents.google.com/?q=AB%253d%28%22Blockchain%22%29+OR+AB%253d%28%22Cryptocurrency%22%29+OR+AB%253d%28%22bitcoin%22%29+OR+AB%253d%28%22consensus+mechanism%22%29+OR+AB%253d%28%22smart+contract%22%29+OR+AB%253d%28%22digital+asset%22%29+OR+AB%253d%28%22non-fungible+token%22%29+OR+AB%253d%28%22decentralized+finance%22%29+OR+AB%253d%28%22initial+coin+offering%22%29+OR+AB%253d%28%22decentralized+autonomous+organization%22%29+OR+AB%253d%28%22decentralized+application%22%29+OR+AB%253d%28%22Ethereum%22%29+OR+AB%253d%28%22Token+Standards%22%29&assignee=International+Business+Machines+Corporation%2CAdvanced+New+Technologies+Co%2CAlibaba+Group+Holding+Limited%2CnChain+Holdings+Limited%2CAlipay+%28Hangzhou%29+Information+Technology+Co%2CMastercard+International+Incorporated%2CBank+Of+America+Corporation%2CCapital+One+Services%2CState+Farm+Mutual+Automobile+Insurance+Company%2CNchain+Licensing+Ag&country=WO%2CEP%2CJP%2CKR%2CCN%2CAE%2CAG%2CAL%2CAM%2CAO%2CAP%2CAR%2CAT%2CAU%2CAW%2CAZ%2CBA%2CBB%2CBD%2CBE%2CBF%2CBG%2CBH%2CBJ%2CBN%2CBO%2CBR%2CBW%2CBX%2CBY%2CBZ%2CCA%2CCF%2CCG%2CCH%2CCI%2CZW%2CZM%2CZA%2CYU%2CVN%2CVE%2CVC%2CUZ%2CUY%2CUG%2CUA%2CTZ%2CTW%2CTT%2CTR%2CTN%2CTM%2CTJ%2CTH%2CTG%2CTD%2CSZ%2CSY%2CSV%2CSU%2CST%2CSN%2CSM%2CSL%2CSK%2CSI%2CSG%2CSE%2CSD%2CSC%2CSA%2CRW%2CRU%2CRS%2CRO%2CQA%2CPY%2CPT%2CPL%2CPH%2CPG%2CPE%2CPA%2COM%2COA%2CNZ%2CNO%2CNL%2CNI%2CNG%2CNE%2CNA%2CMZ%2CMY%2CMX%2CMW%2CMT%2CMR%2CMO%2CMN%2CML%2CMK%2CMG%2CME%2CMD%2CMC%2CMA%2CLY%2CLV%2CLU%2CLT%2CLS%2CLR%2CLK%2CLI%2CLC%2CLA%2CKZ%2CKW%2CKP%2CKN%2CKM%2CKH%2CKG%2CKE%2CJO%2CIT%2CIS%2CIR%2CIN%2CIL%2CIE%2CID%2CIB%2CHU%2CHR%2CHN%2CHK%2CGW%2CGT%2CGR%2CGQ%2CGN%2CGM%2CGH%2CGE%2CGD%2CGC%2CGB%2CGA%2CFR%2CFI%2CES%2CEM%2CCL%2CCM%2CCO%2CCR%2CCS%2CCU%2CCY%2CCZ%2CDD%2CDE%2CDJ%2CDK%2CDM%2CDO%2CDZ%2CEA%2CEC%2CEE%2CEG&before=priority:20230101&after=priority:20090101&dups=language&num=100
#
# These are the patents filed by the Top 10 US Assignees in other countries asides the US
#
# ### For Top 10 UK Blockchain Companies
# https://patents.google.com/?q=AB%253d%28%22Blockchain%22%29+OR+AB%253d%28%22Cryptocurrency%22%29+OR+AB%253d%28%22bitcoin%22%29+OR+AB%253d%28%22consensus+mechanism%22%29+OR+AB%253d%28%22smart+contract%22%29+OR+AB%253d%28%22digital+asset%22%29+OR+AB%253d%28%22non-fungible+token%22%29+OR+AB%253d%28%22decentralized+finance%22%29+OR+AB%253d%28%22initial+coin+offering%22%29+OR+AB%253d%28%22decentralized+autonomous+organization%22%29+OR+AB%253d%28%22decentralized+application%22%29+OR+AB%253d%28%22Ethereum%22%29+OR+AB%253d%28%22Token+Standards%22%29&assignee=Nchain+Holdings+Ltd%2CNchain+Licensing+Ag%2CIbm%2CBritish+Telecomm%2CWalmart+Apollo+Llc%2CBlack+Gold+Coin+Inc%2CTaal+Dit+Gmbh%2CApple+Inc%2CDragon+Infosec+Ltd%2CEmc+Ip+Holding+Co+Llc&country=WO%2CEP%2CJP%2CKR%2CCN%2CAE%2CAG%2CAL%2CAM%2CAO%2CAP%2CAR%2CAT%2CAU%2CAW%2CAZ%2CBA%2CBB%2CBD%2CBE%2CBF%2CBG%2CBH%2CBJ%2CBN%2CBO%2CBR%2CBW%2CBX%2CBY%2CBZ%2CCA%2CCF%2CCG%2CCH%2CCI%2CZW%2CZM%2CZA%2CYU%2CVN%2CVE%2CVC%2CUZ%2CUY%2CUG%2CUA%2CTZ%2CTW%2CTT%2CTR%2CTN%2CTM%2CTJ%2CTH%2CTG%2CTD%2CSZ%2CSY%2CSV%2CSU%2CST%2CSN%2CSM%2CSL%2CSK%2CSI%2CSG%2CSE%2CSD%2CSC%2CSA%2CRW%2CRU%2CRS%2CRO%2CQA%2CPY%2CPT%2CPL%2CPH%2CPG%2CPE%2CPA%2COM%2COA%2CNZ%2CNO%2CNL%2CNI%2CNG%2CNE%2CNA%2CMZ%2CMY%2CMX%2CMW%2CMT%2CMR%2CMO%2CMN%2CML%2CMK%2CMG%2CME%2CMD%2CMC%2CMA%2CLY%2CLV%2CLU%2CLT%2CLS%2CLR%2CLK%2CLI%2CLC%2CLA%2CKZ%2CKW%2CKP%2CKN%2CKM%2CKH%2CKG%2CKE%2CJO%2CIT%2CIS%2CIR%2CIN%2CIL%2CIE%2CID%2CIB%2CHU%2CHR%2CHN%2CHK%2CGW%2CGT%2CGR%2CGQ%2CGN%2CGM%2CGH%2CGE%2CGD%2CGC%2CGA%2CFR%2CFI%2CES%2CEM%2CCL%2CCM%2CCO%2CCR%2CCS%2CCU%2CCY%2CCZ%2CDD%2CDE%2CDJ%2CDK%2CDM%2CDO%2CDZ%2CEA%2CEC%2CEE%2CEG%2CUS&before=priority:20230101&after=priority:20090101&dups=language&num=100
#
#
#
# =IF(ISNUMBER(SEARCH("International Business Machines Corporation", B2)), "International Business Machines Corporation", IF(ISNUMBER(SEARCH("Advanced New Technologies Co", B2)), "Advanced New Technologies Co", IF(ISNUMBER(SEARCH("Alibaba Group Holding Limited", B2)), "Alibaba Group Holding Limited", IF(ISNUMBER(SEARCH("nChain Holdings Limited", B2)), "nChain Holdings Limited", IF(ISNUMBER(SEARCH("Alipay (Hangzhou) Information Technology", B2)), "Alipay (Hangzhou) Information Technology", IF(ISNUMBER(SEARCH("Mastercard International Incorporated", B2)), "Mastercard International Incorporated", IF(ISNUMBER(SEARCH("Bank Of America Corporation", B2)), "Bank Of America Corporation", IF(ISNUMBER(SEARCH("Capital One Services", B2)), "Capital One Services", IF(ISNUMBER(SEARCH("State Farm Mutual Automobile Insurance Company", B2)), "State Farm Mutual Automobile Insurance Company", IF(ISNUMBER(SEARCH("Nchain Licensing Ag", B2)), "Nchain Licensing Ag", ""))))))))))
#
#
# =IF(ISNUMBER(SEARCH("Nchain Holdings",B2)),"Nchain Holdings Ltd",IF(ISNUMBER(SEARCH("Nchain Licensing Ag",B2)),"Nchain Licensing Ag",IF(ISNUMBER(SEARCH("Ibm",B2)),"Ibm",IF(ISNUMBER(SEARCH("British",B2)),"British Telecomm",IF(ISNUMBER(SEARCH("Walmart Apollo",B2)),"Walmart Apollo",IF(ISNUMBER(SEARCH("Black Gold Coin",B2)),"Black Gold Coin Inc",IF(ISNUMBER(SEARCH("Taal Dit",B2)),"Taal Dit Gmbh",IF(ISNUMBER(SEARCH("Apple",B2)),"Apple Inc",IF(ISNUMBER(SEARCH("Dragon Infosec",B2)),"Dragon Infosec Ltd",IF(ISNUMBER(SEARCH("Emc Ip Holding Co",B2)),"Emc Ip Holding Co Llc",IF(ISNUMBER(SEARCH("International Business Machines Corporation",B2)),"Ibm","")))))))))))

# %%
# read a csv file
df_UStop_crossborder = pd.read_csv("us_top10_crossborder.csv", index_col="priority_date",
                                   parse_dates=True, low_memory=False, encoding="latin-1", date_format="%d/%m/%Y")
df_UKtop_crossborder = pd.read_csv("uk_top10_crossborder.csv", index_col="priority_date",
                                   parse_dates=True, low_memory=False, encoding="latin-1", date_format="%d/%m/%Y")

print(df_UStop_crossborder)
print(df_UKtop_crossborder)

# %%
# drop all id duplicates
df_UStop_crossborder = df_UStop_crossborder.drop_duplicates(subset=["id"])
df_UKtop_crossborder = df_UKtop_crossborder.drop_duplicates(subset=["id"])

# drop all company with NaN
df_UStop_crossborder = df_UStop_crossborder.dropna(subset=["company"])
df_UKtop_crossborder = df_UKtop_crossborder.dropna(subset=["company"])

# drop all symbol with NaN
df_UStop_crossborder = df_UStop_crossborder.dropna(subset=["symbol"])
df_UKtop_crossborder = df_UKtop_crossborder.dropna(subset=["symbol"])

print(df_UStop_crossborder)
print(df_UKtop_crossborder)

# %%
# group by company and count the number of patents
us_top10_crossborder = df_UStop_crossborder.groupby(
    'company').size().reset_index(name='number_of_patents')
uk_top10_crossborder = df_UKtop_crossborder.groupby(
    'company').size().reset_index(name='number_of_patents')

# Sort the values in descending order
us_top10_crossborder = us_top10_crossborder.sort_values(
    by='number_of_patents', ascending=False)
uk_top10_crossborder = uk_top10_crossborder.sort_values(
    by='number_of_patents', ascending=False)

print(us_top10_crossborder)
print(uk_top10_crossborder)

# %%
# group by company and count the number of patents with corresponding symbol
us_top10_crossborder = df_UStop_crossborder.groupby(
    ['company', 'symbol']).size().reset_index(name='number_of_patents')
uk_top10_crossborder = df_UKtop_crossborder.groupby(
    ['company', 'symbol']).size().reset_index(name='number_of_patents')

# Sort the values in descending order
us_top10_crossborder = us_top10_crossborder.sort_values(
    by='number_of_patents', ascending=False)
uk_top10_crossborder = uk_top10_crossborder.sort_values(
    by='number_of_patents', ascending=False)

print(us_top10_crossborder.head(5))
print(uk_top10_crossborder.head(5))


# %%
# Create the bar plot to show that amount of patents per company in each country(that is, symbol)
# Plot 1: US
plt.figure(figsize=(10, 6))
sns.barplot(x='number_of_patents', y='company',
            hue='symbol', data=us_top10_crossborder)
plt.xlabel('Number of Patents')
plt.ylabel('Company')
plt.title('Top US Blockchain Companies with Patent filed outside US')
plt.show()

# Plot 2: UK
plt.figure(figsize=(10, 6))
sns.barplot(x='number_of_patents', y='company',
            hue='symbol', data=uk_top10_crossborder)
plt.xlabel('Number of Patents')
plt.ylabel('Company')
plt.title('Top UK Blockchain Companies with Patent filed outside UK')
plt.show()

# %% [markdown]
# ## Calculate the Company Blockchain Innovation Index
#
# Company Innovation Index = FCF / number of patents per company = number of patent citation / (age * number of patents per company) = innovation_index / number of patents per company

# %%
# print(df_USpatents.head())
# print(df_UKpatents.head())

# drop all age less than equal to 2
df_USpatents_f = df_USpatents[df_USpatents['age'] > 4]
df_UKpatents_f = df_UKpatents[df_UKpatents['age'] > 4]

# Get the number of patents per assignee
us_patents_per_assignee = df_USpatents_f.groupby(
    'assignee').size().reset_index(name='number_of_patents')
uk_patents_per_assignee = df_UKpatents_f.groupby(
    'assignee').size().reset_index(name='number_of_patents')

# Sort the values in descending order
us_patents_per_assignee = us_patents_per_assignee.sort_values(
    by='number_of_patents', ascending=False)
uk_patents_per_assignee = uk_patents_per_assignee.sort_values(
    by='number_of_patents', ascending=False)

# innovation_index = cite_number divided by age
df_USpatents_f['innovation_index'] = df_USpatents_f['cite_number'] / \
    df_USpatents_f['age']
df_UKpatents_f['innovation_index'] = df_UKpatents_f['cite_number'] / \
    df_UKpatents_f['age']


# get the mean of innovation_index per assignee
us_innovation_index_per_assignee = df_USpatents_f.groupby(
    'assignee')['innovation_index'].mean().reset_index(name='company_innovation_index')
uk_innovation_index_per_assignee = df_UKpatents_f.groupby(
    'assignee')['innovation_index'].mean().reset_index(name='company_innovation_index')

# Sort the values in descending order
us_innovation_index_per_assignee = us_innovation_index_per_assignee.sort_values(
    by='company_innovation_index', ascending=False)
uk_innovation_index_per_assignee = uk_innovation_index_per_assignee.sort_values(
    by='company_innovation_index', ascending=False)

print(us_innovation_index_per_assignee['assignee'].head(10))
print(uk_innovation_index_per_assignee['assignee'].head(10))

# %%

# Load and preprocess the data
us_patents_per_month_df = us_patents_per_month_df.drop(
    columns=['percentage_increase', 'year', 'month', 'number_of_citations', 'mean_innovation_index', 'moving_average', 'country'])
us_patents_per_month_df['priority_date'] = pd.to_datetime(
    us_patents_per_month_df['priority_date'])
us_patents_per_month_df.set_index('priority_date', inplace=True)
# us_patents_per_month_df.rename('number_of_patents')

# set NaN values in number_of_patents to 0 in order to avoid errors
us_patents_per_month_df['number_of_patents'] = us_patents_per_month_df['number_of_patents'].fillna(
    0)
print(us_patents_per_month_df.head(5))


# %%
# infer the frequency of the data
us_patents_per_month_df = us_patents_per_month_df.asfreq(
    pd.infer_freq(us_patents_per_month_df.index))
print(us_patents_per_month_df.head(5))

# %%
# Visualize the time series data
plt.plot(us_patents_per_month_df)
plt.xlabel('Year')
plt.ylabel('Number of Patents')
plt.title('Blockchain Patent Filings')
plt.legend(['Number of Patents'])
# plt.xticks(patents_per_year_df['filingYear'], rotation=45)
plt.grid()
plt.show()

# Perform Dickey-Fuller test for stationarity
result = adfuller(us_patents_per_month['number_of_patents'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])

# %%
# Perform first differencing to make the data stationary
us_patents_per_month_df_diff = us_patents_per_month_df.diff().dropna()

# Visualize the time series data
plt.plot(us_patents_per_month_df_diff)
plt.xlabel('Year')
plt.ylabel('First Diff of Number of Patents')
plt.title('Blockchain Patent Filings')
plt.legend(['Number of Patents', 'Percentage Change'])
# plt.xticks(patents_per_year_df['filingYear'], rotation=45)
plt.grid()
plt.show()

# %%
# Plot ACF and PACF plots
plot_acf(us_patents_per_month_df_diff['number_of_patents'])
plt.grid()
# Use a smaller number of lags
plot_pacf(us_patents_per_month_df_diff['number_of_patents'])
plt.minorticks_on()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.grid(True, which='major', linestyle='--', linewidth=0.7)
plt.grid()
plt.show()


# %% [markdown]
# ### Based on PACF, we should start with an Auto Regressive Model with lags 1, 2, 7, 15, ....
#
# ### Get training and test sets

# %%
# Set the date index and resample to monthly frequency

# us_patents_per_month_df_diff = us_patents_per_month_df_diff.asfreq('M')
print(us_patents_per_month_df_diff)
train_end = datetime(2021, 12, 1)
test_end = datetime(2022, 12, 1)

# train_data = patents_per_month_df_diff['number_of_patents']  # Select the target column
train_data = us_patents_per_month_df_diff[:train_end]
test_data = us_patents_per_month_df_diff[train_end +
                                         timedelta(days=1):test_end]


# %% [markdown]
# ## Fit the AR Model

# %%
# create the model

model = ARIMA(train_data, order=(7, 1, 0))


# %%
# fit the model
start = time()
model_fit = model.fit()
end = time()
print('Model Fitting Time:', end - start)


# %%
# summary of model
print(model_fit.summary())

# %%

# get prediction start and end dates
pred_start_date = test_data.index[0]
pred_end_date = test_data.index[-1]

# %%

# get the predictions and residuals
predictions = model_fit.predict(start=pred_start_date, end=pred_end_date)

# convert predictions to dataframe with index column= 'priority_date' and next column= 'number_of_patents'
# Convert the dictionary to a DataFrame
predictions = pd.DataFrame(predictions.items(), columns=[
                           'priority_date', 'number_of_patents'])
# Convert the 'priority_date' column to datetime
predictions['priority_date'] = pd.to_datetime(predictions['priority_date'])
# Set 'priority_date' as the index
predictions.set_index('priority_date', inplace=True)


residuals = test_data - predictions
# print(test_data)
# print(predictions)
print(residuals)


# %%
plt.figure(figsize=(10, 4))
plt.plot(residuals)
plt.title('Residuals from AR Model', fontsize=20)
plt.ylabel('Error', fontsize=16)
plt.axhline(0, color='r', linestyle='--', alpha=0.2)
for year in range(2022, 2023):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'),
                color='k', linestyle='--', alpha=0.2)

# %%
plt.figure(figsize=(10, 4))

plt.plot(test_data)
plt.plot(predictions)

plt.legend(('Data', 'Predictions'), fontsize=16)

plt.title('Test Data vs. Predictions', fontsize=20)
plt.ylabel('first difference', fontsize=16)
for year in range(2022, 2023):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'),
                color='k', linestyle='--', alpha=0.2)

# %%
print('Mean Absolute Percentage Error:', round(
    np.mean(abs(residuals['number_of_patents']/test_data['number_of_patents'])), 4))

# %%
print('Root Mean Square Error:', np.sqrt(
    np.mean(residuals['number_of_patents']**2)))
