import joblib
model=joblib.load('student_marks_prediction.pkl')
n=int(input("How many study Hours"))
print("predicted marks= ",model.predict([[n]])[0][0].round(2))