import id3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from sklearn.tree import plot_tree
from gui import apply_theme, page_header, section_header, metric_card, style_matplotlib

# =========================================================
# SUSTAINABLE TRANSPORT CHOICES - FIELD PROJECT ANALYSIS
# Dataset is built directly into this app.
# No CSV upload is required.
# =========================================================

st.set_page_config(
    page_title="Sustainable Transport Choices",
    page_icon="🚆",
    layout="wide"
)
apply_theme()
style_matplotlib()
# ---------------------------------------------------------
# EMBEDDED SURVEY DATA
# ---------------------------------------------------------
CSV_DATA = '"Timestamp","Username","What is your age?  ","Which type of area do you currently live in?  ","What is the main purpose of your regular travel?  ","How far do you usually travel in a day?  ","What is your most frequently used mode of transport?  ","Which of these transport modes do you use at least once in a typical week?  ","Do you use public transportation regularly?  ","How often do you use public or shared transport?  ","Which factors affect your choice of transport? (Select all that apply)","What problems do you usually face while travelling? (Select all that apply)","Before this survey, had you heard about sustainable transport?  ","Which of the following do you consider sustainable transport? (Select all that apply)","How important is sustainable transportation to you?  ","How would you rate the availability of public transportation in your area?  ","How important is environmental impact when choosing transport?  ","How willing are you to switch to a more sustainable mode of transport?  ","Do you agree that sustainable transport can help reduce traffic and pollution?  ","What stops you from choosing sustainable transport more often? (Select all that apply)","Which improvement would encourage you most to use sustainable transport?  ","What is your suggestion for making transportation more sustainable in your area?  "\n"2026/09/04 7:51:43 PM GMT+5:30","govindshekhawat1123@gmail.com","18","Urban/City","Education","5–10 km","Train/Metro","Carpooling/Ride sharing","Yes","Always","Cost;Travel time;Availability","Traffic;Delays;Overcrowding;Poor roads","No","Walking;Cycling;Bus;Train/Metro;Shared transport","3","4","1","4","Agree","Takes more time;Not easily available;Poor connectivity;Less comfort;Safety concerns","Faster service","I would suggest ki people should aware about what actually is sustainable transport is and how good they are"\n"2026/09/04 8:01:17 PM GMT+5:30","laxmijss1998@gmail.com","27","Urban/City","Work","11–20 km","Bus","Bus","Yes","Always","Travel time","Traffic","Yes","Shared transport","3","2","3","2","Agree","Higher cost","Faster service","Yes"\n"2026/09/04 8:05:12 PM GMT+5:30","budyeseher04@gmail.com","19","Urban/City","Education","5–10 km","Auto/Rickshaw/Cab","Train/Metro","Yes","Always","Cost;Travel time;Comfort;Availability","Overcrowding;Poor roads;Safety concerns","Yes","Walking;Cycling","4","4","5","5","Strongly Agree","Not easily available","More frequent services","Improving public transit and better walking path"\n"2026/09/04 8:06:03 PM GMT+5:30","halakhan2007@gmail.com","19","Urban/City","Education","Less than 5 km","Auto/Rickshaw/Cab","Train/Metro","Yes","Always","Travel time;Comfort;Convenience;Availability","High cost;Delays;Overcrowding;Poor roads","Yes","Walking;Cycling;Bus;Train/Metro;Carpooling;Electric vehicles;Shared transport","4","3","5","5","Agree","Takes more time;Higher cost;Less comfort","More frequent services","More availability "\n"2026/09/04 8:07:56 PM GMT+5:30","simonmasih1208@gmail.com","18","Urban/City","Education","11–20 km","Train/Metro","Carpooling/Ride sharing","Yes","Always","Travel time;Comfort;Availability;Reliability","Delays;Overcrowding;Poor roads","Yes","Walking;Cycling;Electric vehicles","5","4","5","5","Strongly Agree","Takes more time;Higher cost;Not easily available","Faster service","Upgrade local bus and train networks to offer cheaper and more frequent services"\n"2026/09/04 8:08:35 PM GMT+5:30","sanjugupta270728@gmail.com","18","Urban/City","Education","Less than 5 km","Train/Metro","Train/Metro","Yes","Always","Cost;Travel time;Convenience;Availability","Delays;Overcrowding;Safety concerns","Yes","Walking;Train/Metro;Shared transport","4","4","3","4","Strongly Agree","Nothing","More frequent services","Increase the number of trains at peak hours to avoid overcrowding"\n"2026/09/04 8:13:15 PM GMT+5:30","amritavishwakarma2008@gmail.com","17","Urban/City","Education","11–20 km","Train/Metro","Train/Metro","Yes","Always","Cost;Travel time;Comfort;Availability","Traffic;Delays;Overcrowding","Yes","Walking;Cycling","5","3","5","4","Agree","Takes more time;Not easily available;Less comfort","Lower fares","Improve public transport services, increase electric buses, and provide better cycling and walking facilities. This can reduce pollution, traffic congestion, and fuel consumption."\n"2026/09/04 8:15:43 PM GMT+5:30","rhujutaumbarkar@gmail.com","19","Suburban","Work","5–10 km","Two-wheeler","Carpooling/Ride sharing","Yes","Sometimes","Travel time;Comfort;Convenience;Availability;Safety;Reliability","Traffic;Delays;Overcrowding;Poor roads;Safety concerns;Pollution","Yes","Walking;Cycling;Bus;Train/Metro;Carpooling;Electric vehicles;Shared transport","3","3","3","3","Neutral","Takes more time;Not easily available;Less comfort;Safety concerns;Unreliable service","Better safety","Keeping crowd and permanent residents as a primary ref to provide public transport accordingly, also basic needs of a smooth travel like Better Roads, Bike Lanes /atleast footpath for pedestrians, not allowing big vehicles to hog small roads, etc"\n"2026/09/04 8:15:50 PM GMT+5:30","sanchitakeluskar100@gmail.com","20","Urban/City","Education","More than 20 km","Train/Metro","Electric vehicle","Yes","Always","Travel time","Traffic;Delays;Overcrowding;Poor roads;Poor connectivity;Safety concerns","No","Cycling","4","3","4","3","Neutral","Takes more time","More frequent services","Nothing "\n"2026/09/04 8:15:57 PM GMT+5:30","shaikhabdur000@gmail.com","18","Urban/City","Education","More than 20 km","Train/Metro","Train/Metro","Yes","Always","Travel time;Comfort;Safety","High cost;Delays","Yes","Walking;Train/Metro;Shared transport","5","4","4","4","Neutral","Less comfort;Safety concerns;Lack of awareness","Faster service","Improve public transport "\n"2026/09/04 8:16:42 PM GMT+5:30","harshtiwari915613@gmail.com","19","Urban/City","Education","5–10 km","Train/Metro","Walking","No","Sometimes","Comfort","Traffic;Overcrowding","No","Walking","5","5","5","5","Strongly Agree","Takes more time;Less comfort","Better walking/cycling facilities","In my area, transportation can be made more sustainable by improving public transport, encouraging cycling and walking, and promoting electric vehicles. More buses and better connectivity can reduce the number of private vehicles on the road. Dedicated cycle lanes and pedestrian-friendly roads can also help. Using electric buses, carpooling, and shared transportation can reduce air pollution and traffic while saving fuel."\n"2026/09/04 8:16:52 PM GMT+5:30","anujtiwari78221@gmail.com","19","Suburban","Work","5–10 km","Train/Metro","Electric vehicle","Yes","Always","Travel time;Comfort","Overcrowding;Poor roads;Poor connectivity","Yes","Bus;Train/Metro;Not sure","5","3","5","5","Neutral","Higher cost;Poor connectivity;Unreliable service","Better connectivity","Using public transport "\n"2026/09/04 8:25:17 PM GMT+5:30","diyashekhawat25@gmail.com","18","Urban/City","Education","5–10 km","Auto/Rickshaw/Cab","Train/Metro","Yes","Always","Cost;Travel time","Delays;Poor roads;Safety concerns","Yes","Walking;Cycling;Bus;Train/Metro;Carpooling;Electric vehicles;Shared transport","2","3","5","5","Agree","Not easily available","Faster service","Availability of more public transport "\n"2026/09/04 8:28:59 PM GMT+5:30","shaikhmaryam873@gmail.com","17","Urban/City","Education","More than 20 km","Train/Metro","Train/Metro","Yes","Always","Cost;Travel time;Comfort;Convenience","Traffic;Overcrowding;Poor roads;Safety concerns;Pollution","Yes","Walking;Cycling;Bus","5","4","4","4","Agree","Takes more time;Higher cost;Poor connectivity;Less comfort","Better walking/cycling facilities","Promote public transport, cycling, walking, and carpooling to reduce emissions."\n"2026/09/04 8:39:18 PM GMT+5:30","pragatipatil3044@gmail.com","20","Rural","Education","More than 20 km","Train/Metro","Bus","No","Never","Availability;Safety","Traffic;High cost;Poor roads;Poor connectivity","No","Walking;Cycling;Train/Metro","1","1","1","1","Strongly Agree","Poor connectivity;Less comfort","Lower fares","Reduce the cost"\n"2026/09/04 8:40:12 PM GMT+5:30","ritikak170608@gmail.com","18","Urban/City","Education","Less than 5 km","Walking","Train/Metro","Yes","Always","Cost;Travel time;Convenience;Availability;Environmental impact","Traffic;Overcrowding;Safety concerns;Pollution","Yes","Walking;Cycling;Train/Metro;Electric vehicles","5","4","4","4","Agree","Less comfort;Safety concerns","Better safety","Make public transport safer and more easily available, with better lighting, frequent buses, and safe walking routes to stops."\n"2026/09/04 8:44:40 PM GMT+5:30","arathinair242@gmail.com","20","Urban/City","Education","5–10 km","Train/Metro","Train/Metro","Yes","Always","Cost;Travel time;Comfort;Convenience;Safety;Reliability","Delays;Safety concerns;Pollution","Yes","Walking;Cycling;Bus;Train/Metro;Electric vehicles","5","4","5","5","Strongly Agree","Takes more time;Higher cost;Less comfort;Safety concerns;Unreliable service","Faster service","We need to move towards sustainability without compromising the needs of the people "\n"2026/09/04 8:47:10 PM GMT+5:30","singhniyati2007@gmail.com","19","Urban/City","Education","5–10 km","Train/Metro","Train/Metro","Yes","Always","Cost;Travel time;Availability","Delays;Overcrowding;Safety concerns","Yes","Train/Metro","5","2","4","3","Strongly Agree","Takes more time;Higher cost","More frequent services","More availability of trains"\n"2026/09/04 8:47:11 PM GMT+5:30","gajbhiyeankita07@gmail.com","19","Suburban","Education","More than 20 km","Train/Metro","Train/Metro","Yes","Always","Cost;Travel time;Comfort;Convenience;Availability","Delays;Overcrowding","No","Walking;Cycling;Bus;Train/Metro;Electric vehicles;Shared transport","5","3","4","5","Strongly Agree","Nothing","Faster service","TO HAVE AUTOSTAND AT CROWDED AREAS, AND RODES SHOULD BE WIDER WITH ENOUGH SPASE FOR WALKING "\n"2026/09/04 8:47:21 PM GMT+5:30","samanisarfaraz21@gmail.com","19","Urban/City","Shopping","5–10 km","Two-wheeler","Train/Metro","No","Never","Travel time","Traffic","No","Electric vehicles","2","2","3","3","Agree","Safety concerns","Better connectivity","I would like to choice this coz it\'s nature friendly, easy availability"\n"2026/09/04 8:54:02 PM GMT+5:30","ishitahedau2006@gmail.com","20","Urban/City","Education","5–10 km","Train/Metro","Walking","Yes","Always","Travel time;Comfort","Overcrowding","Yes","Walking;Electric vehicles","3","3","3","3","Neutral","Takes more time;Poor connectivity;Safety concerns;Unreliable service","Faster service","Awareness about areas "\n"2026/09/04 8:55:44 PM GMT+5:30","abrelferns12@gmail.com","19","Urban/City","Education","Less than 5 km","Walking","Walking","No","Sometimes","Cost;Travel time;Comfort;Safety","Delays;Overcrowding;Poor roads;Safety concerns;Pollution","Yes","Walking;Cycling","3","3","4","4","Agree","Takes more time;Poor connectivity;Less comfort;Safety concerns","Faster service","Improve public transport by making it more frequent, affordable, reliable, and well connected, while also providing safer walking and cycling facilities"\n"2026/09/04 8:55:54 PM GMT+5:30","ishivlogs07@gmail.com","17","Suburban","Education","5–10 km","Two Wheeler and Train","Walking","Yes","Sometimes","Comfort","Overcrowding","Yes","Walking;Bus","3","4","3","3","Neutral","Less comfort","More comfort","Kuch nahi zyada bike pe 4 jann bethke jao(Diya ko bolna uske khas dost ne ye survey mai part liya hai)"\n"2026/09/04 8:56:26 PM GMT+5:30","tragini039@gmail.com","19","Urban/City","Education","Less than 5 km","Walking","Walking","No","Rarely","Cost;Convenience","Delays;Overcrowding","No","Walking;Cycling;Shared transport","4","4","4","5","Strongly Agree","Takes more time;Not easily available;Unreliable service","Better connectivity","Shift from private vehicles to public, shared and electric transport is the key to make transport sustainable."\n"2026/09/04 8:58:23 PM GMT+5:30","shahafsha.2007@gmail.com","19","Suburban","Education","Less than 5 km","Train/Metro","Train/Metro","Yes","Always","Cost","Traffic;Delays","Yes","Cycling","5","4","5","5","Strongly Agree","Lack of awareness","More comfort","expanding the Navi Mumbai Municipal Transport (NMMT) electric bus fleet and integrating last-mile electric vehicle options around transit hubs."\n"2026/09/04 9:05:31 PM GMT+5:30","ishachavan0130@gmail.com","19","Urban/City","Education","5–10 km","Auto/Rickshaw/Cab","Train/Metro","Yes","Sometimes","Cost;Travel time;Safety","Traffic;High cost;Pollution","Yes","Walking;Cycling;Train/Metro;Electric vehicles","5","5","4","3","Strongly Agree","Takes more time;Less comfort;Unreliable service","Better walking/cycling facilities","Promote public transport, cycling, walking and electric vehicles while reducing unnecessary private vehicle use"\n"2026/09/04 9:07:30 PM GMT+5:30","narendertanwar7566@gmail.com","31","Urban/City","Work","5–10 km","Car","Walking","No","Rarely","Travel time;Comfort;Availability;Reliability","Traffic;Pollution","No","Train/Metro","5","4","5","5","Agree","Lack of awareness","Better walking/cycling facilities","Govt should run Metro to control the traffic."\n"2026/09/04 9:09:50 PM GMT+5:30","papyapatil30@gmail.com","17","Urban/City","Education","Less than 5 km","Two-wheeler","Walking","No","Rarely","Cost;Comfort;Availability;Safety","Traffic;High cost;Delays;Overcrowding;Poor roads;Poor connectivity;Safety concerns;Pollution","No","Walking;Cycling","3","1","5","5","Strongly Agree","Nothing","Lower fares","Nice do it i support you not modi jay sustainable development baba ki "\n"2026/09/04 9:12:23 PM GMT+5:30","himeshmore03@gmail.com","18","Urban/City","Education","5–10 km","Two-wheeler","Train/Metro","Yes","Always","Cost;Travel time","Traffic;Poor roads;Safety concerns","Yes","Walking;Cycling;Bus;Train/Metro","5","5","5","5","Agree","Takes more time;Higher cost;Less comfort;Safety concerns","Better connectivity","."\n"2026/09/04 9:15:52 PM GMT+5:30","lavaheshivam3@gmail.com","18","Urban/City","Education","More than 20 km","Two-wheeler","Train/Metro","No","Rarely","Availability","Traffic;Delays;Overcrowding;Poor roads;Poor connectivity;Pollution","No","Cycling;Train/Metro;Electric vehicles","3","3","3","3","Neutral","Takes more time;Poor connectivity;Less comfort;Safety concerns","Lower fares","Make low cost and high availability "\n"2026/09/04 9:16:53 PM GMT+5:30","simranjaiswar1018@gmail.com","20","Urban/City","Work","11–20 km","Auto/Rickshaw/Cab","Walking","Yes","Always","Availability","Traffic;Delays;Overcrowding;Poor roads;Poor connectivity;Pollution","No","Walking;Cycling;Electric vehicles","3","4","5","4","Neutral","Not easily available","More frequent services","Less pollution "\n"2026/09/04 9:17:14 PM GMT+5:30","ap6035939@gmail.com","18","Urban/City","Education","11–20 km","Train/Metro","Bus","Yes","Always","Cost;Travel time;Comfort","Traffic;Delays;Overcrowding","Yes","Walking;Shared transport","5","4","5","5","Neutral","Higher cost","More comfort","Promote public transport, cycling, walking, and carpooling to reduce pollution and traffic."\n"2026/09/04 9:17:45 PM GMT+5:30","shekhawatvijaylaxmi1998@gmail.com","64","Urban/City","Work","More than 20 km","Auto/Rickshaw/Cab","Train/Metro","Yes","Always","Cost;Convenience;Safety","Traffic","No","Walking;Cycling;Electric vehicles","5","5","5","3","Strongly Agree","Takes more time;Poor connectivity;Nothing","Better connectivity","availabllity "\n"2026/09/04 9:18:52 PM GMT+5:30","kalpeshmahajan767@gmail.com","18","Suburban","Education","More than 20 km","Train/Metro","Walking","Yes","Always","Cost;Travel time;Availability","Delays","No","Bus;Train/Metro","5","3","2","4","Agree","Not easily available;Unreliable service","Better connectivity","Poor modi \n"\n"2026/09/04 9:23:49 PM GMT+5:30","reshmachaubey07@gmail.com","18","Urban/City","Education","5–10 km","Walking","Electric vehicle","Yes","Always","Cost;Travel time;Comfort;Availability;Safety;Environmental impact","Delays;Overcrowding;Pollution","Yes","Walking;Cycling;Bus;Train/Metro;Electric vehicles;Shared transport","5","3","5","5","Agree","Higher cost;Not easily available;Lack of awareness","More comfort","Construction of roads and introduce electric vehicle"\n"2026/09/04 9:34:52 PM GMT+5:30","kanojiamanu29@gmail.com","21","Urban/City","Education","5–10 km","Auto/Rickshaw/Cab","Bicycle","Yes","Always","Cost;Travel time;Availability","Traffic;High cost;Delays;Overcrowding","Yes","Walking;Shared transport","4","3","3","3","Agree","Takes more time;Higher cost;Not easily available;Poor connectivity;Unreliable service","Faster service","My suggestion is to improve public transportation and encourage walking and cycling in the area. More frequent and affordable buses, dedicated cycle lanes, safe footpaths, and better connectivity between residential areas and workplaces/colleges can reduce private vehicle use. Promoting electric buses and shared transport can further reduce air pollution and carbon emissions."\n"2026/09/04 9:35:00 PM GMT+5:30","shrutigaud2205@gmail.com","19","Suburban","Education","Less than 5 km","Train/Metro","Train/Metro","Yes","Always","Cost;Availability","Delays;Overcrowding","Yes","Walking;Cycling;Bus;Train/Metro;Shared transport","4","4","5","4","Neutral","Nothing","Lower fares","My suggestion is to promote public transport, cycling, walking, and electric vehicles to reduce pollution and traffic."\n"2026/09/04 9:40:48 PM GMT+5:30","nandanisd2008@gmail.com","18","Urban/City","Education","5–10 km","Train/Metro","Train/Metro","Yes","Always","Cost;Travel time","Traffic;High cost;Delays;Safety concerns","Yes","Cycling;Electric vehicles;Shared transport","3","3","3","3","Neutral","Takes more time;Higher cost;Not easily available;Safety concerns","Lower fares","."\n"2026/09/04 9:46:46 PM GMT+5:30","yughjaiswal@gmail.com","17","Urban/City","Education","5–10 km","Bus","Walking","Yes","Always","Availability;Reliability","Overcrowding","Yes","Train/Metro","4","4","5","3","Agree","Not easily available","More comfort","Covering every region possible "\n"2026/09/04 9:52:15 PM GMT+5:30","sadhnakumari8839@gmail.com","20","Urban/City","Education","Less than 5 km","Walking","Bus","No","Sometimes","Travel time","Safety concerns","Yes","Train/Metro","4","5","3","3","Disagree","Safety concerns","Better safety","Metro\n"\n"2026/09/04 9:59:28 PM GMT+5:30","ankushchaurasiya50@gmail.com","22","Suburban","Work","More than 20 km","Car","Carpooling/Ride sharing","Yes","Always","Cost","Overcrowding","Yes","Not sure","4","2","3","2","Neutral","Higher cost","Better connectivity","Ju"\n"2026/09/04 10:09:00 PM GMT+5:30","mhetrerani72@gmail.com","32","Urban/City","Work","Less than 5 km","Bus","Walking","Yes","Sometimes","Travel time","Traffic","Yes","Bus","5","4","2","1","Agree","Not easily available","More comfort","Ambarnath "\n"2026/09/04 10:13:33 PM GMT+5:30","poojarychirag19b@gmail.com","19","Suburban","Education","5–10 km","Train/Metro","Train/Metro","Yes","Always","Cost;Convenience;Availability","Traffic;Delays;Overcrowding;Poor roads;Pollution","Yes","Walking;Cycling;Train/Metro;Electric vehicles","4","5","4","5","Strongly Agree","Takes more time;Not easily available;Unreliable service","More comfort","Just investing more on the overall infrastructure is important and as a society, upholding the concept itself is an important step towards such sustainability."\n"2026/09/04 10:17:26 PM GMT+5:30","anu566605@gmail.com","19","Suburban","Education","11–20 km","Train/Metro","Electric vehicle","Yes","Always","Cost;Travel time;Availability;Environmental impact","Traffic;Delays;Overcrowding;Poor roads;Pollution","Yes","Walking;Cycling;Electric vehicles;Shared transport","5","4","3","5","Strongly Agree","Not easily available;Less comfort;Unreliable service;Lack of awareness","More frequent services","For eg, cycling and walking in our area there is not a single cycle/ pedestrian friendly pathway to ride cycles/ walk....things should be taken in mind to make a specific parameters which includes a proper area for footpath where no peddlers are allowed to sell their goods and so on...."\n"2026/09/04 10:23:25 PM GMT+5:30","parthsalunke2306@gmail.com","20","Urban/City","Education","5–10 km","Two-wheeler","Walking","Yes","Always","Cost;Travel time;Convenience","Traffic;High cost;Poor roads","Yes","Walking;Bus;Shared transport","4","3","3","4","Strongly Agree","Takes more time;Not easily available;Unreliable service","Faster service","we can go for green energy"\n"2026/09/04 10:26:52 PM GMT+5:30","supriyadawn21@gmail.com","20","Urban/City","Education","11–20 km","Train/Metro","Carpooling/Ride sharing","Yes","Always","Cost;Travel time;Convenience;Availability","Traffic;Delays;Overcrowding;Poor roads;Poor connectivity;Safety concerns;Pollution","Yes","Shared transport","5","4","3","4","Neutral","Poor connectivity;Less comfort;Safety concerns;Unreliable service;Lack of awareness","More frequent services","The maintenance of broken roads and pipes line works "\n"2026/09/04 10:37:59 PM GMT+5:30","roshnigupta2688@gmail.com","19","Urban/City","Education","Less than 5 km","Walking","Auto ","No","Rarely","Cost;Travel time;Comfort;Convenience;Availability;Safety;Reliability;Environmental impact","Traffic;High cost;Delays;Safety concerns","Yes","Walking;Cycling","3","3","3","3","Agree","Takes more time;Higher cost;Not easily available;Safety concerns","Better walking/cycling facilities","Sustainable transport means using modes of transportation that cause less pollution and are environmentally friendly while using fewer natural resources."\n"2026/09/04 10:51:15 PM GMT+5:30","nehajaiswar011@gmail.com","18","Suburban","Education","Less than 5 km","Car","Walking","Yes","Sometimes","Comfort","Traffic","No","Bus;Train/Metro","3","1","4","3","Strongly Disagree","Unreliable service","More frequent services","The is area today most important person."\n"2026/09/04 10:59:44 PM GMT+5:30","jasusramesh013@gmail.com","18","Urban/City","Education","5–10 km","Two-wheeler","Bus","Yes","Rarely","Cost;Availability","Traffic;Poor roads","Yes","Walking;Cycling;Electric vehicles;Shared transport","5","5","3","5","Strongly Agree","Takes more time","Better walking/cycling facilities","Use less of public transportation use if there is urgent work for you if not then use cycling and electric vehicle and by using bicycles you will be stay fit too"\n"2026/09/04 11:07:58 PM GMT+5:30","poojagupta230525@gmail.com","20","Urban/City","Education","Less than 5 km","Auto/Rickshaw/Cab","Walking","No","Sometimes","Cost;Travel time","Delays","No","Walking;Electric vehicles;Shared transport","3","3","4","3","Agree","Nothing","Better connectivity","Nothing "\n"2026/09/04 11:47:10 PM GMT+5:30","haniprofessional.use@gmail.com","19","Rural","Education","11–20 km","Train/Metro","Electric vehicle","Yes","Always","Travel time;Comfort;Convenience;Availability","Traffic;Delays;Overcrowding;Poor connectivity","Yes","Walking;Cycling;Electric vehicles","4","1","4","4","Agree","Higher cost;Not easily available;Poor connectivity","Better connectivity","More trains"\n"2026/09/04 11:50:14 PM GMT+5:30","sadhanapal2607@gmail.com","19","Urban/City","Education","Less than 5 km","Train/Metro","Train/Metro","Yes","Rarely","Cost;Travel time;Environmental impact","Traffic;High cost;Delays;Overcrowding;Poor roads","Yes","Walking;Cycling;Train/Metro;Electric vehicles","3","3","3","3","Neutral","Higher cost","Better walking/cycling facilities","For Ambarnath, my suggestion would be to improve last-mile sustainable connectivity around the station area. Most people still depend on petrol autos for short distances, so if we introduce e-auto and e-rickshaw stands, mini e-bus shuttles for MIDC and residential areas, and proper cycle-sharing with safe footpaths, car and bike use will reduce a lot. Combined with increased frequency of local trains during peak hours and a simple carpool app for MIDC employees, it can make daily travel cheaper, cleaner, and less crowded."\n"2026/09/05 1:35:15 AM GMT+5:30","ankit010265ay@gmail.com","19","Urban/City","Education","More than 20 km","Train/Metro","Train/Metro","Yes","Always","Travel time;Comfort","Traffic;Delays;Overcrowding;Poor roads;Poor connectivity;Safety concerns;Pollution","Yes","Not sure","4","3","3","3","Neutral","Nothing","Better connectivity","“Improve public transportation and increase the number of electric buses.”"\n"2026/09/05 8:39:49 AM GMT+5:30","archanachauhan9029@gmail.com","19","Urban/City","Work","More than 20 km","Walking","Bus","Yes","Rarely","Cost","Delays","No","Train/Metro","2","2","3","4","Neutral","Nothing","Better safety","No suggestion "\n"2026/09/05 9:02:41 AM GMT+5:30","at579881@gmail.com","10","Rural","Education","More than 20 km","Bicycle","Walking","Yes","Always","Cost","Traffic;High cost;Delays;Overcrowding;Poor roads;Poor connectivity;Safety concerns;Pollution;None","No","Train/Metro;Electric vehicles;Shared transport","4","3","2","5","Disagree","Not easily available","Better walking/cycling facilities","Gobi"\n"2026/09/05 9:33:43 AM GMT+5:30","npd.miraclecables@gmail.com","27","Urban/City","Work","11–20 km","Train/Metro","Bus","Yes","Always","Convenience","Overcrowding","Yes","Electric vehicles","4","4","4","4","Strongly Agree","Not easily available","Faster service","no"\n"2026/09/05 10:57:52 AM GMT+5:30","kritikag164@gmail.com","19","Urban/City","Education","Less than 5 km","Train/Metro","Bicycle","Yes","Always","Availability","Delays;Overcrowding","No","Not sure","3","3","3","4","Strongly Disagree","Unreliable service","Better connectivity",".."\n"2026/09/05 11:02:32 AM GMT+5:30","piyushshekhawat13@gmail.com","16","Rural","Education","5–10 km","Train/Metro","Train/Metro","Yes","Always","Cost","Overcrowding","Yes","Train/Metro;Shared transport","5","2","5","1","Agree","Takes more time;Not easily available;Poor connectivity","Lower fares","1.      By providing good roads for transport.   2.      managing overcrowded train \n3.      By reducing delay and adding more compartment in train"\n"2026/09/05 12:39:04 PM GMT+5:30","yashikamahadeshwar@gmail.com","18","Urban/City","Education","5–10 km","Train/Metro","Train/Metro","Yes","Always","Cost;Travel time;Comfort;Convenience;Safety;Environmental impact","Traffic;Safety concerns","No","Walking;Cycling","4","3","5","3","Agree","Lack of awareness","More frequent services","Ntg"\n"2026/09/05 1:42:24 PM GMT+5:30","shreyapandey1189@gmail.com","21","Urban/City","Education","5–10 km","Walking","Bicycle","Yes","Always","Cost;Travel time;Comfort;Convenience;Availability;Safety","Traffic;High cost;Delays;Overcrowding;Poor roads","Yes","Walking;Cycling;Electric vehicles;Shared transport","5","5","5","5","Strongly Agree","Higher cost;Not easily available","Lower fares","Lower fares, easily available for everyone "\n"2026/09/05 2:33:04 PM GMT+5:30","kanojiyaabhishek211@gmail.com","18","Urban/City","Education","5–10 km","Two-wheeler","Train/Metro","No","Sometimes","Cost;Travel time;Availability","Traffic;Delays;Pollution","No","Train/Metro","4","3","4","3","Agree","Takes more time","Better walking/cycling facilities","mobility systems that lower greenhouse gas emissions, reduce environmental damage, and provide safe, affordable access for everyone"\n"2026/09/05 3:04:50 PM GMT+5:30","maryamkohari776@gmail.com","19","Urban/City","Education","11–20 km","Train/Metro","Train/Metro","Yes","Sometimes","Travel time;Availability","Delays;Overcrowding;Safety concerns","Yes","Walking;Cycling;Shared transport","4","4","4","2","Agree","Takes more time;Less comfort;Safety concerns;Unreliable service","More comfort","I\'d suggest investing more in reliable public transit and expanding bike lanes to make it easier to get around without a car. Better walking infrastructure and incentives for electric vehicles could also make a huge difference."\n"2026/09/05 6:16:00 PM GMT+5:30","tiwariastha305@gmail.com","19","Rural","Education","Less than 5 km","Auto/Rickshaw/Cab","Electric vehicle","Yes","Always","Safety","Poor roads","Yes","Electric vehicles","5","3","1","2","Strongly Agree","Less comfort","Faster service","Good"\n"2026/09/05 6:27:36 PM GMT+5:30","gaikwadpravin0085@gmail.com","19","Urban/City","Education","5–10 km","Two-wheeler","Bicycle","No","Always","Cost;Travel time;Comfort;Convenience;Availability","Poor connectivity;Safety concerns;Pollution","No","Bus;Train/Metro","5","5","5","5","Strongly Agree","Lack of awareness","Better walking/cycling facilities","Nothing "\n"2026/09/05 6:57:32 PM GMT+5:30","lalwanibhavesh360@gmail.com","22","Rural","Education","11–20 km","Train/Metro","Electric vehicle","No","Sometimes","Cost;Travel time;Comfort;Convenience;Availability","Traffic;High cost;Delays;Overcrowding;Poor roads","No","Bus;Train/Metro;Shared transport","3","4","3","1","Neutral","Safety concerns","More frequent services","Anything "\n"2026/09/05 7:15:16 PM GMT+5:30","dolassumit5@gmail.com","19","Urban/City","Education","Less than 5 km","Walking","Train/Metro","No","Sometimes","Cost;Travel time;Comfort;Convenience;Availability;Safety;Reliability;Environmental impact","Traffic;High cost;Delays;Overcrowding;Poor roads;Poor connectivity;Safety concerns;Pollution;None","No","Walking;Cycling;Bus;Train/Metro;Carpooling;Electric vehicles;Shared transport;Not sure","4","5","4","4","Neutral","Takes more time;Higher cost;Not easily available;Poor connectivity;Less comfort;Safety concerns;Unreliable service;Lack of awareness;Nothing","Better connectivity","My suggestion is to improve public transport, increase the number of electric buses, provide safe cycling and walking paths, and encourage carpooling. This will reduce traffic, pollution, and fuel consumption."\n"2026/09/05 7:16:06 PM GMT+5:30","deshmukhsanchit37@gmail.com","19","Suburban","Education","More than 20 km","Train/Metro","Train/Metro","Yes","Always","Travel time;Convenience;Availability;Safety;Environmental impact","Overcrowding","Yes","Walking;Cycling;Train/Metro;Shared transport","3","2","3","3","Agree","Not easily available","More frequent services","Increase the frequency of train and improve road  infrastructure to promote walking "\n"2026/09/05 7:52:05 PM GMT+5:30","rajanishtiwari99@gmail.com","21","Urban/City","Work","5–10 km","Walking","Electric vehicle","Yes","Always","Travel time","Traffic","Yes","Electric vehicles","5","5","5","5","Disagree","Safety concerns","Better connectivity","Good "\n"2026/09/05 8:16:29 PM GMT+5:30","bhagyashrikokne30@gmail.com","23","Urban/City","Work","11–20 km","Auto/Rickshaw/Cab","Train/Metro","Yes","Sometimes","Cost;Travel time;Comfort;Safety","Traffic;Delays;Overcrowding;Safety concerns","Yes","Walking;Bus;Train/Metro","5","4","4","3","Agree","Not easily available","Faster service","Nothing "\n"2026/09/05 11:36:42 PM GMT+5:30","pranavkale116@gmail.com","19","Urban/City","Work","11–20 km","Two-wheeler","Train/Metro","No","Sometimes","Comfort","Traffic;Poor roads","No","Walking","3","5","5","5","Neutral","Not easily available","Better connectivity","Petrol diesel price low"\n"2026/09/06 12:54:10 AM GMT+5:30","krishkatariya62@gmail.com","20","Suburban","Work","5–10 km","Two-wheeler","Carpooling/Ride sharing","Yes","Always","Availability","Traffic;Poor roads;Poor connectivity;Pollution","Yes","Cycling;Bus;Train/Metro;Shared transport","4","3","4","5","Strongly Agree","Not easily available;Poor connectivity;Less comfort;Unreliable service","Better connectivity","Just improve the road infrastructure "\n"2026/09/06 1:58:06 AM GMT+5:30","fantic919@gmail.com","30","Urban/City","Work","More than 20 km","Train/Metro","Carpooling/Ride sharing","Yes","Sometimes","Travel time;Comfort;Safety","Traffic;Overcrowding","No","Walking;Cycling;Train/Metro;Carpooling;Shared transport","3","3","3","3","Agree","Takes more time;Not easily available;Poor connectivity;Unreliable service","Faster service","It needs to have better availablity "\n"2026/09/06 12:18:41 PM GMT+5:30","sharvariamirgal@gmail.com","18","Urban/City","Education","More than 20 km","Train/Metro","Train/Metro","Yes","Always","Travel time","Delays","Yes","Walking;Train/Metro","5","4","5","5","Strongly Disagree","Nothing","Better walking/cycling facilities","Better roads for walking and cycling "\n"2026/09/06 1:10:12 PM GMT+5:30","vpss1794@gmail.com","29","Urban/City","Work","5–10 km","Train/Metro","Electric vehicle","Yes","Always","Availability","Traffic","Yes","Train/Metro","5","3","5","5","Strongly Agree","Higher cost;Not easily available;Poor connectivity;Less comfort;Safety concerns","More frequent services","to reduce the fair amount and increase transport vehicles "\n"2026/09/06 1:41:57 PM GMT+5:30","bhawanachouhan2007@gmail.com","26","Urban/City","Work","5–10 km","Train/Metro","Train/Metro","Yes","Always","Cost;Travel time","Overcrowding","Yes","Walking;Cycling;Train/Metro;Electric vehicles;Shared transport","5","4","5","5","Strongly Agree","Higher cost;Not easily available;Poor connectivity","Lower fares","More frequency of public transport"\n"2026/09/06 3:41:23 PM GMT+5:30","dikshakadam77199@gmail.com","20","Urban/City","Education","More than 20 km","Train/Metro","Train/Metro","Yes","Always","Cost;Travel time;Comfort;Availability;Safety","Delays;Overcrowding;Safety concerns","Yes","Walking;Cycling","3","4","4","4","Strongly Agree","Takes more time;Not easily available","Better safety","To make transportation more sustainable in Karjat, the town should introduce electric auto-rickshaws and improve local bus connections to the railway station."\n"2026/09/06 10:24:30 PM GMT+5:30","mishrashweta014@gmail.com","18","Suburban","Education","Less than 5 km","Walking","Train/Metro","Yes","Always","Travel time;Comfort;Convenience;Availability","Delays;Overcrowding;Pollution","No","Not sure","3","4","4","5","Neutral","Not easily available;Nothing","More comfort","Improve public transport, encourage electric vehicles, provide safe cycling and walking paths, and promote carpooling to reduce traffic and pollution."\n"2026/09/06 11:38:58 PM GMT+5:30","parshuramchalwadi539@gmail.com","20 ","Urban/City","Work","More than 20 km","Walking","Train/Metro","Yes","Always","Travel time;Environmental impact","Traffic;Delays;Overcrowding;Poor connectivity","Yes","Walking;Cycling;Train/Metro;Electric vehicles;Shared transport","5","5","5","5","Strongly Disagree","Takes more time;Higher cost;Not easily available;Lack of awareness","Better connectivity","Increase awareness "\n"2026/09/07 1:59:31 PM GMT+5:30","sandhyaselva2007@gmail.com","23","Urban/City","Work","11–20 km","Train/Metro","Train/Metro","Yes","Always","Cost","Poor connectivity","Yes","Train/Metro","5","3","3","5","Strongly Agree","Takes more time;Higher cost","More comfort","I am supporting "\n"2026/09/07 2:00:24 PM GMT+5:30","nishawankhede282@gmail.com","26","Urban/City","Education","5–10 km","Train/Metro","Train/Metro","Yes","Sometimes","Cost;Comfort;Availability","Traffic;High cost;Delays","Yes","Walking;Bus","4","3","5","4","Agree","Lack of awareness","More frequent services","-"\n"2026/09/07 2:01:38 PM GMT+5:30","aachaljy@gmail.com","30","Urban/City","Office","5–10 km","Train/Metro","Train/Metro","Yes","Always","Cost","Delays","Yes","Walking;Cycling;Bus","5","3","5","4","Agree","Takes more time;Higher cost;Not easily available","More comfort","If cost will be low "\n"2026/09/07 2:03:17 PM GMT+5:30","mitakshiiitalwarr.8@gmail.com","17","Urban/City","Education","11–20 km","Train/Metro","Train/Metro","Yes","Always","Travel time;Convenience","Overcrowding","No","Not sure","3","5","4","3","Agree","Not easily available;Less comfort","More frequent services","More availability of public transport "\n"2026/09/07 2:04:36 PM GMT+5:30","kastupatil263@gmail.com","21","Rural","Education","Less than 5 km","Two-wheeler","Train/Metro","Yes","Sometimes","Cost;Availability;Reliability","Delays;Poor roads;Poor connectivity","Yes","Cycling;Train/Metro;Electric vehicles","1","1","2","1","Agree","Lack of awareness","More frequent services","No"\n"2026/09/07 2:05:16 PM GMT+5:30","pruthvishinde9422@gmail.com","30","Urban/City","Work","11–20 km","Train/Metro","Train/Metro","Yes","Always","Travel time;Comfort","Traffic;Poor roads;Pollution","Yes","Walking;Cycling","4","3","5","4","Agree","Takes more time;Not easily available","More frequent services","For making sustainable transport easily available, they should focus in related concerns like road infrastructure, good faires and passanger comfort "\n"2026/09/07 2:08:40 PM GMT+5:30","shantiprajapat437@gmail.com","24","Urban/City","Education","Less than 5 km","Two-wheeler","Train/Metro","Yes","Sometimes","Travel time;Comfort;Convenience","Traffic;Pollution","Yes","Walking","5","4","4","3","Agree","Higher cost","More comfort","Improve public transportation, increase electric buses, and provide better walking and cycling facilities to reduce pollution and make transportation more sustainable."\n"2026/09/07 2:12:29 PM GMT+5:30","adityamaurya5060@gmail.com","Anchal Maurya","Suburban","Education","More than 20 km","Train/Metro","Walking","Yes","Always","Travel time;Environmental impact","Traffic;Delays","Yes","Walking;Train/Metro;Electric vehicles","5","5","5","1","Agree","Takes more time;Higher cost","Faster service","Anchal Maurya"\n"2026/09/07 2:13:03 PM GMT+5:30","ag012546@gmail.com","15","Suburban","Education","More than 20 km","Train/Metro","Electric vehicle","Yes","Sometimes","Travel time","Delays","Yes","Train/Metro","3","3","5","3","Agree","Safety concerns","More comfort","It should not be delay for more period"\n"2026/09/07 2:13:33 PM GMT+5:30","mumtajkh30@gmail.com","15","Suburban","Education","More than 20 km","Train/Metro","Train/Metro","Yes","Sometimes","Travel time","Overcrowding","No","Walking;Shared transport","4","4","3","5","Strongly Agree","Less comfort","Better connectivity","All should try to use less use of vehicles for short areas travelling "\n"2026/09/07 2:14:43 PM GMT+5:30","shamarehmani93@gmail.com","28","Suburban","Work","More than 20 km","Train/Metro","Train/Metro","Yes","Always","Comfort","Delays","No","Not sure","3","3","3","3","Agree","Higher cost","Faster service","-"\n"2026/09/07 2:14:51 PM GMT+5:30","ummeh7253@gmail.com","28","Suburban","Work","More than 20 km","Train/Metro","Train/Metro","Yes","Always","Comfort","Delays","No","Train/Metro","3","3","3","3","Agree","Higher cost","Better safety","-"\n"2026/09/07 2:16:02 PM GMT+5:30","rttiwari0108@gmail.com","29","Suburban","Work","More than 20 km","Train/Metro","Bicycle","Yes","Sometimes","Cost;Travel time;Convenience","Poor roads;Poor connectivity;Safety concerns","Yes","Bus;Carpooling","3","5","4","3","Disagree","Safety concerns;Unreliable service","Better safety","Availablity "\n"2026/09/07 2:18:29 PM GMT+5:30","kumkumsingh2301@gmail.com","28","Urban/City","Work","More than 20 km","Train/Metro","Train/Metro","Yes","Sometimes","Comfort;Availability;Safety","High cost;Delays","Yes","Walking;Cycling;Bus","4","5","3","5","Neutral","Takes more time;Higher cost;Lack of awareness","Lower fares","Availability of public transport "\n"2026/09/07 2:29:36 PM GMT+5:30","s78764813@gmail.com","16","Urban/City","Education","Less than 5 km","Walking","Walking","Yes","Sometimes","Cost","Traffic;High cost;Delays;Pollution","Yes","Walking;Electric vehicles","4","5","4","3","Neutral","Takes more time;Higher cost;Less comfort","Better safety","More comfort"\n"2026/09/07 2:29:58 PM GMT+5:30","virajgupta05134@gmail.com","16","Urban/City","Education","5–10 km","Walking","Autorickshaw ","Yes","Always","Cost;Travel time","Traffic;High cost;Overcrowding;Poor roads","No","Walking","5","4","5","5","Strongly Agree","Nothing","Better walking/cycling facilities","Better roads and lower fare prices "\n"2026/09/07 2:33:12 PM GMT+5:30","s96106831@gmail.com","16","Urban/City","Education","11–20 km","Two-wheeler","Train/Metro","Yes","Sometimes","Cost","Traffic","Yes","Train/Metro","4","2","3","3","Disagree","Less comfort","Faster service","Increase facilities"\n"2026/09/07 2:41:07 PM GMT+5:30","jagritidmaurya11@gmail.com","24","Suburban","Work","Less than 5 km","Train/Metro","Bicycle","Yes","Always","Travel time","Delays","Yes","Bus","1","3","5","3","Neutral","Takes more time","Lower fares","Improvement "\n"2026/09/07 2:41:21 PM GMT+5:30","aakmaurya027@gmail.com","24","Urban/City","Work","Less than 5 km","Train/Metro","Bicycle","Yes","Sometimes","Travel time","Traffic","Yes","Train/Metro","1","2","2","2","Agree","Takes more time","Lower fares","Improvement and development "\n"2026/09/07 2:44:08 PM GMT+5:30","varshakhushalani8@gmail.com","21","Rural","Education","11–20 km","Two-wheeler","Bus","Yes","Always","Travel time","Traffic;High cost;Poor roads","Yes","Bus","3","3","3","3","Neutral","Less comfort","More frequent services","My suggestion is to improve and promote public transportation in my area. More buses should be available, especially during peak hours, and routes should connect residential areas with schools, workplaces, and markets. We should also encourage cycling and walking by creating safe footpaths and bicycle lanes. Using electric buses and other electric vehicles can further reduce air pollution and carbon emissions."\n"2026/09/07 2:44:25 PM GMT+5:30","payalrohira050@gmail.com","20","Urban/City","Education","5–10 km","Two-wheeler","Train/Metro","Yes","Always","Cost;Travel time","Traffic;Poor roads","Yes","Shared transport","3","3","3","3","Agree","Higher cost;Not easily available","Better connectivity","..."\n"2026/09/07 2:44:59 PM GMT+5:30","nehawadhwa045@gmail.com","20","Urban/City","Education","5–10 km","Train/Metro","Walking","Yes","Always","Cost;Travel time;Comfort;Availability;Safety;Reliability;Environmental impact","Traffic;Delays;Overcrowding;Poor connectivity","Yes","Walking;Train/Metro;Shared transport","5","5","5","3","Neutral","Takes more time;Higher cost;Poor connectivity;Less comfort","Lower fares","Nothing"\n"2026/09/07 2:45:17 PM GMT+5:30","chaitalimasurkar13@gmail.com","20","Urban/City","Education","5–10 km","Auto/Rickshaw/Cab","Auto","Yes","Always","Travel time","Overcrowding","Yes","Bus","5","2","5","5","Agree","Takes more time","Lower fares","My suggestion for making transportation more sustainable in my area is to improve public transport facilities, encourage carpooling, and promote the use of electric vehicles. Creating safe cycling lanes and better walking paths can also help reduce pollution and traffic congestion."\n"2026/09/07 2:49:40 PM GMT+5:30","anjalishamnai@gmail.com","16","Urban/City","Education","Less than 5 km","Auto/Rickshaw/Cab","Electric vehicle","Yes","Always","Travel time;Comfort","Traffic","Yes","Electric vehicles","5","3","5","3","Strongly Agree","Takes more time","More frequent services","......"\n"2026/09/07 2:50:15 PM GMT+5:30","dewdasangeeta44@gmail.com","16","Urban/City","Education","Less than 5 km","Auto/Rickshaw/Cab","Walking","Yes","Always","Cost;Travel time;Safety","Traffic;High cost;Poor roads;Pollution","No","Not sure","1","2","1","1","Neutral","Takes more time;Safety concerns","Better safety","Roadsss"\n"2026/09/07 2:51:24 PM GMT+5:30","chiragasnani2008@gmail.com","18","Urban/City","Education","Less than 5 km","Two-wheeler","Walking","No","Always","Travel time","None","No","Not sure","1","1","5","5","Strongly Agree","Nothing","More comfort","Not sure "\n"2026/09/07 2:59:32 PM GMT+5:30","shuklaadarsh250610@gmail.com","16","Suburban","Education","Less than 5 km","Walking","Walking","No","Always","Availability","Delays","No","Walking","3","2","3","2","Agree","Higher cost","Lower fares","By train "\n"2026/09/07 3:02:42 PM GMT+5:30","ps7219472629@gmail.com","17","Urban/City","Education","5–10 km","Train/Metro","Electric vehicle","Yes","Always","Travel time","Traffic;High cost;Overcrowding;Safety concerns;Pollution","Yes","Walking;Train/Metro;Electric vehicles","5","3","1","3","Neutral","Not easily available","More comfort","Make road perfect "\n"2026/09/07 9:23:17 PM GMT+5:30","jaiswaranshika6@gmail.com","21","Urban/City","Work and job","11–20 km","Train/Metro","Car","Yes","Always","Travel time;Comfort;Safety;Environmental impact","Delays;Pollution","No","Walking;Train/Metro;Carpooling;Shared transport","5","5","4","4","Strongly Disagree","Higher cost;Poor connectivity;Safety concerns;Lack of awareness","More comfort","Yes"'

df = pd.read_csv(StringIO(CSV_DATA))

# Remove personal email information from the dashboard
for col in ["Email", "email", "Username", "username"]:
    if col in df.columns:
        df = df.drop(columns=[col])

# Clean column names
df.columns = [str(c).strip() for c in df.columns]

# ---------------------------------------------------------
# COLUMN NAMES FROM THE ACTUAL QUESTIONNAIRE
# ---------------------------------------------------------
age_col = "What is your age?"
area_col = "Which type of area do you currently live in?"
purpose_col = "What is the main purpose of your regular travel?"
distance_col = "How far do you usually travel in a day?"
mode_col = "What is your most frequently used mode of transport?"
weekly_mode_col = "Which of these transport modes do you use at least once in a typical week?"
public_col = "Do you use public transportation regularly?"
frequency_col = "How often do you use public or shared transport?"
factor_col = "Which factors affect your choice of transport? (Select all that apply)"
problem_col = "What problems do you usually face while travelling? (Select all that apply)"
awareness_col = "Before this survey, had you heard about sustainable transport?"
sustainable_col = "Which of the following do you consider sustainable transport? (Select all that apply)"
importance_col = "How important is sustainable transportation to you?"
availability_col = "How would you rate the availability of public transportation in your area?"
environment_col = "How important is environmental impact when choosing transport?"
willing_col = "How willing are you to switch to a more sustainable mode of transport?"
agreement_col = "Do you agree that sustainable transport can help reduce traffic and pollution?"
barrier_col = "What stops you from choosing sustainable transport more often? (Select all that apply)"
improvement_col = "Which improvement would encourage you most to use sustainable transport?"
suggestion_col = "What is your suggestion for making transportation more sustainable in your area?"

# Convert numeric columns
for col in [age_col, importance_col, availability_col, environment_col, willing_col]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# ---------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------
def multi_count(data, column):
    if column not in data.columns:
        return pd.Series(dtype="int64")
    values = (
        data[column]
        .dropna()
        .astype(str)
        .str.split(";")
        .explode()
        .str.strip()
    )
    return values[values != ""].value_counts()

def bar_chart(series, title, xlabel="", ylabel="Number of Responses"):
    if series.empty:
        st.info("No data available for the selected filters.")
        return
    fig, ax = plt.subplots(figsize=(9, 4.8))
    series.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

def pie_chart(series, title):
    # Pie charts become difficult to read when there are many small categories.
    # Use a clean horizontal bar chart for those cases.
    if series.empty or series.sum() == 0:
        st.info("No data available for the selected filters.")
        return
    if len(series) > 5:
        fig, ax = plt.subplots(figsize=(9, 5.5))
        values = series.sort_values()
        bars = ax.barh(values.index, values.values)
        ax.set_title(title)
        ax.set_xlabel("Number of Responses")
        ax.set_ylabel("")
        for bar, value in zip(bars, values.values):
            ax.text(
                bar.get_width() + max(values.values) * 0.01,
                bar.get_y() + bar.get_height() / 2,
                str(value),
                va="center"
            )
        ax.set_xlim(0, max(values.values) * 1.15)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
        return

    fig, ax = plt.subplots(figsize=(7, 5.5))
    wedges, _, autotexts = ax.pie(
        series.values,
        labels=None,
        autopct="%1.1f%%",
        startangle=90,
        pctdistance=0.72,
        wedgeprops={"width": 0.48, "edgecolor": "white"}
    )
    ax.set_title(title)
    ax.legend(
        wedges,
        [f"{name} ({value})" for name, value in series.items()],
        title="Categories",
        loc="center left",
        bbox_to_anchor=(1.0, 0.5)
    )
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------
page_header()
# ---------------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------------

st.sidebar.header("🔎 Filters")

cleaned_df = df.drop_duplicates().copy()
# Clean travel purpose names
cleaned_df[purpose_col] = cleaned_df[purpose_col].replace({
    "Work and job": "Work"
})
# Clean transport mode names
cleaned_df[mode_col] = cleaned_df[mode_col].replace({
    "Two Wheeler and Train": "Two-wheeler",
    "Autorickshaw": "Auto/Rickshaw/Cab"
})

# Use the cleaned dataset for analysis
filtered_df = cleaned_df.copy()

if area_col in cleaned_df.columns:
    options = sorted(cleaned_df[area_col].dropna().astype(str).unique())
    selected = st.sidebar.multiselect("Area Type", options, default=options)
    filtered_df = filtered_df[
        filtered_df[area_col].astype(str).isin(selected)
    ]

if purpose_col in cleaned_df.columns:

    # Original survey options
    options = [
        "Work",
        "Education",
        "Shopping",
        "Medical/Personal work",
        "Recreation",
        "Other"
    ]

    selected = st.sidebar.multiselect(
        "Travel Purpose",
        options,
        default=options
    )

    filtered_df = filtered_df[
        filtered_df[purpose_col].astype(str).isin(selected)
    ]

if mode_col in cleaned_df.columns:
    options = sorted(cleaned_df[mode_col].dropna().astype(str).unique())
    selected = st.sidebar.multiselect(
        "Main Transport Mode", options, default=options
    )
    filtered_df = filtered_df[
        filtered_df[mode_col].astype(str).isin(selected)
    ]
# ---------------------------------------------------------
# OVERVIEW
# ---------------------------------------------------------
st.header("📌 Survey Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Responses", len(filtered_df))

with c2:
    avg_age = filtered_df[age_col].mean() if age_col in filtered_df else None
    st.metric("Average Age", f"{avg_age:.1f}" if pd.notna(avg_age) else "N/A")

with c3:
    if mode_col in filtered_df.columns and len(filtered_df):
        st.metric("Most Used Mode", filtered_df[mode_col].value_counts().idxmax())
    else:
        st.metric("Most Used Mode", "N/A")

with c4:
    if awareness_col in filtered_df.columns and len(filtered_df):
        aware = (
            filtered_df[awareness_col].astype(str).str.strip().str.lower().eq("yes").sum()
        )
        st.metric("Aware Before Survey", f"{aware} responses")
    else:
        st.metric("Aware Before Survey", "N/A")

# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🧹 Data Cleaning",
    "🚌 Travel Habits",
    "🌱 Sustainability",
    "🚧 Problems & Barriers",
    "📊 Ratings",
    "🤖 ID3 Analysis",
    "💡 Suggestions"
])

# ---------------------------------------------------------
# DATA CLEANING
# ---------------------------------------------------------
with tab1:
    st.header("🧹 Data Cleaning")

    original_rows = len(df)
    duplicate_count = int(df.duplicated().sum())
    missing_total = int(df.isna().sum().sum())

    cleaned_df = df.drop_duplicates().copy()

    for col in cleaned_df.select_dtypes(include="object").columns:
        cleaned_df[col] = (
            cleaned_df[col].astype(str).str.strip()
            .replace({"": pd.NA, "nan": pd.NA})
        )

    for col in [age_col, importance_col, availability_col,
                environment_col, willing_col]:
        if col in cleaned_df.columns:
            cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors="coerce")

    remaining_rows = len(cleaned_df)
    removed_rows = original_rows - remaining_rows

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Original Records", original_rows)
    with c2:
        st.metric("Duplicate Records", duplicate_count)
    with c3:
        st.metric("Missing Values", missing_total)
    with c4:
        st.metric("Clean Records", remaining_rows)

    st.subheader("Cleaning Summary")
    cleaning_summary = pd.DataFrame({
        "Check": [
            "Original records", "Duplicate records", "Records removed",
            "Records after duplicate removal", "Missing values before cleaning"
        ],
        "Result": [
            original_rows, duplicate_count, removed_rows,
            remaining_rows, missing_total
        ]
    })
    st.dataframe(cleaning_summary, use_container_width=True, hide_index=True)

    st.subheader("Missing Values by Column")
    missing_by_column = df.isna().sum().reset_index()
    missing_by_column.columns = ["Column", "Missing Values"]
    missing_by_column = missing_by_column[missing_by_column["Missing Values"] > 0]

    if len(missing_by_column):
        st.dataframe(missing_by_column, use_container_width=True, hide_index=True)
    else:
        st.success("No missing values found.")

    st.subheader("Cleaned Dataset Preview")
    st.dataframe(cleaned_df.head(20), use_container_width=True, hide_index=True)

# ---------------------------------------------------------
# TRAVEL HABITS
# ---------------------------------------------------------
with tab2:
    st.header("🚌 Transportation Habits")

    col1, col2 = st.columns(2)

    with col1:
        if purpose_col in filtered_df:
            bar_chart(filtered_df[purpose_col].value_counts(),
                      "Main Purpose of Regular Travel")

    with col2:
        if distance_col in filtered_df:
            bar_chart(filtered_df[distance_col].value_counts(),
                      "Daily Travel Distance")

    if mode_col in filtered_df:
        st.subheader("Most Frequently Used Transport")
        pie_chart(filtered_df[mode_col].value_counts(),
                  "Most Frequently Used Transport Mode")

    col3, col4 = st.columns(2)

    with col3:
        if public_col in filtered_df:
            bar_chart(filtered_df[public_col].value_counts(),
                      "Regular Public Transportation Use")

    with col4:
        if frequency_col in filtered_df:
            bar_chart(filtered_df[frequency_col].value_counts(),
                      "Public / Shared Transport Frequency")

    if weekly_mode_col in filtered_df:
        st.subheader("Transport Modes Used at Least Once a Week")
        bar_chart(multi_count(filtered_df, weekly_mode_col),
                  "Weekly Transport Mode Usage")

# ---------------------------------------------------------
# SUSTAINABILITY
# ---------------------------------------------------------
with tab3:
    st.header("🌱 Sustainability Awareness")

    col1, col2 = st.columns(2)

    with col1:
        if awareness_col in filtered_df:
            pie_chart(filtered_df[awareness_col].value_counts(),
                      "Awareness of Sustainable Transport")

    with col2:
        if agreement_col in filtered_df:
            bar_chart(filtered_df[agreement_col].value_counts(),
                      "Sustainable Transport Can Reduce Traffic & Pollution")

    if sustainable_col in filtered_df:
        st.subheader("Modes Considered Sustainable")
        bar_chart(multi_count(filtered_df, sustainable_col),
                  "Transport Modes Considered Sustainable")

# ---------------------------------------------------------
# PROBLEMS & BARRIERS
# ---------------------------------------------------------
with tab4:
    st.header("🚧 Problems and Barriers")

    if factor_col in filtered_df:
        st.subheader("Factors Affecting Transport Choice")
        bar_chart(multi_count(filtered_df, factor_col),
                  "Factors Affecting Transport Choice")

    if problem_col in filtered_df:
        st.subheader("Problems Faced While Travelling")
        bar_chart(multi_count(filtered_df, problem_col),
                  "Problems Faced While Travelling")

    if barrier_col in filtered_df:
        st.subheader("Barriers to Choosing Sustainable Transport")
        bar_chart(multi_count(filtered_df, barrier_col),
                  "Barriers to Sustainable Transport")

# ---------------------------------------------------------
# RATINGS
# ---------------------------------------------------------
with tab5:
    st.header("📊 Rating Analysis")

    rating_data = {}

    if importance_col in filtered_df:
        rating_data["Sustainable Transport Importance"] = filtered_df[importance_col].mean()

    if availability_col in filtered_df:
        rating_data["Public Transport Availability"] = filtered_df[availability_col].mean()

    if environment_col in filtered_df:
        rating_data["Environmental Impact Importance"] = filtered_df[environment_col].mean()

    if willing_col in filtered_df:
        rating_data["Willingness to Switch"] = filtered_df[willing_col].mean()

    if rating_data:
        ratings = pd.Series(rating_data).round(2)
        st.dataframe(ratings.rename("Average Rating (1–5)").to_frame(),
                     use_container_width=True)
        bar_chart(ratings, "Average Survey Ratings",
                  ylabel="Average Rating")

    if willing_col in filtered_df:
        st.subheader("Willingness to Switch")
        counts = filtered_df[willing_col].value_counts().sort_index()
        bar_chart(counts, "Willingness Rating Distribution",
                  xlabel="Rating (1 = Not Willing, 5 = Very Willing)")
# ---------------------------------------------------------
# ID3 ANALYSIS
# ---------------------------------------------------------
with tab6:
    st.header("🤖 ID3 Analysis")

    result = id3.run(cleaned_df)

    st.metric(
        "ID3 Accuracy",
        f"{result['accuracy'] * 100:.2f}%"
    )

    st.write("**Root Attribute:**", result["root"])

    st.subheader("Feature Importance")
    st.dataframe(
        result["feature_importance"].to_frame("Importance"),
        use_container_width=True
    )

    st.subheader("Confusion Matrix")
    st.write(result["confusion_matrix"])
# ---------------------------------------------------------
# SUGGESTIONS
# ---------------------------------------------------------
with tab7:
    st.header("💡 Improvements and Suggestions")

    if improvement_col in filtered_df:
        st.subheader("Improvement That Would Encourage Sustainable Transport")
        bar_chart(filtered_df[improvement_col].value_counts(),
                  "Most Requested Improvements")

    if suggestion_col in filtered_df:
        st.subheader("Respondents' Suggestions")
        suggestions = filtered_df[[suggestion_col]].dropna()
        st.dataframe(
            suggestions.rename(columns={suggestion_col: "Suggestion"}),
            use_container_width=True,
            height=400
        )

# ---------------------------------------------------------
# KEY INSIGHTS
# ---------------------------------------------------------
st.markdown("---")
st.header("🔎 Key Insights")

if len(filtered_df):
    if mode_col in filtered_df:
        counts = filtered_df[mode_col].value_counts()
        st.write(
            f"• **{counts.idxmax()}** is the most frequently used transport mode "
            f"({counts.max()} responses)."
        )

    if purpose_col in filtered_df:
        st.write(
            f"• The most common purpose of regular travel is "
            f"**{filtered_df[purpose_col].value_counts().idxmax()}**."
        )

    if awareness_col in filtered_df:
        aware = (
            filtered_df[awareness_col].astype(str).str.strip().str.lower().eq("yes").sum()
        )
        st.write(
            f"• **{aware / len(filtered_df) * 100:.1f}%** of respondents "
            f"had heard about sustainable transport before the survey."
        )

    if willing_col in filtered_df:
        st.write(
            f"• Average willingness to switch to sustainable transport: "
            f"**{filtered_df[willing_col].mean():.2f}/5**."
        )

    if improvement_col in filtered_df:
        st.write(
            f"• The most selected improvement is "
            f"**{filtered_df[improvement_col].value_counts().idxmax()}**."
        )
else:
    st.warning("No responses match the selected filters.")

st.markdown("---")
st.caption(
    "Field Project: Sustainable Transport Choices | "
    "Python • Pandas • Matplotlib • Streamlit"
)
