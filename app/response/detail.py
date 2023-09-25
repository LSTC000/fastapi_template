from dataclasses import dataclass


@dataclass(frozen=True)
class Detail:
    exception_error: str = 'We have already started to fix this error'

    email_exists: str = 'This email already exist'
