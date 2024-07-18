import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
arquivo = 'arquivo.csv' 
df = pd.read_csv(arquivo)


df = df[['genre', 'popularity', 'explicit']]


genre_popularity = df.groupby(['genre', 'explicit'])['popularity'].mean().reset_index()


explicit_mean = genre_popularity[genre_popularity['explicit'] == True]
not_explicit_mean = genre_popularity[genre_popularity['explicit'] == False]


explicit_mean = explicit_mean.sort_values(by='popularity', ascending=False)
not_explicit_mean = not_explicit_mean.sort_values(by='popularity', ascending=False)


plt.figure(figsize=(12, 8))

plt.bar(explicit_mean

['genre'], explicit_mean['popularity'], color='red', alpha=0.7, label='Explícito')
plt.bar(not_explicit_mean

['genre'], not_explicit_mean['popularity'], color='blue', alpha=0.7, label='Não Explícito')

plt.xlabel('Genêro Musical')
plt.ylabel('Popularidade Média')
plt.title('Popularidade média de músicas explícitas contra não explícitas por gênero')
plt.xticks(rotation=90)
plt.legend()

plt.tight_layout()
plt.show()
