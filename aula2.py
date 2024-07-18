import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


url = 'https://bea3853.github.io/site_teste/'

response = requests.get(url)


if response.status_code == 200:
   
    soup = BeautifulSoup(response.content, 'html.parser')
    

    table = soup.find('table')
    

    df = pd.read_html(str(table))[0]
    
  
    print(df.head())
    

    metrics_by_region = df.groupby('Região')['Compra'].agg(['mean', 'median', 'std', 'min', 'max'])
    

    plt.figure(figsize=(10, 6))
    df.groupby('Região')['Compra'].sum().plot(kind='bar', color='skyblue')
    plt.title('Compra por Região')
    plt.xlabel('Região')
    plt.ylabel('Compra')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('compra_por_regiao.png') 
    plt.show()
    
