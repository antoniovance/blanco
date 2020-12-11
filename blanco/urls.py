from api import UserInfo
from api import SignInView
from api import SignUpView


def register_view(api):
    api.add_resource(UserInfo, "/user/<int:pk>")
    api.add_resource(SignInView, "/signIn")
    api.add_resource(SignUpView, "/signUp")