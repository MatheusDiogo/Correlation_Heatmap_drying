</head>

<body>
    <h1>Repositório Git - Análise de Correlação entre Variáveis</h1>
    <p>Bem-vindo(a) ao repositório Git da análise de correlação entre variáveis!</p>

  <h2>Descrição do Projeto</h2>
    <p>Este projeto realiza uma análise de correlação entre variáveis a partir de um conjunto de dados fornecido. A biblioteca Pandas é utilizada para manipulação dos dados, Seaborn para visualização dos resultados e Numpy e Matplotlib para operações numéricas e gráficas.</p>

  <h2>Instruções de Instalação</h2>
    <p>Para executar o código, é necessário ter as seguintes bibliotecas instaladas. Caso ainda não as possua, você pode instalá-las usando o comando:</p>

  <pre>!pip install --upgrade xlrd openpyxl</pre>

  <h2>Executando a Análise de Correlação</h2>
    <p>Para realizar a análise de correlação entre as variáveis, siga as instruções abaixo:</p>

  <pre>
import pandas as pd
import seaborn as sn
import numpy as np
import matplotlib.pyplot as mp

data = pd.read_excel("Dados.xlsx", engine='openpyxl')

matriz = data.corr()

mp.figure(figsize=(16, 9))
matrix = np.triu(matriz)
try:
    sn.heatmap(matriz, annot=True, fmt=".2f", linewidths=0.6, linecolor="k", mask=matrix)
except ValueError:
    pass
    </pre>

  <p>Certifique-se de ter o arquivo "Dados.xlsx" no mesmo diretório do código ou forneça o caminho correto para o arquivo, caso esteja em outra localização.</p>

  <h2>Visualizando o Resultado</h2>
    <p>Após executar o código, o resultado da análise será exibido em um mapa de calor, mostrando a relação entre as variáveis e seus respectivos coeficientes de correlação.</p>

  <h2>Contribuição</h2>
    <p>Contribuições para melhorias, correções de bugs ou novas funcionalidades são sempre bem-vindas. Sinta-se à vontade para abrir uma issue ou enviar um pull request.</p>

  <p>Aproveite a análise de correlação de variáveis!</p>
</body>
