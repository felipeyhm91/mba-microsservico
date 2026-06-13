Link Projeto GITHub: https://github.com/felipeyhm91/mba-microsservico/tree/main/estoque-service

Microsserviço de Estoque – Documentação Resumida

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
  1) Através do terminal, navegue até a pasta ...\mba-microsservico-main\estoque-service | Comando> cd estoque-service
  4) Efetue o "Test Suite" | Comando> py -m pytest tests -v

<img width="792" height="209" alt="image" src="https://github.com/user-attachments/assets/49fc10c6-14db-41a7-8c77-c0ba02a605a0" />
