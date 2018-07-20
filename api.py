import apiKeys 
import requests

def cities(city):
    reply= requests.get('https://developers.zomato.com/api/v2.1/cities?q='+city, headers= {
    'user-key': apiKeys.apiKey })
    return reply.json() 

def cuisines(city_id): 
    reply= requests.get('https://developers.zomato.com/api/v2.1/cuisines?city_id='+str(city_id), headers= {
    'user-key': apiKeys.apiKey })
    cuisinesList= {} 
    for cuisineDict in reply.json()["cuisines"]: 
        cuisine= cuisineDict["cuisine"]
        cuisinesList[cuisine["cuisine_name"]]= cuisine["cuisine_id"]
    return cuisinesList

def geocode(lat,long): 
    reply= requests.get('https://developers.zomato.com/api/v2.1/geocode?lat='+str(lat)+'&lon='+str(long), headers= {
    'user-key': apiKeys.apiKey })
    return reply.json()

if __name__=='__main__':
    print(geocode(36,-117))

