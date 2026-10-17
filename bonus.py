# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# Bonus Görev - Meşgul Bekleme ve Zamanlayıcı

import time

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




if __name__ == "__main__":
    tik_tak_calistir(10.0)
