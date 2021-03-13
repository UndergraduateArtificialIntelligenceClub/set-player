from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import time
from collections import defaultdict

cc = None

class App:
    def __init__(self):
        self.game_url = "https://setwithfriends.com/"
        self.opts = webdriver.FirefoxOptions()
        self.opts.add_argument("--incognito")
        self.driver = webdriver.Firefox(options=self.opts)

    def run(self):
        self.driver.get(self.game_url)
        selectText = """1. Press (P/p)lay to play\n2. Press (Q/q)uit to quit\n>> """
        while True:
            inp = input(selectText)

            if inp.isalpha():
                if inp.lower() == 'q':
                    break

                elif inp.lower() == 'p':
                    for _ in range(20):
                        self.play()
                        time.sleep(0.1)

        #self.driver.quit()

    def get_active_cards(self):
        global cc
        root = self.driver.find_element_by_id("root")
        cont = root.find_element_by_class_name("MuiContainer-root")
        g1 = cont.find_elements_by_css_selector('div[class*="MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded"]')[1]
        g2 = g1.find_elements_by_css_selector('div')

        self.activeCardConts = []
        for div in g2:
            if 'visible' in div.get_attribute('style'):
                cardCont = div.find_element_by_css_selector('div')
                self.activeCardConts.append(cardCont)

        cc = self.activeCardConts

    def find_a_set(self, cards):
        # (shape, color, shading, number)

        for card1 in cards:
            for card2 in cards:
                for card3 in cards:
                    if card1 != card2 and card2 != card3 and card3 != card1:
                        shapes, colors, shadings, numbers = map(lambda _: defaultdict(int), range(4))
                        for card in [card1, card2, card3]:
                            shape, color, shading, number = card 

                            shapes[shape] += 1
                            colors[color] += 1
                            shadings[shading] += 1
                            numbers[number] += 1
                        
                        if self.isSet(shapes, colors, shadings, numbers):
                            return (card1, card2, card3)

    def isSet(self, shapes, colors, shadings, numbers):
        # counts of those metric for 3 choosen cards
        for metric in [shapes, colors, shadings, numbers]:
            if 2 in metric.values():
                return False

        # DEBUG
        """
        pprint(shapes)
        pprint(colors)
        pprint(shadings)
        pprint(numbers)
        """

        return True

    def play(self):
        # Sets the activeCardConts
        self.get_active_cards()

        get_card_cont = {}
        cards = []
        for activeCardCont in self.activeCardConts:
            card = self.extract_card_info(activeCardCont)
            get_card_cont[card] = activeCardCont
            cards.append(card)

        for card in (m:=self.find_a_set(cards)):
            get_card_cont[card].click()
        
        print(m)

    def extract_card_info(self, cardCont):
        # cardCont: instance of FirefoxWebElement class

        colorMap = {
            '#800080': 'violet',
            '#ff47ff': 'violet',
            '#ff0101': 'red',
            '#ffb047': 'red',
            '#008002': 'green',
            '#00b803': 'green'
        }

        """
        div # The card div itself
         - [svg]
           - [use] 
               use1: {
                   # Shade
                   href: #shapeName
                   fill: #... // Striped/Shaded
                   mask: ... // Non-empty -> Shaded
                   // No stroke
               }
               use2: {
                   # Border
                   href: ...
                   stroke: #...
               }
        """

        svgs = cardCont.find_elements_by_css_selector('svg')

        # Check only one because the every one of them are identical
        svg = svgs[0]
        uses = svg.find_elements_by_css_selector('use')

        # Shading
        use1 = uses[0]
        href, fill, mask = map(lambda attr: use1.get_attribute(attr), ['href', 'fill', 'mask'])

        # Color
        use2 = uses[1]
        stroke = use2.get_attribute('stroke')

        shape = href.strip("#")
        color = colorMap[stroke]
        shading = 'open' if fill == 'transparent' else ('solid' if mask == "" else 'shaded')
        number = len(svgs)

        #print(shape, color, shading, number)

        return (shape, color, shading, number)


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()