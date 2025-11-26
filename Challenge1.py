import cv2

# PARÂMETROS
fator_reducao = 1.1      # Quanto a imagem é reduzida a para cada escala
nivel_confianca = 5      # Número de vizinhos necessários para confirmar a detecção
tamanho_minimo = (60, 60)  # Tamanho mínimo de uma face detectada

# calculando o classificador Haar Cascade pré-treinado para detecção facial
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

# controles do teclado
print("[INFO] Pressione 'q' para sair do programa.")
print("[A] diminuir fator de reducao")
print("[D] aumentar fator de reducao")
print("[W] aumentar nivel de confianca")
print("[S] diminuir nivel de confianca")

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Converter para cinza (melhora desempenho)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces com os parâmetros ajustáveisq
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=fator_reducao,
        minNeighbors=nivel_confianca,
        minSize=tamanho_minimo
    )

    # Desenha forma ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Exibir parâmetros atuais na tela
    texto = f"fator_reducao={fator_reducao:.2f}, nivel_confianca={nivel_confianca}"
    cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Mostrar imagem
    cv2.imshow("Detecção Facial - Haar Cascade", frame)

    # Ajuste dos parâmetros em tempo real
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):   # sair
        break
    elif key == ord('a'):  # diminuir fator de redução
        fator_reducao = max(1.01, fator_reducao - 0.05)
    elif key == ord('d'):  # aumentar fator de redução
        fator_reducao += 0.05
    elif key == ord('w'):  # aumentar confiança
        nivel_confianca += 1
    elif key == ord('s'):  # diminuir confiança
        nivel_confianca = max(1, nivel_confianca - 1)

camera.release()
cv2.destroyAllWindows()
