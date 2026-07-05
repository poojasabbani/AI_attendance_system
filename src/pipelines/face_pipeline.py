import dlib 
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
    detector=dlib.get_frontal_face_detector()

    sp=dlib.shape_pedictor(
        face_recognition_models.pose_predictor_model_location()
    )


    face_recognizer = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector,sp,face_recognizer

def get_face_embeddings(image_np):
    detector,sp,facerec=load_dlib_models()

    faces=detector(image_np,1) #finds the faces in the image
    encoding=[]
    for face in faces:
        shape=sp(image_np,face) #predicts facial landings=>68 landmarks
        face_descriptor=facerec.computer_face_descriptor(image_np,shape,1)#trained resNet model to get 128 embeddings  
        encoding.append(np.array(face_descriptor))
    return encoding

@st.cache_resource
def get_trained_model():
    X=[]
    Y=[]

    student_db = get_all_students()

    if not student_db:
        return None
    for student in student_db:
        embedding=student.get("face_embedding")
        if embedding:
            X.append(np.array(embedding))
            Y.append(student.get['student_id'])
    if len(X)==0:
        return None
    
    clf=SVC(kernel="Linear",probability=True,class_weight="balanced")

    try:
        clf.fit(X,Y)
    except ValueError:
        pass
    return {'clf':clf,'X':X,'Y':Y}

    def train_classifier():
        st.cache_resource.clear()
        model_data=get_trained_model()
        return bool(model_data)
    
    
    def predict_attendance(class_image_np):
        encodings=get_face_embeddings(class_image_np)

        detected_students={}

        model_data=get_trained_model()
        if not model_data:
            return detected_students,[],len(encodings)
        
        clf=model_data['clf']
        X_train=model_data['X']
        Y_train=model_data['Y']

        all_students=sorted(list(set(y_train)))

        for encoding in encodings:
            if len(all_students)>=2:
                predicted_id=int(clf.predict([encoding])[0])
            else:
                predicted_id=int(all_students[0])

            student_embedding=X_train[Y_train.index(predicted_id)]
            best_match_score=np.linalg(student_embeddings-encoding)
            resemblance_threshold=0.6

            if best_match_score<=resemblance_threshold:
                detected_student[predicted_id] = True
        return detected_student,all_students,len(encodings)