#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def determine_location(city):
    if city in ["Liverpool",'West Bromwich',"Manchester","Burnley","Leicester","Stoke",
                "Wolverhampton","Birmingham","Norwich","Sheffield","Nottingham"]:
        return 'Center'
    elif city in ["Newcastle upon Tyne","Huddersfield","Leeds"]:
        return 'North'
    elif city in ["London","Southampton","Watford","Brighton and Hove","Bournemouth","Swansea","Cardiff","Brentford"]:
        return 'South'

