12_PROJE_Enterprise_Sales_Intelligence_&_Decision_Support_System_Capstone

Gerçek senaryo: Bir şirketin **ham satış verilerini** alıp
- temizleyen
- dönüştüren
- analiz eden
- yönetime **karar desteği** sunan bir **mini analitik sistem** geliştiriyorsun.

## ✅ KAPSANAN TÜM KONULAR (EKSİKSİZ)

### 🔹 Python Core
- Değişkenler, int / float / string
- String metodları, slicing
- List, dict, set, tuple
- Bool, karşılaştırmalar
- if / elif / else
- for / while
- break / continue
- Fonksiyonlar, `args`
- Scope (local / global)
- try / except

### 🔹 NumPy
- Array & matrix oluşturma
- Indexing & slicing
- Matrix indexing
- Vektörel operasyonlar
- NumPy metodları
- `axis` mantığı
- `reshape`, `transpose`, `flatten`
- `np.random`

### 🔹 Pandas
- Series & DataFrame
- Index / reset / set
- Multi-index
- Eksik veriler
- GroupBy & aggregation
- Concat
- Merge
- İleri pandas operasyonlar
- Excel okuma / yazma

## 📁 GERÇEK PROJE DOSYA YAPISI
enterprise_sales_system/
│
├── data_generator.py
├── preprocessing.py
├── analytics.py
├── reporting.py
└── main.ipynb

❗ Tek dosyada yazmak yasak
❗Modüler yapı **zorunlu** 

## 📌 PROJE SENARYOSU (GERÇEK HAYAT)
Şirketin elinde:
- farklı kaynaklardan gelen satış verileri
- eksik ve bozuk kayıtlar
- farklı şehirler, ürünler ve dönemler
Ama yönetim şunu istiyor:
“Bana temiz, özet, karar aldıran bir rapor getir.”

## 🧩 MODÜLLER VE GÖREVLER

## 🟦 data_generator.py
### 🔹 Veri Simülasyonu (NumPy ağırlıklı)
- `np.random` ile:
    - müşteri ID
    - ürün
    - şehir
    - satış tutarı
    - ay bilgisi üret
- Bilerek:
    - NaN değerler koy
    - uç değerler üret
📌 Amaç:
**Gerçek hayattaki bozuk veri**

## 🟦 preprocessing.py
## 🔹 Veri Temizleme (Pandas + Python)
- Eksik verileri tespit et
- Mantıklı stratejiyle doldur / sil
- String kolonları normalize et
- Yeni sütunlar üret (KDV’li satış vb.)
- try/except ile hataya dayanıklı yap
📌 Burada:
- if
- fonksiyon
- pandas ileri işlemler zorunlu

## 🟦 analytics.py
### 🔹 Analitik Motor (NumPy + Pandas)
- NumPy ile:
    - normalize edilmiş matrisler
    - performans skorları
- Pandas ile:
    - şehir bazlı satış
    - ürün bazlı satış
    - ay bazlı trend
- GroupBy + agg yoğun kullanılır
📌 Loop YOK → vektörel düşünce

## 🟦 reporting.py
### 🔹 Karar Destek Katmanı
- En iyi / en kötü şehir
- En kârlı ürün
- Riskli bölgeler (düşük ortalama)
- Yöneticiye okunabilir özet üret
📌 Bool + if + dict + tuple kullanımı

## 🟦 main.ipynb
### 🔹 Sistem Akışı
1. Proje tanımı (Markdown)
2. Veriyi üret
3. Temizle
4. Analiz et
5. Sonuçları yazdır
6. Excel çıktısı al

Örnek çıktı:
Toplamsatış:4.820.000TL
Enkârlı şehir: İstanbul
Eniyiay:Mart
Risklibölge:DoğuAnadolu
Excelraporuoluşturuldu.
