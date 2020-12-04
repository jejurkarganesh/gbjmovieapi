from rest_framework.routers import SimpleRouter
from . views import *




router = SimpleRouter()
router.register('genre', GenreOps)
router.register('poster',PosterOps)
router.register('movies',MovieOps)

urlpatterns = router.urls