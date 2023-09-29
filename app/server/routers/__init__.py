__all__ = ['__routers__']


from .routers import Routers

from app.api import user_router, post_router


__routers__ = Routers(
    routers=(
        user_router,
        post_router,
    )
)
