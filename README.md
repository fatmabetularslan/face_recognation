# Gerçek Zamanlı Yüz Tanıma Uygulaması

Bu proje, gerçek zamanlı olarak kameradan alınan görüntülerde yüz tanıma işlemi gerçekleştiren bir uygulamadır. Kullanıcı tarafından yüklenen fotoğraflar tanımlanır, tanınan yüzler **yeşil çerçeve** ile işaretlenir, tanınmayan yüzler ise **kırmızı çerçeve** ile gösterilir.

---
## Özellikler
- **Yüz Tanıma**: Kullanıcı, vesikalık fotoğrafları sisteme yükler ve bu fotoğraflar tanımlanır.
- **Gerçek Zamanlı Tanıma**: Kamera akışında algılanan yüzler, yüklenen vesikalık fotoğraflarla eşleştirilir
- **Web Arayüzü**: Streamlit kullanılarak oluşturulmuş sezgisel bir arayüz sunar.
- **Yüz Etiketleme**: Tanınan yüzler için yeşil çerçeve ve isim etiketi, tanınmayan yüzler için kırmızı çerçeve ekler.
---
## Kurulum

### 1. Gerekli Kütüphanelerin Yüklenmesi

Projeyi çalıştırmak için aşağıdaki Python kütüphaneleri gereklidir:
- **Streamlit**: Web arayüzü için
- **OpenCV**: Görüntü işleme için
- **face_recognition**: Yüz tanıma işlemleri için
- **dlib**: Yüz tanıma algoritmalarının çalışması için
- **numpy**: Matematiksel işlemler için

Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install streamlit opencv-python face_recognition numpy dlib
```
---
### 2. Proje Dosyalarının Kopyalanması ###

Projeyi klonlayın veya ZIP dosyasını indirerek çıkartın:

```bash
git clone https://github.com/fatmabetularslan/face-recognition.git
cd real-time-face-recognition

```
---

### 3. Bilinen Yüzlerin Tanımlanması

- Streamlit arayüzü üzerinden fotoğraflarınızı sisteme yükleyin.
- Fotoğraf dosyalarının adı, sistemde kişi ismi olarak kullanılacaktır. Örneğin, "Betul.jpg" yüklendiğinde, bu yüz "Betul" olarak tanımlanır.

```python
photos = [
    ("images/person1.jpg", "Person1"),
    ("images/person2.png", "Person2"),
]
```
---

## Kullanım ##

### 1.Streamlit Uygulamasını Başlatın ###

Streamlit uygulamasını başlatmak için aşağıdaki komutu çalıştırın:

```python
streamlit run app.py

```
---
### 2. Kullanıcı Arayüzü ###

- Uygulama tarayıcınızda otomatik olarak açılacaktır.
- **"Fotoğraflarınızı yükleyin"** bölümünden tanımlanmasını istediğiniz kişilerin  fotoğraflarını yükleyin.
- Fotoğraflar yüklendikten sonra, "Kamerayı Başlat" düğmesine tıklayın.
- Kamera akışı sırasında yüz algılama ve eşleştirme işlemleri anlık olarak yapılır.

### 3. Kameradan Yüz Tanıma ###

- Eşleşme sağlanırsa:
    - Yüklediğiniz  fotoğraflarla eşleşen bir yüz algılanırsa, bu yüzün etrafında yeşil çerçeve görüntülenir ve fotoğraf ismi eklenir.
  
- Eşleşme sağlanamazsa:
    - Algılanan yüz sistemde kayıtlı bir fotoğrafla eşleşmezse, bu yüzün etrafında kırmızı çerçeve gösterilir ve "Unknown" etiketi eklenir.

### 4. Uygulamadan Çıkış ###

Kamera akışını sonlandırmak için tarayıcı sekmesini kapatabilirsiniz.
---
## Gereksinimler ##
- Python 3.7 veya üzeri
- Kamera (dahili veya harici)
- dlib için sisteminizde CMake ve diğer yapı araçlarının kurulu olması gerekebilir. Gerekli araçları yüklemek için dlib kurulum kılavuzu sayfasına göz atabilirsiniz.

## Örnek Çıktı ##
Aşağıdaki ekran görüntüsü uygulamanın çalışma şeklini göstermektedir:

Tanınan yüzler:

![image](https://github.com/user-attachments/assets/2964e36c-0e9c-4700-9240-14e322f8ed5c)

---

## Karar Süreci ##
Bu projede yüz tanıma için **Face Recognition** kütüphanesi tercih ettim. Bu tercihin nedeni:

- Küçük veri setlerinde hızlı ve etkili bir çözüm sunması.
- GPU desteği sayesinde işlemleri daha hızlı gerçekleştirmesi.
Gelecekte, veri seti büyütüldüğünde veya daha gelişmiş özellikler eklenmek istendiğinde **DeepFace** ile entegre edilebilir.
