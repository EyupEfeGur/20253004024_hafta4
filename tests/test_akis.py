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

