import pandas as pd

from user_info import get_information
from updates import internal_update

def working_attractions(attractions_spec):
    return attractions_spec[attractions_spec["IsItOpen"] == True]     

def information_parser(attractions_spec):
    spec_df = internal_update(attractions_spec)
    response_dict = get_information(spec_df)
    spec_df = working_attractions(spec_df)
    spec_df = spec_df[(spec_df["MinAge"] <= response_dict["Age"]) | (spec_df["MinAge"].isna())]
    spec_df = spec_df[(spec_df["MinHeight"] <= response_dict["Height"]) | (spec_df["MinHeight"].isna())]
    spec_df = spec_df[(spec_df["MaxAge"] > response_dict["Age"]) | (spec_df["MaxAge"].isna())]
    spec_df = spec_df[(spec_df["MaxHeight"] > response_dict["Height"]) | (spec_df["MaxHeight"].isna())]
    if response_dict["Water"] == "no":
        spec_df = spec_df[spec_df["Water"] == True ]
    if response_dict["Parent"] == "no":
        spec_df = spec_df[(spec_df["AgeAlone"] <= response_dict["Age"]) | (spec_df["AgeAlone"].isna())]
        spec_df = spec_df[(spec_df["HeightAlone"] <= response_dict["Height"]) | (spec_df["HeightAlone"].isna())]
    return spec_df
