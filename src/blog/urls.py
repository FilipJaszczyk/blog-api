from .views import ListBlogEntries, CreateBlogEntry, RetrieveBlogEntry
from rest_framework.urls import path


urlpatterns = [
    path("list", ListBlogEntries.as_view(), name="blog-entry-list"),
    path("create", CreateBlogEntry.as_view(), name="blog-entry-create"),
    path("retrieve", RetrieveBlogEntry.as_view(), name="blog-entry-detail"),
]
