from decouple import config


try:
    API_ID = config('API_ID', cast=int)
    API_HASH = config('API_HASH')
    SESSION_NAME = config('SESSION_NAME')
    DESTINATION_ID = config('DESTINATION_ID')
except KeyError as e:
    raise ValueError(f"Falta la variable requerida: {e}")