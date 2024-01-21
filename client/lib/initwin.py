import ttkbootstrap as ttk
def clean(master:ttk.Window):
    if master.winfo_children() == []:
        pass
    else:
        for i in master.winfo_children():
            i.destroy()