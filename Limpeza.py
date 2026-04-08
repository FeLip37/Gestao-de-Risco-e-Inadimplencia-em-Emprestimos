import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregamento dos dados
df = pd.read_csv('credit_risk.csv')

# 2. Limpeza de Dados
# Corrigimos idades negativas (erros de sistema) substituindo pela mediana de idade do banco
mediana_idade = df[df['idade'] > 0]['idade'].median()
df.loc[df['idade'] <= 0, 'idade'] = mediana_idade

# 3. Segmentação por Faixa de Renda
# Criamos 4 grupos para entender onde reside o maior risco (Baixa, Média-Baixa, Média-Alta, Alta)
df['faixa_renda'] = pd.qcut(df['renda'], q=4, labels=['Baixa', 'Média-Baixa', 'Média-Alta', 'Alta'])

# 4. Cálculo da Taxa de Inadimplência por Faixa (%)
# O objetivo é identificar qual perfil de cliente traz mais risco ao portfólio
analise_risco = df.groupby('faixa_renda')['Inadimplencia'].mean() * 100

# 5. Visualização (Gráfico formal para apresentação)
plt.figure(figsize=(10, 6))
analise_risco.plot(kind='bar', color='#4a90e2', edgecolor='black')
plt.title('Taxa de Inadimplência por Faixa de Renda', fontsize=14)
plt.xlabel('Segmento de Renda', fontsize=12)
plt.ylabel('Inadimplência (%)', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('analise_inadimplencia.png')

# 6. Exportação do arquivo limpo para usar no portfólio
df.to_csv('credit_risk_cleaned.csv', index=False)

print("Análise concluída com sucesso.")