
# IP Analiz Aracı 🔍

Bu Python aracı, yerel makinenizin veya dışarıdan girilen bir IPv4 adresinin sınıfını, ağ adresini, subnet maskesini ve host kapasitesini analiz eder. Ayrıca ağın alt ağlara (subnet) bölünüp bölünemeyeceğini hesaplar.

## Özellikler
* **Otomatik IP Algılama:** Yerel makinenizin IP adresini (eth0/wlan0) otomatik çeker.
* **Sınıf Analizi:** A, B ve C sınıfı IP adreslerini tanımlar.
* **Detaylı Bilgi:** CIDR, Broadcast adresi ve toplam kullanılabilir host sayısını gösterir.
* **Alt Ağ Hesaplama:** Mevcut ağın bölünebilirlik durumunu kontrol eder.

## Kurulum

1. Projeyi klonlayın:
   ```bash
   git clone 
   cd ip-analiz
