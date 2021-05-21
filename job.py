import logging
import logging.config
logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)
logger = logging.getLogger()

if __name__ == '__main__':
    try:
        logger.info("Testing cron job")
    except:
        logger.error("Error")