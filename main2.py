import streamlit as st
import pandas as pd
import numpy as np

import pickle
from sklearn.neighbors import KNeighborsClassifier

model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title('Prediksi Reisko Terkena Penipuan Transaksi Kartu Kretdit')
st.write('Penipuan transaksi kartu kredit merujuk pada kegiatan yang melibatkan penggunaan kartu kredit seseorang secara tidak sah atau tanpa izin untuk mendapatkan keuntungan pribadi atau merugikan pemilik kartu kredit. Bentuk penipuan transaksi kartu kredit sangat bervariasi dan terus berkembang seiring dengan kemajuan teknologi.')
st.write('Silahkan isi form berikut: ')

col1, col2 = st.columns(2)

#inputan
# Input
distance_from_home = st.text_input("Masukkan jarak rumah ke lokasi transaksi", key="distance_from_home")
distance_from_last_transaction = st.text_input("Masukkan jarak  dari transaksi terakhir", key="distance_from_last_transaction")
ratio_to_median_purchase_price = st.text_input("Masukkan rasio harga pembelian rata rata", key="ratio_to_median_purchase_price")
repeat_retailer = st.text_input("Apakah retailer tersebut telah dikunjungi sebelumnya atau tidak [0/1]", key="repeat_retailer")
used_chip = st.text_input("Apakah transaksi melalui kartu kredit [0/1]", key="used_chip")
used_pin_number = st.text_input("Apakah transaksi dilakukan dengan penggunaan nomor PIN [0/1]", key="used_pin_number")
online_order = st.text_input("Apakah transaksi dilakukan secara online? [0/1]", key="online_order")


# Prediksi
pred_fraud = ''

# Tombol untuk prediksi
if st.button('Prediksi'):
    # Konversi nilai input ke tipe numerik
    distance_from_home = float(distance_from_home)
    distance_from_last_transaction = float(distance_from_last_transaction)
    ratio_to_median_purchase_price = float(ratio_to_median_purchase_price)
    repeat_retailer = int(repeat_retailer)
    used_chip = int(used_chip)
    used_pin_number = int(used_pin_number)
    online_order = int(online_order)

    # Lakukan prediksi
    pred_fraud = model.predict([[distance_from_home, distance_from_last_transaction, ratio_to_median_purchase_price, repeat_retailer, used_chip, used_pin_number, online_order]])

    if pred_fraud == 0:
        st.success('Termasuk Transaksi Asli')
    else:
        st.error('Termasuk Transaksi Penipuan')