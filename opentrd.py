import getopt
import logging
import sys

from telethon import TelegramClient, events, custom

import proxy
import secret
import settings

logger = logging.getLogger('opentrd')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('opentrd.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

default_proxy = None
try:
    opts, args = getopt.getopt(sys.argv[1:], 'p', ['proxy'])
    for opt, arg in opts:
        if opt in ('-p', '--proxy'):
            default_proxy = proxy.proxy
except getopt.GetoptError:
    sys.exit(2)

client = TelegramClient('opentrd_session', secret.api_id, secret.api_hash, proxy=default_proxy).start()


async def backup(event: custom.Message):
    # event.message.audio
    # event.message.gif
    # event.message.photo
    # event.message.voice
    # event.message.video
    if event.chat_id not in settings.MEDIA_ONLY or event.message.media is not None:
        await client.forward_messages(settings.BACKUP[event.chat_id], [event.message], event.chat_id)


@client.on(events.NewMessage(outgoing=True))
async def get_chat_id(event: custom.Message):
    if settings.DEBUG:
        for i in (event, event.chat_id, event.chat):
            try:
                logger.info(i)
            except:
                pass


def main():
    final_credits = 'OpenSource Telegram RePoster Daemon is running'
    for chat_id in settings.BACKUP.keys():
        client.on(events.NewMessage(chats=[chat_id, ]))(backup)
    print(final_credits)
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
