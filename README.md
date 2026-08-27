Documentação Microsserviço de Estoque

Este projeto consiste em um microsserviço de gerenciamento de estoque desenvolvido em Python, com foco na aplicação dos conceitos de Engenharia de Software. 

O sistema permite realizar operações básicas de entrada e saída de produtos em estoque, mantendo o controle da quantidade disponível e validando regras de negócio, como a impossibilidade de retirar uma quantidade superior ao saldo existente.

A arquitetura foi estruturada em camadas, separando entidades de domínio, serviços, repositórios e estratégias de validação. Essa organização favorece a manutenção, reutilização e evolução do sistema. 

Foram aplicados os princípios SOLID, principalmente SRP (Single Responsibility Principle), por meio da separação de responsabilidades entre classes, e DIP (Dependency Inversion Principle), através da utilização de abstrações para validações e serviços. Também foram utilizados conceitos GRASP, como Information Expert, Creator, High Cohesion e Low Coupling.

Como padrão de projeto (Design Pattern), foi utilizada a abordagem Strategy para permitir a criação de diferentes regras de validação sem necessidade de alterar o código principal do serviço. Além disso, o sistema foi desenvolvido de forma a facilitar a injeção de dependências e a realização de testes automatizados.

O Test Suite foi implementado utilizando pytest e contempla três cenários principais: 
 - Entrada de produtos em estoque 
 - Saída de produtos em estoque
 - Validação de erro quando a quantidade solicitada para retirada é superior ao saldo disponível. 
 
Esses testes garantem o funcionamento correto das regras de negócio implementadas.

Instrução técnica, siga os passos abaixo: 
  1) Efetue o Download do Projeto através do Botão "Download Zip"</br>
     <img width="331" height="161" alt="image" src="https://github.com/user-attachments/assets/d52a57ae-f194-4afa-838c-c52825210329" />

  2) Efetue o unzip do Projeto</br>
     <img width="456" height="242" alt="image" src="https://github.com/user-attachments/assets/739271e2-38a0-47fc-b0e9-726489af1626" />

  3) Através da ferramenta "Visual Studio Code", ir no menu "File" e clicar na opção "Open Folder", posteriormente selecione a pasta "mba-microsservico-main" para abrir o projeto</br>
     <img width="262" height="170" alt="image" src="https://github.com/user-attachments/assets/61a4797c-70dd-4ba1-a63c-0565f5c5391e" />
     <img width="794" height="372" alt="image" src="https://github.com/user-attachments/assets/fca76e0f-54d2-4eab-979e-a7b2c8c4da05" />

     
  4) Clique com o botão direito do mouse na pasta "estoque-service" e escolha a opção "Open in Integraded Terminal"</br>
     <img width="380" height="228" alt="image" src="https://github.com/user-attachments/assets/e2633a38-a357-494a-ad86-e62ccbe5fa24" />

  5) Efetue o "Test Suite" através do comando "py -m pytest tests -v" no Terminal 
     <img width="792" height="209" alt="image" src="https://github.com/user-attachments/assets/49fc10c6-14db-41a7-8c77-c0ba02a605a0" />
