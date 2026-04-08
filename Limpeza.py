import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('credit_risk.csv')

#corrigi idades negativas substituindo pela mediana de idade do banco
mediana_idade = df[df['idade'] > 0]['idade'].median()
df.loc[df['idade'] <= 0, 'idade'] = mediana_idade

#criei 4 grupos para entender onde reside o maior risco 
df['faixa_renda'] = pd.qcut(df['renda'], q=4, labels=['Baixa', 'Média-Baixa', 'Média-Alta', 'Alta'])

#identificar qual perfil de cliente traz mais risco ao portfólio
analise_risco = df.groupby('faixa_renda')['Inadimplencia'].mean() * 100

plt.figure(figsize=(10, 6))
analise_risco.plot(kind='bar', color='#4a90e2', edgecolor='black')
plt.title('Taxa de Inadimplência por Faixa de Renda', fontsize=14)
plt.xlabel('Segmento de Renda', fontsize=12)
plt.ylabel('Inadimplência (%)', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('analise_inadimplencia.png')

df.to_csv('credit_risk_cleaned.csv', index=False)

print("Análise concluída com sucesso.")
