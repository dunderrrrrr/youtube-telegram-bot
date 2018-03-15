from settings import t_token, t_url, t_group
import requests

def channel_post(content, v_date):
    boturl = "{}{}/sendMessage?chat_id={}&text=New video published at {}!\n{}".format(t_url, t_token, t_group, v_date, content)
    r = requests.request("GET", boturl)
