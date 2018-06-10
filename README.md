# data_analysis_got
Projeto destinado à apresentação de técnicas de análise e exibição de dados utilizando Datasets com informações da série Game of Thrones.

## Começando

As instruções abaixo lhe auxiliarão na configuração dos requisitos necessários para iniciar a análise dos dados, partindo primeiro da instalação dos programas necessários e após isso a execução da aplicação.

### Pre-requisitos

Para instalar o projeto, voce precisa inicialmente do seguinte:

```
Ambiente Windows ou Linux (Descreverei nesse arquivo como realizar a configuração no Windows)
Python 3 (Instalado na versão 3.6.5 de preferência)
PyCharm (Pode ser a versão Community)
```

### Instalando

Primeiro, é necessário baixar o Software PyCharm, que será a IDE utilizada para a execução da aplicação e o Python, que é a linguagem de programação utilizada para realizar a anáise.

* [Download PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=windows)
* [Download Python 3](https://www.python.org/downloads/)

Após baixar e instalar ambos, é necessário configurar o ambiente virtual do python no PyCharm.

Abra o PyCharm e siga os seguintes passos:
```
1. Abra no menu a aba File
2. Selecione Settings
3. Busque por 'project interpreter' (Sem as aspas)
4. Ao lado da barra exibindo <No interpreter>, selecione o botão de configuração e em seguida add.
5. Ele irá buscar o caminho do python automaticamente para ativar o ambiente virtual, basta dar Ok.
6. Em seguida pode dar Ok novamente
```

Agora, instale o git para poder baixar o repositório do projeto e após isso, baixe o código do projeto:

* [Download Git](https://git-scm.com/downloads)
```
git clone https://github.com/rafaellopsilva/data_analysis_got.git
```

Após isso você deverá abrir o projeto baixado dentro do Pycharm, indo em File e em seguida Open.

### Instalando Pacotes

Abra o arquivo 'data_analysis.py' e verifique que a IDE está solicitando que os pacotes sejam instalados. Instale os pacotes e aguarde a finalização.

O PyCharm saberá o que deverá ser baixado através do arquivo requirements.txt, que indica quais pacotes são necessários no projeto.

### Executando aplicação

Com o arquivo data_analysis.py aberto, aperte as teclas Ctrl + Shift + F10 para executar o programa.

Se tudo correr bem, ao final da execução serão exibidos gráficos com algumas informações sobre os datasets análisados.

### Datasets

Os arquivos utilizados para criação das análises se encontram na pasta 'files' do projeto e no total são 3 arquivos.

* Battles.csv: Arquivo contendo informações das batalhas que ocorreram na série.
* Character Deaths.csv: Contém informações sobre a morte dos personagens.
* Character Predictions.csb: Contém informações gerais referentes aos personagens.
* Screentimes.csv: Contém informações úteis sobre os atores e o tempo de tela de cada um.

# Pacotes utilizados

Foi utilizado nesse projeto os recursos do Pandas para a análise dos dados, pois permite a manipulação dos Dataframes de diversas formas e possibilidades, como pode ser observados nos exemplos gerados.
Outro pacote muito utilizado foi o Matplotlib, que ficou encarregado de exibir os diferentes gráficos a partir das análises realizadas. 

## Autor

* **Rafael Lopes Silva** <rafael.lop.silva@hotmail.com.br>

## Duvidas

Em caso de duvidas na preparação do ambiente ou execução pode me contatar pelo e-mail mencionado acima.

