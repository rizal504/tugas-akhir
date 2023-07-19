import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

import pickle
from sklearn.neighbors import KNeighborsClassifier

model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title('Prediksi Risiko Terkena Penipuan Transaksi Kartu Kredit')

image = Image.open('logo.jpg')
st.image(image, use_column_width=True)

st.write('Penipuan transaksi kartu kredit merujuk pada kegiatan yang melibatkan penggunaan kartu kredit seseorang secara tidak sah atau tanpa izin untuk mendapatkan keuntungan pribadi atau merugikan pemilik kartu kredit. Bentuk penipuan transaksi kartu kredit sangat bervariasi dan terus berkembang seiring dengan kemajuan teknologi.')
st.write('Silahkan isi form berikut: ')

# Inputan
distance_from_home = st.text_input("Masukkan jarak rumah ke lokasi transaksi", key="distance_from_home")
distance_from_last_transaction = st.text_input("Masukkan jarak dari transaksi terakhir", key="distance_from_last_transaction")
ratio_to_median_purchase_price = st.text_input("Pilih rasio harga pembelian", key="ratio_to_median_purchase_price")

repeat_retailer_options = ["Tidak", "Ya"]  # Contoh pilihan pengulangan retailer
repeat_retailer = st.selectbox("Apakah retailer tersebut telah dikunjungi sebelumnya?", repeat_retailer_options, key="repeat_retailer")

used_chip_options = ["Tidak", "Ya"]  # Contoh pilihan penggunaan kartu kredit
used_chip = st.selectbox("Apakah transaksi melalui kartu kredit?", used_chip_options, key="used_chip")

used_pin_number_options = ["Tidak", "Ya"]  # Contoh pilihan penggunaan nomor PIN
used_pin_number = st.selectbox("Apakah transaksi dilakukan dengan penggunaan nomor PIN?", used_pin_number_options, key="used_pin_number")

online_order_options = ["Tidak", "Ya"]  # Contoh pilihan transaksi online
online_order = st.selectbox("Apakah transaksi dilakukan secara online?", online_order_options, key="online_order")

# Prediksi
pred_fraud = ''

# Tombol untuk prediksi
if st.button('Prediksi'):
    # Konversi nilai input ke tipe numerik
    distance_from_home = float(distance_from_home)
    distance_from_last_transaction = float(distance_from_last_transaction)
    ratio_to_median_purchase_price = float(ratio_to_median_purchase_price)
    repeat_retailer = int(repeat_retailer == "Ya")
    used_chip = int(used_chip == "Ya")
    used_pin_number = int(used_pin_number == "Ya")
    online_order = int(online_order == "Ya")

    # Lakukan prediksi
    pred_fraud = model.predict([[distance_from_home, distance_from_last_transaction, ratio_to_median_purchase_price, repeat_retailer, used_chip, used_pin_number, online_order]])

    if pred_fraud == 0:
        st.success('Termasuk Transaksi Asli')
    else:
        st.error('Termasuk Transaksi Penipuan')
