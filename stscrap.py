from selenium import webdriver
import requests

class bot:

    def __init__(self, nome_bot):
        self.driver = webdriver.Chrome()

    def steam(self):
        try:
            site = 'https://www.espn.com.br/nfl/estatisticas/time/_/vista/especiais/temporada/2019/tipodetemporada/2'
            self.driver.get(site)
            self.driver.implicitly_wait(7)
#defense
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[3]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[7]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[8]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[9]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[10]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[11]').click()

            stkr = self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]').text
            stty = self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[3]').text
            sty_g =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]').text
            stlkr =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]').text
            sttd =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]').text
            stpr =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[7]').text
            sttpyr =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[8]').text
            styp_g =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[9]').text
            stlpr =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[10]').text
            sttdpr =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[11]').text

            archive = open('buf.html', 'a')
            archive.write('{"ST kickoffs returns":'f'"{stkr}"''}')
            archive.write('{"ST total yards kickoffs return":'f'"{stty}"''}')
            archive.write('{"ST yards/game kickoffs return":'f'"{sty_g}"''}')
            archive.write('{"ST Long kickoffs return":'f'"{stlkr}"''}')
            archive.write('{"ST TD kickoffs return":'f'"{sttd}"''}')
            archive.write('{"ST punts return":'f'"{stpr}"''}')
            archive.write('{"ST total yards punts return":'f'"{sttpyr}"''}')
            archive.write('{"ST yards/game punts return":'f'"{styp_g}"''}')
            archive.write('{"ST long punts return":'f'"{stlpr}"''}')
            archive.write('{"ST TD punts return":'f'"{sttdpr}"''}')


            archive.close()

        except:
        	pass