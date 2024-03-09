# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCadastrodeusurio2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cadastrodeusurio2(self):
    self.driver.get("https://www.cacaushow.com.br/")
    self.driver.set_window_size(1536, 816)
    self.driver.execute_script("window.scrollTo(0,0)")
    assert self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(2) > li:nth-child(2) .it__above--text").text == "Cacau Lovers"
    element = self.driver.find_element(By.CSS_SELECTOR, ".mt-5 > .slick-list .slick-slide:nth-child(4) img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(2) > li:nth-child(2) .it__above--text").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    assert self.driver.find_element(By.ID, "cadastro").text == "Faça já o seu cadastro!"
    self.driver.find_element(By.ID, "cadastro").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".etapa__0 > p:nth-child(1)").text == "Você ainda não é um Cacau Lover?"
    self.driver.find_element(By.CSS_SELECTOR, ".lovers-input__container:nth-child(4) > #cpf").click()
    self.driver.find_element(By.CSS_SELECTOR, ".lovers-input__container:nth-child(4) > #cpf").send_keys("403.094.270-96")
    self.driver.find_element(By.CSS_SELECTOR, ".form__continuar > #continuar").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".nome").text == "Por favor, informe seu nome e sobrenome"
    self.driver.find_element(By.ID, "nome").click()
    self.driver.find_element(By.ID, "nome").send_keys("Teste")
    self.driver.find_element(By.ID, "sobrenome").click()
    self.driver.find_element(By.ID, "sobrenome").send_keys("Qualidade")
    self.driver.find_element(By.CSS_SELECTOR, ".form__continuar > #continuar").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".data__nascimento").text == "Qual é a sua data de nascimento?"
    self.driver.find_element(By.ID, "dataNascimento").click()
    self.driver.find_element(By.ID, "dataNascimento").send_keys("12/09/1984")
    self.driver.find_element(By.CSS_SELECTOR, ".form__continuar > #continuar").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".info__contato").text == "Quais as suas informações de contato?"
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("teste123.teste@qualidade.com")
    self.driver.find_element(By.ID, "celular").click()
    self.driver.find_element(By.ID, "celular").send_keys("(11) 99990-0001")
    self.driver.find_element(By.CSS_SELECTOR, ".form__continuar > #continuar").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".senha").text == "Cadastre sua senha"
    self.driver.find_element(By.ID, "senha").click()
    self.driver.find_element(By.ID, "senha").send_keys("Gg123456")
    self.driver.find_element(By.CSS_SELECTOR, ".form__continuar > #continuar").click()
    self.driver.find_element(By.ID, "confirmarSenha").click()
    self.driver.find_element(By.ID, "confirmarSenha").send_keys("Gg123456")
    assert self.driver.find_element(By.CSS_SELECTOR, ".lovers-checkbox__container > label").text == "Li e aceito os termos e condições do Programa Cacau Lovers"
    self.driver.find_element(By.ID, "termos").click()
    self.driver.find_element(By.ID, "cadastrar").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cadastro__form .header__voltar__acesso").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cadastro__form .header__voltar__acesso").click()
    self.driver.find_element(By.ID, "celular").click()
    self.driver.find_element(By.ID, "celular").send_keys("(11) 99990-1111")
    self.driver.find_element(By.CSS_SELECTOR, ".form__continuar > #continuar").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form__continuar > #continuar").click()
    self.driver.find_element(By.ID, "cadastrar").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cadastro__form .header__voltar__acesso").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cadastro__form .header__voltar__acesso").click()
    self.driver.find_element(By.ID, "celular").click()
    self.driver.find_element(By.ID, "celular").send_keys("(11) 984253143")
    self.driver.find_element(By.CSS_SELECTOR, ".form__continuar > #continuar").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form__continuar > #continuar").click()
    self.driver.find_element(By.ID, "cadastrar").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".parabens").text == "Parabéns Crush!"
    self.driver.find_element(By.CSS_SELECTOR, ".visibility > .popup > .popup__fechar .fechar__icone").click()
  
