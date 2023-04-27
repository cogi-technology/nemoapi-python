# !/usr/bin/env python
# coding: utf-8

__ACCOUNT__ = "0x48b1747b7221c894f1548740435d5d54377e422d"
__METADATA__ = {
    "description": "hero_501_name",
    "image": "https://n69.gsscdn.com/icons/hero/501.png",
    "name": "Maral",
    "attributes": [
        {
            "trait_type": "ID",
            "value": "02e896e7-7bed-4c3b-8000-230fc7777892"
        },
        {
            "trait_type": "NftType",
            "value": "Hero"
        },
        {
            "display_type": "number",
            "trait_type": "HeroId",
            "value": 501
        },
        {
            "display_type": "number",
            "trait_type": "MintId",
            "value": 50010000
        },
        {
            "trait_type": "Avatar",
            "value": "https://n69.gsscdn.com/icons/hero/501.png"
        },
        {
            "trait_type": "Tittle",
            "value": "Blitzkrieg expert. He provides bonus for [d80c0cFF] Tanks [-] in battle."
        },
        {
            "trait_type": "Des",
            "value": "Bóng đêm kinh hoàng"
        },
        {
            "trait_type": "Rarity",
            "value": 5
        },
        {
            "display_type": "number",
            "trait_type": "Level",
            "value": 1
        },
        {
            "display_type": "number",
            "trait_type": "Star",
            "value": 1
        },
        {
            "display_type": "number",
            "trait_type": "Grade",
            "value": 1
        },
        {
            "display_type": "number",
            "trait_type": "Power",
            "value": 1204.165092468262
        },
        {
            "display_type": "number",
            "trait_type": "Growth",
            "value": 90
        },
        {
            "display_type": "number",
            "trait_type": "Morale",
            "value": 109.0899963378906
        },
        {
            "display_type": "number",
            "trait_type": "Physique",
            "value": 109.0899963378906
        },
        {
            "display_type": "number",
            "trait_type": "Support",
            "value": 361.9688110351562
        },
        {
            "display_type": "number",
            "trait_type": "Develop",
            "value": 120.6563034057617
        },
        {
            "trait_type": "Type",
            "value": "Cyborg"
        },
        {
            "display_type": "number",
            "trait_type": "BattlePoint",
            "value": 50.0
        },
        {
            "display_type": "number",
            "trait_type": "ATK",
            "value": 450.0
        },
        {
            "display_type": "number",
            "trait_type": "Range",
            "value": 3.50
        },
        {
            "display_type": "number",
            "trait_type": "Units",
            "value": 1
        },
        {
            "display_type": "number",
            "trait_type": "HP",
            "value": 9600.0
        },
        {
            "display_type": "number",
            "trait_type": "Speed",
            "value": 2.50
        },
        {
            "trait_type": "Ability",
            "value": "This unit doesn't have any special ability."
        },
        {
            "trait_type": "PassiveSkill",
            "value": "[\n   {\n      \"id\" : 100495,\n      \"level\" : 1,\n      \"name\" : \"Tank DEF\"\n   }\n]\n"
        },
        {
            "trait_type": "PVESkill",
            "value": "[\n   {\n      \"level\" : 1,\n      \"name\" : \"Heal IV\"\n   }\n]\n"
        },
        {
            "trait_type": "PVPSkill",
            "value": "[\n   {\n      \"level\" : 1,\n      \"name\" : \"Healing V\"\n   }\n]\n"
        },
        {
            "display_type": "number",
            "trait_type": "CardLevel",
            "value": 1
        }
    ]
}
__CALLBACK__ = "http://testnet.vn:7888/nft/callback/v1?item_id=02e896e7-7bed-4c3b-8000-230fc7777892&sign=b0a70dd5a6f85c8a7b34fc5f6150f140"

class RunConfig(object):

    def __init__(self, host=None, keyid=None, prv=None, pub=None):
        # type: (str, str, str, str) -> None
        self.host = host
        self.key_id = keyid
        self.prv = prv
        self.pub = pub
