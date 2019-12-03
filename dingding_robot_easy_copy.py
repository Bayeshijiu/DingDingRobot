# -*- coding:utf-8 -*-
# import json

import requests
# from tabulate import tabulate
# from manage.dingding import _param_check

class DingDing(object):
    def __init__(self, api_url):
        self.api_url = api_url

    def send_text(self, content, at_switch, *at_numbers):
        """Send an normal text to dingding group by at(@) style or not.

        :param content: message for the new request.
        :type content: str
        :param at_switch: switch for at(@) everyone or not.
        :type at_switch: bool or str
        :param at_numbers: at(@) someone phone numbers, only valid when at_switch is False
        :type: tuple
        :rtype: dict, like {"errcode":0,"errmsg":"ok"}
        """
        try:
            at_switch = bool(at_switch)
        except ValueError:
            return {"code": 400, "message": e}
        data = {
            "msgtype": "text",
            "text": {"content": content},
            "at": {

                "atMobiles": at_numbers,
                "isAtAll": at_switch
            }
        }
        return self._send_request(data)

    def send_link(self, content, title, message_url,  pic_url=""):
        """Send an link message to dingding group.

        :param content: message for the new request.
        :type content: str
        :param title: title for message.
        :type title: str
        :param message_url: message url.txt, like "http://****"
        :type: str
        :param pic_url(optional): picture url.txt for message, like "http://****.jpg|png"
        :type: str
        :rtype: dict, like {"errcode":0,"errmsg":"ok"}
        """
        data = {
            "msgtype": "link",
            "link": {
                "text": content,
                "title": title,
                "picUrl": pic_url,
                "messageUrl": message_url
            }
        }
        return self._send_request(data)

    def send_markdown(self, content, title):
        """Send an markdown message to dingding group.

        :param content: markdown message for the new request.
        :type content: str
        :param title: title for message.
        :type title: str
        :rtype: dict, like {"errcode":0,"errmsg":"ok"}
        """
        data = {
            "msgtype": "markdown",
            "markdown": {
                "text": content,
                "title": title,
            }
        }
        return self._send_request(data)

    def _send_request(self, data):
        # headers = {"Content-type": "application/json"}
        # data = json.dumps(data)
        # result = requests.post(self.api_url, data=data, headers=headers)
        result = requests.post(self.api_url, json=data)
        return result.text


if __name__ == "__main__":
    # Webhook_url = open('url.txt').read().strip()
    Webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=your_token'
    dd = DingDing(Webhook_url)

    text = 'Hello World'

    print(text)
    dd.send_text(text, True)

    print('success')
