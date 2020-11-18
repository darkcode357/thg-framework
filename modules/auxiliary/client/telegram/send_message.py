##
# This module requires lib: https://darkcode0x00.com/download
# Current source: https://github.com/darkcode357/thg-framework
##
from lib.thg.core.BaseXmodeClass.BaseMod import BaseMod
from lib.thg.core.BaseXmodeClass.BaseOption import BaseOption
import requests
from lib.thg.core.auxiliary.Web import Url


class Exploit(BaseMod):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info(
            {
                "name": "Telegram Message Client",
                "description": """ This module will send a Telegram message to given chat ID with the
            given bot token. Please refer to the module documentation for info
            on how to retrieve the bot token and corresponding chat ID values.""",
                "author": ["darkcode0x00"],
                "references": [
                    "telegram api",
                ],
                "disclosure_date": "2020, 9, 5",
                "service_name": "torch",
                "service_version": "telegram send bot msg 0.1",
            }
        )
        self.register_options(
            [
                BaseOption(
                    name="BOT_TOKEN",
                    required=True,
                    description="Telegram BOT token",
                    value="",
                ),
                BaseOption(
                    name="CHAT_ID",
                    required=True,
                    description="Chat ID for the BOT",
                    value="",
                ),
                BaseOption(
                    name="MSG", required=True, description="Message content", value=""
                ),
            ]
        )

    def check(self):
        url_check = "https://api.telegram.org"
        if Url(url_check).check_url_open()[:3] == str(200):
            print("url ok")
        else:
            print(Url(url_check).check_url_open())

    def exploit(self):
        token = self.options.get_option("BOT_TOKEN")
        Chat_id = self.options.get_option("CHAT_ID")
        MSG = self.options.get_option("MSG")
        print(MSG)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": f"{Chat_id}", "text": f"{MSG}"}
        requests.post(url, data).json()
        print(f"mensagem envida =>[{MSG}]")


"""


    register_options(
      [
        
      ], self.class
    )
  end

  def message
    datastore['MSG']
  end

  def formatting
    datastore['FORMATTING']
  end

  def bot_token
    datastore['BOT_TOKEN']
  end

  def run
    params = { chat_id: datastore['CHAT_ID'], parse_mode: formatting, text: message }
    uri.query = URI.encode_www_form(params)
    res = Net::HTTP.get_response(uri)

    if res.is_a?(Net::HTTPSuccess)
      print_good('Message sent!')
    else
      print_error('Unable to send the message!')
      print_error("API Status: #{res.code}")
    end
  end
end
"""
