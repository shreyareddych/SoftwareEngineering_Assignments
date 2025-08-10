# import all model modules so SQLAlchemy sees them
def import_models() -> None:
    from app.models import user        # noqa: F401
    from app.models import restaurant  # noqa: F401
    from app.models import menu_item   # noqa: F401
    from app.models import order       # noqa: F401
    from app.models import order_item  # noqa: F401
    # TODO: add more model files here as you design your DB
