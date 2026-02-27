# ==========================================
# 🟦 MODÜL 3: analytics.py (Analiz Motoru)
# ==========================================

import numpy as np 
import pandas as pd 

def run_analytics(df):
    """
    Temizlenmiş satış verisi üzerinden analitik çıktılar üretir.
    Loop kullanılmaz. Vektörel operasyonlar zorunludur.
    """
    try:
        df = df.copy()

        # -------------------------------------------------
        # 1️⃣ NumPy – Normalize Edilmiş Performans Skoru
        # -------------------------------------------------
        amount_array = df["Amount"].values
        min_val = np.min(amount_array)
        max_val = np.max(amount_array)

        if max_val - min_val == 0:
            df["PerformanceScore"] = 0
        else:
            normalized = (amount_array - min_val) / (max_val - min_val)
            df["PerformanceScore"] = np.round(normalized * 100, 2)

        # -------------------------------------------------
        # 2️⃣ Şehir Bazlı Satış Analizi (Named Aggregation)
        # -------------------------------------------------
        city_analysis = (
            df.groupby("City")
              .agg(
                  TotalSales=("Amount", "sum"),
                  AvgSales=("Amount", "mean"),
                  TransactionCount=("Amount", "count")
              )
              .sort_values(by="TotalSales", ascending=False)
        )

        # -------------------------------------------------
        # 3️⃣ Ürün Bazlı Analiz
        # -------------------------------------------------
        product_analysis = (
            df.groupby("Product")
              .agg(
                  TotalSales=("Amount", "sum"),
                  AvgSales=("Amount", "mean")
              )
              .sort_values(by="TotalSales", ascending=False)
        )

        # -------------------------------------------------
        # 4️⃣ Ay Bazlı Trend
        # -------------------------------------------------
        monthly_trend = (
            df.groupby("Month")
              .agg(TotalSales=("Amount", "sum"))
              .sort_values(by="TotalSales", ascending=False)
        )

        # -------------------------------------------------
        # 5️⃣ Riskli Bölgeler (Düşük Ortalama)
        # -------------------------------------------------
        overall_avg = df["Amount"].mean()
        risk_cities = city_analysis[city_analysis["AvgSales"] < overall_avg]

        return {
            "city_analysis": city_analysis,
            "product_analysis": product_analysis,
            "monthly_trend": monthly_trend,
            "risk_cities": risk_cities,
            "processed_df": df
        }

    except Exception as e:
        print("Analytics sırasında hata oluştu:", e)
        return None