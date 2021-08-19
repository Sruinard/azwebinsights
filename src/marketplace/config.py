import os

def get_log_connection_string():
    connection_string = f"InstrumentationKey={os.environ.get('APPINSIGHTS_INSTRUMENTATIONKEY', '00000000-0000-0000-0000-000000000000')}"
    return connection_string