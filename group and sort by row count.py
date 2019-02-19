import pandas as pd 
pd.set_option('display.max_rows', 5000)

print("loading...")
arcats = pd.read_csv(r'c:\Users\mattk\Downloads\bz2\huge category lookup.txt', sep='\t')
#arc = arcats.groupby(['category']).size().sort_values('count')
arc = arcats.groupby(['category']).size().sort_values(ascending=False)

arc.head(5000)
