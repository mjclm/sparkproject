def import_data(loc,first_year, last_year):
    """ 
        import data from a gas, stations and services file and unzip it
    """
    import zipfile
    import requests
    import urllib.request
 
    # Copy a network object to a local file

    
    table = ["Prix", "Stations", "Services"]
    
    for i in range(first_year, last_year + 1):
        for t in table :
            i = str(i)
            ti = t + i
            tiz = ti+".zip"
            ltiz = loc + tiz
            r = requests.get(ltiz)
            open(tiz, 'wb').write(r.content)
            with zipfile.ZipFile(tiz,"r") as zip_ref:
                zip_ref.extractall("data")
