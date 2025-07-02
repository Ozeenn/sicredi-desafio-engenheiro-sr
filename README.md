![image](https://github.com/user-attachments/assets/96a91dbc-2583-41cf-9ad0-ba037f3dcf88)![image](https://github.com/user-attachments/assets/9476f5d6-63e0-4c81-87a5-4fce8aead388)![sicredi](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Sicredi-logo.png/960px-Sicredi-logo.png)
# sicredi-desafio-engenheiro-sr
## Objetivos:
    - Estrutar banco de dados
    - Criar etl para coleta de dados
    - Tratar os dados
    - Salvá-los no formato CSV
    - Integração com docker
    
## Pré-requisitos:
    - Docker
## Como utilizar:
    1 - Clone o repositório para a máquina local
    2 - Através do cmd, abra o start.bat
      - Esse arquivo será responsável pela inicialização do container Docker
 ![image](https://github.com/user-attachments/assets/99121e27-effb-44b3-beb3-5110574ace5c)

    3 - Quando o container estiver pronto será aberto uma nova página na web
 ![image](https://github.com/user-attachments/assets/e0ce1d64-83ab-4d11-bbdb-f961dca73516)

    4 - Navegue até a página "Resultado" pelo menu à esquerda
 ![image](https://github.com/user-attachments/assets/45379821-e297-4f83-8d7c-3498f157d3fe)

    5 - Aguarde o processamento finalizar e então clique no botão "Gerar arquivo"
      - Esse botão só será desbloqueado quando o processamento finalizar
 ![image](https://github.com/user-attachments/assets/3aded718-6c34-4467-8e05-6b7405a7a96d)

    6 - O download do arquivo CSV será iniciado pelo navegador
    7 - Selecione onde salvar o arquivo
## Observações:
  ### Escolhas
    - Optei por utilizar o Streamlit para criação de uma interface pois:
      - Facilita a utilização pelo usuário final;
      - Garante uma visão mais agradável do produto;
      - Possui integração com Docker;
      - Possibilita utilização de recursos da Web:
        - Um dos maiores desafios era de possibilitar que o usuário escrevesse em qualquer lugar que quisesse o arquivo final, como o container docker só conseguiria acessar pastas definidas como "volumes" isso limitaria o usuário;
        - Utilizando os recursos da web podemos fazer com que o navegador dispare o download do arquivo e possibilite que o usuário selecione onde deseja salvá-lo, assim como qualquer outro arquivo da web;
    - As cores definidas para o processo foram obtidas através do catálogo de [cores do Sicredi](https://marca.sicredi.com.br/cores/#cores);
  ### Dificuldades
    - Garantir liberdade do usuário para selecionar onde desejava salvar sem fazer necssesário a criação de volumes;
    - O Streamlit é uma ferramenta poderosa mas que em muitos momentos peca na documentação;
    - No contexto do meu trabalho atual nunca utilizamos Docker, então foi necessário certo estudo para integração;
  ### E se tivesse mais tempo?
    - Buscaria, principalmente, investir mais na documentação do fluxo como um todo, não só da utilização;
    - Implementaria novas funcionalidades no APP para uma visão mais fluída dos processamentos;
  ### Sugestões
    - Seria interessante a disponibilização da massa de dados junto ao arquivo
      - Dizer que não precisa ser um volume tão grande torna muito amplo
      - Acredito que o foco do desafio não seja sobre geração de dados ficticios mas sim de cargas de processamento e tratamento, existir uma etapa onde o desafiado cria seus próprios dados acaba consumindo tempo do desafio para algo que não deveria ser o foco e possibilita que o desenvolvedor inclua dados da maneira como desejar, inclusive já tratados, impossibilitando uma avaliação de sua capacidade de limpeza dos dados.


      

