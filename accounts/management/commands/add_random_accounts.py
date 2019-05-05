from django.core.management.base import BaseCommand

from django_seed import Seed


from accounts.models import User
from random import randint
# import datetime

# python manage.py add_random_accounts NUMBER OF ACCOUNTS YOUR WANT TO CREATE


class MySeed:
    def __init__(self, amount_of_workers):
        self.amount_of_workers = amount_of_workers
        self.first_name = self.first_name_list[randint(0, len(self.first_name_list)-1)]
        self.last_name = self.last_name_list[randint(0, len(self.last_name_list)-1)]
        self.lvl3 = [i for i in range(2, int(self.amount_of_workers / 100 * 5)-1)]
        self.lvl4 = [i for i in range(int(self.amount_of_workers / 100 * 5), int(self.amount_of_workers / 100 * 15)-1)]
        self.lvl5 = [i for i in range(int(self.amount_of_workers / 100 * 15), int(self.amount_of_workers / 100 * 45))]
        # self.lvl_3_min = 2
        # self.lvl_3_max = (self.amount_of_workers / 100 * 5)-1
        # self.lvl_4_min = self.amount_of_workers / 100 * 5
        # self.lvl_4_max = (self.amount_of_workers / 100 * 15)-1
        # self.lvl_5_min = self.amount_of_workers / 100 * 15
        # self.lvl_5_max = (self.amount_of_workers / 100 * 45)-1
        self.lvl_3_min = 1
        self.lvl_3_max = int((self.amount_of_workers / 100 * 5)-1)
        self.lvl_4_min = int((self.amount_of_workers / 100 * 5)-1)
        self.lvl_4_max = int((self.amount_of_workers / 100 * 15)-1)
        self.lvl_5_min = int((self.amount_of_workers / 100 * 15)-1)
        self.lvl_5_max = int((self.amount_of_workers / 100 * 45)-1)

    first_name_list = ['Ressie', 'Carmine', 'Chi', 'Keeley', 'Dung', 'Richelle', 'Mari', 'Sal', 'Cecil',
                       'Nicole', 'Janee', 'Rigoberto', 'Katheleen', 'Lyman', 'Esteban', 'Madison', 'Shaquana', 'Rickie',
                       'Olin', 'Billie', 'Warner', 'Claud', 'Cornelius', 'Cyril', 'Robert', 'Regalado',
                       'Kendrick', 'Woodrow', 'Alex', 'Willy']
    last_name_list = ['Speelman', 'Page', 'Kindell', 'Mclees', 'Marion', 'Lenihan', 'Meister', 'Obyrne',
                      'Rhymes', 'Beech', 'Caudill', 'Mcfadin', 'Vigna', 'Koss', 'Stonerock', 'Lundin', 'Biro',
                      'Coupe', 'Persing', 'Fast', 'Zawislak', 'Gholston', 'Yadao', 'Dugal', 'Aucoin', 'Regalado',
                      'Fonner', 'Lacourse', 'Cool', 'Dodrill']

    def parent_id(self, available_ids):
        ids = available_ids[User]
        if len(ids) > 0:
            pk = ids[len(ids)-1] + 1
        else:
            pk = 1

        if pk == 1:
            return 0
        elif pk <= int(self.amount_of_workers / 100 * 5):
            return 1
        elif pk <= int(self.amount_of_workers / 100 * 15):
            if self.lvl_3_min <= self.lvl_3_max:
                self.lvl_3_min += 1
            else:
                self.lvl_3_min = 1
                return 2
            return self.lvl_3_min

        elif pk <= int(self.amount_of_workers / 100 * 45):
            if self.lvl_4_min <= self.lvl_4_max:
                self.lvl_4_min += 1
            else:
                self.lvl_4_min = (self.amount_of_workers / 100 * 5)-1
                return self.lvl_4_min + 1
            return self.lvl_4_min + 1
        else:
            if self.lvl_5_min <= self.lvl_5_max:
                self.lvl_5_min += 1
            else:
                self.lvl_5_min = (self.amount_of_workers / 100 * 15)-1
                return self.lvl_5_min + 1
            return self.lvl_5_min

        # if pk == 1:
        #     return 0
        # elif pk <= int(self.amount_of_workers / 100 * 5):
        #     return 1
        # elif pk <= int(self.amount_of_workers / 100 * 15):
        #     return randint(2, int(self.amount_of_workers / 100 * 5)-1)
        # elif pk <= int(self.amount_of_workers / 100 * 45):
        #     return randint(int(self.amount_of_workers / 100 * 5), int(self.amount_of_workers / 100 * 15)-1)
        # else:
        #     return randint(int(self.amount_of_workers / 100 * 15), int(self.amount_of_workers / 100 * 45))

    def change_first_name(self, _):
        self.first_name = self.first_name_list[randint(0, len(self.first_name_list)-1)]
        return self.first_name

    def change_last_name(self, _):
        self.last_name = self.last_name_list[randint(0, len(self.last_name_list)-1)]
        return self.last_name

    def user_name(self, available_ids):
        ids = available_ids[User]
        if len(ids) == 0:
            return self.first_name + self.last_name + "1"
        else:
            return self.first_name + self.last_name + str(ids[len(ids)-1]+1)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('amount_of_workers', type=int)

    def handle(self, *args, **options):
        amount_of_workers = options['amount_of_workers']
        seeder = Seed.seeder()
        my_seed = MySeed(amount_of_workers)

        seeder.add_entity(User, amount_of_workers, {
            'parent_id': my_seed.parent_id,
            # 'is_superuser': 0,
            'username': my_seed.user_name,
            'first_name': my_seed.change_first_name,
            'last_name': my_seed.change_last_name,
            'photo': "user/0f182cb7-8596-4744-a99f-8d5193a72503.jpg"
        })

        inserted_pks = seeder.execute()
