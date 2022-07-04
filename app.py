# import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, closer, dem_say, kilimanjaro, naomi, usd
# import sqlite3

# Configure application
app = Flask(__name__)


#######¡¡¡¡¡ THANKS CS50 !!!!!#######

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///gallery.db")



@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    #read database for user share values and nfts
    rows = db.execute("""SELECT NFT, SUM(edition) as S_total
                            FROM purchases
                            WHERE user_id = :user_id
                            GROUP BY NFT;""",
                            user_id=session["user_id"])

    #create list for database values to display
    portfolio = []

    total_cash = 0



    #update cash
    rows = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])

    total_cash += rows[0]["cash"]

    #return update portfolio
    return render_template("index.html", purchases=portfolio, cash=usd(rows[0]["cash"]), total=usd(total_cash))


@app.route("/buy_closer", methods=["GET", "POST"])
@login_required
def buy_closer():
    """Buy edition of NFT"""
    if request.method == "POST":

        #verify nft field isn't null
        if not request.form.get("NFT"):
            return apology("must provide NFT", 400)

        #verify nft
        elif not closer(request.form.get("NFT")):
            return apology("NFT does not exist", 400)

        #get proper share values
        elif not request.form.get("edition").isdigit():
            return apology("must provide valid edition", 400)

        #get positive values for "edition" input
        edition = int(request.form.get("edition"))

        if edition is None or edition <= 0:
            return apology("please enter proper share values", 403)

        NFT = request.form.get("NFT")
        stock = closer(NFT)
        # image = lookup(NFT)

        rows = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = rows[0]["cash"]

        balance = cash - edition * stock['price']
        if balance < 0:
            return apology("insufficient funds")
        db.execute("UPDATE users SET cash=:balance WHERE id=:id",
                    balance=balance, id=session["user_id"])

        db.execute("""INSERT INTO purchases (user_id, NFT, price, edition)
                    VALUES(:user_id, :NFT, :price, :edition)""",
                    user_id=session["user_id"],
                    NFT = stock["NFT"],
                    price = stock["price"],
                    edition = edition)
        flash("Closer Bought!")
        return redirect("/")
    # else:
    #     return render_template("buy.html")


@app.route("/buy_dem_say", methods=["GET", "POST"])
@login_required
def buy_dem_say():
    """Buy edition of NFT"""
    if request.method == "POST":

        #verify nft field isn't null
        if not request.form.get("NFT"):
            return apology("must provide NFT", 400)

        #verify nft
        elif not dem_say(request.form.get("NFT")):
            return apology("NFT does not exist", 400)

        #get proper share values
        elif not request.form.get("edition").isdigit():
            return apology("must provide valid edition", 400)

        #get positive values for "edition" input
        edition = int(request.form.get("edition"))

        if edition is None or edition <= 0:
            return apology("please enter proper share values", 403)

        NFT = request.form.get("NFT")
        stock = dem_say(NFT)
        # image = lookup(NFT)

        rows = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = rows[0]["cash"]

        balance = cash - edition * stock['price']
        if balance < 0:
            return apology("insufficient funds")
        db.execute("UPDATE users SET cash=:balance WHERE id=:id",
                    balance=balance, id=session["user_id"])

        db.execute("""INSERT INTO purchases (user_id, NFT, price, edition)
                    VALUES(:user_id, :NFT, :price, :edition)""",
                    user_id=session["user_id"],
                    NFT = stock["NFT"],
                    price = stock["price"],
                    edition = edition)
        flash("Dem Say Bought!")
        return redirect("/")
    # else:
    #     return render_template("buy.html")


@app.route("/buy_kilimanjaro", methods=["GET", "POST"])
@login_required
def buy_kilimanjaro():
    """Buy edition of NFT"""
    if request.method == "POST":

        #verify nft field isn't null
        if not request.form.get("NFT"):
            return apology("must provide NFT", 400)

        #verify nft
        elif not kilimanjaro(request.form.get("NFT")):
            return apology("NFT does not exist", 400)

        #get proper share values
        elif not request.form.get("edition").isdigit():
            return apology("must provide valid edition", 400)

        #get positive values for "edition" input
        edition = int(request.form.get("edition"))

        if edition is None or edition <= 0:
            return apology("please enter proper share values", 403)

        NFT = request.form.get("NFT")
        stock = kilimanjaro(NFT)
        # image = lookup(NFT)

        rows = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = rows[0]["cash"]

        balance = cash - edition * stock['price']
        if balance < 0:
            return apology("insufficient funds")
        db.execute("UPDATE users SET cash=:balance WHERE id=:id",
                    balance=balance, id=session["user_id"])

        db.execute("""INSERT INTO purchases (user_id, NFT, price, edition)
                    VALUES(:user_id, :NFT, :price, :edition)""",
                    user_id=session["user_id"],
                    NFT = stock["NFT"],
                    price = stock["price"],
                    edition = edition)
        flash("Kilimanjaro Bought!")
        return redirect("/")
    # else:
    #     return render_template("buy.html")



@app.route("/buy_naomi", methods=["GET", "POST"])
@login_required
def buy_naomi():
    """Buy edition of NFT"""
    if request.method == "POST":

        #verify nft field isn't null
        if not request.form.get("NFT"):
            return apology("must provide NFT", 400)

        #verify nft
        elif not naomi(request.form.get("NFT")):
            return apology("NFT does not exist", 400)

        #get proper share values
        elif not request.form.get("edition").isdigit():
            return apology("must provide valid edition", 400)

        #get positive values for "edition" input
        edition = int(request.form.get("edition"))

        if edition is None or edition <= 0:
            return apology("please enter proper share values", 403)

        NFT = request.form.get("NFT")
        stock = naomi(NFT)
        # image = lookup(NFT)

        rows = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = rows[0]["cash"]

        balance = cash - edition * stock['price']
        if balance < 0:
            return apology("insufficient funds")
        db.execute("UPDATE users SET cash=:balance WHERE id=:id",
                    balance=balance, id=session["user_id"])

        db.execute("""INSERT INTO purchases (user_id, NFT, price, edition)
                    VALUES(:user_id, :NFT, :price, :edition)""",
                    user_id=session["user_id"],
                    NFT = stock["NFT"],
                    price = stock["price"],
                    edition = edition)
        flash("Naomi Bought!")
        return redirect("/")
    # else:
    #     return render_template("buy.html")


@app.route("/records")
@login_required
def records():
    """Show history of transactions"""

    #read database for user share values and NFTs
    rows = db.execute("""SELECT *
                            FROM purchases
                            WHERE user_id = :user_id;""",
                            user_id=session["user_id"])

    #create list for database values to display
    portfolio = []

    total_cash = 0

    #connecting database to corresponding value(list)
    for row in rows:
        portfolio.append({
            "NFT": row["NFT"],
            "edition": row["edition"],
            "price": usd(row["price"]),
            "transacted": row["transaction"]
        })

    #update cash
    rows = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])

    total_cash += rows[0]["cash"]

    #return update portfolio
    return render_template("records.html", purchases=portfolio, cash=usd(rows[0]["cash"]), total=usd(total_cash))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']

        hash = generate_password_hash(password)

        # Ensure username was submitted
        if username is None or not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif password is None or not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide password again.", 400)

        if request.form.get("confirmation") != request.form.get("password"):
            return apology("Password un-matched, try again.", 400)


        try:
            # insert username and password hash to database
            rows = db.execute("INSERT INTO users (username, hash) VALUES(?,?)",
                        username, hash)

        except:
            return apology("Username already taken.", 400)


        flash("Registered!")
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def change_password():

    if request.method == "POST":

        user_id=session["user_id"]

        c_password = request.form['current_password']
        n_password = request.form['new_password']

        hash = generate_password_hash(n_password)

        # update password hash in database
        db.execute("UPDATE users SET hash=? WHERE id=?",
                    hash, user_id)

        # Ensure current password was submitted
        if c_password is None or request.form.get("current_password"):
            return apology("must provide current password", 403)

        # Ensure new password was submitted
        elif n_password is None or not request.form.get("new_password"):
            return apology("must provide a new password", 403)

        #confirm new password
        elif not request.form.get("confirmation"):
            return apology("must confirm new password", 403)

        #verify new password confirmation
        if request.form.get("confirmation") != request.form.get("new_password"):
            return apology("Password un-matched, try again.", 403)

        flash("Password Changed!")
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("settings.html")



@app.route('/nft_closer', methods=['GET', 'POST'])
@login_required
def nft_closer():
    """Open nft_closer"""
    if request.method == "GET":
        return render_template("closer.html")

@app.route('/nft_dem_say', methods=['GET', 'POST'])
@login_required
def nft_dem_say():
    """Open nft_dem_say"""
    if request.method == "GET":
        return render_template("dem_say.html")

@app.route('/nft_kilimanjaro', methods=['GET', 'POST'])
@login_required
def nft_kilimanjaro():
    """Open nft_kilimanjaro"""
    if request.method == "GET":
        return render_template("kilimanjaro.html")

@app.route('/nft_naomi', methods=['GET', 'POST'])
@login_required
def nft_naomi():
    """Open nft_naomi"""
    if request.method == "GET":
        return render_template("naomi.html")



@app.route("/sell_dem_say", methods=["GET", "POST"])
@login_required
def sell_dem_say():
    """Sell edition of NFT"""

    if request.method == "POST":

        NFTs = db.execute("""SELECT NFT, SUM(edition) as S_total
                            FROM purchases
                            WHERE user_id = :user_id
                            GROUP BY NFT;""",
                            user_id=session["user_id"])


        user_id=session["user_id"]

        NFT = request.form.get("NFT")

        stock = dem_say(NFT)

        # image = lookup(NFT)

        #get positive values for "edition" input
        edition = int(request.form.get("edition"))


        if edition is None or edition <= 0:
            return apology("please enter proper edition values", 403)

        owned_editions = db.execute("SELECT edition FROM purchases WHERE user_id= ? AND NFT = ? GROUP BY NFT", user_id, NFT)
        o_editions = owned_editions[0]["edition"]

        if o_editions < edition:
            return apology("Not enough editions!", 400)



        present_cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"]) [0] ["cash"]


        price = edition * stock['price']



        db.execute("UPDATE users SET cash= ? WHERE id= ?",
                    present_cash + price, user_id)

        db.execute("""INSERT INTO purchases (user_id, NFT, price, edition)
                    VALUES(:user_id, :NFT, :price, :edition)""",
                    user_id=session["user_id"],
                    NFT = stock["NFT"],
                    price = stock["price"],
                    edition = -edition)



        flash("Dem Say Sold!")
        return redirect("/")
    else:

        

        NFTs = db.execute("""SELECT NFT, SUM(edition) as S_total
                            FROM purchases
                            WHERE user_id = :user_id
                            GROUP BY NFT;""",
                            user_id=session["user_id"])
        return render_template("sell_dem_say.html", Data=NFTs)




@app.route("/sell_closer", methods=["GET", "POST"])
@login_required
def sell_closer():
    """Sell edition of NFT"""

    
    if request.method == "POST":

        NFTs = db.execute("""SELECT NFT, SUM(edition) as S_total
                            FROM purchases
                            WHERE user_id = :user_id
                            GROUP BY NFT;""",
                            user_id=session["user_id"])


        user_id=session["user_id"]

        NFT = request.form.get("NFT")

        stock = closer(NFT)

        # image = lookup(NFT)

        #get positive values for "edition" input
        edition = int(request.form.get("edition"))


        if edition is None or edition <= 0:
            return apology("please enter proper edition values", 403)

        owned_editions = db.execute("SELECT edition FROM purchases WHERE user_id= ? AND NFT = ? GROUP BY NFT", user_id, NFT)
        o_editions = owned_editions[0]["edition"]

        if o_editions < edition:
            return apology("Not enough editions!", 400)


        present_cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"]) [0] ["cash"]


        price = edition * stock['price']



        db.execute("UPDATE users SET cash= ? WHERE id= ?",
                    present_cash + price, user_id)

        db.execute("""INSERT INTO purchases (user_id, NFT, price, edition)
                    VALUES(:user_id, :NFT, :price, :edition)""",
                    user_id=session["user_id"],
                    NFT = stock["NFT"],
                    price = stock["price"],
                    edition = -edition)



        flash("Closer Sold!")
        return redirect("/")
    else:

        NFTs = db.execute("""SELECT NFT, SUM(edition) as S_total
                            FROM purchases
                            WHERE user_id = :user_id
                            GROUP BY NFT;""",
                            user_id=session["user_id"])
        return render_template("sell_closer.html", Data=NFTs)





@app.route("/sell_kilimanjaro", methods=["GET", "POST"])
@login_required
def sell_kilimanjaro():
    """Sell edition of NFT"""

    if request.method == "POST":

        NFTs = db.execute("""SELECT NFT, SUM(edition) as S_total
                            FROM purchases
                            WHERE user_id = :user_id
                            GROUP BY NFT;""",
                            user_id=session["user_id"])


        user_id=session["user_id"]

        NFT = request.form.get("NFT") 

        stock = kilimanjaro(NFT)
        # for stock in nfts:
        #     stock = stock
            

        # image = lookup(NFT)

        #get positive values for "edition" input
        edition = int(request.form.get("edition"))


        if edition is None or edition <= 0:
            return apology("please enter proper edition values", 403)

        owned_editions = db.execute("SELECT edition FROM purchases WHERE user_id= ? AND NFT = ? GROUP BY NFT", user_id, NFT)
        o_editions = owned_editions[0]["edition"]

        if o_editions < edition:
            return apology("Not enough editions!", 400)


        present_cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"]) [0] ["cash"]


        price = edition * stock['price']



        db.execute("UPDATE users SET cash= ? WHERE id= ?",
                    present_cash + price, user_id)

        db.execute("""INSERT INTO purchases (user_id, NFT, price, edition)
                    VALUES(:user_id, :NFT, :price, :edition)""",
                    user_id=session["user_id"],
                    NFT = stock["NFT"],
                    price = stock["price"],
                    edition = -edition)



        flash("Kilimanjaro Sold!")
        return redirect("/")
    else:

        NFTs = db.execute("""SELECT NFT, SUM(edition) as S_total
                            FROM purchases
                            WHERE user_id = :user_id
                            GROUP BY NFT;""",
                            user_id=session["user_id"])
        return render_template("sell_kilimanjaro.html", Data=NFTs)




@app.route("/sell_naomi", methods=["GET", "POST"])
@login_required
def sell_naomi():
    """Sell edition of NFT"""

    if request.method == "POST":

        NFTs = db.execute("""SELECT NFT, SUM(edition) as S_total
                            FROM purchases
                            WHERE user_id = :user_id
                            GROUP BY NFT;""",
                            user_id=session["user_id"])


        user_id=session["user_id"]

        NFT = request.form.get("NFT") 

        stock = naomi(NFT)
        # for stock in nfts:
        #     stock = stock
            

        # image = lookup(NFT)

        #get positive values for "edition" input
        edition = int(request.form.get("edition"))


        if edition is None or edition <= 0:
            return apology("please enter proper edition values", 403)

        owned_editions = db.execute("SELECT edition FROM purchases WHERE user_id= ? AND NFT = ? GROUP BY NFT", user_id, NFT)
        o_editions = owned_editions[0]["edition"]

        if o_editions < edition:
            return apology("Not enough editions!", 400)


        present_cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"]) [0] ["cash"]


        price = edition * stock['price']



        db.execute("UPDATE users SET cash= ? WHERE id= ?",
                    present_cash + price, user_id)

        db.execute("""INSERT INTO purchases (user_id, NFT, price, edition)
                    VALUES(:user_id, :NFT, :price, :edition)""",
                    user_id=session["user_id"],
                    NFT = stock["NFT"],
                    price = stock["price"],
                    edition = -edition)



        flash("Naomi Sold!")
        return redirect("/")
    else:

        NFTs = db.execute("""SELECT NFT, SUM(edition) as S_total
                            FROM purchases
                            WHERE user_id = :user_id
                            GROUP BY NFT;""",
                            user_id=session["user_id"])
        return render_template("sell_naomi.html", Data=NFTs)




@app.route("/collections", methods=["GET", "POST"])
@login_required
def collections():
    """Sell edition of NFT"""

    if request.method == "GET":

        NFTs = db.execute("""SELECT NFT, SUM(edition) as S_total
                            FROM purchases
                            WHERE user_id = :user_id AND edition > 0
                            GROUP BY NFT;""",
                            user_id=session["user_id"])

        return render_template("collections.html", Data=NFTs)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

