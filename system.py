import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import pandas as pd


labels = ['basophil', 'eosinophil', 'erythroblast', 'ig', 'lymphocyte', 'monocyte', 'neutrophil', 'platelet']

# Função para carregar e redimensionar a imagem
def load_and_preprocess_image(image_file, target_size=(224, 224)):
    image = Image.open(image_file)
    image = image.resize(target_size)
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    return image

# Função para classificar a imagem
def classify_image(image, model):
    preds = model.predict(image)[0]
    return preds

def main():
    st.title("Classificação de Células Sanguíneas")
    st.write("Faça o upload de uma imagem de células sanguíneas para classificação.")

    # Carregar imagem
    uploaded_file = st.file_uploader("Faça o upload de uma imagem", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Mostrar imagem
        image = Image.open(uploaded_file)
        st.image(image, caption='Imagem de células sanguíneas', use_column_width=True)

        # Carregar modelo
        model = tf.keras.models.load_model('./model/best_model.h5')  
        
        # Classificar imagem
        if st.button('Classificar'):
            with st.spinner('Classificando...'):
                image_array = load_and_preprocess_image(uploaded_file)
                predictions = classify_image(image_array, model)
                st.write('**Probabilidade de cada classe:**')
                for i, prob in enumerate(predictions):
                    st.write(f'{labels[i]}: {prob*100:.2f}%')

if __name__ == "__main__":
    main()
