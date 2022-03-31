# Khet-E by AgroPro

## Inspiration
According to the UN, Nearly 1/2 of all fruit & vegetables produced globally are wasted each year. With decreasing energy and resources across the planet, **Khet-E** was made to promote better yield among farmers and better health among malnourished people and animals. Also, we know that it might be difficult for farmers to use websites, we have integrated the functionalities of this website in the form of a WhatsApp Bot as well in order to reach a greater target audience.

## What it does  
---

### The Website-  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929593959917973514/1.jpg)  

---
**1. Crop Recommendation -** In the crop recommendation application, the user can provide the soil data(Nitrogen, Phosphorus, Potassium concentrations, pH value, Rainfall in mm, State and City) from their side and the application will recommend which crop the user should grow. We have used an open weather API to automatically check the temperature, moisture, and humidity for the location provided.  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929593960454828042/3.jpg)  

---
**2. Fertilizer Recommendation -** In the fertilizer recommendation application, the user can input the soil data and the type of crop they are growing, and the application will predict what the soil lacks or has an excess of and will recommend improvements accordingly.  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929593960886837258/4.jpg)  

---
**3. Disease Prediction -** In the disease prediction application, the user can upload the image of the crop with the disease, and the model will predict the disease, tell the cause of it and recommend its cure.  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929593961151098890/5.jpg)  

---  


**Add Ons**  

**1. Soil Classification -** We have also created this add-on streamlit based soil classification application, for you to classify soil with the help of an image of  the soil.  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929441250585751594/Screenshot_2022-01-08_at_11.57.10_PM.png)  

---
**2. Nursery Locator -** We have added an option for you to locate a nursery near you to buy the needed crops and fertilizers.  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929443304024727682/Screenshot_2022-01-09_at_12.05.27_AM.png)  

---
**3. Try the WhatsApp Bot Feature -** We have also added the button to use our WhatsApp bot on the website. Clicking on the button would lead you to connect with out Twilio based Whatsapp Bot.  

---
### Twilio Based WhatsApp Bot-
The bot is developed in a way that it takes up the language with which you message it first and then uses it to ask the questions and provide the answers. The bot has 4 options-  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929447769268170753/Screenshot_2022-01-09_at_12.14.58_AM.png)  

---
**1. Crop Recommendation -** In the crop recommendation option, the user should provide the soil data(Nitrogen, Phosphorus, Potassium concentrations, pH value, Rainfall in mm, State and City) from their side and the bot will recommend which crop the user should grow.  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929447769591128194/Screenshot_2022-01-09_at_12.19.48_AM.png)  

---
**2. Fertilizer Recommendation -** In the fertilizer recommendation option, the user can input the soil data and the type of crop they are growing, and the bot will predict what the soil lacks or has an excess of and will recommend improvements accordingly.  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929447770161565696/Screenshot_2022-01-09_at_12.21.08_AM.png)  

---
**3. Disease Prediction -** In the disease prediction option, the user can upload the image of the crop with the disease, and the bot will predict the disease, tell the cause of it and recommend its cure.  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929447771063320596/Screenshot_2022-01-09_at_12.22.47_AM.png)  

---
**4. Change Language -** If a user wants to change the language, they can send a `Change Language = <Lang>` message and the bot will change the language.  

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929449288969379881/Screenshot_2022-01-09_at_12.29.06_AM.png)  


## How we built it
✅ We built the Machine learning model using images. We have used various types of image processing and image segmentation algorithms to find the soil type from the image.  
✅ Website is built using a html, css, python, flask, streamlit  and machine learning models.  
✅ Built crop and fertilizer prediction model using random forest classifier and data.  
✅ Built disease prediction model using image segmentation and plant disease model.  
✅ Integrated a Google Map for the nearest nursery.  
✅ The WhatsApp Bot is built using Twilio and python and the solutions are provided using all the models developed for the website.  

## Challenges we ran into
While we were working on this project the limited availability of data sets was a big problem we faced. Build different ML model for different diseases detection was another huge problem . Deploying was a problem too. Using these models in a WhatsApp Bot was a very big challenge for us.

## Accomplishments that we're proud of
The implementation of the entire project helped us realize the importance of collaboration and the dynamics of working in a team. In every Hackathon, proper time management ⏰plays a crucial role that can become a determining factor for the overall progress. We understood the instrumentality of following the code of conduct ✨and treating fellow developers with respect while learning and improving through their feedback. We are proud of completing the project in time.

## What we learned
We learnt about how to take Machine Learning to the next level by using it with front end and backend development to empower our project and make it usable for everyone around the world. The major takeaway was about how we can use our skillset and help the planet be a better place. We also learnt how to use Twilio based WhatsApp Bots and how to integrate them with ML models.

## What's next for Khet-E by AgroPro
We are also looking forward to bring this service to our mobile phones. And, if we could collaborate with botanists then we can take this project to the next level. We also want to make a SMS based bot, so that it could reach more people.

## Try It Out 
[Khet-E by AgroPro](https://agropro-hack.herokuapp.com/)  

## Built With
`ai  
api  
css3  
flask  
heroku  
html5  
javascript  
machine-learning  
python  
streamlit  
tensorflow  
torch  
twilio`

![Alt text](https://media.discordapp.net/attachments/926835257444028536/929595515853762581/Screenshot_2022-01-09_at_10.10.18_AM.png?width=2160&height=380)
