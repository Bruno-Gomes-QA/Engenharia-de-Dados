# Engenharia-de-Dados

<div>
  <h2 id="Introdução">Introdução 🧑‍🔧</h2>
  <p>Este repositório tem como objetivo apresentar minhas habilidades como engenheiro de dados, evidenciar o que tenho estudado e demonstrar minha evolução na área.
  Atualmente estou cursando Ciências da Computação na UniFECAF, também tenho experiência como QA em um time de BI, onde desenvolvi sólidos conhecimentos em processos de ETL, análise de dados, criação de dashboards utilizando o Tableau, SQL, Python e no ecossistema da AWS. Essa experiência que despertou minha paixão por dados e me motivou a buscar uma carreira que permita impactar positivamente o setor.
  </p>
</div>
<div>
  <h2 id="Estrutura">ETL para Reciclagem ♻️</h2>
  <p>Para meu primeiro projeto, decidi utilizar dados reais da empresa em que sou sócio, atuante no setor de Reciclagem e Recuperação de Resíduos. Por ser uma empresa de pequeno porte, desenvolvi um sistema simples para gerenciar compras, vendas e o estoque de materiais, utilizando o AppSheet, um framework low-code. Os dados são armazenados em um banco de dados nativo da ferramenta, que, apesar de limitado em configurações, se integra perfeitamente à aplicação, oferecendo praticidade ao usuário.

  No entanto, para análises mais detalhadas, o banco se mostra pouco eficiente. Por isso, desenvolvi um ETL para extrair os dados via API do AppSheet e armazená-los em um Data Lake (bucket S3). Após a extração, os dados passam por transformações para tratamento e refinamento, sendo então carregados no Data Warehouse (Redshift). Essa estrutura permite análises eficientes com dados tratados e armazenados em um banco de alta performance.</p>

  [ETL_RECICLAGEM]: https://img.shields.io/badge/ETL_RECICLAGEM-000?style=for-the-badge&logo=code

  [![app][ETL_RECICLAGEM]](./data_pipeline_project/README.md)


Para mais sobre este projeto consulte a [documentação](https://brunom-gomes.notion.site/ETL-Reciclagem-140b2f7eb75980368afdeec8c7ad0ff7) completa.
