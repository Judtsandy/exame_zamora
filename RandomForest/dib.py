import pandas as pd
df = pd.read_csv('dataset/reduced.csv')

df_half = df.sample(frac=0.2, random_state=42)

df_half.to_csv('reduced1.csv', index=False)