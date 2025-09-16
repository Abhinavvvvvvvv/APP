import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("beer-servings.csv").drop(columns=['Unnamed: 0'])
df = df.dropna(subset=['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol'])

X = df[['beer_servings', 'spirit_servings', 'wine_servings']]
y = df['total_litres_of_pure_alcohol']

model = LinearRegression().fit(X, y)

with open("beer_model.pkl", "wb") as f:
    pickle.dump(model, f)
