#!/usr/bin/env python
# coding: utf-8



from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)



from selenium import webdriver
driver.get("https://www.sitedesmarques.com/magasins-agences-points-de-vente/marque-boulanger-476.htm")



colonne=["magasin","adresse"]
df = pd.DataFrame(columns = colonne)



compteur=0





for i in range (1,102):
    ligne=[]
    magasin=driver.find_element(By.XPATH,"""//*[@id="body"]/div[3]/div/div[2]/a["""+str(i)+"""]/div/p[1]""")
    print(magasin.text)
    ligne.append(magasin.text)
    adresse=driver.find_element(By.XPATH,"""//*[@id="body"]/div[3]/div/div[2]/a["""+str(i)+"""]/div/p[2]""")
    print(adresse.text)
    ligne.append(adresse.text)
    df.loc[compteur]=ligne
    compteur+=1
    




print(df)





df.to_excel("boulanger.xlsx",index=True,header=True)




