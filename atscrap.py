from selenium import webdriver
import requests

class bot:

    def __init__(self, nome_bot):
        self.driver = webdriver.Chrome()

    def attack(self):
        try:
            site = 'https://www.espn.com.br/nfl/estatisticas/time/_/temporada/2019/tipodetemporada/2'
            self.driver.get(site)
            self.driver.implicitly_wait(7)
#attack
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[1]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[2]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[3]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[4]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[5]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[6]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[7]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[8]').click()
            self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[9]').click()


            gp = self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[1]').text
            yds = self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[2]').text
            yds_g =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[3]').text
            pyds =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[4]').text
            pyds_g =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[5]').text
            ryds =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[6]').text
            ryds_g =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[7]').text
            pts =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[8]').text
            pts_g =self.driver.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[9]').text

            archive = open('kc.html', 'w')
            archive.write('{"team":"Kansas City Chiefs"}')
            archive.write('{"league":"AFC West"}')
            archive.write('{"season":"2019-2020"}')
            archive.write('{"games playeds":'f'"{gp}"''}')
            archive.write('{"total yards":'f'"{yds}"''}')
            archive.write('{"yards/game":'f'"{yds_g}"''}')
            archive.write('{"pass yards":'f'"{pyds}"''}')
            archive.write('{"pass yards/game":'f'"{pyds_g}"''}')
            archive.write('{"rush yards":'f'"{ryds}"''}')
            archive.write('{"rush yards/game":'f'"{ryds_g}"''}')
            archive.write('{"total points":'f'"{pts}"''}')
            archive.write('{"points/game":'f'"{pts_g}"''}')

            archive.close()

        except:
            pass