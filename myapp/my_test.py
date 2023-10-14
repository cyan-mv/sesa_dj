# # i would like to use this script "my_test.py", using the values retrieved from the form, can you help me ?  

from django.db import models
from myapp.models import Region, DataEntry
from random import randint

def insert_data_db(region, category, values):
    DataEntry.objects.create(region=region, category=category, values=values)


# Function to get or create a region by name
def get_or_create_region(name):
    region, created = Region.objects.get_or_create(name=name)
    return region

# Assuming you have created instances of Region for region1 and region2
""" region1 = get_or_create_region('region1')
region2 = get_or_create_region('region2')

# Insert data for region1
DataEntry.objects.create(region=region1, category='comunidad', values=[randint(1,10), randint(1,10)])
DataEntry.objects.create(region=region1, category='primer nivel', values=[randint(1,10), randint(1,10)])
DataEntry.objects.create(region=region1, category='segundo nivel', values=[randint(1,10), randint(1,10)])
DataEntry.objects.create(region=region1, category='centros', values=[randint(1,10), randint(1,10)])


# Insert data for region2
DataEntry.objects.create(region=region2, category='comunidad', values=[randint(1,10), randint(1,10)])
DataEntry.objects.create(region=region2, category='primer nivel', values=[randint(1,10), randint(1,10)])
DataEntry.objects.create(region=region2, category='segundo nivel', values=[randint(1,10), randint(1,10)])
DataEntry.objects.create(region=region2, category='centros', values=[randint(1,10), randint(1,10)])
 """