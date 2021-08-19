import os

def get_log_connection_string():
    connection_string = f"InstrumentationKey={os.environ.get('APPINSIGHTS_INSTRUMENTATIONKEY', '82aec5b0-fd80-445c-b06e-047a2e705500')}"
    # connection_string = "InstrumentationKey=82aec5b0-fd80-445c-b06e-047a2e705500;IngestionEndpoint=https://westeurope-5.in.applicationinsights.azure.com/"
    return connection_string