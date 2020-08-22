import web
import plot_speedtest

PLOT_NAME = 'bandwidth.png'

urls = (
    '/', 'bandwidth',
)


class bandwidth:
    def GET(self):
        plot_speedtest.create_plot(PLOT_NAME)
        web.header("Content-Type", 'image/png')
        return open(PLOT_NAME, "rb").read()


app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
