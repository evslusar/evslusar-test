from django.core.management.base import NoArgsCommand
from django.db import connection
from django.db.models import Count 

def get_items_count_list():
    tables = connection.introspection.table_names()
    models = connection.introspection.installed_models(tables)
    return [{'model': model._meta.module_name, 
             'count': len(model.objects.all())}
             for model in models]

class Command(NoArgsCommand):
    help = "Prints all project models and the count of objects in every model"

    def handle_noargs(self, **options):
        items_count = get_items_count_list()
        print '\nInstalled models:'
        for item in items_count:
            print 'Model "%s" contains %d objects.' % (item['model'], item['count'])
