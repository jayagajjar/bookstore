from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import bookstore.views
from django.conf.urls.static import static
from django.conf import settings


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", bookstore.views.index, name="index"),
    path("db/", bookstore.views.db, name="db"),
    path("createbook/", bookstore.views.createbook, name="createbook"),
    path("insertbook/", bookstore.views.insertbook, name="insertbook"),
    path("deletebook/", bookstore.views.deletebook, name="deletebook"),
    path("booklist/", bookstore.views.booklist, name="booklist"),
    path("admin/", admin.site.urls),
    path('success', bookstore.views.success, name = 'success'),
]
#path('book_image_upload', bookstore.views.book_image_upload, name = 'book_image_upload'),

