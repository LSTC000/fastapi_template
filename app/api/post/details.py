from dataclasses import dataclass

from app.utils.response import Details


@dataclass(frozen=True)
class PostDetails(Details):
    user_does_not_exist = 'The user with the specified user id does not exist.'
    get_post_error: str = ('An error occurred while searching for the post. Check the specified '
                           'post id and try again later.')
    add_post_error: str = 'An error occurred when adding a post. Try again later.'
