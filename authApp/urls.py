from django.urls import path

from authApp.views import MyView, fetch_record, create_record, reset_record, edit_record, delete_record, generate_token

urlpatterns = [
    path("my-url/", MyView.as_view, name="my_url"),
    path("fetch/", fetch_record, name="fetch"),
    path("create/", create_record, name="create"),
    path("reset/", reset_record, name="reset"),
    path("edit/", edit_record, name="edit"),
    path("delete/", delete_record, name="delete"),
    path("token/", generate_token, name="token")
]
