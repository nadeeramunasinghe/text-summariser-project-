from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.conponents.data_ingestion import DataIngestion
from TextSummarizer.logging import logger 

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_cofig = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_cofig)
        data_ingestion.download_file()
        data_ingestion.Extract_zip_file()