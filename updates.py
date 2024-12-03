import pandas as pd
import numpy as np

def close_attractions(attractions_spec):
    att_news = input("Has any attraction just closed? (\"yes\" or \"no\")\n").strip().lower()
    if att_news == "yes":
        att_closed = input("Digit separating by comma the attraction/s that has closed\n").strip().lower().replace(" ","")
        att_closed = att_closed.split(",")
    else:
        return attractions_spec
    attractions_spec.loc[attractions_spec["Attraction"].str.lower().isin(att_closed), "IsItOpen"] = False
    return attractions_spec

def open_attractions(attractions_spec):
    att_news = input("Has any attraction just opened? (\"yes\" or \"no\")\n").strip().lower()
    if att_news == "yes":
        att_opened = input("Digit separating by comma the attraction/s that has opened\n").strip().lower().replace(" ","")
        att_opened = att_opened.split(",")
    else:
        return attractions_spec
    attractions_spec.loc[attractions_spec["Attraction"].str.lower().isin(att_opened), "IsItOpen"] = True
    return attractions_spec


def queue_update(attractions_spec):
    print("Update me on the queues of the attractions.")
    while True:
        print("(Indicate queues in minutes and separate it by comma, \"None\" if no news).")
        queue_news = input("The order of the queue has to be:\n (Reset,Divertical,BluRiver,iSpeed,Carousel,FlyingArturo,CasaMatta,MiniRapide,LeprottoExpress,AutoSplash,Raratonga,EuroWheel,MotionSphere,Simulators,KiddyMonster,DiavelRing,DesmoRace,MasterThai,Katun,RioBravo,ElDoradoFalls,GoldDigger,GeronimosTower,OilTower1,OilTower2,AquilaTonante,BuffaloBillRodeo,RaptoTana,Reptilium,Rexplorer,Bicisauro,Monosauro)\nIMPORTANT: YOU HAVE TO DIGIT 32 VALUES\n").strip().replace(" ","")
        if queue_news == "none":
            return attractions_spec
        queue_news = queue_news.split(",")
        queue_news = [0 if x == "" else x for x in queue_news]
        for index, value in enumerate(queue_news):
            try:
                queue_news[index] = int(value)
            except:
                print("Some attractions queue times has not been written in the correct format, please digit it again.")
        if index == attractions_spec.shape[0]-1:
            break
    
    queue_news = pd.Series(queue_news)
    attractions_spec.loc[queue_news != "", "WaitingTime"] = queue_news[queue_news != ""].astype(int)
    attractions_spec["WaitingTime"] = attractions_spec["WaitingTime"].fillna(0)
    return attractions_spec
    
def internal_update(attractions_spec):
    df_update = open_attractions(attractions_spec)
    df_update = close_attractions(df_update)
    df_update = queue_update(df_update)
    return df_update