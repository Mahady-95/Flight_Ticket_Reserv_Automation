import logging
class LogGen:
    @staticmethod
    def logegn():
        logging.basicConfig(filename="./log/automation.log", format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%m:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger