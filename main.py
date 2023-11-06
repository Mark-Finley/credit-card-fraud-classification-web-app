import streamlit as st
import numpy as np
import pickle 

# Path to the file for saving user feedback
feedback_file_path = "C:/Users/Hailey/Documents/CodeEnv/credit-card-fraud-detection/webapp/feedback.txt"  
# path to model - Logistic Regression
lr_model_file_path ='C:/Users/Hailey/Documents/CodeEnv/credit-card-fraud-detection/credit-card-fraud-classification-webapp/trained_model.sav' 
# path to model - Random Forest
rf_model_file_path ='C:/Users/Hailey/Documents/CodeEnv/credit-card-fraud-detection/credit-card-fraud-classification-webapp/trained_model.pkl' 
# path to model - SVM
svm_model_file_path ='C:/Users/Hailey/Documents/CodeEnv/credit-card-fraud-detection/' 
# path to model - KNN
knn_model_file_path ='C:/Users/Hailey/Documents/CodeEnv/credit-card-fraud-detection/'


def app():
    st.title('Credit Card Fraud Detection')
    st.write('''
        This is the Credit Card Fraud Detection app created in Streamlit using the
        [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud) dataset.
        ''')
    st.write('This app predicts the probability of a credit card transaction being fraudulent or not.')
        # st.write('Please select a specific machine learning algorithm from the sidebar to get started!')

    st.sidebar.title('Select Machine Learning Algorithm')
    st.sidebar.write('Please select a machine learning algorithm from the following options:')
    ml_algorithm = st.sidebar.selectbox('ML Algorithm', ('Logistic Regression','Random Forest', 'SVM', 'KNN')) 

    if ml_algorithm == 'Random Forest':    
        #getting the input data of the user
        st.write('Selected Algorithm: Random Forest')
        time_call =st.text_input("Time in Seconds")
        v1 =st.text_input("V1")
        v2 =st.text_input("V2")
        v3 =st.text_input("V3")
        v4 =st.text_input("V4")
        v5 =st.text_input("V5")
        v6 =st.text_input("V6")
        v7 =st.text_input("V7")
        v8 =st.text_input("V8")
        v9 =st.text_input("V9")
        v10 =st.text_input("V10")
        v11 =st.text_input("V11")
        v12 =st.text_input("V12")
        v13 =st.text_input("V13")
        v14 =st.text_input("V14")   
        v15 =st.text_input("V15")
        v16 =st.text_input("V16")
        v17 =st.text_input("V17")
        v18 =st.text_input("V18")
        v19 =st.text_input("V19")
        v20 =st.text_input("V20")
        v21 =st.text_input("V21")
        v22 =st.text_input("V22")
        v23 =st.text_input("V23")
        v24 =st.text_input("V24")
        v25 =st.text_input("V25")
        v26 =st.text_input("V26")
        v27 =st.text_input("V27")
        v28 =st.text_input("V28")
        amount =st.text_input("Transaction Amount")
    elif(ml_algorithm == 'Logistic Regression'):
        st.write('Selected Algorithm: Logistic Regression')
        time_call =st.text_input("Time in Seconds")
        v1 =st.text_input("V1")
        v2 =st.text_input("V2")
        v3 =st.text_input("V3")
        v4 =st.text_input("V4")
        v5 =st.text_input("V5")
        v6 =st.text_input("V6")
        v7 =st.text_input("V7")
        v8 =st.text_input("V8")
        v9 =st.text_input("V9")
        v10 =st.text_input("V10")
        v11 =st.text_input("V11")
        v12 =st.text_input("V12")
        v13 =st.text_input("V13")
        v14 =st.text_input("V14")   
        v15 =st.text_input("V15")
        v16 =st.text_input("V16")
        v17 =st.text_input("V17")
        v18 =st.text_input("V18")
        v19 =st.text_input("V19")
        v20 =st.text_input("V20")
        v21 =st.text_input("V21")
        v22 =st.text_input("V22")
        v23 =st.text_input("V23")
        v24 =st.text_input("V24")
        v25 =st.text_input("V25")
        v26 =st.text_input("V26")
        v27 =st.text_input("V27")
        v28 =st.text_input("V28")
        amount =st.text_input("Transaction Amount")
    elif(ml_algorithm == 'SVM'):
        st.write('Selected Algorithm: SVM')
        time_call =st.text_input("Time in Seconds")
        v1 =st.text_input("V1")
        v2 =st.text_input("V2")
        v3 =st.text_input("V3")
        v4 =st.text_input("V4")
        v5 =st.text_input("V5")
        v6 =st.text_input("V6")
        v7 =st.text_input("V7")
        v8 =st.text_input("V8")
        v9 =st.text_input("V9")
        v10 =st.text_input("V10")
        v11 =st.text_input("V11")
        v12 =st.text_input("V12")
        v13 =st.text_input("V13")
        v14 =st.text_input("V14")   
        v15 =st.text_input("V15")
        v16 =st.text_input("V16")
        v17 =st.text_input("V17")
        v18 =st.text_input("V18")
        v19 =st.text_input("V19")
        v20 =st.text_input("V20")
        v21 =st.text_input("V21")
        v22 =st.text_input("V22")
        v23 =st.text_input("V23")
        v24 =st.text_input("V24")
        v25 =st.text_input("V25")
        v26 =st.text_input("V26")
        v27 =st.text_input("V27")
        v28 =st.text_input("V28")
        amount =st.text_input("Transaction Amount")
    elif(ml_algorithm == 'KNN'):
        st.write('Selected Algorithm: KNN')
        time_call =st.text_input("Time in Seconds")
        v1 =st.text_input("V1")
        v2 =st.text_input("V2")
        v3 =st.text_input("V3")
        v4 =st.text_input("V4")
        v5 =st.text_input("V5")
        v6 =st.text_input("V6")
        v7 =st.text_input("V7")
        v8 =st.text_input("V8")
        v9 =st.text_input("V9")
        v10 =st.text_input("V10")
        v11 =st.text_input("V11")
        v12 =st.text_input("V12")
        v13 =st.text_input("V13")
        v14 =st.text_input("V14")   
        v15 =st.text_input("V15")
        v16 =st.text_input("V16")
        v17 =st.text_input("V17")
        v18 =st.text_input("V18")
        v19 =st.text_input("V19")
        v20 =st.text_input("V20")
        v21 =st.text_input("V21")
        v22 =st.text_input("V22")
        v23 =st.text_input("V23")
        v24 =st.text_input("V24")
        v25 =st.text_input("V25")
        v26 =st.text_input("V26")
        v27 =st.text_input("V27")
        v28 =st.text_input("V28")
        amount =st.text_input("Transaction Amount")


    def FraudPrediction(input_data):
        #changing the input data to numpy array
        input_data_as_numpy_array=np.asarray(input_data)
        #reshape the array as we are predicting for one instance
        input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

        if(ml_algorithm == 'Random Forest'):
            loaded_model=pickle.load(open(rf_model_file_path,'rb'))
            prediction=loaded_model.predict(input_data_reshaped)
        elif(ml_algorithm == 'Logistic Regression'):
            loaded_model=pickle.load(open(lr_model_file_path,'rb'))
            prediction=loaded_model.predict(input_data_reshaped)
        elif(ml_algorithm == 'SVM'):
            loaded_model=pickle.load(open(svm_model_file_path,'rb'))
            prediction=loaded_model.predict(input_data_reshaped)
        elif(ml_algorithm == 'KNN'):
            loaded_model=pickle.load(open(knn_model_file_path,'rb'))
            prediction=loaded_model.predict(input_data_reshaped) 
        print(prediction)
        if(prediction[0]==0):
            return 'You are not Fraud'
        else:
            return 'Sorry, You are Fraud'


    #code for prediction
    fraud=''

    #creating a button for prediction
    if st.button('Fraud Prediction Result'):
        fraud=FraudPrediction([float(time_call), float(v1), float(v2), float(v3), float(v4), float(v5), float(v6), float(v7), float(v8), float(v9), float(v10), float(v11), float(v12), float(v13), float(v14), float(v15), float(v16), float(v17), float(v18), float(v19), float(v20), float(v21), float(v22), float(v23), float(v24), float(v25), float(v26), float(v27), float(v28), float(amount)])

    st.success(fraud)

#function to take user feedback
def feedback():
    st.header("User Feedback")
    user_feedback = st.text_area("Enter your feedback here:")
    if st.button("Submit Feedback"):
        with open(feedback_file_path, "a") as feedback_file:
            feedback_file.write(user_feedback + "\n")
        st.success("Feedback submitted successfully!")

app()
feedback()