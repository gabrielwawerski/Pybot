COOKIES_CLOSE = "//*[@id='u_0_i']"
LOGIN_EMAIL = "//input[@id='email']"
LOGIN_PASS = "//input[@id='pass']"
LOGIN_BUTTON = "//button[@id='loginbutton']"

# i maed this
REMOVE_BUTTON = "//button[@class='_tij _50zy _50zz _50z- _5upp _42ft']"
LOADED_THUMBNAIL = "//div[@class='_52kr']"
#    String INFO_MENU_USER = "//div[@class='_364g']"
#    String INFO_USER_MENU = "//div[@class='_364g']"
#    String INFO_USER_REMOVE_BUTTON = "//div[@class='_3quh _30yy _2t_ _3ay_ _5ixy']"

INFO_REMOVE_USER_BUTTON = "//button[@class='_30yy _38lh _39bl']"

#    INPUT_FIELD = "//div[@class='notranslate _5rpu']";
INPUT_FIELD = '//div[@class="_1mf _1mj"]'

INFO_BUTTON = "//a[@title='Conversation information']"

MESSAGE_CONTAINER = "//div[@aria-label='Messages']"
REMOVE_CONTAINER = "//div[@aria-label='Remove']"
#
# SETTINGS_COG = "//a[contains(@class,'_2agf')]"
# SETTINGS_DROPDOWN = "//span[text()='Settings']"
# SETTINGS_DONE = "//button[@class='_3quh _30yy _2t_ _5ixy']"
# # <br><br>RETURNS -> .<strong>text</strong>/
# MY_REAL_NAME = "//div[@class='_6ct9']"
#
MESSAGE_GROUPS = "//div[@id='js_1']/div"
MESSAGES_ALL = MESSAGE_GROUPS + "/div/div/div[contains(@class,'_o46')]"
STICKER_FILTER = MESSAGES_ALL + "[div/div[@aria-label] or div/div/div/div/img[@src]]"
MESSAGES_OTHERS = STICKER_FILTER + "[contains(@class,'_29_7')]"
MESSAGES_OTHERS_RECENT = "(" + MESSAGES_OTHERS + ")[last()]"
# MESSAGES_MINE = STICKER_FILTER + "[contains(@class,'_nd_')]"
# MESSAGES_MINE_RECENT = "(" + MESSAGES_MINE + ")[last()]"

REACTION_MENU_BUTTON = "//*[@class='_aou']"
REACTION_PRESENT = "//*[@class='_4kf5']"

# Used for checking if received message contains an image     *
# REQUIRES <strong>MESSAGE ELEMENT</strong>
# <br><br>RETURNS -> @<strong>src</strong>
MESSAGE_IMAGE = "./div/div/div/div/img[@src]"

# REQUIRES <strong>MESSAGE ELEMENT</strong>
# <br><br>RETURNS -> @<strong>aria-label</strong>
MESSAGE_TEXT = "./div/div[@aria-label]"

# REQUIRES <strong>MESSAGE ELEMENT</strong>
# <br><br>RETURNS -> @<strong>aria-label</strong>
MESSAGE_SENDER_NICKNAME = "./../h5[@aria-label]"

# REQUIRES <strong>MESSAGE ELEMENT</strong>
# <br><br>RETURNS -> @<strong>data-tooltip-content</strong>
MESSAGE_SENDER_REAL_NAME = "./../../div/*/div[@data-tooltip-content]"
