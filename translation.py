class Translation(object):
    START_TEXT = """<b>Hi Sir!</b>\nI can get your Telegram APP ID & API Hash from my.telegram.org !! \nNo need to go to website & login there. Just Login with me.\n\n<b>Just Send me your Telegram Account's Phone Number to start \nprocess.</b> \n <b>Phone Number should be in International Format.</b>\n<b>Example: +9405748292828</b>"""
    AFTER_RECVD_CODE_TEXT = """A Verification Code sent to you by Telegram. Enter that Verification Code Or Forward That Verification Message."""
    BEFORE_SUCC_LOGIN = "Recieved Code. Scarpping Web Page ..."
    ERRED_PAGE = "<b>Something Went Wrong. Failed To Get App ID.</b> \n\n<b>@Dihanofficial</b>"
    CANCELLED_MESG = "<b>Bye! Please Reply /start the bot conversation</b>"
    IN_VALID_CODE_PVDED = "<b>Sorry, But The Input Does Not Seem To Be A Valid Telegram Web-Login Code</b>"
    IN_VALID_PHNO_PVDED = "<b>Sorry, But The Input Does Not Seem To Be A Valid Phone Number</b>"
