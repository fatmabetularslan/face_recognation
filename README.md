# Gerçek Zamanlı Yüz Tanıma Uygulaması

Bu proje, gerçek zamanlı olarak kameradan alınan görüntülerde yüz tanıma işlemi gerçekleştiren bir uygulamadır. Bilinen yüzler veritabanında tanımlanmışsa, tanınan yüzler **yeşil çerçeve** ile işaretlenir, tanınmayan yüzler ise **kırmızı çerçeve** ile gösterilir.

---

## Kurulum

### 1. Gerekli Kütüphanelerin Yüklenmesi

Projeyi çalıştırmak için aşağıdaki Python kütüphaneleri gereklidir:

- **OpenCV**: Görüntü işleme için
- **face_recognition**: Yüz tanıma işlemleri için
- **dlib**: Yüz tanıma algoritmalarının çalışması için
- **numpy**: Matematiksel işlemler için

Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install opencv-python face_recognition numpy dlib
```
---
### 2. Proje Dosyalarının Kopyalanması ###

Projeyi klonlayın veya ZIP dosyasını indirerek çıkartın:

```bash
git clone https://github.com/username/real-time-face-recognition.git
cd real-time-face-recognition

```
---

### 3. Bilinen Yüzlerin Tanımlanması

**`images`** klasörüne tanımak istediğiniz kişilere ait vesikalık veya portre fotoğraflarını ekleyin. Daha sonra, fotoğrafların adını ve kişiyi `face.py` dosyasındaki şu bölüme ekleyin:

```python
photos = [
    ("images/person1.jpg", "Person1"),
    ("images/person2.png", "Person2"),
]
```
---

## Kullanım ##

### 1.Python Betiğini Çalıştırın: ###

Projeyi çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

```python
python face.py

```
---
### 2. Kameradan Yüz Tanıma: ###

- Kamera açılır ve canlı görüntüde yüzler tanınır.
- Tanınan yüzler için yeşil çerçeve ve isim gösterilir.
- Tanınmayan yüzler için kırmızı çerçeve gösterilir.

### 3. Uygulamadan Çıkış: ###

**q** tuşuna basarak uygulamayı kapatabilirsiniz.

## Gereksinimler ##
- Python 3.7 veya üzeri
- Kamera (dahili veya harici)
- dlib için sisteminizde CMake ve diğer yapı araçlarının kurulu olması gerekebilir. Gerekli araçları yüklemek için dlib kurulum kılavuzu sayfasına göz atabilirsiniz.

## Örnek Çıktı ##
Aşağıdaki ekran görüntüsü uygulamanın çalışma şeklini göstermektedir:

Tanınan yüzler:

![image](https://github.com/user-attachments/assets/2964e36c-0e9c-4700-9240-14e322f8ed5c)


