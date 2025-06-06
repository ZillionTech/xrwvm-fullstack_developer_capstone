from django.db import transaction
from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    with transaction.atomic():
        car_make_instances = [CarMake(name=d['name'], description=d['description']) for d in car_make_data]
        CarMake.objects.bulk_create(car_make_instances)

        # Refresh from DB to get IDs (since bulk_create doesn't return them)
        car_make_instances = list(CarMake.objects.filter(name__in=[d['name'] for d in car_make_data]))

        # Map name to instance for lookup
        car_make_map = {make.name: make for make in car_make_instances}

        car_model_data = [
            {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_map['NISSAN']},
            {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_map['NISSAN']},
            {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_map['NISSAN']},
            {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_map['Mercedes']},
            {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_map['Mercedes']},
            {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_map['Mercedes']},
            {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_map['Audi']},
            {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_map['Audi']},
            {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_map['Audi']},
            {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_map['Kia']},
            {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_map['Kia']},
            {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_map['Kia']},
            {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_map['Toyota']},
            {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_map['Toyota']},
            {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_map['Toyota']},
        ]

        car_model_instances = [CarModel(name=d['name'], type=d['type'], year=d['year'], car_make=d['car_make']) for d in car_model_data]
        CarModel.objects.bulk_create(car_model_instances)

    print("Data inserted successfully!")
