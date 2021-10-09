import requests
query = {'lat':'45', 'lon':'180'}
response = requests.get('https://v2.jokeapi.dev/joke/Any', params=query)
if (response.status_code == 200):
    print("The request was a success!")
  
elif (response.status_code == 404):
    print("Result not found!")
print(response.json())
print(response.headers["date"])
