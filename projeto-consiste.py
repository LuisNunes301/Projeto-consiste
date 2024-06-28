import pandas as pd

pessoas_Df = pd.read_csv("dataset/DATASET.CSV",delimiter=';')
pd.options.mode.chained_assignment = None

df_tmp = pessoas_Df
df_tmp['Peso (kg)'] = df_tmp['Peso (kg)'].str.replace(',', '.').astype(float)
df_tmp['Altura (m)'] = df_tmp['Altura (m)'].str.replace(',', '.').astype(float)
#Fiz isso para que a linguagem nao reconhece , como o portugues e sim . para numero com decimais

def calcular_imc(df):
    # todos os nulos serão substituídos por zero
    df['Peso (kg)'] = df['Peso (kg)'].fillna(0)
    df['Altura (m)'] = df['Altura (m)'].fillna(0)
    # Iterar pelas linhas do DataFrame
    for i, row in df.iterrows():
        #aproveitei para colocar os nomes já em caixa alta e trantando os espaços desncessarios de cada coluna
        df.at[i, 'Primeiro Nome'] = row['Primeiro Nome'].strip().upper()
        sobrenome = ' '.join(row['Sobrenomes'].strip().split())
        df.at[i, 'Sobrenomes'] = sobrenome.upper()
        #Calculando o ICM, aproveitando e colocando os nomes que tem em altura ou peso = 0
        # sejam preenchidos por 0 para contabilizar que eles nao foram preenchidos
        if row['Peso (kg)'] == 0 or row['Altura (m)'] == 0:
            df.at[i, 'IMC'] = 0.0
        else:
            df.at[i, 'IMC'] = round(row['Peso (kg)'] / (row['Altura (m)'] ** 2), 2)
    return df

def mostrar_dados(df):
    # Selecionar e retornar as colunas desejadas
    return df[['Primeiro Nome', 'Sobrenomes', 'IMC']]

def salvar_nome_sobrenome_imc_txt(df, file_path):
    with open(file_path, 'w' ,encoding='utf-8') as f:
        for i,row in df.iterrows():
            nome = row['Primeiro Nome']
            sobrenome = row['Sobrenomes']
            imc = row['IMC']
            # Escrever no arquivo com um espaço entre nome e sobrenome
            f.write(f"{nome} {sobrenome} {imc}\n")
            
def linha_para_string_unica(df):
    # Selecionar a primeira linha do DataFrame
    if not df.empty:
        row = df.iloc[0]
        nome = row['Primeiro Nome']
        sobrenome = row['Sobrenomes']
        imc = row['IMC']
        return "Exemplo de como ficou o tratamento: "+ f"{nome} {sobrenome} {imc}"
    else:
        return "DataFrame está vazio"

calcular_imc(df_tmp)
df_resultado = mostrar_dados(df_tmp)

linha_str = linha_para_string_unica(df_resultado)
print(linha_str)

arquivo_saida = 'resultado_imc.txt'
salvar_nome_sobrenome_imc_txt(df_resultado, arquivo_saida) #Chamar a função para salvar os dados no arquivo txt 
print(f"Os resultados foram salvos em '{arquivo_saida}'.") # printando para que o salvamento funcione
