# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# Akış ve üreteç fonksiyonlarının birim testleri

import itertools
import pytest
from uzay_oyunu.akis import fibonacci


def test_fibonacci_next():
    """next() fonksiyonu ile ilk üç elemanın doğru üretildiğini test ediyoruz."""
    g = fibonacci()
    assert (next(g), next(g), next(g)) == (0, 1, 1)


def test_fibonacci_islice():
    """itertools.islice ile ilk 12 elemanın alındığını test ediyoruz."""
    sonuc = list(itertools.islice(fibonacci(), 12))
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert sonuc == beklenen


def test_fibonacci_takewhile():
    """itertools.takewhile ile 100'den küçük elemanların alındığını test ediyoruz."""
    sonuc = list(itertools.takewhile(lambda x: x < 100, fibonacci()))
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert sonuc == beklenen


def test_fibonacci_tek_kullanimlik():
    """Aynı üreteçten ikinci kez çekildiğinde kaldığı yerden devam ettiğini test ediyoruz."""
    g = fibonacci()
    ilk_bes = list(itertools.islice(g, 5))
    ikinci_bes = list(itertools.islice(g, 5))

    assert ilk_bes == [0, 1, 1, 2, 3]
    assert ikinci_bes == [5, 8, 13, 21, 34]
    assert ilk_bes != ikinci_bes


def test_yakit_gostergesi():
    """PDF'teki ornek ciktinin dogrulugunu test ediyoruz: 100, 30 -> [70, 40, 10, 0]."""
    from uzay_oyunu.akis import yakit_gostergesi

    sonuc = list(yakit_gostergesi(100, 30))
    assert sonuc == [70, 40, 10, 0]


def test_yakit_gostergesi_stop_iteration():
    """Yakit sifira ulastiginda StopIteration hatasi verdigini test ediyoruz."""
    from uzay_oyunu.akis import yakit_gostergesi

    g = yakit_gostergesi(20, 10)
    assert next(g) == 10
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)


def test_seyir_defteri_toplam_yakit():
    """Boru hattindan gecen yolculuklarin toplam yakitini test ediyoruz (88 olmali)."""
    import os
    from uzay_oyunu.akis import ayristir, satirlari_oku

    dosya_yolu = os.path.join("veri", "seyir.txt")
    toplam = sum(y for _, _, y in ayristir(satirlari_oku(dosya_yolu)))
    assert toplam == 88


def test_seyir_defteri_uzun_yolculuklar():
    """Esik degeri 10'dan buyuk hedeflerin dogru suzuldugunu test ediyoruz."""
    import os
    from uzay_oyunu.akis import ayristir, satirlari_oku, uzun_yolculuklar

    dosya_yolu = os.path.join("veri", "seyir.txt")
    kayitlar = ayristir(satirlari_oku(dosya_yolu))
    hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert hedefler == ["sirius", "centauri", "orion", "kara_delik"]


def test_satirlari_oku_tembel():
    """satirlari_oku fonksiyonunun liste degil bir uretec dondurdugunu test ediyoruz."""
    import inspect
    from uzay_oyunu.akis import satirlari_oku

    g = satirlari_oku("veri/seyir.txt")
    assert inspect.isgenerator(g)


def test_rota_sayaci():
    """Onbellekli rota sayaci fonksiyonunu ve cache_info ozelligini test ediyoruz."""
    from uzay_oyunu.akis import rota_sayaci
    from uzay_oyunu.galaksi import veri_yukle

    g = veri_yukle()
    say = rota_sayaci(g["baglantilar"])

    # 0 adimda bulunulan yerde 1 rota vardir
    assert say("dünya", 0) == 1
    # 1 adimda dunya -> [centauri, sirius] = 2 rota
    assert say("dünya", 1) == 2
    # 3 adimda 15 rota
    assert say("dünya", 3) == 15
    # kara delikten baglanti olmadigi icin 0 rota
    assert say("kara_delik", 1) == 0

    # Onbellek (lru_cache) calisiyor mu kontrol ediyoruz
    bilgi = say.cache_info()
    assert hasattr(bilgi, "hits")
    assert hasattr(bilgi, "misses")


def test_istatistik_buyuk_harfler():
    """Gezegen adlarinin buyuk harfe cevrilmesini iki yontemle test ediyoruz."""
    from uzay_oyunu.galaksi import veri_yukle
    from uzay_oyunu.istatistik import (
        buyuk_harfli_gezegenler_comprehension,
        buyuk_harfli_gezegenler_map,
    )

    g = veri_yukle()
    sonuc_map = buyuk_harfli_gezegenler_map(g)
    sonuc_comp = buyuk_harfli_gezegenler_comprehension(g)

    assert sonuc_map == sonuc_comp
    assert "DÜNYA" in sonuc_map
    assert "SIRIUS" in sonuc_map


def test_istatistik_baglanti_filtreleme():
    """En az 2 baglantisi olan gezegenlerin filtrelenmesini test ediyoruz."""
    from uzay_oyunu.galaksi import veri_yukle
    from uzay_oyunu.istatistik import (
        baglantisi_cok_olanlar_comprehension,
        baglantisi_cok_olanlar_filter,
    )

    g = veri_yukle()
    sonuc_filter = baglantisi_cok_olanlar_filter(g, 2)
    sonuc_comp = baglantisi_cok_olanlar_comprehension(g, 2)

    assert sonuc_filter == sonuc_comp
    # kara delik haric diger 4 gezegenin baglantisi >= 2'dir
    assert "kara_delik" not in sonuc_filter
    assert "dünya" in sonuc_filter


def test_istatistik_toplam_baglanti():
    """Toplam baglanti sayisini reduce ve sum ile test ediyoruz."""
    from uzay_oyunu.galaksi import veri_yukle
    from uzay_oyunu.istatistik import (
        toplam_baglanti_reduce,
        toplam_baglanti_sum,
    )

    g = veri_yukle()
    sonuc_reduce = toplam_baglanti_reduce(g)
    sonuc_sum = toplam_baglanti_sum(g)

    assert sonuc_reduce == sonuc_sum
    assert sonuc_reduce == 11


def test_hizli_yolculuk_partial():
    """functools.partial ile turetilen hizli_yolculuk fonksiyonunu test ediyoruz."""
    from uzay_oyunu.istatistik import hizli_yolculuk

    assert hizli_yolculuk.keywords == {"hiz": 3}
    # 90 birim mesafe hiz=3 ile 30 birim sure surer
    assert hizli_yolculuk(90) == 30.0




