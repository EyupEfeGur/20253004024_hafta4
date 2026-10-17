# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# Üreteçler ve veri işleme akışı

from collections.abc import Iterator


def fibonacci() -> Iterator[int]:
    """Sonsuz Fibonacci sayı dizisi üreten üreteç fonksiyonu."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]:
    """Her adımda yakıtı tüketim kadar azaltıp kalan miktarı üreten üreteç."""
    kalan = yakit
    while kalan > 0:
        kalan -= tuketim
        if kalan < 0:
            kalan = 0
        yield kalan
        if kalan == 0:
            break

