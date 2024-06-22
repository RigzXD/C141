from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies = movies_data[["original_title", "poster_link", "release_date", "runtime", "weighted_rating"]]

# variables to store data
liked_movies = []
not_liked_movies = []
did_not_watch = []

# method to fetch data from database
def assign_var():
  m_data = {
    "original_title" : all_movies.iloc[0,0],
    "poster_link" : all_movies.iloc[0, 1],
    "release_date" : all_movies.iloc[0,2] or "N/A",
    "duration" : all_movies.iloc[0,3],
    "rating" : all_movies.iloc[0,4]/2
  }
  return m_data

# /movies api
@app.route("/movies")
def get_movie():
  movie_data = assign_var()
  return jsonify({
    "data" : movie_data,
    "status" : "success"
  })

# /like api
@app.route("/like")
def liked_movie():
  global all_movies
  movie_data = assign_var()
  liked_movies.append(movie_data)
  all_movies.drop([0], inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    "status" : "succss"
  })

# /dislike api
@app.route("/dislike")
def disliked_movie():
  global all_movies
  movie_data = assign_var()
  not_liked_movies.append(movie_data)
  all_movies.drop([0], inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    "status" : "succss"
  })

# /did_not_watch api
@app.route("/did_not_watch")
def did_not_watch_movie():
  global all_movies
  movie_data = assign_var()
  did_not_watch.append(movie_data)
  all_movies.drop([0], inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    "status" : "succss"
  })

if __name__ == "__main__":
  app.run()