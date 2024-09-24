import djp
import dj_database_url


@djp.hookimpl
def settings(current_settings):
    current_settings["DATABASES"]["default"] = dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
