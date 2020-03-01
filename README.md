# OpenTRD
OpenSource Telegram RePoster Daemon

## Run script

### Method 1. 24/7 run
1. Setup proxy.py, secret.py and settings.py from templates
2. `docker image build -t opentrd .`
3. `docker container run -d --name opentrd --restart always opentrd`
4. PROFIT!!!

### Method 2. One-time run
1. `pip3 install -r reqirements.txt`
2. Add [API token and hash](https://core.telegram.org/api/obtaining_api_id) to secret.template.py and rename it to secret.py
3. `python3 opentrd.py`

### Dependencies
* Latest version of Telethon: http://telethon.readthedocs.io/en/stable/
