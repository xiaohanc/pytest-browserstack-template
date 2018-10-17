options = {
    "iPhone-7-Safari": {'device': 'iPhone 7 Plus', 'realMobile': 'true', 'os_version': '10.0'},
    "iPad-Pro-Safari": {'browserName': 'iPad', 'platform': 'MAC', 'device': 'iPad Pro'},
    "iPhone-6-Safari": {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 6'},
    "Samsung-Galaxy-S8-Chrome": {'device': 'Samsung Galaxy S8', 'realMobile': 'true', 'os_version': '7.0'},
    "Motorola-Moto-X-Chrome": {'device': 'Motorola Moto X 2nd Gen', 'realMobile': 'true', 'os_version': '5.0'},
    "Google-Nexus-6-Chrome": {'device': 'Google Nexus 6', 'realMobile': 'true', 'os_version': '6.0'},
    "Google-Pixel-Chrome": {'device': 'Google Pixel', 'realMobile': 'true', 'os_version': '8.0'},
    "Windows-10-Chrome": {'browser': 'Chrome', 'browser_version': '65.0', 'os': 'Windows', 'os_version': '10'},
    "Windows-8-Chrome": {'browser': 'Chrome', 'browser_version': '65.0', 'os': 'Windows', 'os_version': '8'},
    "OSX-Sierra-Chrome": {'browser': 'Chrome', 'browser_version': '65.0', 'os': 'OS X', 'os_version': 'Sierra'},
    "OSX-Sierra-Safari-10": {'browser': 'Safari', 'browser_version': '10.1', 'os': 'OS X', 'os_version': 'Sierra'},
    "firefox": {'browser': 'Firefox', 'browser_version': '56.0', 'os': 'Windows', 'os_version': '10'}
}

mobilelist = ["iPhone-7-Safari", "iPad-Pro-Safari", "iPhone-6-Safari",
              "Samsung-Galaxy-S8-Chrome",
              "Google-Nexus-6-Chrome", "Google-Pixel-Chrome"]

weblist = ["Windows-10-Chrome", "Windows-8-Chrome", "OSX-Sierra-Chrome"]

cross_all_browser_config = mobilelist + weblist

cross_mobile_browser_config = mobilelist

cross_web_browser_config = weblist
