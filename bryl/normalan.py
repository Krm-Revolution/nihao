import time
import sys
from colorama import init, Fore, Style

init()

def print_smooth(text, delay=0.07):
    for char in text:
        sys.stdout.write(Fore.WHITE + Style.BRIGHT + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_normalan():
    verses = [
        "Dapat mong malaman",
        "Walang personalan ang mga kaganapan",
        "Puwede bang normalan lang lahat ng ito?",
        "Sana ay magkatotoo, pero sa ngayon",
        "",
        "Dapat mong malaman",
        "Walang personalan ang mga kaganapan",
        "Puwede bang normalan lang lahat ng ito?",
        "Sana ay magkatotoo, pero sa ngayon",
        "",
        "'Wag na muna natin isipin",
        "Hirap pa 'ko 'paliwanag ang malabo",
        "Pero lahat ay kaya kong sabihin sa 'yo",
        "Kasi nga wala akong tinatago",
        "'Di ka hahayaan na mabitin pa",
        "Kapag tayo na lang at walang tao",
        "Kaso alam mong ayokong sumugal",
        "Sa mga bagay na alam mong 'di ko kayang ipanalo",
        "",
        "Pangako na 'di kita papangakuan",
        "'Di pa ba natatauhan? (Yeah)",
        "Sa kabila ng magarbong hapunan",
        "Hampasan ng unan ay walang kasiguraduhan",
        "Kasama kang nasa bakuran, sagarang inuman",
        "Alam ko na sa'n papunta",
        "Pero mayro'n bang patutunguhan ang lahat ng ito?",
        "",
        "Sana marinig sa inyo",
        "Para lang alam nilang komplikado man, ang sarap gawin",
        "\"Oo\" na lang ang nasasabi mong tono",
        "Sa tuwing 'babayo ko nang todo",
        "Heto ako 'pag hindi mo trip solo",
        "Malalang paalala din kung mamahalin mo 'ko",
        "",
        "Dapat mong malaman",
        "Walang personalan ang mga kaganapan",
        "Puwede bang normalan lang lahat ng ito?",
        "Sana ay magkatotoo, pero sa ngayon",
        "",
        "Dapat mong malaman",
        "Walang personalan ang mga kaganapan",
        "Puwede bang normalan lang lahat ng ito?",
        "Sana ay magkatotoo, pero sa ngayon",
        "",
        "Sa ngayon, 'di ko lang alam",
        "Sa'n pa ba papunta mga laro nating dalawa",
        "Kumain ka na ba? Walang malisya",
        "Mahalaga, masaya kapag sa 'min ka na aabutan ng umaga",
        "Parang mag-asawa kapag nasa kama, sahig o sala",
        "Banig man na talo-talo na, basta ikaw kasama",
        "",
        "Alam mo na 'yon kung bakit eto lang tayo",
        "Sabihin na nating ayoko pang maniwala",
        "Sa iba't sarili ko na din",
        "'Pag ganitong usapin, nadarang na 'ko dati",
        "Mas natuto makisa-, mahalin mo pa rin",
        "Kaya 'ko sa kabila ng kahit 'di ako kilala?",
        "Walang camera na nakaabang",
        "Kada mapapadaan sa ganap",
        "",
        "At sabay pamasahe lamang nasa pitaka, yeah",
        "Balewala ka sa karamihan",
        "Kasi nga wala 'kong salapi ng",
        "Katulad sa mga magagaling diyan",
        "Magawa mo pa kayang mag-alala sa 'kin",
        "Na parang 'di mo 'ko kayang mawala?",
        "Manatili pa kayang maligaya ka sa 'kin",
        "Kahit 'la 'kong magawa, sila may perang mataba, ha? (Ha, ha)",
        "",
        "Dapat mong malaman",
        "Walang personalan ang mga kaganapan",
        "Puwede bang normalan lang lahat ng ito?",
        "Sana ay magkatotoo (oh), pero sa ngayon",
        "",
        "Dapat mong malaman",
        "Walang personalan ang mga kaganapan",
        "Puwede bang normalan lang lahat ng ito? (Puwede ba?)",
        "Sana ay magkatotoo (oh), pero sa ngayon"
    ]

    for line in verses:
        if line.strip() == "":
            time.sleep(1.8)
        else:
            print_smooth(line)
            time.sleep(0.15 if len(line) < 40 else 0.25)

if __name__ == "__main__":
    sing_normalan()
