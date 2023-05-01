#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### splitting the time of the day in 3

def get_time_of_day(hour):
    if hour < 14:
        return 'Lunch'
    elif hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'

