# Projeto Libras com TinyML

O dataset original foi obtido em [https://universe.roboflow.com/gomes-project/projeto-libras](https://universe.roboflow.com/gomes-project/projeto-libras), e contém todas as letras do alfabeto brasileiro, além de alguns gestos para palavras simples. Este dataset foi enriquecido com números de 0 a 9 em Libras, criados por nós.

O dataset foi utilizado para treinar um modelo baseado na arquitetura **MobileNetV2** em **Keras**, com a capacidade de aprender tanto a **classificação** dos gestos quanto as **coordenadas do retângulo** envolvendo os objetos nas imagens. O modelo alcançou ótimos resultados, especialmente na **classificação** dos mais de 50 tipos de gestos, com uma **acurácia de aproximadamente 97%**.

Após o treinamento, o modelo foi convertido para o formato **TFLite** e **quantificado** para ser aplicado em dispositivos **TinyML**. Devido às limitações do dispositivo, apenas uma fração do dataset original foi utilizada. Além disso, foi observada uma perda de **performance**, especialmente em relação à **detecção dos gestos**. Contudo, a **classificação dos gestos** continuou sendo eficiente, mostrando o potencial do modelo mesmo em dispositivos com recursos limitados.

