from django.apps import AppConfig
class FooConfig(AppConfig):
    name = 'full.python.path.to.your.my_store'
    label = 'my_store'  # <-- this is the important line - change it to anything other than the default, which is the module name ('foo' in this case)

    default_app_config = 'full.python.path.to.your.my_store.apps.FooConfig'
