# 📋 Geliştirme Günlüğü — Django E-Ticaret Projesi
---
### Proje Başlangıcı
Bulut Bilişim dersi final projesi olarak **Django + AWS E-Ticaret Uygulaması** yapılmasına karar verildi.
Teknoloji stack'i belirlendi:
- Backend: Python / Django
- Veritabanı: PostgreSQL (AWS RDS)
- Bulut: AWS (EC2, RDS, Auto Scaling, Elastic Load Balancer)

## 26 Mayıs 2026 — 12:20
  
#### 1.Geliştirme Ortamı Kurulumu
#### 2.Django Projesi Oluşturuldu
#### 3.Veritabanı Modelleri Yazıldı
- **Category** — Ürün kategorilerini tutar
- **Product** — Ürün adı, açıklama, fiyat, stok ve görsel bilgilerini tutar
- **Order** — Müşteri sipariş bilgilerini tutar
- **OrderItem** — Siparişe ait ürün kalemlerini tutar
Migration'lar oluşturulup uygulandı:
#### 4.Sayfalar ve URL Yapısı Oluşturuldu
`store/views.py` dosyasına şu view'lar eklendi:
- `home` — Tüm ürünleri listeler
- `product_detail` — Seçilen ürünün detayını gösterir
`store/urls.py` ve `core/urls.py` dosyaları yapılandırıldı.
#### 5.Template'ler Hazırlandı
#### 6.Admin Paneli Yapılandırıldı
