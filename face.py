import streamlit as st
import cv2
import face_recognition
import numpy as np

st.title("Gerçek Zamanlı Yüz Tanıma Uygulaması")

# Bilinen yüzlerin tanımlanması
known_face_encodings = []
known_face_names = []

# Kullanıcının görseller yüklemesine izin ver
uploaded_files = st.file_uploader(
    "Tanımak istediğiniz kişilerin resimlerini yükleyin", 
    type=["jpg", "jpeg", "png"], 
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            image = face_recognition.load_image_file(uploaded_file)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_face_encodings.append(encodings[0])
                # Dosya adını (uzantısı olmadan) kişinin ismi olarak kullanma
                name = uploaded_file.name.rsplit('.', 1)[0]
                known_face_names.append(name)
            else:
                st.warning(f"{uploaded_file.name} dosyasında yüz algılanamadı.")
        except Exception as e:
            st.error(f"{uploaded_file.name} yüklenirken bir hata oluştu: {e}")

    st.success("Yüzler başarıyla yüklendi. Kamerayı başlatabilirsiniz!")

# Kamera akışını başlat
if st.button("Kamerayı Başlat"):
    # OpenCV kullanarak video yakalama
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        st.error("Kamera açılamadı!")
    else:
        st.write("Kamerayı kapatmak için pencereyi kapatın veya 'q' tuşuna basın.")

        # Streamlit'te video akışını göstermek için bir döngü
        frame_placeholder = st.empty()

        while True:
            ret, frame = video_capture.read()
            if not ret:
                st.error("Kamera görüntüsü alınamadı!")
                break

            # Çerçeveyi işleme
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            # Yüz tanıma
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

                # Çerçeve ve isim ekleme
                top, right, bottom, left = [v * 4 for v in face_location]
                color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
                cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Streamlit'te görüntü gösterme
            frame_placeholder.image(frame, channels="BGR")

            # Çıkış için 'q' tuşuna basma kontrolü
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()
