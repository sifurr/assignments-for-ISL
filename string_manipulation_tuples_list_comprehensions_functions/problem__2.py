cards = ["1234567812345678", "9876543298765432", "1111222233334444"]


def mask_bank_cards(cards):
    masked_version = ["*" * 12 + card[12:] for card in cards]

    return masked_version


masked_cards = mask_bank_cards(cards)
print(masked_cards)