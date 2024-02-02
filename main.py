import os
import sys

# Add the 'src' directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.append(src_path)

# from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from textSummarizer.logging import logger

# STAGE_NAME = "Data Ingestion stage"
# try:
#     logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=====x")
# except Exception as e:
#         logger.exception(e)
#         raise e




# from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from textSummarizer.logging import logger


# STAGE_NAME = "Data Ingestion stage"
# try:
#     logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#     data_ingestion= DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e

# STAGE_NAME = "Data Validation stage"
# try:
#     logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#     data_validation= DataValidationTrainingPipeline()
#     data_validation.main()
#     logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e


# from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from textSummarizer.logging import logger


# STAGE_NAME = "Data Ingestion stage"
# try:
#     logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#     data_ingestion= DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e

# STAGE_NAME = "Data Validation stage"
# try:
#     logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#     data_validation= DataValidationTrainingPipeline()
#     data_validation.main()
#     logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e



# STAGE_NAME = "Data Transformation stage"
# try:
#     logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#     data_transformation= DataTransformationTrainingPipeline()
#     data_transformation.main()
#     logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e


from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_validation= DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_transformation= DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_transformation= ModelTrainerTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e