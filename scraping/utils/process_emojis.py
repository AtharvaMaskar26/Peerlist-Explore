import emoji

def remove_emojis(text):
    return emoji.replace_emoji(text, '')