# game setup
WIDTH    = 1280 
HEIGHT   = 720
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0}

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/font/joystix.ttf'  # noqa: E501
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#17ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

#weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/weapons/sword/full.png'},  # noqa: E501
    'lance': {'cooldown': 400, 'damage': 30, 'graphic':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/weapons/lance/full.png'},  # noqa: E501
    'axe': {'cooldown': 300, 'damage': 20, 'graphic':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/weapons/axe/full.png'},  # noqa: E501
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/weapons/rapier/full.png'},  # noqa: E501
    'sai': {'cooldown': 80, 'damage': 10, 'graphic':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/weapons/sai/full.png'}}  # noqa: E501

#magic
magic_data = {
    'flame': {'strength': 5,'cost': 20,'graphic':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/flame/fire.png'},  # noqa: E501
    'heal': {'strength': 20,'cost': 10,'graphic':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/heal/heal.png'}}  # noqa: E501

#enemy
monster_data = {
    'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/audio/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/audio/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/audio/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/audio/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}