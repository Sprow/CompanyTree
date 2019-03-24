from django.core.management.base import BaseCommand

from accounts.models import User
from random import randint
import datetime

# python manage.py add_random_accounts NUMBER OF ACCOUNTS YOUR WHANT TO CREATE


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('amount_of_workers', type=int)

    def handle(self, *args, **options):
        amount_of_workers = options['amount_of_workers']

        def make_random_acc(amount_of_workers):
            first_name_list = ['Ressie', 'Carmine', 'Chi', 'Keeley', 'Dung', 'Richelle', 'Mari', 'Sal', 'Cecil',
                               'Nicole',
                               'Janee', 'Rigoberto', 'Katheleen', 'Lyman', 'Esteban', 'Madison', 'Shaquana', 'Rickie',
                               'Olin', 'Billie', 'Warner', 'Claud', 'Cornelius', 'Cyril', 'Robert', 'Regalado',
                               'Kendrick',
                               'Woodrow', 'Alex', 'Willy']
            last_name_list = ['Speelman', 'Page', 'Kindell', 'Mclees', 'Marion', 'Lenihan', 'Meister', 'Obyrne',
                              'Rhymes',
                              'Beech', 'Caudill', 'Mcfadin', 'Vigna', 'Koss', 'Stonerock', 'Lundin', 'Biro', 'Coupe',
                              'Persing', 'Fast', 'Zawislak', 'Gholston', 'Yadao', 'Dugal', 'Aucoin', 'Regalado',
                              'Fonner',
                              'Lacourse', 'Cool', 'Dodrill']
            workers_list = {5: [], 4: [], 3: [], 2: [], 1: []}
            for i in range(1, amount_of_workers+1):
                if i == 1:
                    level = 5
                elif i <= amount_of_workers/100*5:
                    level = 4
                    id_min, id_max = 1, 1
                elif i <= amount_of_workers/100*15:
                    level = 3
                    id_min, id_max = 2, amount_of_workers / 100 * 5
                elif i <= amount_of_workers/100*45:
                    level = 2
                    id_min, id_max = amount_of_workers / 100 * 5, amount_of_workers / 100 * 30
                else:
                    level = 1
                    id_min, id_max = amount_of_workers / 100 * 30, amount_of_workers / 100 * 55

                rand_first_name = first_name_list[randint(0, len(first_name_list)-1)]

                rand_last_name = last_name_list[randint(0, len(last_name_list)-1)]

                rand_username = rand_first_name+rand_last_name+str(i)

                rand_password = rand_last_name+str(i)

                now = datetime.datetime.now()
                rand_date_joined = datetime.datetime(now.year - randint(0, 10),
                                                     now.month - randint(0, now.month - 1),
                                                     now.day - randint(0, now.day - 1))

                rand_salary = randint(10, 30) * pow(10, level)

                if level == 5:
                    rand_position = "boss"
                else:
                    rand_position = "Position" + str(randint(1, 1000))

                workers_list[level].append(rand_username)

                if i == 1:
                    rand_parent_id = None
                else:
                    rand_parent_id = randint(id_min, id_max)

                User.objects.create(parent_id=rand_parent_id,
                                    username=rand_username,
                                    password=rand_password,
                                    first_name=rand_first_name,
                                    last_name=rand_last_name,
                                    date_joined=rand_date_joined,
                                    salary=rand_salary,
                                    position=rand_position)
        make_random_acc(amount_of_workers)
