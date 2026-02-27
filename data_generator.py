# ==========================================
# 🟦 MODÜL 1: data_generator.py
# ==========================================

def generate_sales_data(n_rows=1000):
    """
    İstatistiki dağılımlar kullanarak gerçekçi satış verisi üretir.
    """
    np.random.seed(42)

    customer_ids = np.random.randint(1000, 1100, size=n_rows)

    products = np.random.choice(
        ["Laptop", "Phone", "Tablet", "Monitor", "Accessory"],
        size=n_rows
    )

    cities = np.random.choice(
        ["Istanbul", "Ankara", "Izmir", "Bursa", "Adana"],
        size=n_rows
    )

    months = np.random.choice(
        ["January", "February", "March", "April", "May", "June"],
        size=n_rows
    )

    # 📈 Satış tutarları: Normal dağılım (Mean=5000, StdDev=2000)
    amounts = np.random.normal(loc=5000, scale=2000, size=n_rows)
    amounts = np.round(amounts, 2)

    # Negatifleri sıfıra çek (Mantıksal koruma)
    amounts[amounts < 0] = 0

    # ❗ Bilerek NaN ekle (%5 oranında)
    nan_indices = np.random.choice(n_rows, size=int(n_rows * 0.05), replace=False)
    amounts[nan_indices] = np.nan

    data = pd.DataFrame({
        "CustomerID": customer_ids,
        "Product": products,
        "City": cities,
        "Month": months,
        "Amount": amounts
    })

    return data