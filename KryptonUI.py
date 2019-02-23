from appJar import *
from datetime import datetime
from time import gmtime, strftime



app = gui("KryptonUI","320x240")
app.setOnTop(stay=True)
app.showSplash("KryptonUI", fill='silver', stripe='red', fg='white', font=44)
app.addLabel("date", strftime('%I:%M'))
app.addLabel("time", strftime('%d/%m/%Y') )
app.setSize("fullscreen")




app.go()
