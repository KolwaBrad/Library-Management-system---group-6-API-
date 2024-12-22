from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, MemberViewSet, BorrowRecordViewSet, LibrarianViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrowrecords', BorrowRecordViewSet)
router.register(r'librarians', LibrarianViewSet)

urlpatterns = [
    path('', include(router.urls)),
]