# Esteira de Aprendizado de Máquina — Palmer Penguins

Classificação supervisionada das espécies de pinguins (`Adelie`, `Chinstrap` e `Gentoo`) com uma esteira completa: preparação dos dados, transformações, divisão em treino/validação/teste, treinamento, avaliação e predição com modelo implantado.

**Dataset:** [Palmer Penguins — Kaggle](https://www.kaggle.com/datasets/ashkhagan/palmer-penguins-datasetalternative-iris-dataset) (344 registros, 7 colunas, problema de classificação).

## Resultados obtidos

- Base após limpeza: 333 registros (11 linhas com valores ausentes removidas).
- Divisão estratificada: 199 treino / 67 validação / 67 teste (60/20/20).
- Modelo escolhido na validação: Regressão Logística (pipeline com one-hot + padronização).
- **Acurácia no teste: 100% (67/67)** — matriz de confusão e relatório de classificação estão no notebook.
- Predição do modelo implantado: novo exemplar de Biscoe classificado como `Gentoo` com 99,78% de confiança.

> A acurácia perfeita é esperada nesta base: ela é pequena e as espécies são bem separáveis pelas medidas do bico e da nadadeira.

## Estrutura do repositório

```
.
├── palmer_penguins_ml_pipeline.ipynb   # notebook com a esteira completa (executado)
├── predict.py                          # CLI que carrega o modelo salvo e classifica um novo exemplar
├── data/penguins.csv                   # cópia local do dataset do Kaggle
├── models/                             # modelo gerado pelo notebook (joblib)
├── requirements.txt
└── README.md
```

## Como reproduzir

1. Clone o repositório e entre na pasta do projeto:

   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>.git
   cd <NOME_DO_REPOSITORIO>
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   No Windows: `.venv\Scripts\activate`

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o notebook (todas as células, em ordem):

   ```bash
   jupyter notebook palmer_penguins_ml_pipeline.ipynb
   ```

   Ou, sem abrir a interface:

   ```bash
   jupyter nbconvert --to notebook --execute --inplace palmer_penguins_ml_pipeline.ipynb
   ```

   A execução imprime as estatísticas descritivas, as transformações, a matriz de confusão, a acurácia e salva `models/modelo_penguins.joblib`.

5. Teste o modelo implantado pela linha de comando:

   ```bash
   python predict.py
   python predict.py --ilha Dream --comprimento-bico 46.5 --altura-bico 15.9 --nadadeira 190 --massa 3700 --sexo male
   ```

   Observação: execute o notebook antes do `predict.py`, pois ele gera o arquivo do modelo.

## Requisitos da atividade atendidos

| Requisito | Seção do notebook |
| --- | --- |
| Base de classificação do Kaggle | 1 — Carga do conjunto de dados |
| Estatísticas descritivas gerais | 2 — Estatísticas descritivas gerais |
| Transformação em colunas | 3 — `proporcao_bico`, one-hot e escalonamento |
| Transformação em linhas | 4 — remoção de ausentes e duplicados |
| Treino, validação e teste | 5 — divisão estratificada 60/20/20 |
| Treinamento e avaliação | 6 — dois modelos avaliados na validação |
| Matriz de confusão e acurácia | 7 — avaliação no teste |
| Predição do modelo implantado | 8 — `joblib` + nova observação |

## Vídeo (até 5 minutos)

Link do YouTube: **preencher após publicar**.

Roteiro sugerido:

- 00:00–00:40 — apresentação do projeto, dataset, objetivo e requisitos.
- 00:40–01:20 — carga do CSV e estatísticas descritivas (`shape`, `describe`, classes).
- 01:20–02:00 — transformações: coluna `proporcao_bico`, one-hot/scaling e limpeza de linhas.
- 02:00–02:40 — divisão 60/20/20 estratificada e treinamento dos dois modelos.
- 02:40–03:40 — matriz de confusão, acurácia de 100% no teste e predição do modelo implantado.
- 03:40–04:20 — execução do `predict.py` no terminal.
- 04:20–05:00 — resumo da esteira e link do repositório.

## Entrega

Prazo: 25/11/2026. Formulário: https://forms.gle/wRFct5kfubGnxffH7
