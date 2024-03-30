from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from rest_framework import routers, permissions
from classes import views as classes_views
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="My API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', users_views.UserViewSet)
router.register(r'eleves', users_views.EleveViewSet)
router.register(r'groups', users_views.GroupViewSet)
router.register(r'classes', classes_views.ClasseViewSet)
router.register(r'promotions', classes_views.PromotionViewSet)
router.register(r'trimestres', classes_views.TrimestreViewSet)
router.register(r'devoirs', classes_views.DevoirViewSet)
router.register(r'matieres', classes_views.MatiereViewSet)
router.register(r'notes', classes_views.NoteViewSet)
router.register(r'coefficents', classes_views.CoefficientViewSet)
router.register(r'filieres', classes_views.FiliereViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('logout/', users_views.LogoutView.as_view(), name ='logout'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

