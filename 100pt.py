#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")



class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Up", background= "green")
		self.button1.grid(row=0,column=0)
					
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)

		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		
		def animate():
		    tx1,ty1,tx2,ty2 = drawpad.coords(target)
		    direction = 1
		    drawpad.move(target,direction,0)
		    
	def collisionDetect(self):
	    
            global oval
	    global drawpad
            x1,y1,x2,y2 = drawpad.coords(player)
            tx1,ty1,tx2,ty2 = drawpad.coords(target)
            # Do your if statement - remember to return True if successful!
            if (x1 > tx1) and (x2 < tx2) and (y1 > ty1) and (y2 < ty2):
	       drawpad.itemconfig(target,fill="red")
	       drawpad.after(1,self,animate)
	       return True	    

	def button1Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
		


		# Ensure that we are doing our collision detection
		# After we move our object!
                didWeHit = collisionDetect()
                if(didWeHit == True):
                    # We made contact! Stop our animation!
                    print "Do something"
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	
myapp = MyApp(root)

root.mainloop()