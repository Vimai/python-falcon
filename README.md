Links úteis para a realização do risco de crédito

https://www.bcb.gov.br/htms/relinf/port/2000/06/ri200006b1p.pdf

https://www.bcb.gov.br/content/estabilidadefinanceira/Documents/Leiaute_de_documentos/scrdoc3040/SCR_InstrucoesDePreenchimento_Doc3040.pdf

Duvidas:
--
Peguei os dados do mock e separei no seguinte dict:

```buildoutcfg
  "relatório visual": {
    "Créditos a vencer de 91 a 180 dias": {
      "total": 2628183.29,
      "Empréstimos": 1222938.98,
      "Financiamentos": 14324.44,
      "Operações de arrendamento": 524088.43,
      "Títulos descontados Direitos creditórios descontados": 128503.14,
      "Coobrigações": 738328.3
    },
    "Créditos a vencer até 30 dias": {
      "total": 7064999.38,
      "Empréstimos": 4133727.33,
      "Financiamentos": 4983.36,
      "Operações de arrendamento": 191695.38,
      "Títulos descontados Direitos creditórios descontados": 2721259.67,
      "Adiantamentos a depositantes": 13333.64
    },
    "Créditos a vencer de 181 a 360 dias": {
      "total": 4206044.720000001,
      "Financiamentos": 27285.95,
      "Operações de arrendamento": 1017852.06,
      "Empréstimos": 1524626.48,
      "Coobrigações": 1636280.23
    },
    "Créditos a vencer de 361 a 720 dias": {
      "total": 5274514.66,
      "Financiamentos": 49555.44,
      "Operações de arrendamento": 1657646.29,
      "Empréstimos": 1076463.71,
      "Coobrigações": 2490849.22
    },
    "Créditos a vencer de 31 a 60 dias": {
      "total": 2787218.8699999996,
      "Financiamentos": 4932.37,
      "Operações de arrendamento": 185743.89,
      "Empréstimos": 413190.07,
      "Títulos descontados Direitos creditórios descontados": 1720888.39,
      "Coobrigações": 462464.15
    },
    "Créditos a vencer de 61 a 90 dias": {
      "total": 2936245.09,
      "Financiamentos": 4878.45,
      "Operações de arrendamento": 183564.64,
      "Empréstimos": 1392217.06,
      "Títulos descontados Direitos creditórios descontados": 1079720.79,
      "Coobrigações": 275864.15
    },
    "Créditos a vencer de 721 a 1080 dias": {
      "total": 7785159.85,
      "Financiamentos": 33179.0,
      "Operações de arrendamento": 858087.25,
      "Empréstimos": 284695.92,
      "Coobrigações": 6609197.68
    },
    "Créditos a vencer de 1801 a 5400 dias": {
      "total": 21452.19,
      "Operações de arrendamento": 21452.19
    },
    "Créditos a vencer de 1441 a 1800 dias": {
      "total": 648616.1,
      "Operações de arrendamento": 648616.1
    },
    "Créditos a vencer de 1081 a 1440 dias": {
      "total": 714251.36,
      "Operações de arrendamento": 714251.36
    },
    "Limite de crédito com vencimento até 360 dias": {
      "total": 3820370.88,
      "Limite": 3820370.88
    }
  }
```

O crédito a vencer do json acima são a letra A do PDF,
O limite de credito é a letra H

O que são as outras letras do PDF?

---

O que seria total do PDF?

---

Para calcular o risco não teria que ter alguma parcela já vencida?

---

Para realizar o cálculo de risco teria que saber mais da lógica do negócio.

No caso, acho ler algo parecido com isso:

https://www.bcb.gov.br/content/estabilidadefinanceira/Documents/Leiaute_de_documentos/scrdoc3040/SCR_InstrucoesDePreenchimento_Doc3040.pdf

Pelo tamanho é meio inviavel, vou perder muito tempo.