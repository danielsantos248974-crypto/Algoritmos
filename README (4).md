# Sistema de Controle de Qualidade para Embalagens

Protótipo em Python desenvolvido para o **Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento**, da disciplina *Algoritmos e Lógica de Programação* (UniFECAF).

O sistema automatiza a inspeção de embalagens de uma linha de produção: recebe os dados de cada peça, aprova ou reprova segundo critérios de qualidade, guarda as aprovadas em caixas de 10 unidades e gera um relatório consolidado.

---

## Funcionamento

### Critérios de qualidade

Uma embalagem é **aprovada** somente se atender aos três critérios ao mesmo tempo:

| Critério     | Faixa aceita     |
|--------------|------------------|
| Cor          | azul ou verde    |
| Comprimento  | 10 cm a 20 cm    |
| Peso         | 95 g a 105 g     |

Se falhar em qualquer um, é **reprovada**, e o sistema registra quais critérios foram violados.

### Armazenamento em caixas

- Cada caixa comporta **10 embalagens aprovadas**.
- Quando uma caixa atinge 10 unidades, ela é **fechada** e a próxima embalagem aprovada abre uma nova caixa.
- Se uma embalagem for removida da caixa aberta, a capacidade dela diminui. Se for removida de uma caixa fechada, a caixa continua fechada.

### Menu

| Opção | Ação |
|-------|------|
| 1 | Cadastrar nova embalagem (cor, tamanho, peso). O id é gerado automaticamente, começando em 0 |
| 2 | Listar embalagens aprovadas (por caixa) e reprovadas (com o motivo) |
| 3 | Remover uma embalagem cadastrada pelo id |
| 4 | Listar caixas fechadas |
| 5 | Gerar relatório final: aprovadas, reprovadas, motivos e caixas utilizadas |
| 0 | Sair |

### Estrutura do código

- **Listas** guardam os dados: cada embalagem é `[id, cor, comprimento, peso]`; `caixas` reúne todas as caixas; `reprovadas` guarda as embalagens reprovadas; `cores`, `comprimentos` e `pesos` guardam os valores que causaram reprovação.
- **Funções** separam as responsabilidades: `cadastro()`, `estoque()`, `remover()`, `listar_caixas_fechadas()` e `relatorio()`, uma para cada opção, além das auxiliares `motivos()` e `fechadas()`.
- **Condições** (`if/else` e `match/case`) avaliam as embalagens, controlam a abertura e o fechamento das caixas e direcionam as opções do menu.
- **Repetição**: `while True` mantém o menu ativo e `for` percorre caixas e embalagens.
- **Tratamento de erros** com `try/except` no menu e na remoção: letras no lugar de números não encerram o programa.

---

## Como rodar o programa

### Pré-requisito

**Python 3.10 ou superior** (o menu usa `match/case`). Não há bibliotecas externas.

Para verificar a versão instalada:

```bash
python --version
```

### Passo a passo

1. Clone o repositório (ou baixe o arquivo `sistema_embalagens.py`):

   ```bash
   git clone [LINK_DO_REPOSITORIO]
   cd [NOME_DA_PASTA]
   ```

2. Execute o programa:

   ```bash
   python sistema_embalagens.py
   ```

   No Linux/macOS, se `python` não funcionar, use `python3 sistema_embalagens.py`.

3. Digite o número da opção desejada no menu e responda às perguntas na tela.

### Observações de uso

- Digite a cor em letras minúsculas (`azul`, `verde`).
- Tamanho e peso devem ser números inteiros (ex.: `15`, `100`).

---

## Exemplos de entradas e saídas

### Opção 1 — Cadastro de embalagem aprovada

```
Escolha umas das opções: 1
Responda as perguntas para cadastrar uma nova embalagem.
Qual é a cor da embalagem? azul
Qual é o seu tamanho? (cm) 15
Quanto ela pesa? (g) 100
Abrindo caixa...
Caixa aberta com sucesso.
Embalagem adicionada com sucesso.
```

### Fechamento de caixa (10ª embalagem aprovada)

```
Escolha umas das opções: 1
Responda as perguntas para cadastrar uma nova embalagem.
Qual é a cor da embalagem? azul
Qual é o seu tamanho? (cm) 15
Quanto ela pesa? (g) 100
Embalagem adicionada com sucesso.
Caixa fechada, abrindo uma nova...
```

### Opção 1 — Cadastro de embalagem reprovada

```
Escolha umas das opções: 1
Responda as perguntas para cadastrar uma nova embalagem.
Qual é a cor da embalagem? azul
Qual é o seu tamanho? (cm) 25
Quanto ela pesa? (g) 110
Infelizmente essa embalagem não atende aos nossos padrões de qualidade
Tente cadastrar uma nova embalagem!
```

### Opção 2 — Listar aprovadas e reprovadas

```
Escolha umas das opções: 2
APROVADAS
id | cor | comprimento | peso
[0, 'azul', 15, 100]
--------------------
[1, 'azul', 15, 100]
--------------------
...
[9, 'azul', 15, 100]
--------------------
====================
[10, 'verde', 12, 98]
--------------------
====================
REPROVADAS
id | cor | comprimento | peso | motivo
[11, 'vermelho', 15, 100] -> cor
--------------------
[12, 'azul', 25, 110] -> comprimento, peso
--------------------
```

### Opção 3 — Remover embalagem

```
Escolha umas das opções: 3
Digite o id da embalagem que deseja remover: 12
Embalagem removida com sucesso.
```

### Opção 4 — Listar caixas fechadas

```
Escolha umas das opções: 4
Caixa 1 - 10 embalagens
[0, 'azul', 15, 100]
[1, 'azul', 15, 100]
...
[9, 'azul', 15, 100]
====================
```

### Opção 5 — Relatório final

Após cadastrar 11 aprovadas e 2 reprovadas e remover a embalagem de id 12:

```
Escolha umas das opções: 5
========================================
       RELATÓRIO CONSOLIDADO DE PRODUÇÃO
========================================
Total de peças aprovadas: 11.
Total de peças reprovadas: 1.
----------------------------------------
Motivos das reprovações:
Cores são diferentes de azul ou verde: 1 peça(s).
id 11: cor
----------------------------------------
Quantidade de caixas utilizadas: 2.
Caixas fechadas: 1.
========================================
```

### Entrada inválida no menu

```
Escolha umas das opções: x
Opção inválida!
Escolhe uma opção entre 0 e 5.
```

---

## Autor

Daniel Alves dos Santos — Graduação em Inteligência Artificial e Automação Digital, UniFECAF.
