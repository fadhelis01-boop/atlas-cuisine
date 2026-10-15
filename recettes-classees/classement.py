# -*- coding: utf-8 -*-
"""Règles de tri automatique des recettes vidéo (titres FR/EN/DE/NL), partagées par build_youtube.py et ajout_auto.py."""
import re, unicodedata

def nrm(t): return unicodedata.normalize("NFD", t.lower().replace("œ", "oe")).encode("ascii", "ignore").decode()

HC = re.compile(r"\b(vlog|faq|interview|concours|giveaway|livre|book|merci|mon histoire|food tour|je teste|on teste|testing|restaurant|restaurants|documentaire|abonne|abonnes|sneak peak|is back|unboxing|q&a|haul|mukbang|reaction|trailer|teaser|annonce|live|podcast|routine|what i eat|psg|liverpool|retour au laos|traverse l.algerie|histoire du rai|prefecture|g-shock)\b|^\d{1,2} \w+ 20\d\d$")
CAT_RULES = [  # (catégorie, motif) : le premier qui correspond gagne ; la cuisine d'origine passe avant le type (pain, dessert)
 ("boissons", r"\b(jus|juice|smoothie|lassi|limonade|lemonade|cocktail|mocktail|the glace|iced tea|iced coffee|ijskoffie|cafe frappe|chai|milkshake|milk shake|bissap|hot chocolate|chocolat chaud|sirop|drink|boisson|kompot|limo)\b"),
 ("techniques", r"\b(comment (cuisiner|utiliser|faire des bouillons|rendre)|astuce|tips?|hack|je vous explique|ce que vous devez savoir|on vous ment|c.est quoi|how to (cut|store|cook rice)|technique|differents|guide)\b"),
 ("zero_dechet", r"\b(pain rassis|restes|leftover|anti.?gaspi|trognon|epluchure)\b"),
 ("sauces", r"^(la recette (de la|du|des) )?(sauce|mayo|mayonnaise|ketchup|vinaigrette|pesto|aioli|harissa|chutney|dressing|houmous|hummus|tzatziki|salsa|nam prik|huile pimentee|chili oil|pate de piment|marinade|bouillon|fond de)\b|\b(sauce|mayo|ketchup|vinaigrette|pesto|bouillon) maison\b|arrete d.acheter|fais ta sauce|les sauces"),
 ("street_food", r"\b(burger|burgers|tacos|kebab|doner|shawarma|hot dog|hot-dog|sandwich|sando|panini|nuggets|wings|ailes de poulet|fried chicken|poulet frit|frites|fries|corn dog|croque|quesadilla|street.?food|snack|toasts|loaded)\b"),
 ("maghreb", r"\b(couscous|tajine|tagine|chorba|harira|rfissa|chakchouka|shakshuka|mhadjeb|mhajeb|bourek|brick|msemen|makrout|tlitli|rechta|chtitha|loubia|dolma algerienne|omek houria|kefta|merguez|algerie|algerien|algerienne|maroc|marocain|marocaine|tunisie|tunisien|tunisienne|moroccan|algerian|frite omelette|garantita|karantika|mechoui|zaalouk)\b"),
 ("afrique", r"\b(ndole|eru|okok|koki|mbongo|nkui|achu|kouakou|macabo|plantain|alloco|attieke|garba|mafe|yassa|thieb|thieboudienne|dibi|jollof|fufu|foufou|watafufu|placali|sauce graine|sauce gombo|gombo|manioc|cassava|tapioca|bobolo|miondo|puff.?puff|beignets haricots|koki|pkwem|safou|kondre|poulet dg|soya|soja grille|cameroun|camerounais|senegal|ivoirien|congo|africain|african|nigerian|ghana|ethiopian|injera)\b"),
 ("moyen_orient", r"\b(falafel|houmous|mezze|kebbe|kibbeh|fattoush|taboule|tabbouleh|shawarma|manakish|zaatar|lahmacun|pide|kofta|kofte|kebab|turkish|turc|turque|liban|libanais|lebanese|syrien|persian|iranian|tahdig|baklava|kunafa|knafeh|balkans?|kosovo|albanie|albanais|bosnian|bosnie|serbian|cevapi|cevapcici|burek|pite|sarma|ajvar|tavce|flija|fli|khachapuri|khatchapouri|georgien)\b"),
 ("asie", r"\b(ramen|udon|soba|somen|sushi|maki|onigiri|onigirazu|katsu|katsudon|donburi|don|gyudon|butadon|oyakodon|teriyaki|yakitori|karaage|tempura|tonkatsu|okonomiyaki|takoyaki|miso|dashi|japonais|japonaise|japanese|kimchi|bibimbap|bulgogi|tteok|tteokbokki|gochujang|kimbap|coreen|coreenne|korean|jjigae|mandu|pajeon|chinois|chinoise|chinese|dim sum|siu mai|ha kao|wonton|jiaozi|gyoza|bao|char siu|mapo|kung pao|chow mein|lo mein|chow fun|fried rice|riz saute|nouilles|noodles|vermicelles|pho|bo bun|bun|banh|nems|rouleaux de printemps|spring rolls?|vietnamien|vietnamienne|vietnamese|thai|thaie|thailandais|pad thai|pad see ew|pad kee mao|tom yum|tom kha|curry vert|curry rouge|green curry|laap|laab|larb|lao|laotien|laotienne|khao|cambodgien|lok lak|loc lac|satay|sate|nasi|rendang|laksa|biryani|tikka|masala|korma|karahi|nihari|haleem|pakora|samosa|samoussa|dal|daal|chana|paneer|kheer|pakistani|indian|indien|indienne|desi|qeema|keema|aloo|chapli|seekh)\b"),
 ("italie", r"\b(pasta|pates|spaghetti|penne|tagliatelle|lasagne|lasagna|carbonara|bolognaise|bolognese|alfredo|risotto|gnocchi|ravioli|tortellini|arancini|focaccia|tiramisu|italien|italienne|italian|parmigiana|osso buco|piccata|cacio|amatriciana|puttanesca|pesto)\b"),
 ("ameriques", r"\b(tex.?mex|chili|enchiladas?|fajitas?|burrito|nachos|guacamole|mexicain|mexican|bresil|bresilien|brazilian|feijoada|ribs|bbq|barbecue|mac and cheese|mac n cheese|cajun|jambalaya|gumbo|cornbread|biscuits and gravy|pulled|brisket|meatloaf|pot roast|colombo|accras|antillais|creole|haiti|jamaican|jerk|rasta pasta|alfredo|southern|soul food|peach cobbler|banana pudding|pound cake|kentucky|texas)\b"),
 ("france", r"\b(blanquette|bourguignon|pot.?au.?feu|gratin|quiche|tartiflette|raclette|fondue|cassoulet|choucroute|ratatouille|hachis|parmentier|endives|croque|petit sale|navarin|daube|confit|magret|terrine|veloute|potage|soupe a l.oignon|bouillabaisse|moules|coq au vin|boeuf carottes|tarte flambee|flammekueche|crepes|galette|omelette|cancoillotte|comte|mont d.or|morteau|franc.comtois|savoyard|sauce mironton|charcutiere|paillasson|poulet de bresse|bistrot|francaise|french)\b"),
 ("pains", r"\b(pain|pains|bread|brot|brotchen|brood|broodjes|brioche|baguette|naan|pita|chapati|paratha|focaccia|bagel|bao|baozi|nikuman|batbout|msemen|kifle|pogaca|pogacice|lepinja|somun|samuna|buns?|croissant|broodje|fougasse|muffin anglais|english muffin|pizza|pide|lahmacun|panozzo|khatchapouri|khachapuri|burek|bourek|pite|pita me|tortilla|wrap)\b"),
 ("desserts", r"\b(gateau|gateaux|cake|kuchen|taart|tarte au|tart|pie|cheesecake|brownie|brownies|cookie|cookies|koekjes|biscuit|muffin|cupcake|donut|beignet|churros|crepe|crepes|pancake|pancakes|gaufre|waffle|tiramisu|mousse|flan|creme brulee|panna|pudding|dessert|desserts|toetje|chocolat|chocolate|chocolade|caramel|karamell|glace|ice cream|sorbet|macaron|eclair|choux|chantilly|ganache|praline|nougat|baklava|makrout|kalb|chebakia|basbousa|trilece|kipferl|kolaci|palacinke|tulumba|perles de coco|mochi|dorayaki|taiyaki|purin|castella|dulce de leche|fudge|blondies|babka|cinnamon rolls?|zimtschnecken|crumble|muffins?|kekse|keks|cupcakes?|pavlova|berliner|kipferl|liegeois|danettes|oranges givrees|gurabija|tullumba|petulla|crisp|roule|banh lot|khanom|nam van|gelee|wun|mi-cuit|oreo|ferrero|kruidnoten|monchou|tompouce)\b"),
]
ASIE_SUB = [("Japon", r"ramen|udon|soba|somen|sushi|maki|onigiri|onigirazu|katsu|don\b|donburi|teriyaki|yakitori|karaage|tempura|tonkatsu|okonomiyaki|takoyaki|miso|dashi|japon|japanese|nikujaga|shogayaki|kakuni|hambagu|korokke|nanban|chawanmushi|tamago|agebitashi|mugen|shigureni|mushidori|nitsuke|purin|sando|omurice|chahan|natto|tebasaki|dorayaki|taiyaki|narutomaki|inari|chirashi|temari|yakisoba|zaru|chanko|kakiage|gari|furikake"),
 ("Corée", r"kimchi|bibimbap|bulgogi|tteok|gochujang|kimbap|coreen|korean|jjigae|mandu|pajeon|buldak|bossam|galbi|kkakdugi|eomuk|danmuji|kalguksu|haejangguk|ojingeo|kkwabaegi|gimmari|jjajangmyeon|budae|bibimmyeon|duruchigi|tangsuyuk|kkanpunggi|so-tteok|ssamjang|oi muchim|beoseot"),
 ("Vietnam", r"pho|bo bun|bun\b|banh|nems|vietnam|goi|thit|cha trung|com tam|hu tieu|mien ga|bo kho|ga kho"),
 ("Thaïlande", r"thai|pad |tom yum|tom yam|tom kha|khao man|khao pad|kai|gai yang|sakoo|khanom|wun kati|nam prik|yam |massaman|panang|pa thong ko|khao kha moo|tigre qui pleure"),
 ("Laos & Cambodge", r"\blao\b|laotien|laap|laab|larb|khao piek|khao poun|khua mee|mee kati|sai gok|sai ua|tam khao|soup nor|ho mok|cambod|lok lak|loc lac|sach ko|mee katang|kampot|tom khem"),
 ("Inde & Pakistan", r"biryani|tikka|masala|korma|karahi|nihari|haleem|pakora|samosa|samoussa|dal\b|daal|chana|paneer|kheer|pakistani|indian|indien|desi|qeema|keema|aloo|chapli|seekh|naan|paratha|roti|chai|lassi|tandoori|butter chicken|achari|jalfrezi|kofta curry|halwa|gulab|jalebi|raita|chaat|pulao|zarda|shami|bihari|handi|qorma"),
 ("Chine & Taïwan", r".")]
JUNK = re.compile(r"^(l.ardoise porto-vecchio|fire|trickshot|chez nous|ustensiles cuisine|eplucher electrique|alerte canicule|eid mubarak|muy bueno|fumage express|four a pizza)\b")
PORK = re.compile(r"\b(porc|pork|cochon|bacon|lardons?|jambon|ham|prosciutto|pancetta|guanciale|chorizo|saucisses? de toulouse|saucisson|schwein|speck|varkens|spek|ham|char siu|cha siu|dong po|kakuni|tonkatsu|butadon|shogayaki|bossam|thit|lu rou|travers de porc|spam|saucisses? chinoises|lap cheong|mortadelle|salami|pepperoni|rillettes|andouillette|boudin|petit sale|demi-sel|morteau|knacki|hot dog franc|rouelle|echine|charcutiere|mironton|moo\b|moo |sakoo sai moo|tonkotsu|carbonara)\b")
ALCOHOL = re.compile(r"\b(vin|vins|wine|biere|beer|bier|rhum|rum|cognac|armagnac|whisky|bourbon|vodka|liqueur|likor|calvados|cidre|cider|champagne|sake|mirin|shaoxing|marsala|porto|amaretto|limoncello|vin jaune|baileys|drunken|spritz|aperol|mojito|sangria|pastis|liqueur)\b")

def clean(t):
    t = re.sub(r"\s*[-|]\s*(le riz jaune|recette facile|recette simple|recette super facile)\s*$", "", t, flags=re.I)
    t = re.sub(r"\s*-\s*Le [Rr]i[zZ] [Jj]aune\s*", " ", t)
    t = re.sub(r"(Liste d.ingr.dients|Ingr.dients)\s*:.*$", "", t, flags=re.I)
    t = re.sub(r"#\S+", "", t); t = re.sub(r"\| Day \d+/100 Japanese Recipes", "", t)
    t = re.sub(r"\s+", " ", t).replace("[", "(").replace("]", ")").strip(" ·-|,")
    if len(t) > 110: t = t[:107].rsplit(" ", 1)[0] + "…"
    return t


LABELS = {"afrique": "🌍 Afrique de l'Ouest & centrale", "maghreb": "🌍 Maghreb", "moyen_orient": "🌍 Moyen-Orient, Turquie & Balkans", "italie": "🌍 Europe : Italie",
          "france": "🇫🇷 France", "ameriques": "🌎 Amériques", "street_food": "🍔 Street food & fast-food fait maison", "pains": "🥖 Pains, pâtes & bases",
          "sauces": "🥫 Sauces maison", "fait_maison": "🍯 Fait maison sans additifs", "desserts": "🍰 Desserts & pâtisserie", "boissons": "🥤 Boissons",
          "techniques": "🔪 Techniques & astuces", "zero_dechet": "♻️ Zéro déchet", "a_verifier": "❓ À vérifier (titre trop vague)"}

def section_of(title, default="a_verifier", channel=""):
    """Rubrique du fichier classé pour un titre ; None = hors recette."""
    n = nrm(clean(title))
    if len(n) < 4 or HC.search(n): return None
    cat = next((c for c, rx in CAT_RULES if re.search(rx, n)), None)
    if cat is None: cat = "a_verifier" if JUNK.search(n) else default
    if cat == "asie":
        sub = next(s for s, rx in ASIE_SUB if re.search(rx, n))
        if channel == "CookwithNabeela" and sub == "Chine & Taïwan" and not re.search(r"chinese|chow|noodle|manchurian|fried rice", n): sub = "Inde & Pakistan"
        return f"🌏 Asie : {sub}"
    return LABELS[cat]

def flags_of(title):
    n = nrm(clean(title))
    return (" · 🐖 porc probable" if PORK.search(n) else "") + (" · 🍷 alcool" if ALCOHOL.search(n) else "")
