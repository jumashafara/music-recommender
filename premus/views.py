from copyreg import pickle
from django.shortcuts import render
import joblib
from pathlib import Path


def index(request):
    return render(request, "base.html", {"prediction": "None"})


def prediction(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    premus = joblib.load(BASE_DIR / "premus/premus.joblib")
    gender, age = request.POST["gender"], request.POST["age"]
    prediction = premus.predict([[age, gender]])
    settings = {"gender": gender, "age": age}
    return render(request, "base.html", {"prediction": prediction[0], "settings": settings})
