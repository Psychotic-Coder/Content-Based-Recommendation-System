# PRETTIFY THE PREDICTED RESULTS AND FORMAT UNWANTED DATA

# -------------------IMPORTS---------------------
# IMPORT FOR WEBSCRAPE GOOGLE SEARCH RESLUTS
from googlesearch import search 

# IMPORT FOR GETTING RECOMMENDER ENGINE RESULTS
import engine as eng

# ---------------DATA FILTERING-----------------
# FUNCTION TO GET BRAND NAME
def getName(name):
    if name[0] == 'D':
        return 'Dell'
    elif name[0] == 'M':
        return 'MSI'
    elif name[0] == 'L':
        return 'Lenovo'
    elif name[0] == 'H':
        return 'Hp'
    elif name[0] == 'A':
        if 'Acer' in name:
            return 'Acer'
        elif 'Asus' in name:
            return 'Asus'
        else:
            return 'Apple'
    else:
        return 'NoImg'

# FOR EACH RECOMMENDATION, SCRAPE FIRST WEBSITE.
# STORE RESULTS IN A DICTIONARY FOR EASY JSON CONVERSION
res = []
for i in range(len(eng.res)):
    query = eng.res[i]
    temp = {}
    for j in search(query, tld="co.in", num=10, stop=1, pause=2):
        temp['Name'] = eng.res[i]
        temp['Cpu'] = eng.cpu[i]
        temp['Gpu'] = eng.gpu[i]
        temp['Mem'] = eng.mem[i]
        temp['Price'] = eng.price[i]
        temp['Ram'] = eng.ram[i]
        temp['Link'] = j
        temp['Img'] = getName(eng.res[i])
        res.append(temp) 