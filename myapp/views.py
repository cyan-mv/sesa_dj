from django.shortcuts import render, redirect
from django.http import HttpResponse
from .create_excel import create_excel  # Import your script function
from .models import Region, DataEntry 
from .my_test import insert_data_db, get_or_create_region
from random import randint
from django.contrib import messages

def home(request):
    # Fetch all data entries
    data_entries = DataEntry.objects.all()
    # Organize data into the desired dictionary format
    data_dict = {}
    for entry in data_entries:
        region_name = entry.region.name
        category = entry.category
        values = entry.values

        if region_name not in data_dict:
            data_dict[region_name] = {}

        data_dict[region_name][category] = values
    
    # Pass the data dictionary to the template
    context = {'data_entries': data_entries, 'data_dict': data_dict}
    #context = {'data_entries': data_entries}
    # return render(request, 'index.html', context)
    return render(request, 'test.html', context)

def data_dummy(request): 
    # Assuming you have created instances of Region for region1 and region2
    region1 = get_or_create_region('region1')
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

    return HttpResponse("dummy data generated")

def save_data(request):
    if request.method == 'POST':
       
        region_name = "region1"
        
        # Get or create the region
        region = get_or_create_region(region_name)

        # Extract data from the form
        categories = ['comunidad', 'primer nivel', 'segundo nivel', 'centros']
        for category in categories:
            value_1 = int(request.POST.get(f'{category}_1', randint(1, 10)))
            value_2 = int(request.POST.get(f'{category}_2', randint(1, 10)))

            # Call the function in my_test.py to insert data
            insert_data_db(region, category, [value_1, value_2])

        data_entries = DataEntry.objects.all()
    
        data_dict = {}
        for entry in data_entries:
            region_name = entry.region.name
            category = entry.category
            values = entry.values

            if region_name not in data_dict:
                data_dict[region_name] = {}

            data_dict[region_name][category] = values

        """ data_dict = {'region1': {'comunidad': [4, 8], 'primer nivel': [1, 6], 'segundo nivel': [4, 8], 'centros': [1, 6]}, 'region2': {'comunidad': [1, 7], 'primer nivel': [10, 6], 'segundo nivel': [3, 4], 'centros': [10, 6]}} """
        """ data_dict = {
    "region1": {
        "comunidad": [1, 2],
        "primer nivel": [1, 3],
        "segundo nivel": [1, 4],
        "centros": [1, 5]
    },
    "region2": {
        "comunidad": [8, 6],
        "primer nivel": [8, 7],
        "segundo nivel": [8, 8],
        "centros": [8, 9]
    }} """
        data_dict["region2"] = {
            "comunidad": [randint(1,10), randint(1,10)],
            "primer nivel": [randint(1,10), randint(1,10)],
            "segundo nivel": [randint(1,10), randint( 1,10)],
            "centros": [randint(1,10), randint(1,10)]
        }
        create_excel(data_dict)  # Call your script function
        
        print(data_dict)
        return HttpResponse(data_dict)
        
        
    return HttpResponse("Invalid request method")


def delete_all_regions_view(request):
    # Delete all regions
    Region.objects.all().delete()
    return HttpResponse("Deleted all regions")

def create_region(request):
    if request.method == 'POST':
        form = RegionDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_regions')
    else:
        form = RegionDataForm()

    return render(request, 'create_region.html', {'form': form})

def run_script(request):
    # Assuming your data is defined somewhere or you fetch it dynamically
    """ regions = Region.objects.all()

    for region in regions:
            data[region.region_name] = {
                "comunidad": region.comunidad,
                "primer nivel": region.primer_nivel,
                "segundo nivel": region.segundo_nivel,
                "centros": region.centros
            } """

    data_dict = {
        "region1": {
            "comunidad": [1, 2],
            "primer nivel": [1, 3],
            "segundo nivel": [1, 4],
            "centros": [1, 5]
        },
        "region2": {
            "comunidad": [8, 6],
            "primer nivel": [8, 7],
            "segundo nivel": [8, 8],
            "centros": [8, 9]
        }
    }
    """ data_entries = DataEntry.objects.all()
    data_dict = {}

    for entry in data_entries:
        region_name = entry.region.name
        category = entry.category
        values = entry.values

        if region_name not in data_dict:
            data_dict[region_name] = {}

        data_dict[region_name][category] = values """

    create_excel(data_dict)  # Call your script function

    return HttpResponse("Script executed successfully")

def save_data_2(request):
    if request.method == 'POST':
        return HttpResponse("gooooood")

