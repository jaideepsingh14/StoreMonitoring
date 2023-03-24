import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def store(request):
    populateDatabase()
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def populateDatabase():
    with open('timezone.csv', mode='r') as file:
        csvFile = csv.reader(file)
        i=0
        for lines in csvFile:
            print(lines)
            i+=1
            if i==100:
                break