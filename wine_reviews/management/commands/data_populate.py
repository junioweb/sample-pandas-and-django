import pandas as pd

from django.core.management.base import BaseCommand

from tqdm import tqdm

from wine_reviews.managers import BulkCreateManager
from wine_reviews.models import Country, Wine


def populate_with_iterrows(file):
    df = pd.read_csv(file)
    df_tratado = df.iloc[:, 1:]
    df_tratado['price'].fillna(df_tratado['price'].mean(), inplace=True)
    bulk_mgr = BulkCreateManager(chunk_size=500)

    for index, row in tqdm(df_tratado.iterrows(), total=df_tratado.shape[0]):
        country, create = Country.objects.get_or_create(name=row.pop('country'))
        row['country'] = country
        bulk_mgr.add(Wine(**row))
    bulk_mgr.done()


def populate_with_numpy(file):
    df = pd.read_csv(file)
    df_tratado = df.iloc[:, 1:]
    df_tratado['price'].fillna(df_tratado['price'].mean(), inplace=True)
    bulk_mgr = BulkCreateManager(chunk_size=500)

    df_to_numpy = df_tratado.to_numpy()
    for np in tqdm(df_to_numpy, total=len(df_to_numpy)):
        data = {
            'description': np[1],
            'designation': np[2],
            'points': np[3],
            'price': np[4],
            'province': np[5],
            'region_1': np[6],
            'region_2': np[7],
            'taster_name': np[8],
            'taster_twitter_handle': np[9],
            'title': np[10],
            'variety': np[11],
            'winery': np[12],
        }
        country, create = Country.objects.get_or_create(name=np[0])
        data['country'] = country
        bulk_mgr.add(Wine(**data))
    bulk_mgr.done()


class Command(BaseCommand):
    help = """Comando criado para popular os dados iniciais na base."""

    def add_arguments(self, parser):
        parser.add_argument(
            '-f', type=str,
            dest='file',
            required=True,
            help="Caminho do arquivo CSV utilizado para leitura.")
        parser.add_argument(
            '-i',
            dest='iterrows',
            action='store_true',
            help="Opção para utilizar iterrows do pandas.")
        parser.add_argument(
            '-n',
            dest='numpy',
            action='store_true',
            help="Opção para utilizar numpy.")

    def handle(self, *args, **options):
        if options['iterrows'] and options['numpy']:
            raise Exception('Deve ser escolhida apenas uma flag, -i ou -n')
        elif options['iterrows']:
            populate_with_iterrows(options['file'])
        elif options['numpy']:
            populate_with_numpy(options['file'])
