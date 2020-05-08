from bs4 import BeautifulSoup
import requests

def gitsavannahgnuorgCode(sp):
    return(sp.code.text)

def gitsambaorg(sp):
    rtn = ""
    outerDiv = sp.findAll("div", {"class": "page_body"})
    for div in outerDiv:
        pres = div.findAll("div", {"class": "pre"})
        for pre in pres:
            txt = pre.find(text = True, recursive = False)
            rtn += txt + "\n"
    return(rtn)

def gitphpnet(sp):
    rtn = ""
    outerDiv = sp.findAll("div", {"class": "page_body"})
    for div in outerDiv:
        pres = div.findAll("div", {"class": "pre"})
        for pre in pres:
            txt = pre.find(text = True, recursive = False)
            rtn += txt + "\n"
    return(rtn)

def cgitkdeorg(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitganetiorg(sp):
    rtn = ""
    outerDiv = sp.findAll("div", {"class": "page_body"})
    for div in outerDiv:
        pres = div.findAll("div", {"class": "pre"})
        for pre in pres:
            spans = pre.findAll("span")
            for span in spans:
                txt = span.find(text = True, recursive = False)
                if txt is not None:
                    rtn += txt + "\n"
    return(rtn)