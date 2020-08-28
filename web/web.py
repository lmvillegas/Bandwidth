from flask import Flask, render_template
from monitor import plot_speedtest

PLOT_NAME = 'web/static/images/bandwidth.png'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'BANDWIDTHUSERSACTIVESTI'


@app.route('/')
def index():
    plot_speedtest.create_plot(PLOT_NAME)
    plots = open(PLOT_NAME, "rb").read()
    return render_template('index.html', plots = plots)


# class bandwidth:
#     def GET(self):
#         plot_speedtest.create_plot(PLOT_NAME)
#         web.header("Content-Type", 'image/png')
#         return open(PLOT_NAME, "rb").read()
#
#
# app = web.application(urls, globals())

if __name__ == "__main__":
    app.run(debug = True)
