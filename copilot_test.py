#%%
def getTitleFromWebpage(url):
    import requests
    from bs4 import BeautifulSoup

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('title').get_text()
    return title

print(getTitleFromWebpage('https://github.com/github/copilot-docs'))

#%%
def getAllImagesFromWebpage(url):
    import requests
    from bs4 import BeautifulSoup

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    return images

print(getAllImagesFromWebpage('https://talkbate.com/'))

#%%
def sieveOfEratosthenes(n):
    import math
    import time

    start = time.time()
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            for j in range(i*2, n+1, i):
                prime_list.append(j)
    end = time.time()
    print(f'Time taken: {end-start}')
    return prime_list

print(sieveOfEratosthenes(100))
# %%
def travellingSalespersonSolution(data):
    import numpy as np
    #initialize the solution
    solution = [0]
    #initialize the distance
    distance = 0
    #initialize the current city
    current_city = 0
    #initialize the next city
    next_city = 0
    #loop through the cities
    for i in range(1, len(data)):
        #find the next city
        next_city = np.argmin(data[current_city] + data[:, current_city])
        #add the distance
        distance += data[current_city, next_city]
        #add the city to the solution
        solution.append(next_city)
        #update the current city
        current_city = next_city
    #add the distance
    distance += data[current_city, 0]
    #add the first city to the solution
    solution.append(0)
    return solution, distance
import numpy as np
data = np.array([[11,32,43,14,55,36,37,68,49]])
print(data)
print(travellingSalespersonSolution(data))
# %%
#create a function that takes a string and returns tokens
def get_tokens(string):
    #split the string into a list
    tokens = string.split()
    #take each of the tokens and remove punctuations
    for i in range(len(tokens)):
        tokens[i] = tokens[i].translate(str.maketrans('','', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
    #return the list of tokens
    return tokens


print(get_tokens("how is tommorow's weather?"))
# %%
def capitalizeString(string):
    #split the string into a list
    tokens = string.split()
    #take each of the tokens and remove punctuations
    for i in range(len(tokens)):
        tokens[i] = tokens[i].capitalize()
    #return the list of tokens
    return tokens

print(capitalizeString("how is tommorow's weather?"))

# %%

