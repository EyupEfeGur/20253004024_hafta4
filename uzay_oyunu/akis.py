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
