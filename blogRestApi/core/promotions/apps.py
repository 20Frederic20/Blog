from django.apps import AppConfig


class PromotionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.promotions'
    label='core_promotions'
    
    def ready(self):
        import core.promotions.signals
