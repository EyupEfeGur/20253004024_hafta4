# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# Bonus Görev - Meşgul Bekleme ve Zamanlayıcı

import time
from uzay_oyunu.akis import zamanlayici


def tik_tak_calistir(toplam_sure: float = 10.0) -> None:
    """10 saniye boyunca her 2 saniyede 'tik', her 5 saniyede 'tak' yazdırır."""
    baslangic = time.time()
    bitis = baslangic + toplam_sure

    hedef_tik = baslangic + 2.0
    hedef_tak = baslangic + 5.0

    print("Zamanlayıcı başlatıldı...")
    while time.time() < bitis:
        simdi = time.time()
        if simdi >= hedef_tik:
            print(f"[{simdi - baslangic:.1f}s] tik")
            hedef_tik += 2.0
        if simdi >= hedef_tak:
            print(f"[{simdi - baslangic:.1f}s] tak")
            hedef_tak += 5.0

    print("Zamanlayıcı tamamlandı.")


# ==============================================================================
# Açıklama:
# 1. Neden bu bir "meşgul bekleme"dir (busy waiting)?
#    Program while döngüsü içinde işlemciyi serbest bırakmadan sürekli olarak
#    time.time() fonksiyonunu çağırır ve şartın sağlanıp sağlanmadığını denetler.
#    Bu esnada işlemci çekirdeği %100 kapasiteyle boş döngü döndürür ve kaynak tüketir.
#
# 2. time.sleep ile farkı nedir?
#    time.sleep() fonksiyonu kullanıldığında işlem işletim sistemi seviyesinde
#    uyutulur (bloklanır). İşlemci bu süreçte hiçbir döngü harcamaz ve başka işlere
#    odaklanır. Süre dolduğunda işletim sistemi işlemi tekrar uyandırır.
# ==============================================================================


if __name__ == "__main__":
    tik_tak_calistir(10.0)
