from django.urls import path,include
from .views import home,secret_page,settings,UserDetailView,UserFollowView,UserFollowRemoveView,UserDetailsUpdateView,UserProfileDetailsUpdateView
from allauth.account.views import EmailView as allauth_AccountEmail



urlpatterns=[
    path('', home, name='home'),
    path('secret/',secret_page,name='secret'),
    path('accounts/email/',allauth_AccountEmail.as_view(),name='account_email'),
    path('accounts/', include('allauth.urls')),
    path('settings/', settings, name='settings'),
    path('settings/<slug>/update/', UserDetailsUpdateView.as_view(), name='upd-user'),
    path('settings/id/<int:pk>/update/', UserProfileDetailsUpdateView.as_view(), name='upd-profile'),
    path('profile/<slug>/', UserDetailView.as_view(), name='user-profile'),
    path('profile/<slug>/follow/', UserFollowView.as_view(), name='user-follow'),
    path('profile/<slug>/followremove/', UserFollowRemoveView.as_view(), name='user-follow-remove'),
]