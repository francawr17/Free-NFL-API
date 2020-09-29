from selenium import webdriver
import requests

class bot:

    def __init__(self, nome_bot):
        self.driver = webdriver.Chrome()

    def erros(self):
        try:
            site = 'https://www.espn.com.br/nfl/estatisticas/time/_/vista/turnovers/temporada/2019/tipodetemporada/2'
            self.driver.get(site)
            self.driver.implicitly_wait(7)
#defense
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[10]/td[3]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[10]/td[4]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[10]/td[6]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[10]/td[7]').click()

            inte = self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[10]/td[3]').text
            fr = self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[10]/td[4]').text
            sinter =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[10]/td[6]').text
            fl =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[10]/td[7]').text

            archive = open('buf.html', 'a')
            archive.write('{"interceptions":'f'"{inte}"''}')
            archive.write('{"fumbles recovered":'f'"{fr}"''}')
            archive.write('{"suffered interceptions":'f'"{sinter}"''}')
            archive.write('{"fumbles lost":'f'"{fl}"''}')

            archive.close()

        except:
        	pass