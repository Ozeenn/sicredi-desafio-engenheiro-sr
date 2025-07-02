"""
    @author: patrick_moraes
    Created 2025-06-30
"""
######################Imports##########################
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
import pandas as pd
from config.credentials import Configs
#######################################################

postgre_config = Configs.get_credentials()
spark = SparkSession.builder \
    .appName("Conexao PostgreSQL") \
    .config("spark.jars", "/opt/spark/jars/postgresql-42.6.0.jar") \
    .getOrCreate()

#######################################################

def get_data_from_postgre(table):
    """
        Lê dados de uma tabela do PostgreSQL e retorna como um DataFrame do Spark.

        Parâmetros:
        ----------
        table : str
            Nome da tabela no banco de dados PostgreSQL a ser lida.

        Retorna:
        -------
        pyspark.sql.DataFrame
            DataFrame do Spark contendo os dados da tabela especificada no PostgreSQL.

    """

    df = spark.read.format("jdbc") \
        .option("url", postgre_config.host) \
        .option("dbtable", table) \
        .option("user", postgre_config.user) \
        .option("password", postgre_config.password) \
        .option("driver", "org.postgresql.Driver") \
        .load()
    
    return df


def create_flat_table(
        df_conta, df_movimento,
        df_cartao, df_associado
    ):
    """
        Cria uma tabela flat a partir da junção de múltiplos DataFrames relacionados 
        a transações financeiras, cartões, contas e associados.

        Parâmetros:
        ----------
        df_conta : pyspark.sql.DataFrame
            DataFrame contendo informações das contas, incluindo tipo e data de criação.
        
        df_movimento : pyspark.sql.DataFrame
            DataFrame com os dados dos movimentos financeiros, como valor, descrição e data da transação.
        
        df_cartao : pyspark.sql.DataFrame
            DataFrame que contém informações dos cartões, como número, nome impresso e associações com contas e associados.
        
        df_associado : pyspark.sql.DataFrame
            DataFrame com dados dos associados, incluindo nome, sobrenome e idade.

        Retorna:
        -------
        pyspark.sql.DataFrame
            DataFrame resultante da junção dos dados com colunas renomeadas e tipadas como string, representando 
            uma tabela achatada consolidando informações de associados, cartões, contas e movimentos.
    """
    movimento_flat = (
        df_cartao
        .join(df_movimento, df_movimento.id_cartao ==  df_cartao.id, 'inner')
        .join(df_associado, df_associado.id ==  df_cartao.id_associado, 'inner')
        .join(df_conta, df_conta.id ==  df_cartao.id_conta, 'inner')
    )

    movimento_flat =  movimento_flat.select(
        f.col('nome').alias('nome_associado').cast('String'),
        f.col('sobrenome').alias('sobrenome_associado').cast('String'),
        f.col('idade').alias('idade_associado').cast('String'),
        f.col('vlr_transacao').alias('vlr_transacao_movimento').cast('String'),
        f.col('des_transacao').alias('des_transacao_movimento').cast('String'),
        f.col('dat_movimento').alias('data_movimento').cast('String'),
        f.col('num_cartao').alias('numero_cartao').cast('String'),
        f.col('nom_impresso').alias('nome_impresso_cartao').cast('String'),
        f.lit(None).alias('data_criacao_cartao').cast('String'),
        f.col('tpo_conta').alias('tipo_conta').cast('String'),
        f.col('data_criacao').alias('data_criacao_conta').cast('String')
    )
    return movimento_flat

