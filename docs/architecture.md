# Arquitetura do Aporte

## 1. Visão geral

O Aporte é uma plataforma local-first de análise de investimentos e planejamento de aportes, desenvolvida inicialmente como um monólito modular.

A aplicação separa a interface HTTP, os serviços de aplicação e as regras do domínio financeiro.

## 2. Tecnologias

- Python
- FastAPI
- Pydantic
- pytest
- PostgreSQL (planejado)
- SQLAlchemy (planejado)

## 3. Camadas

### API

Responsável por receber requisições HTTP, validar entradas e devolver respostas.

Localização: `app/api/`

### Schemas

Define os contratos de entrada e saída da API.

Localização: `app/schemas/`

### Serviços de aplicação

Coordena os casos de uso e combina operações do domínio.

Localização: `app/services/`

### Domínio

Contém os conceitos e as regras financeiras fundamentais, sem depender do framework HTTP ou do banco de dados.

Localização: `app/domain/`

### Infraestrutura

Será responsável por persistência, consultas ao banco de dados e integração com fontes externas de dados financeiros.

Ainda não implementada.

## 4. Fluxo de uma análise

1. O cliente envia os dados do cenário à API.
2. A API valida os dados de entrada.
3. Um serviço de aplicação cria ou recebe o cenário financeiro.
4. O mecanismo de cálculo determina os resultados.
5. O serviço organiza a resposta.
6. A API devolve o resultado ao cliente.

## 5. Princípios

- Separação de responsabilidades.
- Baixo acoplamento entre camadas.
- Regras financeiras independentes do framework.
- Testes automatizados para cálculos.
- Explicabilidade das análises.
- Nenhuma projeção deve ser apresentada como retorno garantido.

## 6. Evolução planejada

1. Consolidar os cálculos financeiros.
2. Definir o modelo de domínio.
3. Implementar testes das regras financeiras.
4. Adicionar persistência com PostgreSQL.
5. Integrar dados históricos do mercado.
6. Desenvolver comparação de investimentos e simulação de aportes.
