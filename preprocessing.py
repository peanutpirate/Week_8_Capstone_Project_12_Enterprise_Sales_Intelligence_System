# ==========================================
# 🟦 MODÜL 2: preprocessing.py (Temizleme)
# ==========================================

import numpy as np
import pandas as pd
import os

def preprocess_data(df):
    """
    Pandas ve Python Core kullanarak veriyi temizler ve normalize eder.
    """
    try:
        df_clean = df.copy()

        # 1. Eksik Veri: Amount boş olanları medyan ile doldur
        df_clean['Amount'] = df_clean['Amount'].fillna(df_clean['Amount'].median())

        # 2. String Normalizasyonu (Veri Tutarlılığı)
        # Şehir isimlerini standartlaştırır (örn: istanbul -> Istanbul)
        df_clean['City'] = df_clean['City'].str.capitalize()
        # Ürün isimlerindeki gereksiz boşlukları temizler (örn: " Laptop " -> "Laptop")
        df_clean['Product'] = df_clean['Product'].str.strip()

        # 3. KDV'li Sütun Üretimi (%20 Güncel KDV)
        df_clean['Amount_With_KDV'] = np.round(df_clean['Amount'] * 1.20, 2)

        return df_clean
    except Exception as e:
        print(f"Preprocessing Hatası: {e}")
        return None

