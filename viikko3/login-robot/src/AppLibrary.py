from stub_io import StubIO
from repositories.user_repository import UserRepository
from services.user_service import UserService
from app import App


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._user_repository = UserRepository()
        self._user_service = UserService(self._user_repository)
        self._app = App(self._user_service, self._io)

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if value not in outputs:
            raise AssertionError(f'Output "{value}" is not in {str(outputs)}')

    def run_application(self):
        self._app.run()

    def create_user(self, username, password):
        try:
            self._user_service.create_user(username, password)
        except Exception as err:
            self._io.outputs.append(str(err))

    def user_should_exist(self, username):
        if not self._user_repository.find_by_username(username):
            raise AssertionError(f"User {username} does not exist")
