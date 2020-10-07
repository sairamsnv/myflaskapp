from flask import Flask,render_template,request,url_for


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])


def fun():
    return render_template('my.html')




if __name__ == "__main__":
    app.run(debug=True)


