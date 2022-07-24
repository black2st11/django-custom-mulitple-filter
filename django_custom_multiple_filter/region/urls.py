from rest_framework.routers import SimpleRouter
from .views import BigCityView, SmallCityView, StateView
router = SimpleRouter()

router.register('state', StateView)
router.register('small_city', SmallCityView)
router.register('big_city', BigCityView)

urlpatterns = router.get_urls()