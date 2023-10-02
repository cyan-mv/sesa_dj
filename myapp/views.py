from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run


def home(request):
    return render(request, 'index.html')

def generate_excel(request):
    # Run your script
    run(["python", "generate_excel.py"])
    result = run(["python", "myapp/generate_excel.py"], capture_output=True, text=True)
    print("Script Output:", result.stdout)
    print("Script Error:", result.stderr)

    # You can customize the response message if needed
    return HttpResponse("Excel file generation initiated.")
