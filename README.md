📊 Enterprise Sales Intelligence System

Bu repo, gerçek dünya satış verilerini kullanarak Enterprise Sales Intelligence System geliştirilmesini içeren bir Capstone projesi niteliğindedir. Proje, ham verileri alıp temizleme → analiz etme → karar destekte rapor üretme aşamalarından geçirerek yönetim için kullanılabilir içgörüler sağlar.

📌 İçindekiler

Proje modülleri:

enterprise_sales_system/
├── data_generator.py        # Veri oluşturma ve simülasyonu
├── preprocessing.py         # Veri temizleme & hazırlama
├── analytics.py             # Analitik hesaplamalar
├── reporting.py             # Raporlama ve sonuç özetleri
└── main.ipynb               # Jupyter Notebook akışında tüm sistemi çalıştırma

🧠 Proje Amacı

Bu proje ile:

Farklı kaynaklardan gelen satış verileri işlenir,

Eksik/bozuk veriler mantıklı kriterlere göre düzeltilir,

Pandas ve NumPy kullanılarak trendler ve ilişkiler analiz edilir,

Yöneticiye karar desteği sağlayacak rapor çıkarılır.

Kısa versiyon:
📈 Bir şirketin ham satış verilerinden anlamlı, karar-verici sonuçlar üretmek.

🛠️ Kullanılan Teknolojiler

Python

Pandas & NumPy

Jupyter Notebook

(İsteğe bağlı) Excel çıktı alma

🚀 Nasıl Çalıştırılır

Repo’yu klonlayın

Python ortamınızı oluşturun (venv veya conda)

Gerekli paketleri yükleyin:

pip install -r requirements.txt

main.ipynb dosyasını çalıştırın

📦 Modül Görevleri
🔹 data_generator.py

Rastgele ama gerçek hayata benzer satış verileri üretir (müşteri, ürün, şehir, vs).

🔹 preprocessing.py

Veri temizleme: eksik değerleri doldurma, string normalize etme vb.

🔹 analytics.py

Veri üzerinden trend, toplam, şehir‑ürün bazlı satış analizi yapar.

🔹 reporting.py

Sonuçları raporlaştırır ve yönetim için özet çıkarır.

🤝 Katkıda Bulunma

Bu proje açık kaynaklıdır! İstersen:

Yeni metrikler ekleyebilirsin

Dashboard veya grafiksel raporlar geliştirebilirsin

Kod yapısını daha modüler hale getirebilirsin

📝 Lisans

Açık — dilediğin gibi kullanabilirsin!
