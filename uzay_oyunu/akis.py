# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# Üreteçler ve veri işleme akışı

from collections.abc import Iterator
from functools import lru_cache
import time


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


def satirlari_oku(yol: str) -> Iterator[str]:
    """Dosyayı satır satır okur, boş ve # ile başlayan satırları atlar."""
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            temiz = satir.strip()
            # Boş veya yorum olan satırları atlıyoruz
            if not temiz or temiz.startswith("#"):
                continue
            yield temiz


def ayristir(satirlar: Iterator[str]) -> Iterator[tuple[str, str, int]]:
    """Satırlardan (kaynak, hedef, yakit) şeklinde demet üretir."""
    for satir in satirlar:
        parcalar = satir.split()
        kaynak = parcalar[0]
        # parcalar[1] -> ok simgesi
        hedef = parcalar[2]
        yakit = int(parcalar[3])
        yield (kaynak, hedef, yakit)


def uzun_yolculuklar(
    kayitlar: Iterator[tuple[str, str, int]], esik: int
) -> Iterator[tuple[str, str, int]]:
    """Yakıtı eşikten büyük olan yolculukları süzer."""
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield (kaynak, hedef, yakit)


def rota_sayaci(baglantilar: dict):
    """Verilen bağlantı haritasına göre rota sayısını hesaplayan önbellekli fonksiyon döndürür."""

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """Verilen gezegenden başlayıp tam adim yolculuk yapan farklı rota sayısını hesaplar."""
        if adim == 0:
            return 1

        komsu_listesi = baglantilar.get(gezegen, [])
        if not komsu_listesi:
            return 0

        return sum(rota_sayisi(komsu, adim - 1) for komsu in komsu_listesi)

    return rota_sayisi


def zamanlayici(aralik: float) -> Iterator[float]:
    """Belirtilen saniye aralığında çalışan zamanlayıcı üreteci (meşgul bekleme)."""
    sonraki = time.time() + aralik
    while True:
        simdi = time.time()
        if simdi >= sonraki:
            yield simdi
            sonraki = simdi + aralik




