from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


ZomatoData = pd.read_csv('zomato.csv',encoding="ISO-8859-1")
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['Ahmedabad','Bangalore','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer','Aligarh','Amravati','Amritsar','Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi','Bhopal','Bhubaneswar','Bikaner','Bilaspur','BokaroSteelCity','Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad','Bhilai','Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur','Gwalior','Gurgaon','Guwahati','Hamirpur','Hubli–Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jalgaon','Jammu','Jamnagar','Jamshedpur','Jhansi','Jodhpur','Kakinada','Kannur','Kanpur','Karnal','Kochi','Kolhapur','Kollam','Kozhikode','Kurnool','Ludhiana','Lucknow','Madurai','Malappuram','Mathura','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik','Nellore','Noida','Patna','Pondicherry','Purulia','Prayagraj','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Ratlam','Salem','Sangli','Shimla','Siliguri','Solapur','Srinagar','Surat','Thanjavur','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tirunelveli','Tiruvannamalai','Ujjain','Bijapur','Vadodara','Varanasi','Vasai-VirarCity','Vijayawada','Vizag','Vellore','Warangal']



def RestaurantSearch(City,Cuisine,pricerange):
        if pricerange == 'Less than 300':
                TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (ZomatoData['Average Cost for two']<300)]
        elif pricerange == '300 to 700':
                TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (ZomatoData['Average Cost for two']>=300) & (ZomatoData['Average Cost for two']<=700)]
        elif pricerange == 'More than 700':
                TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (ZomatoData['Average Cost for two']>700)]
        TEMPn = TEMP[['Restaurant Name','Address','Aggregate rating']]
        TEMPn.sort_values(by=['Aggregate rating'],inplace=True,ascending=False)
        return TEMPn

class ActionSearchRestaurants(Action):
        def name(self):
                
                return 'action_search_restaurants'

        def run(self, dispatcher, tracker, domain):
                #config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
                loc = tracker.get_slot('location')
                cuisine = tracker.get_slot('cuisine')
                price = tracker.get_slot('pricerange')
                results = RestaurantSearch(City=loc,Cuisine=cuisine,pricerange=price)
                response=""
                if results.shape[0] == 0:
                        response= "no results for the selected preferences, please try other options"
                elif loc.capitalize() not in WeOperate:
                        response = "Sorry, We do not operate in that area yet, Can you please specify some other location"
                else:
                        for restaurant in RestaurantSearch(loc,cuisine,price).iloc[:5].iterrows():
                                restaurant = restaurant[1]
                                response = response + "Found " + restaurant['Restaurant Name'] + " in " + restaurant['Address'] + " has been rated " + str(restaurant['Aggregate rating']) + "\n"
                dispatcher.utter_message("------"+response)
                return [SlotSet('location',loc)]

def sendmail(mailid,loc1,cuisine1,price1):
        response10=""
        count = 0
        for restaurant10 in RestaurantSearch(loc1,cuisine1,price1).iloc[:10].iterrows():
                count = count + 1
                restaurant10 = restaurant10[1]
                response10 = response10 + str(count) + ") Found " + restaurant10['Restaurant Name'] + " in " + restaurant10['Address'] + " has been rated " + str(restaurant10['Aggregate rating']) + "\n"
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login("enter email id","enter password")
        subject = 'Foodie Restaurant- Top 10 Restaurants information'
        msg = MIMEMultipart()
        msg['Subject'] = subject
        message = "Hey foodie!, \n \n Let us take you on a trip to the tastiest corners as per your selected price range in " + loc1 + "\n" + "\n" + response10 + "\n\nThanks & Regards\nFoodie Team\nPlease reply to this mail for more information/feedback/suggestions.\nHave a nice day :)"
        msg.attach(MIMEText(message,'plain'))
        text = msg.as_string()
        s.sendmail("enter email id",mailid,text)
        s.quit()
        

class ActionSendMail(Action):
        def name(self):
                return 'action_send_mail'

        def run(self, dispatcher, tracker, domain):
                loc1 = tracker.get_slot('location')
                cuisine1 = tracker.get_slot('cuisine')
                price1 = tracker.get_slot('pricerange')
        
                MailID = tracker.get_slot('emailid')
                sendmail(MailID,loc1,cuisine1,price1)
                dispatcher.utter_message("Have a Good day! Mail is sent")
                return [SlotSet('emailid',MailID)]
