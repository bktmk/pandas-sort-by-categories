import pandas as pd 
pd.set_option('display.max_rows', 100)

arcats = pd.read_csv(r'c:\Users\yyy\Downloads\bz2\huge category lookup.txt', sep='\t')

revenue_lookup = pd.read_csv(r'c:\Users\yyy\Downloads\bz2\revenue-lookup.tsv', sep='\t')

revenue_lookup.columns = ['sku','product','revenue']
revenue_lookup.head()

arcats.columns = ['sku','price','url','category']
arcats.head()

newtable = arcats
newtable.head()

df3 = newtable.merge(revenue_lookup,on=['sku'])

df3['revenue'] = df3['revenue'].str.replace('$','')
df3['revenue'] = df3['revenue'].str.replace(',','')
df3['revenue'] = df3['revenue'].astype(float)

df3 = df3.sort_values(by='revenue',ascending=False) 

df4 = df3[['category','revenue']]
df4 = df4.groupby(['category']).sum().reset_index()
df4 = df4.sort_values(by='revenue', ascending=False)
new = df4['category'].str.split('>', 3, expand=True)
df4['type'] = new[0]
df4['c1'] = new[1]
df4['c2'] = new[2]
df4['c3'] = new[3]
df4.to_clipboard(sep="\t")
df5 = df4.groupby(['type','c1','c2']).sum().reset_index().sort_values(by='revenue', ascending=False)
df5['perc'] = df5['revenue']/df5['revenue'].sum()
df5
