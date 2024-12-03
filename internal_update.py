import pandas as pd
import numpy as np

def attractions_closed():
    att_news = input("Has any attraction just closed?\n").strip().lower()
    if att_news == "yes":
        att_closed = input("Digit separating by comma the attraction/s that has closed\n").strip().lower().replace(" ","")
        att_closed = att_closed.split(",")
    attractions_spec.loc[attractions_spec["Attraction"].isin(att_closed), "IsItOpen"] = False
    return attractions_spec

def attraction_open():
    att_news = input("Has any attraction just opened?\n").strip().lower()
    if att_news == "yes":
        att_opened = input("Digit separating by comma the attraction/s that has opened\n").strip().lower().replace(" ","")
        att_opened = att_opened.split(",")
    attractions_spec.loc[attractions_spec["Attraction"].isin(att_opened), "IsItOpen"] = True
    return attractions_spec


def queue_update():
    print("Update me on the queues of the attractions.")
    while True:
        print("(Indicate queues in minutes and separate it by comma, \"None\" if no news).\n")
        queue_news = input("The order of the queue has to be:\n (Reset,Divertical,BluRiver,iSpeed,Carousel,FlyingArturo,CasaMatta,MiniRapide,LeprottoExpress,AutoSplash,Raratonga,EuroWheel,MotionSphere,Simulators,KiddyMonster,DiavelRing,DesmoRace,MasterThai,Katun,RioBravo,ElDoradoFalls,GoldDigger,GeronimosTower,OilTower1,OilTower2,AquilaTonante,BuffaloBillRodeo,RaptoTana,Reptilium,Rexplorer,Bicisauro,Monosauro)").strip().lower()
        queue_news = queue_news.split(",")
        for index, value in enumerate(queue_news):
            try:
                queue_news[index] = int(value)
                if index == len(queue_news)-1:
                    break
            except:
                print("Some attractions queue times has not been written in the correct format, please digit it again.")
    queue_news = pd.Series(queue_news)
    attractions_spec.loc[queue_news != "", "WaitingTime"] = queue_news[queue_news != ""].astype(int)
    attractions_spec["WaitingTime"] = attractions_spec["WaitingTime"].fillna(0)
    return attractions_spec
    
