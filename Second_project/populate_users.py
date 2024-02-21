import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Second_project.settings')

import django
django.setup()


import random 
from AppTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=10):
    for entry in range(N):
        # get the topic for the entry
       
        fake_name = fakegen.name().split()
        fake_firstname = fake_name[0]
        fake_lastname = fake_name[1]
        fake_email = fakegen.email()

        

        # create the new web page entry
        user = User.objects.get_or_create(firstname=fake_firstname,
                                          lastname= fake_lastname,
                                          Email=fake_email)[0]



if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")