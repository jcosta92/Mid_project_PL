#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def determine_nightfall(row):
    
    fixed_date = datetime.datetime(2000, 1, 1)
    sunset = datetime.datetime.strptime(row["sunset"], "%H:%M:%S").time()
    time = datetime.datetime.combine(fixed_date, row["Time"]).time()
    time_plus_one_hour = (datetime.datetime.combine(fixed_date, row["Time"]) + datetime.timedelta(hours=1)).time()
    time_plus_three_hours = (datetime.datetime.combine(fixed_date, row["Time"]) + datetime.timedelta(hours=3)).time()

    if sunset < time:
        return "Night"
    elif sunset <= time_plus_one_hour:
        return "Night is falling"
    else:
        return "Day"

