import streamlit as st
import pandas as pd 
import numpy as np


st.write("""#DATA HISTORI""")

option = st.sidebar.selectbox('Pilih:',('Data', 'Visualisasi', 'Keterangan'))

if option == 'Data':
    df = pd.read_csv('history.csv')
    df
elif option == 'Visualisasi':
    st.title("Visualisasi Jumlah Gerakan Yang sudah di Scan")
    df = pd.read_csv('history.csv')
    jumlah = df['nama_gerakan'].value_counts()
    jumlah
    st.bar_chart(data = df, x = ['nama_gerakan'], y= 'nama_gerakan' ,use_container_width=True)
    st.write("Keterangan : Nomor dibawah adalah gerakan yang di scan sesuai index")
else:
    st.write("CRAZY XIAO YAN")