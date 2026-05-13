import streamlit as st
import pandas as pd
import pickle as pkl
import numpy as np

st.title("Movie Recommentation")
st.write("Welcome to pruthviraj chavan's project")

similarity=pkl.load(open("similarity.pkl","rb+"))
ds=pd.read_csv("cleaned_data.csv")

name=sorted(ds["Title"].unique())



def get_movie_index(Name):
    index=-1
    for i in ds.index:
        if ds.iloc[i]["Title"].lower()==Name.lower():
            index=i
            break
    return index

def get_movie_name(index):
    if index > len(ds)-1:
        return ""
    else:
        return ds.iloc[index]["Title"]
     
Name=st.text_input("Enter the movie name")
index=get_movie_index(Name)
if index ==-1:
    st.write("Soory movie not found")
else:
    st.write("Movie Found:")
    similarity_indexes=list(enumerate(similarity[index]))
    similarity_indexes=sorted(similarity_indexes,key=lambda x:x[1],reverse=True)

    if st.button("See The Recommentation:"):
       for i in range(1,6):
           st.write(str(i)+"."+get_movie_name(similarity_indexes[i][0]))    
