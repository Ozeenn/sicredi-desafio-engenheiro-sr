
# Sicredi — Desafio Engenheiro de Dados Sênior

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Sicredi-logo.png/960px-Sicredi-logo.png" width="200"/>
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-concluído-green" />
  <img alt="Docker" src="https://img.shields.io/badge/docker-integrado-blue" />
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green" />
</p>

---

## 📌 Objetivos

- Estruturar banco de dados relacional
- Criar pipeline ETL para ingestão de dados
- Realizar limpeza e transformação de dados
- Exportar o resultado final em formato `.CSV`
- Executar tudo em ambiente isolado com Docker

---

## 🧰 Tecnologias Utilizadas

- Python
- Apache Spark
- Streamlit
- Docker
- PostgreSQL
- Pandas

---

## 🐳 Como Utilizar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/sicredi-desafio-engenheiro-sr.git
   cd sicredi-desafio-engenheiro-sr
   ```

2. **Execute o `start.bat`** (Windows):
   - Esse script irá iniciar o container Docker automaticamente.

   ![Execução do start.bat](https://github.com/user-attachments/assets/99121e27-effb-44b3-beb3-5110574ace5c)

3. Quando o container estiver pronto, uma nova página será aberta no navegador.  

   ![Tela inicial](https://github.com/user-attachments/assets/e0ce1d64-83ab-4d11-bbdb-f961dca73516)

4. Acesse a aba **"Resultado"** no menu lateral esquerdo.  

   ![Navegação para resultado](https://github.com/user-attachments/assets/45379821-e297-4f83-8d7c-3498f157d3fe)

5. Após o processamento, clique no botão **"Gerar arquivo"**.  
   - Esse botão só será habilitado após o término do processamento.  

   ![Botão de exportação](https://github.com/user-attachments/assets/3aded718-6c34-4467-8e05-6b7405a7a96d)

6. O navegador fará o download do CSV.  
7. Escolha onde deseja salvar o arquivo.

---

## ⚙️ Pré-requisitos

- Docker instalado  
- Acesso à porta 8501 (caso já exista um serviço Streamlit rodando)

---

## 💡 Decisões de Projeto

- **Streamlit** foi escolhido pela facilidade de uso e boa apresentação visual para usuários finais;
- O botão de exportação é habilitado **apenas após** o processamento completo dos dados;
- O CSV é gerado diretamente no navegador para evitar o uso de volumes no Docker, dando mais liberdade ao usuário;
- As cores do projeto seguem o [guia de identidade visual do Sicredi](https://marca.sicredi.com.br/cores/#cores).

---

## 📈 Possíveis Melhorias

- Melhor documentação do fluxo interno de processamento
- Adição de testes unitários para as funções de ETL
- Paginação e filtros nos `dataframes` exibidos
- Exportação adicional em outros formatos (e.g. Excel, JSON)

---

## 📌 Sugestões sobre o desafio

- A disponibilização de uma massa de dados padronizada permitiria:
  - Comparabilidade entre entregas
  - Menor tempo gasto com mock de dados
  - Avaliação mais justa da etapa de limpeza e transformação

---

## 👨‍💻 Autor

**Patrick Moraes**  
[LinkedIn](https://www.linkedin.com/in/patrick-moraes-1b231a183/) | [GitHub](https://github.com/Ozeenn)

---

## 📝 Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
