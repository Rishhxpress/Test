import pandas as pd
xl_data = pd.read_excel('movie.xlsx')
data = pd.DataFrame(xl_data, columns='movie_name','movie_rating', 'movie_release', 'movie_duration','movie_desc')