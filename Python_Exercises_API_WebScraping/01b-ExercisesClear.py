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
# api_key =''
# http://api.openweathermap.org/data/2.5/weather?q=&appid=&units=metric

# In[1]:


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
# 

# In[5]:


import requests
import string 
from collections import Counter

ExampleText = 'of her affection.”\r\n\r\n“and your assurance of it, i suppose, carried immediate convic12331232WQ$!##$!!@#'
ExampleText = ExampleText.lower() 
print(ExampleText)
print(string.ascii_lowercase)
LetterInText = [char for char in ExampleText]
print(LetterInText)
OnlyAsciiLowerCaseLetterInText = [char for char in ExampleText if char in string.ascii_lowercase]
print(OnlyAsciiLowerCaseLetterInText)
CounterChars = Counter(OnlyAsciiLowerCaseLetterInText)
DictCounterChars = dict(CounterChars)
print(DictCounterChars)


# In[6]:


def GetFrequencyOfLettersInText(url: str) -> dict:
    try:
        r = requests.get(url)
        r.raise_for_status 
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)
    Text = r.text.lower()
    OnlyAsciiLowerCaseLetterInText = [char for char in Text if char in string.ascii_lowercase]
    CounterCharInText = Counter(OnlyAsciiLowerCaseLetterInText)
    DictCounterCharInText = dict(CounterCharInText)
    
    return DictCounterCharInText
    


# In[7]:


print(GetFrequencyOfLettersInText('https://www.gutenberg.org/files/1342/1342-0.txt'))
print(GetFrequencyOfLettersInText('https://www.gutenberg.org/files/74775/74775-0.txt'))
print(GetFrequencyOfLettersInText('https://www.gutenberg.org/files/74770/74770-0.txt'))


# Zadanie 4: Wyszukiwanie najpopularniejszych słów w tekście
# 
# Korzystając z otwartego zbioru danych z Project Gutenberg (https://www.gutenberg.org/) np.,
# napisz funkcję, która zwraca n najpopularniejszych słów w tekście.
# 
# "https://www.gutenberg.org/files/2701/2701-0.txt"  # Moby Dick by Herman Melville  
# 

# In[8]:


orginalString = 'Lukasz'
firstString = 'Luk'
secondString ='Ada'
thirdString = 'asz'
print(f'Orginal string: {orginalString}')
translation = orginalString.maketrans(firstString,secondString,thirdString)
translated = orginalString.translate(translation)
print(f'Translated string: {translated}')


# In[9]:


import requests
from collections import Counter 
import string

def GetTheMostFrequentWordsInText(url: str, n: int) -> dict:
    try:
        r = requests.get(url)
        r.raise_for_status 
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)
    Text = r.text.lower()
    CleaningTextFromPunctuationChar = Text.maketrans(Text,Text,string.punctuation)
    CleanedTextFromPunctuationChar = Text.translate(CleaningTextFromPunctuationChar)
    SplitEachWordFromText = CleanedTextFromPunctuationChar.split()
    CounterWords = Counter(SplitEachWordFromText).most_common(n)
    DictCounterWords = dict(CounterWords)
    return DictCounterWords


# In[10]:


print(GetTheMostFrequentWordsInText('https://www.gutenberg.org/files/2701/2701-0.txt',10))
print(GetTheMostFrequentWordsInText('https://www.gutenberg.org/files/100/100-0.txt',15))
print(GetTheMostFrequentWordsInText('https://www.gutenberg.org/files/64317/64317-0.txt',20))


# Zadanie 6: Pobieranie kursów walut
# 
# Napisz funkcję, która pobiera kursy walut z serwisu https://www.x-rates.com/ i zwraca je jako słownik.
# Np. konwersja z jednej waluty do drugiej np. wpisujesz PLN na CHF na bazie tego
# Dwie wersje - wykorzystujac link https://www.x-rates.com/calculator/?from=GBP&to=USD&amount=1 i podmieniajc ilosc
# albo po prostu zrobic ze jeden gbp to iles dolarow i sciagnac i pomnozyc to.
# Wpisujesz po prostu symbole i ci zwraca.
# 

# In[11]:


import requests 
from bs4 import BeautifulSoup

def GetCurrencyExchangeTableUSD() -> dict:
    url ='https://www.x-rates.com/table/?from=USD&amount=1'
    try:
        r = requests.get(url)
        r.raise_for_status 
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)
    
    RequestXRates = r.text 
    
    soup = BeautifulSoup(RequestXRates,'html')  
    #Looking for Currency
    element_listCurrencySymbol = soup.find_all('td')
    CurrencySymbol = [element.get_text() for element in element_listCurrencySymbol[0::3]]
    CurrencySymbol.insert(0, 'USD') 
    #Looking for Value of Currency
    element_listValueCurrency = soup.find_all('td')
    ValueCurrency = [element.get_text() for element in element_listValueCurrency[1::3]]
    ValueCurrency.insert(0, '1.00')
    #Putting all data into Dictionary Comprehension
    new_dict = {k : v for k, v in zip(CurrencySymbol, ValueCurrency)}
    return new_dict

        


# In[12]:


GetCurrencyExchangeTableUSD()


# In[13]:


def GetPercentChangeInTheLast24Hours() -> dict:
    url ='https://www.x-rates.com/table/?from=USD&amount=1'
    try:
        r = requests.get(url)
        r.raise_for_status 
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)
    RequestXRates = r.text 
    soup = BeautifulSoup(RequestXRates,'html')  
    #Looking for Percent Change in The Last 24 hours table
    CurrencyPair = soup.find_all(class_='currencyPairUL')
    CurrencyPercentChange = CurrencyPair[0].find_all('li')
    # Getting Currency
    Currency = [element.get_text()[:7] for element in CurrencyPercentChange]
    Currency.insert(0,'Date')
    
    # Looking for date
    Dates = soup.find_all('span',id='ratesTrendsTimestamp' )

    DateList = [str(Date.get_text()) for Date in Dates]

    DateList = ' '.join(DateList)
    # Looking for Percent Change Values:
    PercentChange = [element.get_text()[7::1] for element in CurrencyPercentChange]
    PercentChange.insert(0,DateList)
    PercentChange

    PercentChangeInTheLast24HoursValues = {k:v for k,v in (zip(Currency,PercentChange))}
    
    return PercentChangeInTheLast24HoursValues


# In[14]:


GetPercentChangeInTheLast24Hours()


# In[15]:


def ConvertingCurrency(From: str,To: str,Amount: float) -> float:
    url = f'https://www.x-rates.com/calculator/?from={From}&to={To}&amount=1'
    try:
        r = requests.get(url)
        r = r.text
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)
    soup = BeautifulSoup(r,'html.parser')
      
    ToAmount = soup.find(class_='ccOutputRslt').text[:8]
    Cal = float(Amount) * float(ToAmount)
    Output = f'{Amount} {From} is {Cal} {To}'
    return Output


# In[16]:


print(ConvertingCurrency('EUR','PLN',123))
print(ConvertingCurrency('USD','EUR',100))
print(ConvertingCurrency('EUR','USD',50))


# Zadanie 7: Pobieranie informacji o filmach z IMDb
# 
# Napisz funkcję, która pobiera informacje o 10 najlepszych filmach na stronie https://www.imdb.com/chart/top/ i
#  zwraca je jako listę słowników. (tytul, rok, ocena)
# 

# In[17]:


import requests 
from bs4 import BeautifulSoup

def GetTop10Movies() -> dict:
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    url = "https://www.imdb.com/chart/top/"
    try:
        page = requests.get(url, headers = headers)
        page.raise_for_status 
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)
    
    page = page.text
    soup = BeautifulSoup(page,'html.parser')
    
    #Looking for Movies name
    
    MovieName = soup.find_all('h3')
    MovieNames = [Movie.get_text() for Movie in MovieName]
    MovieNames = MovieNames[1:11]
    #Looking for Year of Production for Movies

    YearOfMovie = soup.find_all(class_='sc-6ade9358-7 exckou cli-title-metadata-item')
    MovieYear = ListYear = [Year.get_text() for Year in YearOfMovie]
    MovieYear = MovieYear[::3]
    Top10MovieYear = MovieYear[0:11]
    #Looking for ratings for each movie
    
    Ratings = soup.find_all(class_='ipc-rating-star--rating')
    ListRating = [Raiting.get_text() for Raiting in Ratings]
    ListRating = ListRating[1:11]
    ListRating
    #Put it on List of Dictionaries
    Films = [{'Movie': Movie, 'year':year, 'rating':rating} for Movie,year, rating in zip(MovieNames,Top10MovieYear,ListRating)]
    
    return Films



# In[18]:


GetTop10Movies()


# Zadanie 7:
# Napisz funkcję, która pobiera tytuły artykułów z bloga na stronie https://blog.python.org/ i zwraca je jako listę.

# In[19]:


import requests 
from bs4 import BeautifulSoup

def GetArticleTitles() -> list:
    url = "https://blog.python.org/"
    try:
        r = requests.get(url)
        r.raise_for_status 
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)
    r = r.text
    soup = BeautifulSoup(r,'html.parser')
    
    Titles = soup.find_all('h3',class_='post-title entry-title')
    ListOfTitles = [Title.get_text().strip() for Title in Titles]
    return ListOfTitles



# In[20]:


GetArticleTitles()


# Zadanie 8 
# Napisz program, który pobierze od użytkownika (funkcja input) wysokość i szerokość geograficzną, a następnie wykona request na API pogodowe. 
# Odpowiedź powinna być zmapowana na klasę Weather. Program powinien zapisać wypełnioną klasę Weather do pliku pkl pickle i zapisac w postaci JSONa z danymi: latitude: ,longitude: ,windspeed: ,temperature. Najpierw powinna zwrocic dane z URL, a nastepnie zapisac wybrane zmienne do JSON
# URL = https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m
# 
# Najpierw zrobic request API zeby zwrocic JSONA z tej strony, potem zdefiniowac klasy gdzie zapisze tego jsona za pomoca klasy Weather z danymi, nastepnie zapisac te dane w postaci JSONa.

# In[21]:


import requests 
from dataclasses import dataclass, asdict
import json
from datetime import date 
def GetWeather(City: str, latitude: float, longitude: float) -> dict:
    today = date.today()
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    try:
        r = requests.get(url)
        r.raise_for_status 
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)
    WeatherJSONData = r.json()
    
    @dataclass
    class Weather:
        Latitude: float
        Longitude: float 
        Temperature: float 
        Windspeed: float 
        Winddrection: float 
    
    Weather = Weather(
    WeatherJSONData['latitude'],
    WeatherJSONData['longitude'],
    WeatherJSONData['current_weather']['temperature'],
    WeatherJSONData['current_weather']['windspeed'],
    WeatherJSONData['current_weather']['winddirection'])
    
    DictWeather = asdict(Weather)
    
    with open(f'{City} WeatherOpenMeteo {today}.json', 'w') as f:
        json.dump(DictWeather,f)
        
        
    return DictWeather
    


# In[22]:


print(GetWeather('Lodz',51.759445,19.457216))
print(GetWeather('Warsaw',52.237049,21.017532))
print(GetWeather('London',51.509865,-0.118092))
print(GetWeather('Zurich',47.373878,8.545094))



# Zadanie 8. 
# Stworzenie aplikacji, ktora tworzy haslo i zapisuje je z odpowiednia aplikacja np. pisze sie aplikacje a nastepnie generuje sie haslo

# In[23]:


import random 
import string


# In[24]:


characters = string.ascii_letters + string.digits + string.punctuation
length = random.randint(4,29)
randomcharacters = random.choice(characters)
password = []

for i in range(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    length = random.randint(4,29)
    randomcharacters = random.choice(characters)
    password.append(randomcharacters)

password = ''.join(password)    
print(password)


# In[25]:


GeneratedPassword = [random.choice(characters) for i in range(length)]
''.join(GeneratedPassword)


# In[26]:


def generate_password():
    length = random.randint(8, 32)
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(characters) for i in range(length))
    return password 

print(generate_password())


# In[27]:


def generate_password_for_app(Application: str) -> str:
    length = random.randint(8, 32)
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(characters) for i in range(length))
    Text = Application + ': ' + password

    with open('Passwords.txt', 'a') as f:
        f.write(Text + ' \n')    


# In[28]:


generate_password_for_app(Application=input('Enter your application to generate password for its'))


# Zadanie 9
# Napisz funkcje, ktora pobierze informacje o polaczeniu miedzy dwiema dowolnymi miastami w Szwajcarii. Informacje powinny zawierac stacje/platforme, kiedy odjazd i przyjazd, obliczyc czas ile trwa, postarac zwrocic przystanki
# https://transport.opendata.ch/docs.html
# 

# In[29]:


import requests 
from dataclasses import dataclass, asdict
import json
from datetime import datetime, date

url = 'http://transport.opendata.ch/v1/connections?from=Zurich&to=Basel'
r = requests.get(url)
TransportData = r.json()
print(f'Quantity of stations: {len(TransportData)}')
#Looking for first station in nested json:
TransportData['connections'][0]['sections'][0]['journey']['passList'][0]['station']['name']
FourthScheduleTransportStations = TransportData['connections'][3]['sections'][0]['journey']['passList']
print('Stations on the route on the fourth schedule:')       
for Station in FourthScheduleTransportStations:
    stations = Station['station']
    print(stations['name'])


# In[30]:


def GetStationBetweenCitySwiss(FromCity: str, ToCity: str) -> str:
    url = f'http://transport.opendata.ch/v1/connections?from={FromCity}&to={ToCity}'
    r = requests.get(url)
    TransportData = r.json()
    TransportData['connections'][0]['sections'][0]['journey']['passList'][0]['station']['name']
    FirstScheduleTransportStations = TransportData['connections'][0]['sections'][0]['journey']['passList']
    SecondScheduleTransportStations = TransportData['connections'][1]['sections'][0]['journey']['passList']
    ThirdScheduleTransportStations = TransportData['connections'][2]['sections'][0]['journey']['passList']
    FourthScheduleTransportStations = TransportData['connections'][3]['sections'][0]['journey']['passList']
    print('Stations on the route on the first schedule:')
    FirstSchedule = [Station['station']['name'] for Station in FirstScheduleTransportStations]
    print(FirstSchedule)
    print('Stations on the route on the second schedule:')  
    SecondSchedule = [Station['station']['name'] for Station in SecondScheduleTransportStations]
    print(SecondSchedule)
    print('Stations on the route on the third schedule:')    
    ThirdSchedule = [Station['station']['name'] for Station in ThirdScheduleTransportStations]   
    print(ThirdSchedule)
    print('Stations on the route on the fourth schedule:')           
    FourthSchedule = [Station['station']['name'] for Station in FourthScheduleTransportStations]  
    print(FourthSchedule)
        


# In[31]:


GetStationBetweenCitySwiss("Zurich","Bern")
GetStationBetweenCitySwiss("Zurich","Basel")
#GetStationBetweenCitySwiss("Zurich","Lucern")
#GetStationBetweenCitySwiss("Zurich","Lausanne")
#GetStationBetweenCitySwiss("Zurich","Geneve")


# In[32]:


def GetTransportSwiss(FromCity: str, ToCity:str) -> str:
    today = date.today()
    url = f'http://transport.opendata.ch/v1/connections?from={FromCity}&to={ToCity}'
    r = requests.get(url)
    TransportData = r.json()
    #Looking for arrival and departure from nested json
    FirstScheduleDeparture = TransportData['connections'][0]['from']
    FirstScheduleArrival = TransportData['connections'][0]['to']
    #Calculating Time of Traveling between two places:
    Arrival = datetime.fromtimestamp(FirstScheduleArrival['arrivalTimestamp'])
    Departure = datetime.fromtimestamp(FirstScheduleDeparture['departureTimestamp'])
    TimeOfTravel = (Departure - Arrival).total_seconds() / 60.0
    TimeOfTravel = f'{abs(TimeOfTravel):.0f} minutes'
    #Looking for stations between two places
    FirstScheduleStations = TransportData['connections'][0]['sections'][0]['journey']['passList']
    FirstScheduleListCompNameOfStation =[NameOfStation['station']['name'] for NameOfStation in FirstScheduleStations]
    #Defining dataclass
    @dataclass
    class FirstScheduleTransport:
        From: str 
        To: str 
        Departure: str 
        DepartureTimeStamp: int 
        DeparturePlatform: int 
        Arrival: str 
        ArrivalTimeStamp: int 
        ArrivalPlatform: int 
        Stations: str
        TimeOfTravel: int 
    #storing objects in dataclass
    FirstScheduleTransport = FirstScheduleTransport(
        FirstScheduleDeparture['station']['name'],
        FirstScheduleArrival['station']['name'],
        FirstScheduleDeparture['departure'],
        FirstScheduleDeparture['departureTimestamp'],
        FirstScheduleDeparture['platform'],
        FirstScheduleArrival['arrival'],
        FirstScheduleArrival['arrivalTimestamp'],
        FirstScheduleArrival['platform'],
        FirstScheduleListCompNameOfStation,
        TimeOfTravel
    )
    
    DictFirstScheduleTransport = asdict(FirstScheduleTransport)
    
    with open(f'Transport Swiss Schedule between {FromCity} and {ToCity} from {today}.json','w') as f:
        json.dump(DictFirstScheduleTransport, f)
        
    
    return DictFirstScheduleTransport


# In[33]:


GetTransportSwiss("Zurich","Bern")


# In[34]:


GetTransportSwiss("Zurich","Basel")


# In[35]:


GetTransportSwiss("Zurich","Luzern")


# In[36]:


GetTransportSwiss("Zurich","Geneve")


# In[37]:


GetTransportSwiss("St. Gallen","Zurich")


# In[38]:


GetTransportSwiss("Biel","Zurich")


# In[39]:


GetTransportSwiss("Basel","Lugano")

