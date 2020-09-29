from selenium import webdriver
import requests

class bot:

    def __init__(self, nome_bot):
        self.driver = webdriver.Chrome()

    def defense(self):
        try:
            site = 'https://www.espn.com.br/nfl/estatisticas/time/_/vista/defense/temporada/2019/tipodetemporada/2'
            self.driver.get(site)
            self.driver.implicitly_wait(7)
#defense
            '''self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[9]/td[1]').click()'''
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[2]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[3]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[4]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[5]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[6]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[7]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[8]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[9]').click()

            '''dgp = self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[9]/td[1]').text'''
            dyds = self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[2]').text
            dyds_g =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[3]').text
            dpyds =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[4]').text
            dpyds_g =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[5]').text
            dryds =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[6]').text
            dryds_g =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[7]').text
            dpts =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[8]').text
            dpts_g =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[9]').text

            archive = open('buf.html', 'a')
            archive.write('{"defensive total yards":'f'"{dyds}"''}')
            archive.write('{"defensive yards/game":'f'"{dyds_g}"''}')
            archive.write('{"defensive pass yards":'f'"{dpyds}"''}')
            archive.write('{"defensive pass yard/game":'f'"{dpyds_g}"''}')
            archive.write('{"defensive rush yard":'f'"{dryds}"''}')
            archive.write('{"defensive rush yard/game":'f'"{dryds_g}"''}')
            archive.write('{"defensive total points":'f'"{dpts}"''}')
            archive.write('{"defensive points/game":'f'"{dpts_g}"''}')

            archive.close()

        except:
        	pass