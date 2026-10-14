# Aporte

**Plataforma open-source de análise de investimentos e planejamento de aportes.**

O Aporte é um projeto local-first que busca ajudar usuários a compreender suas carteiras de investimentos, comparar produtos financeiros e tomar decisões mais fundamentadas sobre novos aportes.

A proposta é analisar investimentos para além da rentabilidade anunciada, considerando fatores como tributação, liquidez, inflação, risco e objetivos financeiros.

## Funcionalidades

*Em desenvolvimento.*

Funcionalidades planejadas:

- Acompanhamento de carteira de investimentos
- Histórico de indicadores financeiros
- Cálculo de rentabilidade
- Comparação de produtos financeiros
- Simulação de aportes
- Análises explicáveis baseadas em regras

## Tecnologias

- **Linguagem:** Python
- **API:** FastAPI
- **Validação de dados:** Pydantic
- **Testes:** pytest
- **Banco de dados planejado:** PostgreSQL
- **Análise de dados planejada:** pandas e NumPy

## Estado do projeto

**Desenvolvimento inicial — MVP em construção.**

O foco inicial é desenvolver um mecanismo confiável de cálculos financeiros, definir os modelos de domínio e estabelecer testes automatizados antes de integrar dados externos do mercado e persistência em banco de dados.

## Como começar

### Pré-requisitos

- Python 3.11 ou superior
- pip

### Instalação

Clone o repositório e acesse o diretório do projeto:

```bash
git clone https://github.com/gustavo-h-k-oliveira/Aporte.git
cd Aporte
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows PowerShell, utilize:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Executar a API

```bash
fastapi dev app/main.py
```

Acesse `http://127.0.0.1:8000/docs` para explorar a documentação interativa da API.

### Executar os testes

```bash
pytest
```

## Princípios de desenvolvimento

- Explicabilidade antes de inteligência artificial.
- Correção financeira antes da expansão de funcionalidades.
- Dados históricos antes de modelos preditivos.
- Separação das regras de negócio da infraestrutura.
- Testes automatizados para cálculos financeiros.
- Nenhuma rentabilidade deve ser tratada como garantida.

## Roadmap

- [x] Estrutura inicial do projeto
- [x] Cálculo básico de juros compostos
- [x] Endpoint inicial da API
- [ ] Precisão monetária e validações financeiras
- [ ] Modelagem de produtos financeiros e indicadores de mercado
- [ ] Coleta de dados históricos do mercado
- [ ] Persistência com PostgreSQL
- [ ] Comparação de investimentos e simulação de aportes
- [ ] Regras de análise explicáveis

## Aviso

O Aporte é um projeto educacional de software em desenvolvimento. Seus cálculos e análises não garantem rentabilidade nem substituem aconselhamento financeiro profissional. Os usuários devem verificar independentemente as informações financeiras e as regulamentações aplicáveis.

## Licença

Este projeto é distribuído sob a licença [MIT](LICENSE).

Você pode usar, copiar, modificar, distribuir e comercializar o software, desde que preserve o aviso de direitos autorais e o texto da licença nas cópias ou partes substanciais do software.
