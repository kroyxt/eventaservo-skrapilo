from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import skrapado.constants as const


class ProksimaEvento(webdriver.Firefox):
    def __init__(self):
        self.service = FirefoxService(GeckoDriverManager().install())
        self.options = Options()
        self.options.add_argument("-headless")
        super(ProksimaEvento, self).__init__(options=self.options)
        self.implicitly_wait(30)
        self.maximize_window()

    def iru_al_cxefpagxo(self):
        self.get(const.BAZA_LIGILO)
        print(const.BAZA_LIGILO)

    def selektu_mondparto(self, mondparto):
        elektita_mondparto = self.find_element(
            By.XPATH,
            f"//div[@id='events_container']/div[@class='text-center m-2']/a[contains(text(), '{mondparto.capitalize()}')]"
        )
        elektita_mondparto.click()

    def obtenu_okazantajn_eventojn(self):
        okazantaj_eventoj = self.find_elements(
            By.XPATH,
            "//div[@class='okazantaj-eventoj']"
        )
        if len(okazantaj_eventoj) >= 1:
            # print("**********")
            # print("Okazantaj Eventoj:")
            # print("**********")
            for okazanta_evento in okazantaj_eventoj:
                nomo = okazanta_evento.find_element(By.XPATH, "./h6/a").text
                dato = okazanta_evento.find_element(By.XPATH, "./h6/div").text
                print(f"Nomo: {nomo}")
                print(f"Dato: {dato}")
                print("**********")
