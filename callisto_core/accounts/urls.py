from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^signup/", views.SignupView.as_view(), name="signup"),
    url(r"^login/", view=views.LoginView.as_view(), name="login"),
    url(r"^logout/", view=views.LogoutView.as_view(), name="logout"),
    url(
        r"^change_password/",
        view=views.PasswordChangeView.as_view(),
        name="change_password",
    ),
    url(r"^forgot_password/$", view=views.PasswordResetView.as_view(), name="reset"),
    url(
        r"^forgot_password/sent/$",
        view=views.PasswordForgetSentView.as_view(),
        name="password_reset_sent",
    ),
    url(
        r"^reset/confirm/(?P<uidb64>.+)/(?P<token>.+)/$",
        view=views.PasswordResetConfirmView.as_view(),
        name="reset_confirm",
    ),
    url(
        r"^activate/(?P<uidb64>.+)/(?P<token>.+)/$",
        view=views.AccountActivationView.as_view(),
        name="activate_account",
    ),
]
