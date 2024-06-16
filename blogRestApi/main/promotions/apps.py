from django.apps import AppConfig


class PromotionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main.promotions"
    label = "main_promotions"

    def ready(self):
        import main.promotions.signals
