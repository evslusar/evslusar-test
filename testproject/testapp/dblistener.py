from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from testapp.models import DbChangesLog

def handle_post_save(sender, **kwargs):
    if not issubclass(sender, DbChangesLog):
        if kwargs['created']:
            action_value = 'CREATE'
        else:
            action_value = 'EDIT'
        log_entry = DbChangesLog(action=action_value, modelname=sender._meta.module_name)
        log_entry.save()

def handle_post_delete(sender, **kwargs):
    if not issubclass(sender, DbChangesLog):
        log_entry = DbChangesLog(action='DELETE', modelname=sender._meta.module_name)
        log_entry.save()

class Listener:
    def __init__(self):
        self.installed = False

    def install(self):
        if not self.installed:
            post_save.connect(handle_post_save)
            post_delete.connect(handle_post_delete)
            self.installed = True
            print '\nListener installed'

    def uninstall(self):
        if self.installed:
            post_save.disconnect(handle_post_save)
            post_delete.disconnect(handle_post_delete)
            self.installed = False

listener = Listener()

