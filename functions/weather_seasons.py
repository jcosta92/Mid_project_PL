#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#getting the weather seasons
def get_season(month, day):
    if (month == 12 and day >= 21) or (month == 3 and day < 20) or (month == 1 or month == 2):
        return 'Winter'
    elif (month == 3 and day >= 20) or (month == 6 and day < 21) or (month == 4 or month == 5):
        return 'Spring'
    elif (month == 6 and day >= 21) or (month == 9 and day < 22) or (month == 7 or month == 8):
        return 'Summer'
    else:
        return 'Autumn'

