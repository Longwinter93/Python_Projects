#!/usr/bin/env python
# coding: utf-8

# Zadanie 1: Użycie dataclass do reprezentacji danych pogodowych
# 
# Korzystając z API OpenWeatherMap (https://openweathermap.org/api), napisz funkcję,
# która pobiera dane pogodowe (miasto, temperatura, wilgotność, ciśnienie, opis) 
# dla danego miasta i zwraca je jako instancję klasy Weather.
# 
# 
# http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric
# city ='Warsaw'
# api_key ='9ab4c99fcf3024c2feea8532c904e48b'
# http://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid=9ab4c99fcf3024c2feea8532c904e48b&units=metric

# In[ ]:


import requests
import json 
from dataclasses import dataclass, asdict
from datetime import date 
today = date.today()



def GetDataWeather(city: str) -> str:
    API_KEY = ''
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)
        
    data_json = r.json()
    
    @dataclass
    class Weather:
        country: str
        city: str
        description: str
        temperature: float 
        pressure: int 
        humidity: int 
        
    DataWeather = Weather(
        country = data_json['sys']['country'],
        city = data_json['name'],
        description = data_json['weather'][0]['description'],
        temperature = data_json['main']['temp'],
        pressure = data_json['main']['pressure'],
        humidity = data_json['main']['humidity'])
    
    DataWeatherAsDict = asdict(DataWeather)
    
    with open(f'Weather {city} {today}.json', 'w') as f:
        json.dump(DataWeatherAsDict, f)
        
    
    return DataWeatherAsDict
    


# In[2]:


print(GetDataWeather('Warsaw'))
print(GetDataWeather('London'))
print(GetDataWeather('Stockholm'))
print(GetDataWeather('Zurich'))
print(GetDataWeather('Paris'))


# Zadanie 2: Użycie dataclass do reprezentacji danych o filmie
# 
# Korzystając z tvmaze (https://www.tvmaze.com/api), napisz funkcję, która pobiera informacje o filmie
#  (tytul, typ (genres), jezyk, kiedy wyswietlany film (schedule),status,fabula (summary), network,rating_average ) na podstawie jego tytułu i zwraca je jako instancję klasy Movie.
# 
# 
# https://api.tvmaze.com/singlesearch/shows?q=batman
# https://www.tvmaze.com/shows
# 

# In[3]:


import requests
from dataclasses import dataclass, asdict
import json 
from datetime import date

def GetMoviesData(Movie: str) -> str:
    today = date.today()
    url =f'https://api.tvmaze.com/singlesearch/shows?q={Movie}'
    try:
        r = requests.get(url)
        r.raise_for_status 
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)

    DataMovie = r.json()
    
    @dataclass
    class Movies:
        Name: str
        Genres: str 
        Language: str
        Time: str 
        Days: str 
        AverageRating: float 
        
    Movies = Movies(
        Name = DataMovie['name'],
        Genres = DataMovie['genres'],
        Language = DataMovie['language'],
        Time = DataMovie['schedule']['time'],
        Days = DataMovie['schedule']['days'],
        AverageRating = DataMovie['rating']['average']
    )
    
    DictMovies= asdict(Movies)
        
    with open(f"{Movie} {today}.json", 'w') as f:
        json.dump(DictMovies, f)

    return DictMovies



# In[4]:


print(GetMoviesData('Superman & Lois'))
print(GetMoviesData('Gilmore Girls'))
print(GetMoviesData('House'))
print(GetMoviesData('The Penguin'))
print(GetMoviesData('All Creatures Great and Small'))
print(GetMoviesData('The Event'))



# Zadanie 3: Analiza częstotliwości liter w tekście
# 
# Korzystając z otwartego zbioru danych z Project Gutenberg (https://www.gutenberg.org/), napisz funkcję, 
# która analizuje częstotliwość występowania liter w tekście i zwraca je jako słownik.
# 
#  "https://www.gutenberg.org/files/1342/1342-0.txt"  # Pride and Prejudice by Jane Austen  
#  Wykorzysac lower,asicii_lowercase i counter()
#  
# import requests  
# from collections import Counter  
# import string  
# 

# In[ ]:





# Zadanie 4: Wyszukiwanie najpopularniejszych słów w tekście
# 
# Korzystając z otwartego zbioru danych z Project Gutenberg (https://www.gutenberg.org/) np.,
# napisz funkcję, która zwraca n najpopularniejszych słów w tekście.
# 
# "https://www.gutenberg.org/files/2701/2701-0.txt"  # Moby Dick by Herman Melville  
# 
# import requests  
# from collections import Counter  
# import string  
# lower(), maketrans(), translate(), most_common(), punctuation
# 

# 

# Zadanie 5: Wyszukiwanie cytowań w tekście
# 
# Korzystając z otwartego zbioru danych z korpusu Open American National Corpus (http://www.anc.org/data/oanc/), napisz funkcję, która wyszukuje i zwraca wszystkie cytowania w tekście.

# In[ ]:





# Zadanie 6: Pobieranie kursów walut
# 
# Napisz funkcję, która pobiera kursy walut z serwisu https://www.x-rates.com/ i zwraca je jako słownik.
# Np. konwersja z jednej waluty do drugiej

# In[ ]:





# Zadanie 7: Pobieranie informacji o filmach z IMDb
# 
# Napisz funkcję, która pobiera informacje o 10 najlepszych filmach na stronie https://www.imdb.com/chart/top/ i
#  zwraca je jako listę słowników. (tytul, rok, ocena)
# 

# In[ ]:





# Zadanie 7:
# Napisz funkcję, która pobiera tytuły artykułów z bloga na stronie https://blog.python.org/ i zwraca je jako listę.

# 

# Zadanie 8 
# Napisz program, który pobierze od użytkownika (funkcja input) wysokość i szerokość geograficzną, a następnie wykona request na API pogodowe. 
# Odpowiedź powinna być zmapowana na klasę Weather. Program powinien zapisać wypełnioną klasę Weather do pliku pkl pickle i zapisac w postaci JSONa z danymi: latitude: ,longitude: ,windspeed: ,temperature. Najpierw powinna zwrocic dane z URL, a nastepnie zapisac wybrane zmienne do JSON
# URL = https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m
# 
# Najpierw zrobic request API zeby zwrocic JSONA z tej strony, potem zdefiniowac klasy gdzie zapisze tego jsona za pomoca klasy Weather z danymi, nastepnie zapisac te dane w postaci JSONa.

# In[ ]:





# Zadanie 8. 
# Stworzenie aplikacji, ktora tworzy haslo i zapisuje je z odpowiednia aplikacja np. pisze sie aplikacje a nastepnie generuje sie haslo

# 

# # https://transport.opendata.ch/docs.html
# # https://gameofthronesquotes.xyz/
# 
# 
