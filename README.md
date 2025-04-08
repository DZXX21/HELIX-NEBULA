# The Hacker News Özetleyici

Bu proje, The Hacker News (https://thehackernews.com/) sitesinden en son siber güvenlik haberlerini çeker ve Google Gemini API kullanarak bu haberleri Türkçe olarak özetler. Her haber tek tek işlenir ve özetleme istekleri arasında 10 saniye beklenir, böylece API kota sınırlarına daha az yük bindirilir.

## Özellikler
- The Hacker News anasayfasından 5 haber çeker.
- Her haberin başlığını, URL'sini ve içeriğini alır.
- Google Gemini API ile haber içeriklerini Türkçe özetler.
- Her özetleme isteği arasında 10 saniye bekler.

## Gereksinimler
- Python 3.12 veya üstü
- Gerekli kütüphaneler:
  - `requests`
  - `beautifulsoup4`
  - `google-generativeai`
- Geçerli bir Google Gemini API anahtarı (kodda `GEMINI_API_KEY` olarak ayarlanır).

## Kurulum
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install requests beautifulsoup4 google-generativeai
   ```
2. Google Cloud Console'dan bir Gemini API anahtarı alın ve kodda `GEMINI_API_KEY` değişkenine ekleyin.
3. Kodu bir dosyaya kaydedin (örneğin `thehackernews_gemini_slow_fetcher.py`).

## Kullanım
Terminalde şu komutu çalıştırın:
```bash
python thehackernews_gemini_slow_fetcher.py
```
- Kod, 5 haberi çeker ve her birini özetleyerek ekrana yazar.
- Her haber arasında 10 saniye bekler.

## Örnek Çıktı
```
The Hacker News'ten Haberler ve Özetler:
======================================================================
1. Başlık: CISA and FBI Warn Fast Flux
   URL: https://thehackernews.com/2025/04/cisa-and-fbi-warn-fast-flux-is-powering.html
   Özet: CISA ve FBI, fast flux tekniğinin kötü amaçlı ağları gizlediğini belirtti.
======================================================================
10 saniye bekleniyor...
```

## Notlar
- **Kota Sorunu:** Gemini API ücretsiz kotasını aşarsanız `429 ResourceExhausted` hatası alabilirsiniz. Google Cloud'da faturalandırmayı etkinleştirerek bu sorunu çözebilirsiniz.
- **Hata Durumu:** Özetleme başarısız olursa, hata mesajı ekrana yazılır.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
