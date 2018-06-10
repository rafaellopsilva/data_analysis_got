import import_file
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter


class DataAnalysis:

    def __init__(self):
        '''
        Definição da função de inicialização da Classe DataAnalysis.
        '''
        imports = import_file.ImportFile()
        # Importação dos arquivos de base de dados utilizando a classe ImportFile.
        self.battles = imports.read_file('Battles.csv', ';')
        self.character_predictions = imports.read_file('Character Predictions.csv')
        self.character_deaths = imports.read_file('Character Deaths.csv')
        self.screentimes = imports.read_file('Screentimes.csv')
        self.treat_battles()

    def treat_battles(self):
        '''
        Método para tratar a última coluna da tabela 'Battles', que não possui nome na base de dados.
        :return: Dataframe, Retorna o dataframe corrigido.
        '''
        return self.battles.rename(columns={'Unnamed: 25': 'location2'}, inplace=True)

    def analyze_time_for_popularity(self):
        '''
        Método para pegar os personagens mais importantes da série baseado no tempo de tela e na popularidade.
        '''
        ch_predictions = self.character_predictions.sort_values('name')
        # Pegando apenas personagens com popularidade.
        ch_predictions = ch_predictions[ch_predictions['popularity'] > 0]
        screentimes = self.screentimes.sort_values('name')
        # Criando um dataframe com personagens em ambas as bases utilizadas.
        matching = ch_predictions[ch_predictions['name'].isin(screentimes['name'])]
        ch_predictions = ch_predictions[ch_predictions['name'].isin(matching['name'])]
        screentimes = screentimes[screentimes['name'].isin(matching['name'])]
        matching['screentime'] = list(screentimes['screentime'])
        # Multiplicando a popularidade dos personagens com o tempo de tela para pegar a importância de cada um.
        matching['popularity_by_time'] = matching['screentime'] * matching['popularity'] / max(matching['screentime'])
        # Ordenando por popularidade.
        df = matching.sort_values(by='popularity_by_time', ascending=False)
        x = np.array(range(10))
        # Preparando para exibir os 10 primeiros resultados.
        y = np.array(np.array(df['popularity_by_time'].head(10)))
        my_xticks = np.array(df['name'].head(10))
        plt.xticks(x, my_xticks)
        plt.bar(x, y, 0.3, color='blue')
        # Configurando exibição.
        plt.title('Importância de Personagens', fontsize=18, color='red')
        plt.ylabel('Importância', fontsize=14, color='blue')
        plt.xlabel('Personagem', fontsize=14, color='blue')
        # Exibindo resultado.
        plt.show()

    def analyze_more_popular_death_characters(self):
        '''
        Função para exibir os personagens mais populares que não estão mais vivos.
        '''
        ch_predictions = self.character_predictions.sort_values('name')
        # Pegando apenas personagens com popularidade.
        ch_predictions = ch_predictions[ch_predictions['popularity'] > 0]
        # Filtrando personagens mortos.
        ch_predictions = ch_predictions[ch_predictions['isAlive'] == 0]
        # Ordenando por popularidade.
        df = ch_predictions.sort_values(by='popularity', ascending=False)
        x = np.array(range(10))
        # Preparando para exibir os 10 primeiros resultados.
        y = np.array(np.array(df['popularity'].head(10)))
        my_xticks = np.array(df['name'].head(10))
        plt.xticks(x, my_xticks)
        plt.bar(x, y, 0.3, color='blue')
        # Configurando exibição.
        plt.title('Popularidade de Personagens mortos', fontsize=18, color='red')
        plt.ylabel('Popularidade', fontsize=14, color='blue')
        plt.xlabel('Personagem (Morto)', fontsize=14, color='blue')
        # Exibindo resultado.
        plt.show()

    def analyze_family_in_battles(self):
        '''
        Função para análisas as famílias quem mais participaram de guerras
        '''
        battles = self.battles
        attacker = 'attacker_'
        defender = 'defender_'
        families_battling = []
        # Realiza um loop para pegar as famílias atacantes e defensoras nas guerras.
        for i in range(1, 5):
            att = attacker + str(i)
            defe = defender + str(i)
            for family in battles[att]:
                families_battling.append(family)
            for family in battles[defe]:
                families_battling.append(family)
        # Filtra apenas os valores que são não nulos.
        family_list_battle = [family for family in families_battling if str(family) != 'nan']
        # Conta quantas vezes cada família lutou em uma guerra.
        family_battle_ocurrences = Counter(family_list_battle)
        df = pd.DataFrame.from_dict(family_battle_ocurrences, orient='index').reset_index()
        # Ordena os dados por participação em guerras.
        df = df.sort_values(by=0, ascending=False).head(5)
        # Define as variáveis que serão utilizadas para a criação do gráfico.
        labels = list(df['index'])
        titulos = list(df[0])
        cores = ['darkred', 'whitesmoke', 'yellow', 'darkgray', 'midnightblue']
        # Explode o primeiro pedaço
        explode = (0.1, 0, 0, 0, 0)
        total = sum(titulos)
        # Define as configurações do gráfico de pizza.
        plt.pie(titulos, explode=explode, labels=labels, colors=cores,
                autopct=lambda p: '{:.0f}'.format(p * total / 100), shadow=True, startangle=90)
        # Determina que as proporções sejam iguais de modo a desenhar o círculo
        plt.axis('equal')
        # Configurando exibição.
        plt.title('Participação de Famílias em Guerras', fontsize=18, color='red')
        plt.show()

    def analyze_death_noble_for_books(self):
        '''
        Função para análisar quantas mortes de nobres e não nobres tiveram por livro.
        '''
        # Filtro os personagens já mortos.
        deaths = self.character_deaths[self.character_deaths['Book of Death'] > 0]
        # Carrego a quantidade de personagens mortos por libro que são nobres e não nobres.
        deaths_noble = list(
            map(lambda x: len(deaths[(deaths['Book of Death'] == x) & (deaths['Nobility'] == 1)]), range(1, 6)))
        deaths_non_noble = list(
            map(lambda x: len(deaths[(deaths['Book of Death'] == x) & (deaths['Nobility'] == 0)]), range(1, 6)))
        indice = np.arange(5)
        # Configurações do gráfico
        bar_larg = 0.4
        transp = 0.7
        plt.bar(indice, deaths_noble, bar_larg, alpha=transp, color='gold', label='Nobre')
        plt.bar(indice + bar_larg, deaths_non_noble, bar_larg, alpha=transp, color='gray', label='Não Nobre')
        plt.xlabel('Livros', fontsize=14, color='blue')
        plt.ylabel('Mortes', fontsize=14, color='blue')
        plt.title('Mortes por livro de nobres', fontsize=18, color='red')
        plt.xticks(indice + bar_larg, ('Livro 1', 'Livro 2', 'Livro 3', 'Livro 4', 'Livro 5'))
        plt.legend()
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    data_analysis = DataAnalysis()
    data_analysis.analyze_time_for_popularity()
    data_analysis.analyze_more_popular_death_characters()
    data_analysis.analyze_family_in_battles()
    data_analysis.analyze_death_noble_for_books()
