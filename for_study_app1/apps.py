from django.apps import AppConfig


class ForStudyApp1Config(AppConfig):
    name = 'for_study_app1'
    def ready(self):
        import for_study_app1.signals
        
