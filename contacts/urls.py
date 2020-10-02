from django.urls import path
from .views import index, ContactsListView, ContactDetailsView, ContactCreateView, ContactDeleteView, ContactEditView

urlpatterns = [
    path("", index, name="home"),
    path("contacts/", ContactsListView.as_view(), name="contacts"),
    path("contacts/create/", ContactCreateView.as_view(), name="create"),
    path("contacts/<int:pk>/details/", ContactDetailsView.as_view(), name="details"),
    path("contacts/<int:pk>/edit/", ContactEditView.as_view(), name="edit"),
    path("contacts/<int:pk>/delete/", ContactDeleteView.as_view(), name="delete"),

]
