import pandas as pd

from model import information_parser

numerical_col = ["Xpos","Ypos","WaitingTime","AvgWaitingTime","MinAge","MinHeight","AgeAlone","HeightAlone","MaxAge","MaxHeight"]

attractions_spec = pd.read_csv("AttractionsSpec.csv", sep = ";", dtype={col: float for col in numerical_col})
attractions_dist = pd.read_csv("AttractionsDist.csv", sep = ";")
attractions_spec = attractions_spec.replace({"T":True, "F": False})

information_parser(attractions_spec)