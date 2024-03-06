## Classificação de Células Sanguíneas 🩸

Este script implementa uma aplicação web usando Streamlit para classificar imagens de células sanguíneas em diferentes tipos. Ele utiliza um modelo de rede neural convolucional pré-treinado para realizar a classificação das imagens.

### Como Usar

1. Faça o upload de uma imagem de células sanguíneas.
2. Clique no botão "Classificar" para iniciar o processo de classificação.
3. O script mostrará a imagem carregada e as probabilidades de pertencer a cada classe de células sanguíneas.

### Bibliotecas Utilizadas

- streamlit: Para criar a aplicação web interativa.
- PIL (Python Imaging Library): Para manipulação de imagens.
- numpy: Para operações numéricas.
- tensorflow: Para carregar o modelo de classificação.
- pandas: Para manipulação de dados.

### Funções Principais

- `load_and_preprocess_image(image_file, target_size)`: Função para carregar e redimensionar a imagem de entrada para o tamanho esperado pelo modelo.
- `classify_image(image, model)`: Função para classificar a imagem carregada usando o modelo pré-treinado.
- `main()`: Função principal que cria a interface da aplicação web e controla o fluxo de execução.

### Como Executar

1. Certifique-se de ter todas as bibliotecas necessárias instaladas.
2. Execute o script em um ambiente Python.
3. Acesse a aplicação web pelo navegador no endereço indicado pelo Streamlit.

### Observações

- Este script utiliza um modelo pré-treinado para classificação de células sanguíneas. Certifique-se de ter o modelo treinado disponível no caminho especificado (`best_model.h5`).
- O modelo pré-treinado deve ser treinado para classificar imagens de células sanguíneas em oito classes específicas: 'basophil', 'eosinophil', 'erythroblast', 'ig', 'lymphocyte', 'monocyte', 'neutrophil', 'platelet'.
