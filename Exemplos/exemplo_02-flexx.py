from flexx import flx

class Example(flx.Widget):

    def init(self):
        self.set_title("A simple GUI")
        with flx.VBox():
            flx.Label(text="This is our first GUI!")
            flx.Button(text='Greet')
            flx.Button(text='Close')


app = flx.App(Example)
app.launch('app')  # to run as a desktop app
#app.launch('browser')  # to open in the browser
flx.run()  # mainloop will exit when the app is closed