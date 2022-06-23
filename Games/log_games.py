import logging
import os
from logging.handlers import TimedRotatingFileHandler

from settings import PATH_LOG, PATH_FILE_LOG, PATH_FILE_ROT

logging.basicConfig(
    filename=os.path.join(PATH_LOG, PATH_FILE_LOG),
    format=" %(asctime)s %(levelname)s %(module)s %(message)s",
    level=logging.INFO
)

logger = logging.getLogger('basic')

rot_time = TimedRotatingFileHandler(filename=os.path.join(PATH_LOG, PATH_FILE_ROT), when="H", interval=24, backupCount=3,
                                    utc=True)

logger.addHandler(rot_time)

if __name__ == "__main__":
    logger.info("Игровой модуль логов")
