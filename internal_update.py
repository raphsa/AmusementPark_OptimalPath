

def attractions_closed():
    att_news = input("Has any attraction just closed?\n").strip().lower()
    if att_news == "yes":
        att_closed = input("Digit separating by comma the attraction/s that has closed\n").strip().lower().replace(""," ")
        att_closed = att_closed.split(",")
    attractions_spec.loc[attractions_spec["Attraction"].isin(att_closed), "IsItOpen"] = False
    return attractions_spec

def attraction_open():
    att_news = input("Has any attraction just opened?\n").strip().lower()
    if att_news == "yes":
        att_opened = input("Digit separating by comma the attraction/s that has opened\n").strip().lower().replace(""," ")
        att_opened = att_opened.split(",")
    attractions_spec.loc[attractions_spec["Attraction"].isin(att_opened), "IsItOpen"] = True
    return attractions_spec


def queue_update():
    pass