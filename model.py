import pandas as pd

from user_info import get_information

attractions_spec = pd.read_csv("AttractionsSpec.csv", sep = ";")
attractions_dist = pd.read_csv("AttractionsDist.csv", sep = ";")
attractions_spec = attractions_spec.replace("T":True, "F": False)

response_dict = get_information()


def information_parser(response_dict):
    spec_df = attractions_spec[(attractions_spec["MinAge"] <= response_dict["Age"]) | (attractions_spec["MinAge"].isna())]
    spec_df = spec_df[(spec_df["MinHeight"] <= response_dict["Height"]) | (spec_df["MinHeight"].isna())]
    spec_df = spec_df[(spec_df["MaxAge"] > response_dict["Age"]) | (spec_df["MaxAge"].isna())]
    spec_df = spec_df[(spec_df["MaxHeight"] > response_dict["Height"]) | (spec_df["MaxHeight"].isna())]
    if response_dict["Water"] == "no":
        spec_df = spec_df[spec_df["Water"] == True ]
    if response_dict["Parent"] == "no":
        spec_df = spec_df[(spec_df["AgeAlone"] <= response_dict["Age"]) | (spec_df["AgeAlone"].isna())]
        spec_df = spec_df[(spec_df["HeightAlone"] <= response_dict["Height"]) | (spec_df["HeightAlone"].isna())]
    return spec_df
