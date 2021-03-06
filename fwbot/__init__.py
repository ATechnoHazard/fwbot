import logging
import os
import sys
import telegram.ext as tg

# enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

LOGGER = logging.getLogger(__name__)

ENV = bool(os.environ.get('ENV', False))

if ENV:
	TOKEN = os.environ.get('TOKEN', None)

else:
	from fwbot.Config import Vars
	TOKEN = Vars.API_KEY

updater = tg.Updater(TOKEN, workers=16)

dispatcher = updater.dispatcher
