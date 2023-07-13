import logging #
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)

# not used in this stub but often useful for finding various files
project_dir = Path(__file__).resolve().parents[1]

# find .env automagically by walking up directories until it's found, then
# load up the .env entries as environment variables
load_dotenv(find_dotenv())
