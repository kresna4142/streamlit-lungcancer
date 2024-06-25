import pickle
import streamlit as st

#untuk load model
model = pickle.load(open('lungcancer_model.sav', 'rb'))

#website

#judul
st.title('Prediksi Kanker Paru Paru')

#GENDER	AGE	SMOKING	YELLOW_FINGERS	ANXIETY	PEER_PRESSURE	CHRONIC 
#DISEASE	FATIGUE 	ALLERGY 	WHEEZING	
# ALCOHOL CONSUMING	COUGHING	SHORTNESS OF BREATH	SWALLOWING DIFFICULTY	CHEST PAIN	LUNG_CANCER

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Gender = st.selectbox('Jenis Kelamin (Laki-Laki:1, Perempuan:0)',['Laki-Laki', 'Perempuan'])
with col1:
    Age = st.text_input('Usia')
with col1:
    Smoking = st.selectbox('Merokok: 2/Tidak: 1', ['YES','NO'])
with col1:
    Yellow_Fingers = st.selectbox('Menderita tangan kuning: 2/ Tidak: 1', ['YES','NO'])
with col1:
    Anxiety = st.selectbox('Anxiety: 2/ Tidak : 1', ['YES','NO'])
with col1:
    Peer_Pressure = st.selectbox('Mendapatkan tekanan: 2/ Tidak: 1', ['YES','NO'])
with col1:
    Chronic_Disease = st.selectbox('Memiliki penyakit kronis: 2/ Tidak: 1', ['YES','NO'])
with col1:
    Fatigue = st.selectbox('Mengalami Kelelahan : 2/ Tidak: 1', ['YES','NO'])
with col2:
    Allergy = st.selectbox('Memiliki Alergi: 2/ Tidak: 1', ['YES','NO'])
with col2:
    Wheezing = st.selectbox('Memiliki gangguan nafas berbunyi: 2/ Tidak: 1', ['YES','NO'])
with col2:
    Alcohol_Consuming = st.selectbox('Mengkonsumsi Alkohol: 2/ Tidak: 1', ['YES','NO'])
with col2:
    Coughing = st.selectbox('Apakah anda batuk: 2/ Tidak: 1', ['YES','NO'])
with col2:
    Shortness = st.selectbox('Menderita Sesak Nafas: 2/ Tidak: 1', ['YES','NO'])
with col2:
    Swallow = st.selectbox('Kesulitan menelan: 2/ Tidak: 1', ['YES','NO'])
with col2:
    Chest = st.selectbox('Menderita Nyeri Dada: 2/ Tidak: 1', ['YES','NO'])

categorical_mapping = {
    'YES' : 2, 'NO' : 1,
    'Laki-Laki' : 1, 'Perempuan' : 0
}
# code prediksi
lungcancer_diagnonis = ''

#membuat tombol
if st.button('Test Prediksi Kanker Paru-Paru'):
    lungcancer_prediction = model.predict([[categorical_mapping[Gender],Age,categorical_mapping[Smoking], categorical_mapping[Yellow_Fingers],categorical_mapping[Anxiety], categorical_mapping[Peer_Pressure], 
                                           categorical_mapping[Chronic_Disease], categorical_mapping[Fatigue],categorical_mapping[Allergy],categorical_mapping[Wheezing],categorical_mapping[Alcohol_Consuming],
                                           categorical_mapping[Coughing],categorical_mapping[Shortness],categorical_mapping[Swallow],categorical_mapping[Chest]]])
    if(lungcancer_prediction[0] == 1):
        lungcancer_diagnonis = 'Pasien terkena Kanker Paru-Paru'
        st.error(lungcancer_diagnonis)
    else :
        lungcancer_diagnonis = 'Pasien tidak terkena Kanker Paru-Paru'
        st.success(lungcancer_diagnonis)

# Footer
st.markdown("---")
footer = """
    <style>
    .footer {
        left: 0;
        bottom: 0;
        width: 100%;
        color: White;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        © 2024 Hamman Khadafi Al Habibie 21.11.4164
    </div>
"""
#menyisipkan css
st.markdown(footer, unsafe_allow_html=True)

    
    
