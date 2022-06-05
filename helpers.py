# import os
# import requests
# import urllib.parse
from urllib.parse import quote, urlencode, quote_plus
# import json

from flask import redirect, render_template, request, session, url_for, json
from functools import wraps

from requests.models import Response
from werkzeug.wrappers import response


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def closer(data):
    """Look up quote for symbol."""

    

    data=  {
                'Closer.Alt':    {
                            'companyName':'Closer.Alt',
                            'currency':'USD',
                            'latestPrice':40.91,
                            'nft':'Closer.Alt'
                            # 'image':url
                        }
                    
                }

   
    try:
        for k, v in data.items():
            if type(v) is dict:
                return {
                    "name": v["companyName"],
                    "price": float(v["latestPrice"]),
                    "NFT": v["nft"]
                    # "image": nft["image"]
                }
    except (KeyError, TypeError, ValueError):
        return None


def dem_say(data):
    """Look up quote for symbol."""


    data=  {
                'Dem.Say.Alt': {
                            'companyName':'Dem.Say.Alt',
                            'currency':'USD',
                            "latestPrice":24.54,
                            'nft':'Dem.Say.Alt'
                        }                    
                }

  
    
    try:
        for k, v in data.items():
            if type(v) is dict:
                return {
                    "name": v["companyName"],
                    "price": float(v["latestPrice"]),
                    "NFT": v["nft"]
                    # "image": nft["image"]
                }
    except (KeyError, TypeError, ValueError):
        return None


def kilimanjaro(data):
    """Look up quote for symbol."""

    # url = f"file:///Users/z.emmanuel/Documents/CS50/finance/static/images/img1.jpg"

    data=  {                
                'Kilimanjaro.Alt':  {
                            'companyName':'Kilimanjaro.Alt',
                            'currency':'USD',
                            'latestPrice':29.76,
                            'nft':'Kilimanjaro.Alt'
                        }
                }

    # NFT = data.value()
    
    try:
        for k, v in data.items():
            if type(v) is dict:
                return {
                    "name": v["companyName"],
                    "price": float(v["latestPrice"]),
                    "NFT": v["nft"]
                    # "image": nft["image"]
                }
    except (KeyError, TypeError, ValueError):
        return None


def naomi(data):
    """Look up quote for symbol."""

    # url = f"file:///Users/z.emmanuel/Documents/CS50/finance/static/images/img1.jpg"

    data=  {                
                'Naomi.Alt':  {   
                            'companyName':'Naomi.Alt',
                            'currency':'USD',
                            'latestPrice':30.76,
                            'nft':'Naomi.Alt'
                        }
                    
                }

    # NFT = data.value()
    
    try:
        for k, v in data.items():
            if type(v) is dict:
                return {
                    "name": v["companyName"],
                    "price": float(v["latestPrice"]),
                    "NFT": v["nft"]
                    # "image": nft["image"]
                }
    except (KeyError, TypeError, ValueError):
        return None

        
        
   
    
def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
