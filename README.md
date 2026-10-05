# 🧪 Bootcamp QA: Fundamentos de Testes com Pytest

Bem-vindos ao repositório prático do Bootcamp de Qualidade de Software!
Neste projeto, vão aprender e aplicar técnicas de testes de Caixa Preta (como Análise de Valor Limite) e automatizar a vossa estratégia utilizando o framework **Pytest** em Python.

---

## 🎯 Objetivo do Projeto
O objetivo não é apenas aprender a escrever testes, mas sim **como evoluir a escrita de testes**. 
Começaremos com uma abordagem mais simples (e repetitiva) e evoluiremos para técnicas profissionais de automação utilizando **Data-Driven Testing (Parametrize)** e **Injeção de Dependência (Fixtures)**.

---

## 🌳 Navegando pelas Branches (Roteiro de Aprendizagem)

Este repositório está dividido em **branches** (ramificações). Cada branch representa uma fase diferente do nosso aprendizado. Podem mudar de branch utilizando o comando `git checkout <nome-da-branch>` ou através da interface do GitHub.

### 1️⃣ Branch: `main` (O Início)
* **O que tem aqui:** A função inicial do desenvolvedor (`validador_conta.py`), os cenários de teste pensados de forma intuitiva, e a implementação de testes Pytest da forma mais básica (um teste para cada cenário, com repetição de código).
* **O que aprender:** A sintaxe básica do Pytest e o uso do `pytest.raises` para capturar exceções.

### 2️⃣ Branch: `feat/parametrize` (Subindo de Nível)
* **O que tem aqui:** Refatorámos os testes da branch `main` utilizando o poderoso decorador `@pytest.mark.parametrize`.
* **O que aprender:** Data-Driven Testing. Como uma única função de teste pode executar múltiplos cenários de uma Tabela de Decisão, tornando o código incrivelmente limpo e fácil de manter.

### 3️⃣ Branch: `feat/fixtures` (Injeção de Dados)
* **O que tem aqui:** Uma demonstração de como utilizar o `@pytest.fixture`.
* **O que aprender:** Como separar a "criação dos dados de teste" da "execução do teste". Entender como preparar ambientes (ou dados) e injetá-los automaticamente nos teus testes.

### 4️⃣ Branch: `feat/desafio-extra` (Modo Full-Stack)
* **O que tem aqui:** A resolução do desafio da funcionalidade `calcular_desconto`.
* **O que aprender:** Aplicação completa do que foi aprendido. Encontrarão a lógica de negócio implementada, os cenários baseados em Valor Limite/Partição de Equivalência, e os testes escritos das 3 formas diferentes (Direto, Parametrize e Fixtures) para efeitos de comparação.

---

## 🧩 Desafio Extra para a Aula

Nesta branch, o ficheiro `src/tests/cenários/cenarios_desafio_aluno.txt`
apresenta um novo exercício de validação de transferências bancárias. Ele
define o contrato, as regras e os cenários, mas não inclui implementação nem
testes de referência: a proposta é que vocês desenvolvam ambos, aplicando
`@pytest.mark.parametrize` e fixtures.

Os exemplos de desconto e de validação de cliente premium continuam disponíveis
como material de estudo; são independentes deste desafio.

## 🛠️ Atividade Completa: Implementar e Testar

A atividade de saque está organizada em etapas para vocês seguirem:

1. Ler os requisitos e critérios de aceite em
   `src/tech/angelofdiasg/qabank/operacoes/requisito_atividade_saque.txt`.
2. Implementar a função inicial em
   `src/tech/angelofdiasg/qabank/operacoes/validar_saque.py`.
3. Escrever os cenários manualmente em
   `src/tests/cenários/cenarios_atividade_saque.txt`.
4. Completar os testes em
   `src/tests/tests_validar_saque/test_validar_saque.py`, usando o
   `parametrize` e a fixture já preparados. Os testes-esqueleto estão ignorados
   até vocês removerem os marcadores de skip.

## 🚀 Como Executar os Testes

Para executar os testes em qualquer uma das branches, certifiquem-se de que estão na raiz do projeto e executem o seguinte comando no terminal:

`python -m pytest -v`

* **Dica:** O `-v` (verbose) permite ver exatamente qual o teste que passou ou falhou detalhadamente!

---

## 🤖 Uso da IA na Atividade
Durante a aula, exploraremos como utilizar a Inteligência Artificial (Copilot/ChatGPT/Gemini) para gerar a estrutura destes ficheiros Pytest rapidamente. O foco do QA é **pensar nos cenários (Análise)**; a codificação (Automação) pode ser agilizada com o uso de Prompts assertivos!

Bom estudo e bons testes! 🐛🔨