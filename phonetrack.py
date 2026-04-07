import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder
pepnumber=phonenumbers.parse(str(number))
location=geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro=phonenumbers.parse(str(number))
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import  OpenCageGeocode
key='35bf1c98a2524ca8a062916a6558238e'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
#print(results)

Lat=results[0]['geometry']['lat']
Lng=results[0]['geometry']['lng']
print(Lat , Lng)

# Purani line ki jagah yeh likhein:
myMap = folium.Map(location=[Lat, Lng], zoom_start=9, tiles='CartoDB positron')
folium.Marker([Lat,Lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")
