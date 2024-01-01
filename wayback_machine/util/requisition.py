import requests
from bs4 import BeautifulSoup
from random import choice

def _get_source_html(url):
    with open('./wayback_machine/util/user_agents.txt', 'r') as agent_file:
        lines = [linha.strip() for linha in agent_file.readlines()[:1000]]
        user_agent = choice(lines)
    
    headers = requests.utils.default_headers()
    
    headers.update(
        {
            'User-Agent' : user_agent
        }
    )

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f'requests failed: {response.status_code}')

def get_bs4_object(url):
    source_html = _get_source_html(url)
    return BeautifulSoup(source_html, 'html.parser')

if __name__ == '__main__':
    bs4 = get_bs4_object('https://web.archive.org/web/20170727045210/https://www.baka-tsuki.org/project/index.php?title=High_School_DxD')
    print(bs4)