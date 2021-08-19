from fastapi import FastAPI
import uvicorn
from marketplace.domain import model
from marketplace import config
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(
    AzureLogHandler(connection_string=config.get_log_connection_string())
)
LOGGER.setLevel(logging.INFO)
app = FastAPI()


DATABASE = [
    model.ElectricCharger(
        sku='echarger',
        location='WestEurope')
]
properties = {'custom_dimensions': {'key_1': 'value_1', 'key_2': 'value_2'}}

@app.get("/")
def available_items():
    print(config.get_log_connection_string()) 
    LOGGER.warning(msg="hello world", extra=properties)
    return DATABASE 

@app.get("/items")
def available_items():
    return "hello items 1" 
    
if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)