# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# map, filter, reduce ve partial fonksiyonları

from functools import partial, reduce


# 1. Soru: Gezegen adlarının büyük harfli listesi
def buyuk_harfli_gezegenler_map(galaksi: dict) -> list[str]:
    """map() kullanarak gezegen adlarını büyük harfe dönüştürür."""
    return list(map(lambda g: g.upper(), galaksi["gezegenler"]))


def buyuk_harfli_gezegenler_comprehension(galaksi: dict) -> list[str]:
    """Liste üreteci kullanarak gezegen adlarını büyük harfe dönüştürür."""
    return [g.upper() for g in galaksi["gezegenler"]]


# 2. Soru: En az iki bağlantısı olan gezegenler
def baglantisi_cok_olanlar_filter(galaksi: dict, esik: int = 2) -> list[str]:
    """filter() kullanarak en az iki bağlantısı olan gezegenleri süzer."""
    return list(
        filter(
            lambda g: len(galaksi["baglantilar"].get(g, [])) >= esik,
            galaksi["gezegenler"],
        )
    )


def baglantisi_cok_olanlar_comprehension(galaksi: dict, esik: int = 2) -> list[str]:
    """Liste üreteci kullanarak en az iki bağlantısı olan gezegenleri süzer."""
    return [
        g
        for g in galaksi["gezegenler"]
        if len(galaksi["baglantilar"].get(g, [])) >= esik
    ]


# 3. Soru: Toplam bağlantı sayısı
def toplam_baglanti_reduce(galaksi: dict) -> int:
    """reduce() fonksiyonu ile toplam bağlantı sayısını hesaplar."""
    baglantilar = galaksi["baglantilar"]
    return reduce(lambda toplam, g: toplam + len(baglantilar[g]), baglantilar, 0)


def toplam_baglanti_sum(galaksi: dict) -> int:
    """sum() ve üreteç ifadesi ile toplam bağlantı sayısını hesaplar."""
    return sum(len(b) for b in galaksi["baglantilar"].values())


# Yolculuk ve partial fonksiyonu
def yolculuk(mesafe: int, hiz: int = 1) -> float:
    """Verilen mesafe ve hız değerine göre süreyi hesaplar."""
    return mesafe / hiz


# functools.partial ile hiz=3 sabit hızlı yolculuk fonksiyonu
hizli_yolculuk = partial(yolculuk, hiz=3)


# Yorum:
# Liste üreteçleri (list comprehension) ve sum() kullanımı, map/filter/reduce'a göre
# Python'da çok daha okunaklı ve pratik. Özellikle lambda fonksiyonları arttıkça
# kodun okunabilirliği düşüyor; liste üreteçlerinde ise neyin dönüştürüldüğü ve
# hangi şarta göre filtrelendiği tek bir satırda çok daha net anlaşılıyor.


if __name__ == "__main__":
    try:
        from uzay_oyunu.galaksi import veri_yukle
    except ModuleNotFoundError:
        from galaksi import veri_yukle

    g = veri_yukle()
    print("Büyük harfli (map):", buyuk_harfli_gezegenler_map(g))
    print("Büyük harfli (comp):", buyuk_harfli_gezegenler_comprehension(g))
    print("En az 2 bağlantı (filter):", baglantisi_cok_olanlar_filter(g))
    print("En az 2 bağlantı (comp):", baglantisi_cok_olanlar_comprehension(g))
    print("Toplam bağlantı (reduce):", toplam_baglanti_reduce(g))
    print("Toplam bağlantı (sum):", toplam_baglanti_sum(g))
    print("Hızlı yolculuk süresi (mesafe=90):", hizli_yolculuk(90))
