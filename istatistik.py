# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# uzay_oyunu.istatistik modülünden fonksiyonları içe aktarıyoruz
from uzay_oyunu.istatistik import *

if __name__ == "__main__":
    from uzay_oyunu.galaksi import veri_yukle

    g = veri_yukle()
    print("Büyük harf:", buyuk_harfli_gezegenler_map(g))
    print("En az 2 bağlantı:", baglantisi_cok_olanlar_filter(g))
    print("Toplam bağlantı:", toplam_baglanti_reduce(g))
    print("Hızlı yolculuk (90 birim):", hizli_yolculuk(90))
