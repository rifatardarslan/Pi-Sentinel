# 🛰️ Pi Sentinel — Akıllı Ev Güvenlik Sistemi (Yapay Zeka + IoT)

**Pi Sentinel**, yapay zeka (AI) ve Nesnelerin İnterneti (IoT) teknolojilerini birleştirerek düşük maliyetli, taşınabilir ve enerji verimli bir **akıllı ev güvenlik sistemi** sunar.
Sistem, **Raspberry Pi Zero 2 W** üzerinde çalışacak şekilde tasarlanmış ve hem donanım hem yazılım tarafında özelleştirilmiştir.

**PIR sensör** ile hareket algılandığında kamera otomatik olarak etkinleşir. Elde edilen görüntüler, **YOLOv8** modeliyle analiz edilerek insan, hayvan veya araç gibi nesneler tespit edilir.
İnsan algılandığında sistem, **yüz tanıma** (OpenCV + Dlib) modülünü devreye alır ve yalnızca tanımsız kişiler için güvenlik uyarısı verir.

Sistem, bulut altyapısına bağımlı olmadan tamamen **yerel** çalışır ve **SSH** üzerinden uzaktan yönetilebilir.

---

## ⚙️ Özellikler
- Gerçek zamanlı YOLOv8 nesne tespiti  
- Dlib ile yüz tanıma  
- SSH üzerinden uzaktan erişim  
- Raspberry Pi Zero 2 W için optimize edilmiş  
- Düşük güç tüketimi ve taşınabilir tasarım  
- Bulut bağımsız veri işleme  

---

## 🔧 Kurulum
```bash
pip install -r requirements.txt
python pi_sentinel.py
```

---

## 📦 Model Dosyası (Önemli ⚠️)
`yolov8n.pt` dosyası GitHub deposuna dahil edilmemiştir.  
Aşağıdaki bağlantıdan manuel olarak indirmeniz gerekmektedir:

👉 [yolov8n.pt Modelini İndir](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt)

İndirdiğiniz dosyayı `pi_sentinel.py` ile aynı klasöre yerleştirin.

```
Pi-Sentinel/
├── pi_sentinel.py
├── yolov8n.pt
├── requirements.txt
├── README.md
└── README_TR.md
```

---

## 🧪 Teknoloji Hazırlık Seviyesi (TRL)
Proje **TRL 4** seviyesindedir ve prototip düzeyinde test edilerek işlevselliği doğrulanmıştır.

---

## 🏫 Akademik Katkı
Proje, **Afyon Kocatepe Üniversitesi Proje Pazarı**’nda sergilenmiş ve yapay zeka destekli güvenlik sistemleri alanında dikkat çekici bir çözüm olarak sunulmuştur.

Bu sistem; bireysel kullanıcılar, küçük işletmeler ve akademik araştırmalar için güvenli, ekonomik ve sürdürülebilir bir alternatif sağlar.

---

## 📄 Lisans
Bu proje açık kaynaklıdır ve **MIT Lisansı** ile paylaşılmaktadır.  
Detaylar için [LICENSE](./LICENSE) dosyasına göz atabilirsiniz.
