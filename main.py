import streamlit as st
import csv
import os
import pandas as pd
import random

st.title('Montecarlo')
st.subheader('created by : 152017114 Anisa Putri Setyaningrum')


@st.cache(persist=True)
def exploredata(data):
    df = pd.read_csv(os.path.join(data))
    return df


# untuk sum/penjumlahan frekuensi


def jumlah(arr):
    hasil = 0
    for i in range(0, len(arr)):
        hasil = hasil + arr[i]
    return str(hasil)


# untuk penjumlahan probabilitas kumulatif


def kumulatif(arr):
    new_list = []
    j = 0
    for i in range(0, len(arr)):
        j = round((j + arr[i]), 3)
        new_list.append(j)
    return new_list

# mencari probabilitas


def prob(banyak, arrays):
    new_list = []
    p = 0
    for i in range(0, len(arrays)):
        p = round((arrays[i]/int(banyak)), 3)
        new_list.append(p)
    return new_list

# batas interval atas


def intvalbawah(arr):
    new_list = [0]
    b = 0
    for i in range(0, len(arr)-1):
        b = round((arr[i] + 0.001), 3)
        new_list.append(b)
    return new_list

# Penaksiran


def taksir(angka, valatas):
    new_list = []
    t = 0
    for i in range(0, len(angka)):
        if angka[i] < valatas[0]:
            t = 0
            new_list.append(t)
        elif angka[i] < valatas[1]:
            t = 1
            new_list.append(t)
        elif angka[i] < valatas[2]:
            t = 2
            new_list.append(t)
        elif angka[i] < valatas[3]:
            t = 3
            new_list.append(t)
        else:
            t = 4
            new_list.append(t)
    return new_list


# Random Number
def randnum(n):
    i = 1
    r = 0
    new_list = []
    while i <= n:
        na = random.random()
        r = round(na, 3)
        i += 1
        new_list.append(r)
    return new_list

# total dengan harga


def total(permintaan, harga):
    new_list = []
    total = 0
    for i in range(0, len(permintaan)):
        total = permintaan[i]*int(harga)
        new_list.append(total)
    return new_list

# jumlah permintaan


def jmlpermintaan(permintaan):
    hasil = 0
    for i in range(0, len(permintaan)):
        hasil += permintaan[i]
    return hasil

# jumlah harga


def jmlharga(harga):
    hasil = 0
    for i in range(0, len(harga)):
        hasil += harga[i]
    return str(hasil)

# rata-rata


def rata(jml, n):
    rata = round((int(jml)/int(n)), 3)
    return rata


try:
    # Tampilan Index
    data_file = st.file_uploader("Upload CSV", type=['csv'])
    data = exploredata(data_file.name)
    st.write("Data yang digunakan")
    st.write(data)

    jumlah = jumlah(data['Frekuensi'])
    prob = prob(jumlah, data['Frekuensi'])
    st.write("Total Frekuensi :", jumlah)
    st.write("Probabilitas :", prob)
    st.write("Probabilitas kumulatif :", kumulatif(prob))
    st.write("Batas Interval Bawah :", intvalbawah(kumulatif(prob)))
    st.write("Batas Interval Atas :", kumulatif(prob))

    st.success('Generalisasi dan Penaksiran')
    n = st.number_input('Input banyak data :', 0, 100, 0)
    ran = randnum(n)
    st.write('Angka Acak :', ran)

    permintaan = taksir(ran, kumulatif(prob))
    jmlpermintaan = jmlpermintaan(permintaan)
    jmlharga = jmlharga(total(permintaan, 3000000))

    st.write('Permintaan', taksir(ran, kumulatif(prob)))
    st.write('Asumsi harga 1 handphone Rp. 3.000.000')
    st.write('Dalam Rp. :', total(permintaan, 3000000))
    st.write('Jumlah Permintaan : ', jmlpermintaan)
    st.write('Rata-rata permintaan per minggu : ', rata(jmlpermintaan, n))
    st.write('Rata-rata Pemasukkan per minggu : Rp.', rata(jmlharga, n))

except:
    st.write("Silahkan Pilih terlebih dahulu file data yang akan digunakan !")
