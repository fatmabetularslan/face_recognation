import cv2
import face_recognition

print("Kütüphaneler başarıyla yüklendi!")

# Yüzlerin tanımlanması
known_face_encodings = []
known_face_names = []

photos = [
    ("images/person1.jpg", "Betul"),
    ("images/person3.jpg", "emıne"),
]

# Yüzlerin yüklenmesi
for photo_path, name in photos:
    try:
        image = face_recognition.load_image_file(photo_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_face_encodings.append(encodings[0])
            known_face_names.append(name)
        else:
            print(f"Uyarı: {photo_path} içerisinde yüz algılanamadı.")
    except Exception as e:
        print(f"Hata: {photo_path} yüklenirken bir sorun oluştu: {e}")

# Kamerayı başlatma
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Kamera açılmadı!")
    exit()

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Kamera görüntüsü alınamadı.")
        break

    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Yüz algılama
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = []

    if face_locations:
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]

        # Çerçeve ve isim yazma
        top, right, bottom, left = [v * 4 for v in face_location]
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    
    cv2.imshow('Video', frame)

    # çıkış
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
