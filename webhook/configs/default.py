# The MIT License (MIT)
#
# Copyright (c) 2021 Scott Lau
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

DEFAULT_CONFIG = {
    # whether this program is running is development mode
    "dev": {
        "dev_mode": False,
    },
    # flask server info
    "server": {
        # flask server IP
        "ip": "localhost",
        # flask server port
        "port": 8080,
    },
    # rocketmq configurations
    "rocketmq": {
        # name server IP
        "name_server_ip": "localhost",
        # name server port
        "name_server_port": 9876,
        # group id
        "group_id": "GITLAB_WEBHOOK_MSG",
        # message topic
        "msg_topic": "GITLAB_WEBHOOK",
        # message keys
        "msg_keys": "GITLAB",
        # message tags
        "msg_tags": "GITLAB",
    },
}
