import objectify as ob

cr = ob.WebCrawler()

cr.__init__()

cr.setup_webdriver()

cr.navigate_to_category()

cr.extract_data()

cr.analyze_data()

cr.send_email()



