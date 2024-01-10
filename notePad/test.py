# import tkinter as tk
#
# def get_text_font():
#     # Create a Text widget
#     text_widget = tk.Text(root)
#     text_widget.pack()
#
#     text_widget.config(font=("微软雅黑", 12))
#     print(text_widget.cget("font"))
#
#     # Insert some text with a specific font
#     text_widget.insert("1.0", "Hello, World!")
#     text_widget.tag_add("custom_font", "1.0", "1.5")
#
#     # Configure the tag with the font
#     text_widget.tag_configure("custom_font", font=("Arial", 12, "bold"))
#
#     # Get the font details from the tag
#     tag_font = text_widget.tag_cget("custom_font", "font")
#     print("Font:", tag_font)
#
# root = tk.Tk()
# get_text_font()
# root.mainloop()



import sys
def fibonacci(n):
	a, b, counter = 0, 1, 0
	while True:
		if counter > n:
			return
		yield a
		a, b = b, a + b
		counter += 1

r = fibonacci(10)
while True:
	try:
		print(next(r), end=" ")
	except StopIteration:
		sys.exit()
