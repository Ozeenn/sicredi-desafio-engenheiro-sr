"""
    @author: patrick_moraes
    Created 2025-06-30
"""

######################Imports##########################
import streamlit as st
import pandas as pd
import base64 
import os
from css import style
from etl import script
#######################################################

if os.path.isdir('app/'):
    base_path = 'app/'
else:
    base_path = '/opt/spark/app/'

#######################################################

def init_app_config():
    """
        Inicializa a configuração da aplicação Streamlit, definindo título da página, ícones,
        layout e aplicando estilos personalizados.

        Ações realizadas:
        -----------------
        - Define o título da página como "Desáfio Técnico".
        - Define o ícone da aba do navegador com uma imagem localizada em `images/logo-sicredi.png`.
        - Define o layout da página como centralizado.
        - Expande a barra lateral ao iniciar a aplicação.
        - Adiciona um logotipo no topo da página com duas imagens (principal e ícone), ambas baseadas no caminho `base_path`.
        - Aplica o estilo CSS definido em `style.app_style` via `st.markdown`.
    """

    st.set_page_config(
        page_title="Desáfio Técnico", 
        page_icon=f'{base_path}images/logo-sicredi.png',
        layout="centered", 
        initial_sidebar_state="expanded"
    )

    st.logo(
        image=f'{base_path}images/sicredi.png',
        icon_image=f'{base_path}images/sicredi_logo_branco.png',
        size='large'
    )

    st.markdown(
        style.app_style, 
        unsafe_allow_html=True
    )

def displayPDF(file):
    """
        Exibe um arquivo PDF dentro da aplicação Streamlit usando um componente HTML embutido.

        Parâmetros:
        ----------
        file : str
            Caminho para o arquivo PDF que será exibido.

        Ações realizadas:
        -----------------
        - Lê o conteúdo do arquivo PDF em modo binário.
        - Codifica o conteúdo em base64 para embutir diretamente no HTML.
        - Cria um elemento `<embed>` HTML com o conteúdo do PDF, definindo altura e largura fixas.
        - Renderiza o HTML com `st.markdown`, permitindo visualização do PDF diretamente na página Streamlit.
    """

    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="660" height="1000" type="application/pdf">'
    st.markdown(
        pdf_display, 
        unsafe_allow_html=True
    )

def welcome_page():
    """
        Exibe a página inicial de boas-vindas do desafio técnico.

        Ações realizadas:
        -----------------
        - Renderiza um texto de boas-vindas utilizando Markdown
        - Exibe um arquivo PDF com os detalhes do desafio, localizado no caminho 
        `{base_path}/images/Desafio técnico engenharia de dados 8 2.pdf`, utilizando a função `displayPDF`.
    """

    st.markdown(
        """
            ## Seja bem vindo(a) ao desafio técnico do Sicredi para a posição de Engenheiro de dados sênior. 
            ### Abaixo você encontrará mais detalhes sobre o desafio.
        """
    )
    displayPDF(
        f'{base_path}/images/Desafio técnico engenharia de dados 8 2.pdf'
    )

def export_result_page():
    """
        Exibe a página de exportação dos resultados do desafio técnico, com carregamento progressivo 
        dos dados e geração de um arquivo CSV consolidado.

        Ações realizadas:
        -----------------
        - Exibe um título introdutório à seção de resultados.
        - Cria duas colunas na interface:
            - Coluna 1: barra de progresso indicando o andamento da carga e transformação dos dados.
            - Coluna 2: botão inicialmente desabilitado, que será ativado ao final do processamento.
        - Define um dicionário `dfs` com os nomes das tabelas do PostgreSQL e o percentual de progresso 
        correspondente à sua carga.
        - Para cada tabela:
            - Lê os dados usando `script.get_data_from_postgre`.
            - Exibe os dados em um expander com `st.dataframe`.
            - Atualiza a barra de progresso conforme o percentual definido.
        - Após o carregamento de todos os dados, cria uma tabela final consolidada (`df_flat`) com a função 
        `script.create_flat_table`.
        - Quando o processamento atinge 100%, substitui o botão por um botão de download, permitindo exportar
        os dados consolidados no formato CSV.
    """

    st.markdown(
        """
            ### Agora que sabemos o que queremos realizar, está na hora do resultado. 
        """
    )
    col1, col2 = st.columns([5, 2])

    with col1:
        progress_bar = st.progress(
            0, 
            text='Processando dados... 0%'
        )

    with col2:
        button = st.empty()
        button.button("Gerar arquivo", disabled=True)


    dfs = {
        'df_conta': ['engsr_desafio.conta', 20],
        'df_movimento': ['engsr_desafio.movimento', 40],
        'df_cartao': ['engsr_desafio.cartao', 60],
        'df_associado': ['engsr_desafio.associado', 80],
    }

    for df_name in dfs:
        percent = dfs[df_name][1]
        table_name = dfs[df_name][0]
        with st.expander(table_name.capitalize()):
            df = script.get_data_from_postgre(table_name)
            st.dataframe(
                pd.DataFrame(df.toPandas())
            )
            dfs[df_name].append(df)

        progress_bar.progress(
            value=percent, text=f'Processando dados... {percent}%', 
        )
    
    df_flat = script.create_flat_table(
        dfs['df_conta'][-1], dfs['df_movimento'][-1],
        dfs['df_cartao'][-1], dfs['df_associado'][-1]
    )

    progress_bar.progress(
        value=100, text=f'Processamento concluído... {100}%', 
    )


    if df_flat:
        with col2:
            button.download_button(
                label="Gerar arquivo",
                data=df_flat.toPandas().to_csv(index=False).encode("utf-8"),
                file_name="movimento_flat.csv",
                mime="text/csv"
            )

def run_app():
    """
        Inicializa e executa a aplicação Streamlit com navegação entre páginas.

        Ações realizadas:
        -----------------
        - Chama a função `init_app_config()` para configurar a aparência da aplicação (título, ícones, layout e estilos).
        - Define a navegação entre páginas da aplicação utilizando `st.navigation`, com as seguintes rotas:
            - Página "Boas vindas", que exibe a função `welcome_page`.
            - Página "Resultado", que exibe a função `export_result_page`.
        - Inicia a execução da navegação com `.run()`.
    """

    init_app_config()
    st.navigation(
        pages=[
            st.Page(welcome_page, title="Boas vindas"),
            st.Page(export_result_page, title="Resultado")
        ], 
        expanded=True
    ).run()

if __name__ == '__main__':
    run_app()
