from api import UserDetailView
from api import SignInView
from api import SignUpView


def register_view(api):
    api.add_resource(UserDetailView, "/user/<int:pk>")
    api.add_resource(SignInView, "/signIn")
    api.add_resource(SignUpView, "/signUp")