
def translate_text(text, language):
    translations = {
        "Spanish": "[Traducido al español] " + text,
        "French": "[Traduit en français] " + text,
        "Swahili": "[Imetafsiriwa kwa Kiswahili] " + text,
        "Arabic": "[تمت الترجمة إلى العربية] " + text,
        "Bambara": "[Wɔrɔkɔ Bambara] " + text
    }
    return translations.get(language, text)
