# İleri Python Programlama - Hafta 4 Lab Ödevi

**Ad :** Eyüp Efe  
**Soyad :** GÜR  
**Numara :** 20253004024  
**Bölüm :** Bilişim Sistemleri ve Teknolojileri  
**Ders :** İleri Python Programlama  
**Öğretim Üyesi :** Dr. Öğr. Üyesi Murat Emeç  
**GitHub Deposu :** https://github.com/EyupEfeGur/20253004024_hafta4  

---

### Açıklama
Bu laboratuvar ödevinde uzay oyunu projesine sonsuz Fibonacci üreteci, yakıt tüketim göstergesi üreteci, dosya okuma ve filtreleme yapan üreteç tabanlı veri işleme boru hattı, `@lru_cache` destekli önbellekli rota hesaplayıcı ve `map`/`filter`/`reduce`/`partial` fonksiyonel araçları eklenmiştir.

---

### Görev 4: Önbellek Performans Ölçümü (adim=20)

Dünya gezegeninden başlayıp 20 adım yolculuk yapan rota sayısı hesaplanarak önbelleksiz ve `@lru_cache` önbellekli sürümler `time.perf_counter()` ile test edilmiştir.

- **Hesaplanan Rota Sayısı:** 22.456.663
- **Önbelleksiz Süre:** 7.944842 saniye
- **Önbellekli Süre:** 0.000099 saniye
- **`cache_info()` Çıktısı:** `CacheInfo(hits=110, misses=98, maxsize=None, currsize=98)`

> **Değerlendirme:** Önbelleksiz sürümde aynı gezegen ve adım ikilisi binlerce kez tekrar hesaplandığı için süre ~8 saniyeyi bulmaktadır. `@lru_cache` ile hesaplanan değerler saklandığı için arama süresi mikrosaniyelere inmiş ve yaklaşık 80.000 katlık bir hız artışı elde edilmiştir.
