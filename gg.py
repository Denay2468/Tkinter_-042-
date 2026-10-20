import tkinter as tk
def prediction_result():
    result_label.config(text="Information Technology")
top = tk.Tk()
title_label = tk.Label(top, text="Preferred Study Program Prediction App")
title_label.pack(pady=10)
subjects = ["subject1:", "subject2:", "subject3:", "subject4:", "subject5:", "subject6:", "subject7:", "subject8:", "subject9:", "subject10:"]
for name in subjects:
    frame = tk.Frame(top)
    frame.pack()
    L = tk.Label(frame, text=name, width=20)
    L.pack(side=tk.LEFT)
    E = tk.Entry(frame, bd=5)
    E.pack(side=tk.RIGHT)

B = tk.Button(top, text="Prediction Result", command=prediction_result)
B.pack(pady=10)

result_label = tk.Label(top, text="", relief=tk.RAISED, width=30)
result_label.pack(pady=10)
top.mainloop()