
from flask import redirect, render_template, session
from functools import wraps
import sqlite3

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
                            'currency':'Beta',
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
                            'currency':'Beta',
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
                            'currency':'Beta',
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
                            'currency':'Beta',
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

        
def get_db_connection():
    conn = sqlite3.connect('zapa.db')
    conn.row_factory = sqlite3.Row
    # with open('schema.sql') as f:
    #     conn.executescript(f.read())
    return conn
   
    
def usd(value):
    """Format value as Beta(made up) Currency."""
    return f"ß {value:,.2f}"
