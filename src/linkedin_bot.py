import time
from src import config
from src.utils.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class LinkedInBot:
    def __init__(self):
        self.browser = Browser()
        self.driver = self.browser.driver

    def login(self):
        print("Opening LinkedIn login page...")
        self.browser.open("https://www.linkedin.com/login")
        time.sleep(2)

        # Preencher email e senha
        self.driver.find_element(By.ID, "username").send_keys(config.LINKEDIN_EMAIL)
        self.driver.find_element(By.ID, "password").send_keys(config.LINKEDIN_PASSWORD)

        # Clicar no botão de login
        self.driver.find_element(By.XPATH, '//*[@type="submit"]').click()

        time.sleep(3)
        print("Login complete!")

    def close(self):
        self.browser.quit()

    def search_recruiters(self, keyword="Tech Recruiter", locations=None):
        """
        Busca pessoas na rede com base na keyword e nas localizações.
        :param keyword: palavra-chave a pesquisar
        :param locations: lista de países ou cidades
        :return: lista de URLs de perfis encontrados
        """
        if locations is None:
            locations = []

        print(f"Searching for '{keyword}' in locations: {locations}")

        # Abrir pesquisa de pessoas
        self.browser.open("https://www.linkedin.com/search/results/people/")
        time.sleep(3)

        # Inserir palavra-chave
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@role="combobox" and (contains(@placeholder, "Search") or contains(@placeholder, "Pesquisar"))]')
            )
        )
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # Abrir menu "Todos os filtros"
        try:
            all_filters_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "search-reusables__all-filters-pill-button")
                )
            )
            all_filters_button.click()
            time.sleep(2)
        except:
            print("Could not open 'All filters'. Layout may have changed.")
            return []

        # Map de localidades em português
        location_map = {
            "India": "Índia",
            "Colombia": "Colômbia",
            "Argentina": "Argentina",
            "Ukraine": "Ucrânia",
            "Istanbul": "Istambul",
            "United States": "Estados Unidos",
            "Spain": "Espanha",
            "Italy": "Itália"
        }

        # Aplicar filtros de localização
        for location in locations:
            try:
                # Clicar no botão "Adicionar localidade"
                print('# Clicar no botão "Adicionar localidade"')
                add_location_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "reusable-search-filters-advanced-filters__add-filter-button")]//span[contains(text(), "Adicionar localidade")]')))
                
                print(f"ADD localtindon button: {add_location_button}" )

                add_location_button.click()
                time.sleep(1)

                # # Encontrar o input de localidade
                # location_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Adicionar localidade")]')))

                # # Limpar e digitar a localidade
                # location_input.clear()
                # location_name = location_map.get(location, location)
                # location_input.send_keys(location_name)
                # time.sleep(2)  # Esperar o dropdown carregar

            except Exception as e:
                print(f"Could not select location: {location}. Error: {e}")
                continue


        #         # Selecionar a primeira opção do dropdown
        #         # Tentar diferentes seletores para maior robustez
        #         try:
        #             first_option = WebDriverWait(self.driver, 5).until(
        #                 EC.element_to_be_clickable(
        #                     (By.XPATH, '//div[contains(@class, "basic-result")]//span[contains(@class, "basic-typeahead__highlight")]')
        #                 )
        #             )
        #             first_option.click()
        #         except:
        #             # Tentar outro seletor
        #             first_option = WebDriverWait(self.driver, 5).until(
        #                 EC.element_to_be_clickable(
        #                     (By.XPATH, '//li[contains(@class, "search-reusables__collection-values-item")]')
        #                 )
        #             )
        #             first_option.click()
                    
        #         time.sleep(1)

        #         # Se precisar adicionar mais localidades, clicar novamente no botão "Adicionar"
        #         if location != locations[-1]:
        #             add_location_button = WebDriverWait(self.driver, 5).until(
        #                 EC.element_to_be_clickable(
        #                     (By.XPATH, '//button[contains(text(), "Adicionar") or contains(@aria-label, "Adicionar")]')
        #                 )
        #             )
        #             add_location_button.click()
        #             time.sleep(1)

        #     except Exception as e:
        #         print(f"Could not select location: {location}. Error: {e}")
        #         continue

        # # Aplicar os filtros
        # try:
        #     show_results_button = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable(
        #             (By.XPATH, '//button[contains(@aria-label, "Aplicar") or contains(@aria-label, "Aplicar filtros") or contains(text(), "Aplicar")]')
        #         )
        #     )
        #     show_results_button.click()
        #     time.sleep(3)
        # except:
        #     print("Could not find apply filters button.")
        #     # Tentar alternativa caso o botão principal não seja encontrado
        #     try:
        #         alternative_button = WebDriverWait(self.driver, 5).until(
        #             EC.element_to_be_clickable(
        #                 (By.XPATH, '//button[contains(@aria-label, "Exibir resultados")]')
        #             )
        #         )
        #         alternative_button.click()
        #         time.sleep(3)
        #     except:
        #         print("Could not apply filters.")
        #         return []

        # # Coletar URLs dos perfis da primeira página
        # profiles = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "/in/")]'))
        # )
        
        # profile_links = []
        # for p in profiles:
        #     href = p.get_attribute("href")
        #     if href and "search" not in href and href not in profile_links:
        #         profile_links.append(href)

        # print(f"Found {len(profile_links)} profiles")
        # return profile_links

