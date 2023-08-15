from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import random

def Buy_product():

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-button')))
    add_to_cart_button.click()

    go_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, 'sw-gtc')))
    go_to_cart_button.click()

    quantity_dropdown = wait.until(EC.element_to_be_clickable((By.ID, 'a-autoid-0')))
    quantity_dropdown.click()

    dropdown_value_select = wait.until(EC.element_to_be_clickable((By.ID, 'quantity_10')))
    dropdown_value_select.click() 

    qty_value = wait.until(EC.element_to_be_clickable((By.NAME, 'quantityBox')))
    qty_value.send_keys('999')

    
    update_button = wait.until(EC.element_to_be_clickable((By.ID, 'a-autoid-1-announce')))
    update_button.click()

    time.sleep(3)

    proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.NAME, 'proceedToRetailCheckout')))
    proceed_to_checkout.click()
    
    time.sleep(3)

    time.sleep(6)

    change_address = wait.until(EC.element_to_be_clickable((By.ID, 'addressChangeLinkId')))
    change_address.click()

    time.sleep(5)

    use_address = wait.until(EC.element_to_be_clickable((By.ID, 'shipToThisAddressButton')))
    use_address.click()

    time.sleep(5)

    bank_account = wait.until(EC.element_to_be_clickable((By.ID, 'apx-add-bank-account-content-trigger-declarative-action-test-id')))
    bank_account.click()

    time.sleep(10)


    driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@style="display: inline;"]'))
    #payment details Enter account number and then futher details
    #Name on Account
    Acc_name = driver.find_element(By.NAME,'ppw-accountHolderName')
    Acc_name.send_keys('Your Name')
    
    #Bank Routing Number
    acc_routing_num = driver.find_element(By.NAME,'addBankAccountRoutingNumber')
    acc_routing_num.send_keys('123456789')

    #Checking Account Number
    bank_number = driver.find_element(By.NAME,'addBankAccountNumber')
    bank_number.send_keys('12345678912345678')

    #Re-enter Checking Account Number
    re_bank_number = driver.find_element(By.NAME,'confirmBankAccountNumber')
    re_bank_number.send_keys('12345678123456789')

    #Driver’s License Number or other State-issued ID
    linc_number = driver.find_element(By.NAME,'addBankAccountDriversLicense')
    linc_number.send_keys('784538546856853')

    time.sleep(2)

    select = driver.find_element(By.XPATH, '//span[@data-action="a-dropdown-button"]')
    select.click()

    time.sleep(3)

    state = driver.find_element(By.LINK_TEXT, 'AZ')
    state.click()

    time.sleep(2)

    check_out = driver.find_element(By.NAME,'ppw-widgetEvent:AddBankAccountEvent')
    check_out.click()
    check_out.send_keys(Keys.RETURN)

    time.sleep(3)



#Here you can update your product list. every product should be in '' and seprated by ,
Product_list = ['https://www.amazon.com/Nightwing-Vol-Get-Grayson/dp/1779517459/ref=pd_bxgy_img_sccl_1/144-7279112-0873911?pd_rd_w=ybDMg&content-id=amzn1.sym.26a5c67f-1a30-486b-bb90-b523ad38d5a0&pf_rd_p=26a5c67f-1a30-486b-bb90-b523ad38d5a0&pf_rd_r=V8ZXTETKNP1GXZGK2XY4&pd_rd_wg=ToaZM&pd_rd_r=10d9c743-cd90-4f52-b9f1-b8430eebefdd&pd_rd_i=1779517459&psc=1',
                'https://www.amazon.com/Nightwing-Vol-1-Leaping-into-Light/dp/1779512783/ref=pd_bxgy_img_sccl_2/144-7279112-0873911?pd_rd_w=ybDMg&content-id=amzn1.sym.26a5c67f-1a30-486b-bb90-b523ad38d5a0&pf_rd_p=26a5c67f-1a30-486b-bb90-b523ad38d5a0&pf_rd_r=V8ZXTETKNP1GXZGK2XY4&pd_rd_wg=ToaZM&pd_rd_r=10d9c743-cd90-4f52-b9f1-b8430eebefdd&pd_rd_i=1779512783&psc=1',
                'https://www.amazon.com/Andalou-Naturals-Roses-Facial-Lotion/dp/B00JEMRFIU/?_encoding=UTF8&_ref=dlx_gate_sd_dcl_tlt_c03d82dd_dt&pd_rd_w=a9sNZ&content-id=amzn1.sym.81a68cec-8afc-4296-99f7-78cf5ddc15b5&pf_rd_p=81a68cec-8afc-4296-99f7-78cf5ddc15b5&pf_rd_r=2SZA6B4A0EKP3X5QVSC5&pd_rd_wg=dFSoF&pd_rd_r=e7ad1bea-5f99-4851-80cc-a1db9c2eb9e3&ref_=pd_gw_unk',
                'https://www.amazon.com/Nightwing-Fear-State-Tom-Taylor/dp/1779515502/ref=pd_vtp_h_pd_vtp_h_sccl_5/144-7279112-0873911?pd_rd_w=nXheV&content-id=amzn1.sym.e16c7d1a-0497-4008-b7be-636e59b1dfaf&pf_rd_p=e16c7d1a-0497-4008-b7be-636e59b1dfaf&pf_rd_r=JRARM754A9GS472KVB2S&pd_rd_wg=LZQAJ&pd_rd_r=4651a314-72c5-4191-9d0e-27e61e0728b3&pd_rd_i=1779515502&psc=1'
                'https://www.amazon.com/Funko-57422/dp/B08WBT7FV2/ref=pd_vtp_h_pd_vtp_h_sccl_2/144-7279112-0873911?pd_rd_w=IDfpK&content-id=amzn1.sym.e16c7d1a-0497-4008-b7be-636e59b1dfaf&pf_rd_p=e16c7d1a-0497-4008-b7be-636e59b1dfaf&pf_rd_r=SXTNK4KY7K6FH4J62Q80&pd_rd_wg=9M8du&pd_rd_r=5fce98a6-c32f-4629-ade0-477abf890e77&pd_rd_i=B08WBT7FV2&psc=1',
                'https://www.amazon.com/Funko-POP-Games-GK/dp/B08WCJ8CT5/ref=pd_bxgy_img_sccl_2/144-7279112-0873911?pd_rd_w=wtHzm&content-id=amzn1.sym.26a5c67f-1a30-486b-bb90-b523ad38d5a0&pf_rd_p=26a5c67f-1a30-486b-bb90-b523ad38d5a0&pf_rd_r=62WHXJH0BXJVQJJNE7ZE&pd_rd_wg=f4ngL&pd_rd_r=102aa9f5-8633-4a96-97a2-fe78f86fcf6d&pd_rd_i=B08WCJ8CT5&psc=1',
                ]


#here you can add your account. by default everyaccount will buy 3 products.
login_dict = {'email':'password'}

chunk_size = 3
j = 0
for email, password in login_dict.items():

    try:
        driver_path = '/path/to/chromedriver'

        # Initialize ChromeDriver
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
        driver.get('https://www.amazon.com')
        driver.maximize_window()
        time.sleep(15)
        # Find the sign-in link and click it
        sign_in_link = driver.find_element(By.XPATH, '//div[@id="nav-tools"]/a[@data-nav-role="signin"]')
        sign_in_link.click()

        # Wait for the login form to appear
        wait = WebDriverWait(driver, 10)
        email_input = wait.until(EC.presence_of_element_located((By.ID, 'ap_email')))

        # Fill in the email and password fields
        time.sleep(random.uniform(2, 5))
        email_input.send_keys(email)
        time.sleep(random.uniform(2, 5))
        email_input.send_keys(Keys.RETURN)
        time.sleep(random.uniform(2, 5))
        password_input = driver.find_element(By.ID, 'ap_password')
        time.sleep(random.uniform(2, 5))
        password_input.send_keys(password)
        # Submit the form
        time.sleep(random.uniform(2, 5))
        password_input.send_keys(Keys.RETURN)        
        time.sleep(random.uniform(8, 11))

        for i in range(j, len(Product_list)):
            chunk = Product_list[i:i + chunk_size]
            j += len(chunk)
            for element in chunk:
                driver.get(element)
                # Wait for the login form to appear
                wait = WebDriverWait(driver, 15)
                Flag = True
                while Flag:
                    try:
                        tag = driver.find_element(By.ID, "availabilityInsideBuyBox_feature_div")
                        tag_text = tag.text
                        if "In Stock" in tag_text:
                        #if product in stoick function will buy it 
                            Buy_product()
                    except: 
                        Flag = False      
            break
        
    except:
        continue
