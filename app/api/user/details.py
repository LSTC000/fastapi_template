from dataclasses import dataclass

from app.response import Details


@dataclass(frozen=True)
class UserDetails(Details):
    email_exist: str = 'This email already exist'
    get_user_error: str = ('An error occurred while searching for the user. Check the specified '
                           'user id and try again later.')
    add_user_error: str = 'An error occurred when adding a user. Try again later.'
    edit_user_error: str = ('An error occurred while editing the user. Check the correctness of '
                            'the entered user id and try again later.')
    delete_user_error: str = ('An error occurred when deleting the user. Check the correctness of '
                              'the entered user id and try again later.')
