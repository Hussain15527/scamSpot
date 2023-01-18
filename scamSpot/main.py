# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.chrome.options import Options

# import time
# PATH = "D:\yaha\PROJECT\SELENIUM\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

#method 1
# driver.get('http://14.139.221.18:9001/admissionprint.aspx?Id=21U10540')


# mehtod 2

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=options, executable_path=PATH)

# driver.get('http://14.139.221.18:9001/admissionprint.aspx?Id=21U10540')



# method 3

def download_pdf(lnk):
    
    from selenium import webdriver
    from time import sleep
    
    options = webdriver.ChromeOptions()
    
    download_folder = "D:\\yaha\\PROJECT\\scamSpot\\file"  
    # "C:\\Users\\omprakashpk\\Documents
    profile = {"plugins.plugins_list": [{"enabled": False,
                                         "name": "Chrome PDF Viewer"}],
                "download.prompt_for_download": False,
               "download.default_directory": download_folder,
               "download.extensions_to_open": "",
               "plugins.always_open_pdf_externally": True,
               
               }
    
    options.add_experimental_option("prefs", profile)
    
    # print("Downloading file from link: {}".format(lnk))
        
    driver = webdriver.Chrome(chrome_options = options)
    driver.get(lnk)
    sleep(2)
    # filename = lnk.split("/")[4].split(".cfm")[0]
    # print("File: {}".format(filename))
    
    # print("Status: Download Complete.")
    # print("Folder: {}".format(download_folder))
    
    driver.close()


link = 'http://14.139.221.18:9001/admissionprint.aspx?Id=21U10540'
download_pdf(link)