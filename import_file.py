import pandas as pd

from configparser import ConfigParser


class ImportFile:

    def __init__(self):
        '''
        Função de inicialização que pega a configuração do caminho do arquivo.
        '''
        self.config = ConfigParser()
        self.config.read('resources/config.ini')
        self.file_path = self.config.get('PATH', 'files')

    def read_file(self, file, delimiter=','):
        '''
        Função utilizada para realizar a leitura de um arquivo CSV.
        :param file: String, Nome do arquivo que será importado.
        :param delimiter: String, opcional, Indica o delimitador utilizado no arquivo (Padrão ',')
        :return: df, Dataframe pandas com os dados do arquivo.
        '''
        df = pd.read_csv(self.file_path + file, encoding='iso-8859-1', delimiter=delimiter)
        return df
