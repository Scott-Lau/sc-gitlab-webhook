import logging

from webhook.handler import BaseHandler


class LoggingHandler(BaseHandler):
    """Logging handler: logging request json to file

    """

    def handle(self, json):
        result = BaseHandler.handle(self, json)
        if not result:
            return False
        logging.getLogger(__name__).info("request json: %s", json)
        return True
