from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from rest_framework_simplejwt import views as jwt_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

from core.classrooms.views import ClassroomViewSet
from core.promotions.views import PromotionViewSet
from core.users.views import UserViewSet, StudentViewSet, TeacherViewSet, LogoutView
from core.instructs.views import InstructViewSet
from core.registries.views import RegisterViewSet
from core.subjects.views import SubjectViewSet
from core.scores.views import ScoreViewSet
from core.coefficients.views import CoefficientViewSet
from core.courses.views import CourseViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="MonScolaire API",
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
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
# router.register(r'groups', users_views.GroupViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'promotions', PromotionViewSet)
router.register(r'instructs', InstructViewSet)
router.register(r'registries', RegisterViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'scores', ScoreViewSet)
router.register(r'coefficents', CoefficientViewSet)
router.register(r'courses', CourseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('logout/', LogoutView.as_view(), name ='logout'),
    # path('calculate/<eleve_id>', classes_views.CalculationsView.as_view(), name='calculate'),
    # path('classes-notes/', classes_views.CreateorUpdateNoteView.as_view(), name='classes-notes'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # #definition des vues de templates uniquement
    # path('login', users_views.login, name='login'),
] 

