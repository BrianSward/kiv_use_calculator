from tkinter import *
import json
import locale

# set local
locale.setlocale(locale.LC_ALL, '')

with open('data.json') as d:
    data = json.load(d)

fields = data

KIV_REMAINING = 0.0


def update_remaining():
    """function to update KIV remaining"""
    global KIV_REMAINING
    KIV_REMAINING = float(kiv_entry.get())
    kiv_r_label.configure(text=KIV_REMAINING)


def reset():
    global KIV_REMAINING
    print(f"{root.winfo_children()[1].get()} hello")
    print(f"hello from reset")
    KIV_REMAINING = root.winfo_children()[1].get()
    print(KIV_REMAINING)
    kiv_r_label.configure(text=KIV_REMAINING)
    main()
    # for index, thing in enumerate(root.winfo_children()):
    #     print(index, thing)
    #     thing.configure(text=index)



def calc():
    global KIV_REMAINING
    kiv_consumed = 0
    root.winfo_children()[20].configure(text=float(root.winfo_children()[19].get()) 
                                             * float(root.winfo_children()[18].cget("text")))
    kiv_consumed += float(root.winfo_children()[19].get()) * (float(root.winfo_children()[18].cget("text")))

    kiv_r_label.configure(text=KIV_REMAINING-kiv_consumed)
    # proof of concept if here, I would just have to write 17*5 different lines 
    # but i think there should be an easier way and I'm going to look for it


def oil_remaining():
    pass
    # global KIV_REMAINING
    # KIV_REMAINING = MATH
    # kiv_r_label.configure(text=OIL_REMAINING)


def make_headers(root):
    header_0 = Label(root, text="Product", bg="white", highlightthickness=0)
    header_0.grid(column=0, row=1, sticky="E")
    header_1 = Label(root, text="COGS", bg="white", highlightthickness=0)
    header_1.grid(column=1, row=1, sticky="E")
    header_2 = Label(root, text="Price", bg="white", highlightthickness=0)
    header_2.grid(column=2, row=1, sticky="E")
    header_3 = Label(root, text="KIV/Unit", bg="white", highlightthickness=0)
    header_3.grid(column=3, row=1, sticky="E")
    # Commented out for simplicity of concept, as this is for ONE Key Input Variable not two
    # header_4 = Label(text="KIV Category", bg="white", highlightthickness=0)
    # header_4.grid(column=4, row=1, sticky="E")
    # header_5 = Label(text="Adjusted KIV per Unit", bg="white", highlightthickness=0)
    # header_5.grid(column=5, row=1, sticky="E")
    header_6 = Label(root, text="Amount Desired (AD)", bg="white", highlightthickness=0)
    header_6.grid(column=6, row=1, sticky="E")
    header_7 = Label(root, text="KIV Consumed", bg="white", highlightthickness=0)
    header_7.grid(column=7, row=1, sticky="E")
    header_8 = Label(root, text="Total Sales on AD", bg="white", highlightthickness=0)
    header_8.grid(column=8, row=1, sticky="E")
    header_9 = Label(root, text="COGs on AD", bg="white", highlightthickness=0)
    header_9.grid(column=9, row=1, sticky="E")
    header_10 = Label(root, text="$/KIV", bg="white", highlightthickness=0)
    header_10.grid(column=10, row=1, sticky="E")


def list_products(root, datum):
    for i, field in enumerate(datum):
        lab_1 = Label(root, text=field["product"],bg="white", highlightthickness=0)
        lab_2 = Label(root, text=field["cogs"], bg="white", highlightthickness=0)
        lab_3 = Label(root, text=field["wholesale_price"], bg="white", highlightthickness=0)
        lab_4 = Label(root, text=field["kiv_per_unit"], bg="white", highlightthickness=0)
        ent = Entry(root)
        lab_5 = Label(root, text="test", bg="white", highlightthickness=0)
        lab_6 = Label(root, text="test", bg="white", highlightthickness=0)
        lab_7 = Label(root, text="test", bg="white", highlightthickness=0)
        lab_8 = Label(root, text="test", bg="white", highlightthickness=0)
        ent.bind("<Return>", reset)
        lab_1.grid(column=0, row=i+2, sticky="E")
        lab_2.grid(column=1, row=i+2, sticky="E")
        lab_3.grid(column=2, row=i+2, sticky="E")
        lab_4.grid(column=3, row=i+2, sticky="E")
        ent.grid(column=6, row=i+2, sticky="E")
        lab_5.grid(column=7, row=i+2, sticky="E")
        lab_6.grid(column=8, row=i + 2, sticky="E")
        lab_7.grid(column=9, row=i + 2, sticky="E")
        lab_8.grid(column=10, row=i+2, sticky="E")


def main():
    root.title("KIV Use Calculator")
    root.config(bg="white", padx=20, pady=20, width=200, height=200)
    make_headers(root)
    list_products(root, fields)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    kiv_on_hand = Label(root, text="KIV on hand (in grams): ", bg="white", highlightthickness=0)
    kiv_entry = Entry()
    kiv_entry.bind("<Return>", update_remaining)
    kiv_remaining = Label(root, text="KIV Remaining (in grams): ", bg="white", highlightthickness=0)
    kiv_r_label = Label(root, text=KIV_REMAINING, bg="white", highlightthickness=0)
    kiv_on_hand.grid(column=0, row=0, sticky="E")
    kiv_entry.grid(column=1, row=0, sticky="E")
    kiv_remaining.grid(column=2, row=0, sticky="E")
    kiv_r_label.grid(column=3, row=0, sticky="E")
    clear_button = Button(root, text="Reset", command=reset)
    clear_button.grid(column=9, row=0, sticky="E")
    calculate_button = Button(root, text="Calculate", command=calc)
    calculate_button.grid(column=10, row=0, sticky="E")
    main()
