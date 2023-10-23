import random

class Pepe:
    def __init__(self):
        self.pepes = {
            "4an_8934_Pepe_King": "<:4an_8934_Pepe_King:1163577155352018954>",
            "12g_ysp_pepe_king": '<:12g_ysp_pepe_king:1163577163086311527>',
            "Edaskdas": "<:Edaskdas:1163577193784418325>",
            "PepePoint82": "<:PepePoint82:1163577298642030617>",
            "_pepesimp_": "<:_pepesimp_:1163577151648448572>",
            "memerangry": "<:memerangry:1163577214445555896>",
            "monkas": "<:monkas:1163577217373175888>",
            "njf_pepe_pride": "<:njf_pepe_pride:1163577222758682644>",
            "olzking": "<:olzking:1163577227741499513>",
            "pepe_spit": "<:pepe_spit:1163577267696435281>",
            "pepeapusad22": "<:pepeapusad22:1163577273497169971>",
            "pepebox90": "<:pepebox90:1163577276995207238>",
            "pepel19": "<:pepel19:1163577287732625458>",
            "pepenavaja": "<:pepenavaja:1163577295525650524>",
            "pepeslice85": "<:pepeslice85:1163577301208944690>",
            "pepe_cowboy_fast": '<a:pepe_cowboy_fast:1163577259182018643>',
            "03o_memes": "<a:03o_memes:1163577153649115257>",
            "Creeper": "<a:Creeper:1163577185056071801>",
            "Pepe": "<a:Pepe:1163577245483421796>",
            "PepeLul51": "<a:PepeLul51:1163577290559606874>",
            "Pepe_Guitar12": "<a:Pepe_Guitar12:1163577262499709098>",
            "Peperiding": "<a:Peperiding:1163577236344029264>",
            "Pepethinking": "<a:Pepethinking:1163577241091985529>",
            ":__:": "<a:__:1163577146866941953>",
            "e9r_1674_pepe_wave": "<a:e9r_1674_pepe_wave:1163577191146209280>",
            "j7z_PEPE_RAGE": "<a:j7z_PEPE_RAGE:1163577208825204827>",
            "jj3_pepe_eggplant": "<a:jj3_pepe_eggplant:1163577210502926386>",
            "ntcart38": "<a:ntcart38:1163577224243445830>",
            "peepohug60": "<a:peepohug60:1163577231235350580>",
            "pepe_band_guitar18": "<a:pepe_band_guitar18:1163577249228914688>",
            "pepe_band_piano36": "<a:pepe_band_piano36:1163577254358548601>",
            "pepe_band_trumpet79": "<a:pepe_band_trumpet79:1163577256745115729>",
            "pepe_typing_pixelated": "<a:pepe_typing_pixelated:1163577269969756310>",
            "pepeconfetti": "<a:pepeconfetti:1163577281533452288>",
            "pepegifrun": "<a:pepegifrun:1163577286528868433>",
            "pepetoilet": "<a:pepetoilet:1163577243797299300>",
            "zpepelmao": "<a:zpepelmao:1163612258979553312>",
        }

    def pick_one(self, pepe_tag):
        try: 
            list(self.pepes.keys()).index(pepe_tag)
            return self.pepes[pepe_tag]
        except ValueError:
            return '🇵🇪'

    def pick_random(self):
        pepe_values = list(self.pepes.values())
        return random.choice(pepe_values)