# ==========================================
# 🟦 MODÜL 4: reporting.py (Karar Destek)
# ==========================================

import numpy as np
import pandas as pd

def generate_executive_report(analytics_results):
    """
    Yöneticiye özet rapor ve aksiyon önerileri sunar.
    """
    try:
        # Analytics modülünden gelen verileri al
        metrics = analytics_results['city_analysis']
        # analytics.py'de risk_cities zaten hesaplandığı için oradan çekebiliriz
        risky_regions_df = analytics_results['risk_cities']
        
        # Temel Metrikler
        top_city = metrics.index[0]
        worst_city = metrics.index[-1]
        best_month = analytics_results['monthly_trend']['TotalSales'].idxmax()
        
        # Toplam satışı analytics'ten alamazsak burada hesaplayalım (Güvenli yöntem)
        total_sales = analytics_results.get('overall_total', metrics['TotalSales'].sum())
        
        # Riskli bölgeleri liste formatına getir
        risky_regions = risky_regions_df.index.tolist()

        report = f"""
    ╔══════════════════════════════════════════════════╗
    ║      ENTERPRISE SALES INTELLIGENCE REPORT        ║
    ╚══════════════════════════════════════════════════╝

    📍 GENEL DURUM:
    - Toplam Brüt Satış: {total_sales:,.2f} TL
    - En Başarılı Şehir: {top_city}
    - En Zayıf Performans: {worst_city}
    - En Verimli Ay: {best_month}

    ⚠️ RİSK ANALİZİ:
    - Riskli Bölgeler (Ortalamanın Altı): {', '.join(risky_regions) if risky_regions else 'Yok'}

    💡 KARAR DESTEK ÖNERİSİ:
    - {top_city} bölgesindeki stokları %15 artırın ve VIP sadakat programını başlatın.
    - {risky_regions[0] if risky_regions else 'İlgili bölgeler'} için %10 indirimli kampanya kurgulayın.
    - {best_month} dönemindeki başarı modelini diğer aylara projeksiyon olarak uygulayın.
        """
        return report

    except Exception as e:
        return f"Rapor oluşturulurken bir hata oluştu: {str(e)}"

