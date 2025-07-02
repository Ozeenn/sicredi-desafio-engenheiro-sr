"""
    @author: patrick_moraes
    Created 2025-06-30
"""
######################Imports##########################
from configparser import ConfigParser
from types import SimpleNamespace
import os
#######################################################

class Configs:
    @staticmethod
    def get_config_file():
        """
            Busca recursivamente no diretório atual por um arquivo com extensão `.config`.

            Retorna:
            -------
            str
                Caminho completo para o primeiro arquivo `.config` encontrado.

            Observações:
            ------------
            - A busca começa a partir do diretório de execução atual (`os.getcwd()`).
            - Utiliza `os.walk` para percorrer recursivamente todos os diretórios e subdiretórios.
            - Retorna o caminho completo como string, unindo o diretório onde o arquivo foi encontrado com o nome do arquivo.
        """

        current_path = os.getcwd()

        for path in os.walk(current_path):
            if any('.config' in element for element in path[2]):
                return path[0] + '/' + list(filter(lambda x: '.config' in x, path[2]))[0]

    @staticmethod
    def get_credentials(section='postgresql'):
        """
            Lê as credenciais de acesso a partir de um arquivo `.config` e retorna um objeto com os parâmetros da seção especificada.

            Parâmetros:
            ----------
            section : str, opcional (padrão='postgresql')
                Nome da seção no arquivo de configuração da qual os parâmetros serão extraídos.

            Retorna:
            -------
            types.SimpleNamespace
                Objeto com os atributos correspondentes às chaves da seção, permitindo acesso via notação de ponto (e.g., `credentials.user`).

            Exceções:
            --------
            Exception
                Lançada caso a seção especificada não seja encontrada no arquivo de configuração.

            Ações realizadas:
            -----------------
            - Localiza o arquivo `.config` utilizando a função `Configs.get_config_file()`.
            - Utiliza `ConfigParser` para ler o arquivo.
            - Extrai os parâmetros da seção especificada.
            - Armazena os parâmetros como atributos em um objeto `SimpleNamespace`.
        """
        parser = ConfigParser()
        file = Configs.get_config_file()
        parser.read(file)
        credentials = SimpleNamespace()
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                setattr(credentials, param[0], param[1])
    
        return credentials
        