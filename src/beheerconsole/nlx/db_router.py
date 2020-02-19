from typing import Optional

NLX_DB_ALIAS = "nlx"


class NLXRouter:

    app_label = "nlx"

    def db_for_read(self, model, **hints) -> Optional[str]:
        if model._meta.app_label == self.app_label:
            return NLX_DB_ALIAS
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Block migrations for the NLX app.

        The NLX app is completely managed externally.
        """
        if app_label == self.app_label:
            return False
        return None
