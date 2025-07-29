import time
import sys
from colorama import init, Fore, Style

init()

def print_lyric(char, speed):
    sys.stdout.write(Fore.WHITE + Style.BRIGHT + char + Style.RESET_ALL)
    sys.stdout.flush()
    time.sleep(speed)

def sing_nadarang():
    lyrics = [
        ("Andiyan ka na naman", 0.06),
        ("Ba't 'di ko maiwasang tumingin sa 'yong liwanag?", 0.05),
        ("Nadarang na naman sa 'yong apoy", 0.06),
        ("Bakit ba laging hinahayaan?", 0.07),
        ("", 0),
        ("Andiyan ka na naman", 0.06),
        ("Ba't 'di ko maiwasang tumingin sa 'yong liwanag?", 0.05),
        ("Nadarang na naman sa 'yong apoy", 0.06),
        ("Handang masaktan kung kinakailangan", 0.07),
        ("", 0),
        ("May lakad ka ba mamaya?", 0.08),
        ("Puwede ka ba makasama sa paggagala?", 0.06),
        ("Kung sakaling 'di ka puwede", 0.07),
        ("Sa bagay, mayro'n din akong ginagawa", 0.06),
        ("Siguro nga, napapaisip ka", 0.07),
        ("Ba't ako nangangamusta?", 0.08),
        ("Ilang araw ka nang naroon sa panaginip ko", 0.05),
        ("Nag-aalala lang ako, baka sa'n ka mapunta", 0.06),
        ("", 0),
        ("Pero mukhang ayos ka naman", 0.07),
        ("Kahit 'di na kita abalahin pa", 0.06),
        ("Ilang \"Ama Namin\" pa ba ang dapat", 0.07),
        ("Para patago kang mag-alala sa 'kin? Uh", 0.06),
        ("Habang pinapantasya lamang nila", 0.07),
        ("Ay maskara mo sa gabi at pitaka mo sa umaga", 0.05),
        ("'Yung \"ikaw\" sa likod ng kolorete pa din", 0.06),
        ("Ang nangangahulugan sa salitang \"paraiso\" para sa 'kin", 0.05),
        ("", 0),
        ("Bakit kaya kayamanan ko pa din kinikilala ang iyong pagtawa?", 0.05),
        ("Kahit na sa puso mo man ay ilang dosena na din ang kasya", 0.05),
        ("Dati pa 'ko pinagdamutan ng kapalaran", 0.06),
        ("Kaya 'di na bago sa 'kin mawalan ng pag-asa", 0.06),
        ("Ala-una ng umaga na naman", 0.07),
        ("Tawagan mo na lang ulit ako kapag hindi na kayo magkasama", 0.05),
        ("", 0),
        ("Andiyan ka na naman", 0.06),
        ("Ba't 'di ko maiwasang tumingin sa 'yong liwanag?", 0.05),
        ("Nadarang na naman sa 'yong apoy", 0.06),
        ("Bakit ba laging hinahayaan?", 0.07),
        ("", 0),
        ("Andiyan ka na naman", 0.06),
        ("Ba't 'di ko maiwasang tumingin sa 'yong liwanag?", 0.05),
        ("Nadarang na naman sa 'yong apoy", 0.06),
        ("Handang masaktan kung kinakailangan", 0.07),
        ("", 0),
        ("May lakad ka ba mamaya?", 0.08),
        ("Sana madaanan mo 'ko pagkatapos", 0.06),
        ("Sabihin mo ngayong ako'y makakaasang", 0.06),
        ("Dito ka dadalhin ng iyong sapatos", 0.06),
        ("Kung ngayong gabi lang naman ang magiging dahilan", 0.05),
        ("Ay handang-handa pa din naman ako mamaos", 0.06),
        ("Makakaluwag ka man ay sa mas nakakalibang", 0.05),
        ("Na paraan kita tutulungan makaraos", 0.06),
        ("", 0),
        ("Bakit ka nagparamdam?", 0.08),
        ("Siguro, 'di na kayo nilanggam", 0.07),
        ("Bakit kaya 'di n'ya alam", 0.07),
        ("Ang 'yong halaga't kung gaano ka kalinamnam?", 0.06),
        ("Iniwasan ko mang matakam nang 'di halata", 0.05),
        ("Ang hirap nang magpabaya", 0.07),
        ("Kapag tawag na ng laman ang nagbadya", 0.06),
        ("Makipaglangit-lupa nang walang taya", 0.06),
        ("", 0),
        ("Mata sa mata, bibig sa bibig", 0.07),
        ("Mga ingay na tayo lang dalawa nakadinig", 0.06),
        ("Nakatawang umidlip sa kama", 0.07),
        ("Pero ba't wala ka na pagsapit ng umaga?", 0.06),
        ("", 0),
        ("Andiyan ka na naman", 0.06),
        ("Ba't 'di ko maiwasang tumingin sa 'yong liwanag?", 0.05),
        ("Nadarang na naman sa 'yong apoy", 0.06),
        ("Bakit ba laging hinahayaan?", 0.07),
        ("", 0),
        ("Andiyan ka na naman", 0.06),
        ("Ba't 'di ko maiwasang tumingin sa 'yong liwanag?", 0.05),
        ("Nadarang na naman sa 'yong apoy", 0.06),
        ("Handang masaktan kung kinakailangan", 0.07)
    ]

    for line, speed in lyrics:
        if not line:
            time.sleep(2.0)
            continue

        for char in line:
            print_lyric(char, speed)
            if char in ",.?!":
                time.sleep(0.3)

        print()
        time.sleep(0.8 if len(line) < 40 else 1.2)

if __name__ == "__main__":
    sing_nadarang()
