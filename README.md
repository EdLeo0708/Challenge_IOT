# Challenge IoT – Detecção Facial com Python / OpenCV

## Objetivo do trabalho
- Implementar detecção facial local e interativa.
- Demonstrar impacto dos parâmetros `precisao_busca` e `confianca_deteccao`.
- Exibir resultados (retângulos) em tempo real.
- Fornecer instruções claras para execução e material para apresentação.

---

`precisao_busca`:

- Quanto menor → mais preciso

- Quanto maior → mais rápido, porém detecta menos

`confianca_deteccao`:

- Quantos retângulos precisam confirmar a detecção

- Evita erros e falsos positivos

`tamanho_minimo_rosto`:

- Evita detectar objetos pequenos como se fossem faces

---

  O scaleFactor define o quão rápido o algoritmo reduz a imagem. Quanto menor, mais preciso, porém mais lento.
Já o minNeighbors define quantos retângulos precisam concordar para confirmar que realmente existe uma face. Quanto maior esse valor, mais rigorosa fica a detecção.


---

###Grupo / 3ESPA:

Edson Leonardo: RM553737

Eduardo Mazelli: RM553236

Lucas Masaki: RM553084

Joseh Gabriel:553094

Pedro Henrique:552743
