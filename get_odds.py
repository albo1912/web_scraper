from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import NoSuchElementException

import time


scroll_max = 0
# Start the driver
z = 0
link_list = open('links.txt', 'r')
lines = link_list.readlines()
with webdriver.Chrome('C:\\Users\\geri\\Desktop\\drivers\\chromedriver') as driver:
    # Open URL
    driver.get("https://www.sofascore.com/football/2021-11-14")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)
    driver.set_window_size(375, 900)
    time.sleep(5)
    try:
        driver.find_element(By.XPATH, " //*[text()='Browser']").click()
    excpect NoSuchElementException:
        pass
    for line in lines:
        z += 1
        driver.get(line)
        time.sleep(1)
        teams = driver.find_element(By.CLASS_NAME, "Cell-sc-t6h3ns-0").text #team names
        teams = teams.split(' - ')
        team1 = teams[0]
        team2 = teams[1]
        print(team1, team2)
        driver.execute_script("window.scrollTo(0,300)")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(300,600)")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(600,900)")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(900,1200)")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(1200,1500)")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(1500,1800)")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(1800,2100)")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(2100,2400)")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(2400,2700)")
        time.sleep(1)
        try:
            odds_location = driver.find_element(By.XPATH,
                    f"(//h3[@class='Panel__PanelTitle-sc-1e1p9xt-1 eSSBnm' and text()='winning odds'])")
            print("odds location found")
            driver.execute_script("return arguments[0].scrollIntoView(true);", odds_location)
            time.sleep(1)
            try:

                streaks_h = driver.find_element(By.XPATH,
                        "//div[@class='styles__StreaksTitle-sc-vqcp5e-0 clCIhv' and text()='Head to head streaks']")

                try:
                    time.sleep(1)
                    team_1_odds = driver.find_element(locate_with(By.XPATH,
                            f"(//div[@class='Content-sc-1morvta-0 ixemiF' and text()='{team1}'])").above(streaks_h))
                    print("team 1 odds found streak h")
                    odds_1 = driver.find_element(locate_with(By.CLASS_NAME,
                                                 "styles__Value-sc-8qeh75-2").below(odds_location))  # when the odds are <span color="#00265a" class="styles__Value-sc-8qeh75-2 dDouwH">1.67</span>
                    print(odds_1.text)
                    odds_2 = driver.find_element(locate_with(By.TAG_NAME, 'strong').below(team_1_odds))  # the expected chances of winning are <strong>60%</strong>
                    print(odds_2.text)
                    odds_3 = driver.find_element(locate_with(By.CLASS_NAME, "styles__Opportunity-sc-8qeh75-1").below(odds_location))
                    ##buttonsFrame this team wins with these odds <span class="styles__Opportunity-sc-8qeh75-1 hsTKVS">82%</span>
                    print(odds_3.text)
                    stat = f"{team1}>>{odds_1.text}>>{odds_2.text}>>{odds_3.text}\n"
                    with open('odds.txt', 'a', encoding="utf-8") as f:
                        f.write(stat)
                except (NoSuchElementException, IndexError):
                    print("Cant find team 1 odds")
                    pass
                try:
                    team_2_odds = driver.find_element(locate_with(By.XPATH,
                            f"(//div[@class='Content-sc-1morvta-0 ixemiF' and text()='{team2}'])").above(streaks_h))
                    print("team 2 odds found streak h")
                    odds_1 = driver.find_element(locate_with(By.CLASS_NAME,
                                                             "styles__Value-sc-8qeh75-2").below(team_2_odds))  # when the odds are <span color="#00265a" class="styles__Value-sc-8qeh75-2 dDouwH">1.67</span>
                    print(odds_1.text)
                    odds_2 = driver.find_element(locate_with(By.TAG_NAME, 'strong').below(team_2_odds))  # the expected chances of winning are <strong>60%</strong>
                    print(odds_2.text)
                    odds_3 = driver.find_element(
                        locate_with(By.CLASS_NAME, "styles__Opportunity-sc-8qeh75-1").below(team_2_odds))
                    ##buttonsFrame this team wins with these odds <span class="styles__Opportunity-sc-8qeh75-1 hsTKVS">82%</span>
                    print(odds_3.text)
                    stat = f"{team2}>>{odds_1.text}>>{odds_2.text}>>{odds_3.text}\n"
                    with open('odds.txt', 'a', encoding="utf-8") as f:
                        f.write(stat)
                except (NoSuchElementException, IndexError):
                    print("Cant find team 2 odds")
                    pass
            except NoSuchElementException:
                print("No h2h")
                try:
                    streaks_t = driver.find_element(By.XPATH,
                                                "//div[@class='styles__StreaksTitle-sc-vqcp5e-0 clCIhv' and text()='Team streaks']")
                    try:
                        time.sleep(1)
                        team_1_odds = driver.find_element(locate_with(By.XPATH,
                                f"(//div[@class='Content-sc-1morvta-0 ixemiF' and text()='{team1}'])").above(streaks_t))
                        print("team 1 odds found streak h")
                        odds_1 = driver.find_element(locate_with(By.CLASS_NAME,
                                                     "styles__Value-sc-8qeh75-2").below(odds_location))  # when the odds are <span color="#00265a" class="styles__Value-sc-8qeh75-2 dDouwH">1.67</span>
                        print(odds_1.text)
                        odds_2 = driver.find_element(locate_with(By.TAG_NAME, 'strong').below(team_1_odds))  # the expected chances of winning are <strong>60%</strong>
                        print(odds_2.text)
                        odds_3 = driver.find_element(locate_with(By.CLASS_NAME, "styles__Opportunity-sc-8qeh75-1").below(odds_location))
                        ##buttonsFrame this team wins with these odds <span class="styles__Opportunity-sc-8qeh75-1 hsTKVS">82%</span>
                        print(odds_3.text)
                        stat = f"{team1}>>{odds_1.text}>>{odds_2.text}>>{odds_3.text}\n"
                        with open('odds.txt', 'a', encoding="utf-8") as f:
                            f.write(stat)
                    except (NoSuchElementException, IndexError):
                        print("Cant find team 1 odds")
                        pass
                    try:
                        team_2_odds = driver.find_element(locate_with(By.XPATH,
                                                                      f"(//div[@class='Content-sc-1morvta-0 ixemiF' and text()='{team2}'])").above(
                            streaks_t))
                        print("team 2 odds found streak h")
                        odds_1 = driver.find_element(locate_with(By.CLASS_NAME,
                                                                 "styles__Value-sc-8qeh75-2").below(
                            team_2_odds))  # when the odds are <span color="#00265a" class="styles__Value-sc-8qeh75-2 dDouwH">1.67</span>
                        print(odds_1.text)
                        odds_2 = driver.find_element(locate_with(By.TAG_NAME, 'strong').below(
                            team_2_odds))  # the expected chances of winning are <strong>60%</strong>
                        print(odds_2.text)
                        odds_3 = driver.find_element(
                            locate_with(By.CLASS_NAME, "styles__Opportunity-sc-8qeh75-1").below(team_2_odds))
                        ##buttonsFrame this team wins with these odds <span class="styles__Opportunity-sc-8qeh75-1 hsTKVS">82%</span>
                        print(odds_3.text)
                        stat = f"{team2}>>{odds_1.text}>>{odds_2.text}>>{odds_3.text}\n"
                        with open('odds.txt', 'a', encoding="utf-8") as f:
                            f.write(stat)
                    except (NoSuchElementException, IndexError):
                        print("Cant find team 2 odds")
                        pass
                except (NoSuchElementException, IndexError):
                    print('No t streaks')
                    pass


        except NoSuchElementException:
            print("Cant find odds")
            pass

