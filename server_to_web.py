#!/usr/bin/env python
import web
import plot_speedtest

PLOT_NAME = 'bandwidth.png'

urls = (
'/bandwidth', 'showplot',
'/showplot1', 'showplot1',
)

class showplot:
	def GET(self):
		plot_speedtest.create_plot(PLOT_NAME)
		web.header("Content-Type", 'image/png')
		return open(PLOT_NAME,"rb").read()

class showplot1:
    def GET(self):
        plot_speedtest.create_plot(PLOT_NAME)
        web.header("Content-type", 'image/png')
        return open(PLOT_NAME,"rb").read()
    
app = web.application(urls, globals())

if __name__ == "__main__":
	app.run()