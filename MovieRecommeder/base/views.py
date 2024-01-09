from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("movie_list1.pkl", "rb"))

def home(request):

    movies_data = pickle.load(open('movie_list1.pkl' , 'rb'))
    movies_df = pd.DataFrame(movies_data)
    movies = movies_df['title'].values
    context = {'movies':movies}
    return render(request , 'index.html' , context)

def results(request):
    selected=request.GET('mainselectedoption')
    recommendations = model.recommend(selected)
    context = {'recommendations': recommendations}

    return render(request ," results.html" , context)   