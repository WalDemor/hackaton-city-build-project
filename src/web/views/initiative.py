

@app.route("/initiative", methods=['GET', 'POST'])
def initiative():
    return render_template("initiative.html")