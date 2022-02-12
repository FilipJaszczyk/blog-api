from .views import ListBlogEntries, CreateBlogEntry, RetrieveBlogEntry, archive, publish
from rest_framework.urls import path

urlpatterns = [
    path("list", ListBlogEntries.as_view(), name="blog-entry-list"),
    path("create", CreateBlogEntry.as_view(), name="blog-entry-create"),
    path("retrieve/<int:pk>/", RetrieveBlogEntry.as_view(), name="blog-entry-detail"),
    path("archive/<int:pk>/", archive, name="blog-entry-archive"),
    path("publish/<int:pk>/", publish, name="blog-entry-publish"),
]
