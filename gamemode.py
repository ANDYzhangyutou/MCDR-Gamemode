from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'Gamemode',
    'version': '1.0.0',
    'name': 'Gamemode',
    'author': 'ANDYzytnb',
    'link': 'https://github.com/your-repo',
    'dependencies': {
        'mcdreforged': '>=1.6.2'
    }
}

def on_info(server, info):
    if info.content == '!c':
        server.execute(f'gamemode spectator {info.player}')
        server.tell(info.player, '已切换至旁观者模式')

    if info.content == '!s':
        server.execute(f'gamemode survival {info.player}')
        server.tell(info.player, '已切换至生存模式')

def on_load(server, old_module):
    server.register_help_message('!c', '切换至旁观者模式')
    server.register_help_message('!s', '切换至生存模式')

def on_unload(server):
    pass