from fastapi import FastAPI
from marketplace.domain import model
from marketplace import config
# import logging
# from opencensus.ext.azure.log_exporter import AzureLogHandler

# LOGGER = logging.getLogger(__name__)
# LOGGER.addHandler(
#     AzureLogHandler(connection_string=config.get_log_connection_string())
# )
# LOGGER.setLevel(logging.INFO)
app = FastAPI()


DATABASE = [
    model.ElectricCharger(
        sku='echarger',
        location='WestEurope'
    )
]

properties = {'custom_dimensions': {'key_1': 'value_1', 'key_2': 'value_2'}}

@app.get("/")
def available_items():
    print(config.get_log_connection_string()) 
    # logging.warning("Hello Stef Ruinard from Logs", extra=properties)
    return DATABASE 

@app.get("/items")
def available_items():
    return "hello items 2" 