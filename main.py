# Imports
from tkinter import *
import json

# Data
d = open('data.json')
data = json.load(d)
d.close()

# global variables

OIL_REMAINING = 0.0


# functions
def update_remaining(event):
    """function to update KIV remaining"""
    global OIL_REMAINING
    OIL_REMAINING = float(oil_entry.get())
    oil_r_label.configure(text=OIL_REMAINING)
    print("hello")


def evaluate_0(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_07.configure(text=(int(product_06.get()) * product_03v))
    product_08.configure(text=(int(product_06.get()) * float(product_02v)))
    product_09.configure(text=(int(product_06.get()) * float(product_01v)))
    product_010.configure(text=((int(product_06.get()) * float(product_02v))
                                / (int(product_06.get()) * product_03v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_06.get()) * product_03v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_1(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_17.configure(text=(int(product_16.get()) * product_13v))
    product_18.configure(text=(int(product_16.get()) * float(product_12v)))
    product_19.configure(text=(int(product_16.get()) * float(product_11v)))
    product_110.configure(text=((int(product_16.get()) * float(product_12v))
                                / (int(product_16.get()) * product_13v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_16.get()) * product_13v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_2(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_27.configure(text=(int(product_26.get()) * product_23v))
    product_28.configure(text=(int(product_26.get()) * float(product_22v)))
    product_29.configure(text=(int(product_26.get()) * float(product_21v)))
    product_210.configure(text=((int(product_26.get()) * float(product_22v))
                                / (int(product_26.get()) * product_23v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_26.get()) * product_23v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_3(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_37.configure(text=(int(product_36.get()) * product_33v))
    product_38.configure(text=(int(product_36.get()) * float(product_32v)))
    product_39.configure(text=(int(product_36.get()) * float(product_31v)))
    product_310.configure(text=((int(product_36.get()) * float(product_32v))
                                / (int(product_36.get()) * product_33v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_36.get()) * product_33v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_4(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_47.configure(text=(int(product_46.get()) * product_43v))
    product_48.configure(text=(int(product_46.get()) * float(product_42v)))
    product_49.configure(text=(int(product_46.get()) * float(product_41v)))
    product_410.configure(text=((int(product_46.get()) * float(product_42v))
                                / (int(product_46.get()) * product_43v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_46.get()) * product_43v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_5(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_57.configure(text=(int(product_56.get()) * product_53v))
    product_58.configure(text=(int(product_56.get()) * float(product_52v)))
    product_59.configure(text=(int(product_56.get()) * float(product_51v)))
    product_510.configure(text=((int(product_56.get()) * float(product_52v))
                                / (int(product_56.get()) * product_53v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_56.get()) * product_53v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_6(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING
    product_67.configure(text=(int(product_66.get()) * product_63v))
    product_68.configure(text=(int(product_66.get()) * float(product_62v)))
    product_69.configure(text=(int(product_66.get()) * float(product_61v)))
    product_610.configure(text=((int(product_66.get()) * float(product_62v))
                                / (int(product_66.get()) * product_63v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_66.get()) * product_63v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_7(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_77.configure(text=(int(product_76.get()) * product_73v))
    product_78.configure(text=(int(product_76.get()) * float(product_72v)))
    product_79.configure(text=(int(product_76.get()) * float(product_71v)))
    product_710.configure(text=((int(product_76.get()) * float(product_72v))
                                / (int(product_76.get()) * product_73v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_76.get()) * product_73v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_8(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_87.configure(text=(int(product_86.get()) * product_83v))
    product_88.configure(text=(int(product_86.get()) * float(product_82v)))
    product_89.configure(text=(int(product_86.get()) * float(product_81v)))
    product_810.configure(text=((int(product_86.get()) * float(product_82v))
                                / (int(product_86.get()) * product_83v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_86.get()) * product_83v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_9(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_97.configure(text=(int(product_96.get()) * product_93v))
    product_98.configure(text=(int(product_96.get()) * float(product_92v)))
    product_99.configure(text=(int(product_96.get()) * float(product_91v)))
    product_910.configure(text=((int(product_96.get()) * float(product_92v))
                                / (int(product_96.get()) * product_93v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_96.get()) * product_93v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_10(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_107.configure(text=(int(product_106.get()) * product_103v))
    product_108.configure(text=(int(product_106.get()) * float(product_102v)))
    product_109.configure(text=(int(product_106.get()) * float(product_101v)))
    product_1010.configure(
        text=((int(product_106.get()) * float(product_102v)) / (int(product_106.get()) * product_103v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_106.get()) * product_103v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_11(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_117.configure(text=(int(product_116.get()) * product_113v))
    product_118.configure(text=(int(product_116.get()) * float(product_112v)))
    product_119.configure(text=(int(product_116.get()) * float(product_111v)))
    product_1110.configure(text=((int(product_116.get()) * float(product_112v))
                                 / (int(product_116.get()) * product_113v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_116.get()) * product_113v)
    oil_r_label.configure(text=OIL_REMAINING)


def evaluate_12(event):
    """function to populate required fields and deduct oil used from oil remaining"""
    global OIL_REMAINING

    product_127.configure(text=(int(product_126.get()) * product_123v))
    product_128.configure(text=(int(product_126.get()) * float(product_122v)))
    product_129.configure(text=(int(product_126.get()) * float(product_121v)))
    product_1210.configure(text=((int(product_126.get()) * float(product_122v))
                                 / (int(product_126.get()) * product_123v)))
    OIL_REMAINING = OIL_REMAINING - (int(product_126.get()) * product_123v)
    oil_r_label.configure(text=OIL_REMAINING)


# UI/Tkinter Config

window = Tk()
window.title("KIV Use Calculator")
window.config(bg="white", padx=20, pady=20, width=200, height=200)

oil_on_hand = Label(text="KIV on hand (in grams): ", bg="white", highlightthickness=0)
oil_entry = Entry()
oil_entry.bind("<Return>", update_remaining)
oil_remaining = Label(text="KIV Remaining (in grams): ", bg="white", highlightthickness=0)
oil_r_label = Label(text=OIL_REMAINING, bg="white", highlightthickness=0)

# Super Header
oil_on_hand.grid(column=0, row=0, sticky="E")
oil_entry.grid(column=1, row=0, sticky="E")
oil_remaining.grid(column=2, row=0, sticky="E")
oil_r_label.grid(column=3, row=0, sticky="E")

# Header Row
header_0 = Label(text="Product", bg="white", highlightthickness=0)
header_0.grid(column=0, row=1, sticky="E")
header_1 = Label(text="COGS", bg="white", highlightthickness=0)
header_1.grid(column=1, row=1, sticky="E")
header_2 = Label(text="Price", bg="white", highlightthickness=0)
header_2.grid(column=2, row=1, sticky="E")
header_3 = Label(text="KIV/Unit", bg="white", highlightthickness=0)
header_3.grid(column=3, row=1, sticky="E")
# Commented out for simplicity of concept, as this is for ONE Key Input Variable not two
# header_4 = Label(text="KIV Category", bg="white", highlightthickness=0)
# header_4.grid(column=4, row=1, sticky="E")
# header_5 = Label(text="Adjusted KIV per Unit", bg="white", highlightthickness=0)
# header_5.grid(column=5, row=1, sticky="E")
header_6 = Label(text="Amount Desired (AD)", bg="white", highlightthickness=0)
header_6.grid(column=6, row=1, sticky="E")
header_7 = Label(text="KIV Consumed", bg="white", highlightthickness=0)
header_7.grid(column=7, row=1, sticky="E")
header_8 = Label(text="Total Sales on AD", bg="white", highlightthickness=0)
header_8.grid(column=8, row=1, sticky="E")
header_9 = Label(text="COGs on AD", bg="white", highlightthickness=0)
header_9.grid(column=9, row=1, sticky="E")
header_10 = Label(text="$/KIV", bg="white", highlightthickness=0)
header_10.grid(column=10, row=1, sticky="E")

# Product Name Imports
product_0 = Label(text=f"{data[0]['product']}", bg="white", highlightthickness=0)
product_0.grid(column=0, row=2, sticky="E")
product_1 = Label(text=f"{data[1]['product']}", bg="white", highlightthickness=0)
product_1.grid(column=0, row=3, sticky="E")
product_2 = Label(text=f"{data[2]['product']}", bg="white", highlightthickness=0)
product_2.grid(column=0, row=4, sticky="E")
product_3 = Label(text=f"{data[3]['product']}", bg="white", highlightthickness=0)
product_3.grid(column=0, row=5, sticky="E")
product_4 = Label(text=f"{data[4]['product']}", bg="white", highlightthickness=0)
product_4.grid(column=0, row=6, sticky="E")
product_5 = Label(text=f"{data[5]['product']}", bg="white", highlightthickness=0)
product_5.grid(column=0, row=7, sticky="E")
product_6 = Label(text=f"{data[6]['product']}", bg="white", highlightthickness=0)
product_6.grid(column=0, row=8, sticky="E")
product_7 = Label(text=f"{data[7]['product']}", bg="white", highlightthickness=0)
product_7.grid(column=0, row=9, sticky="E")
product_8 = Label(text=f"{data[8]['product']}", bg="white", highlightthickness=0)
product_8.grid(column=0, row=10, sticky="E")
product_9 = Label(text=f"{data[9]['product']}", bg="white", highlightthickness=0)
product_9.grid(column=0, row=11, sticky="E")
product_10 = Label(text=f"{data[10]['product']}", bg="white", highlightthickness=0)
product_10.grid(column=0, row=12, sticky="E")
product_11 = Label(text=f"{data[11]['product']}", bg="white", highlightthickness=0)
product_11.grid(column=0, row=13, sticky="E")
product_12 = Label(text=f"{data[12]['product']}", bg="white", highlightthickness=0)
product_12.grid(column=0, row=14, sticky="E")

# COGs Imports
product_01v = data[0]['cogs']
product_01 = Label(text=f"{data[0]['cogs']}", bg="white", highlightthickness=0)
product_01.grid(column=1, row=2, sticky="E")
product_11v = data[1]['cogs']
product_11 = Label(text=f"{data[1]['cogs']}", bg="white", highlightthickness=0)
product_11.grid(column=1, row=3, sticky="E")
product_21v = data[2]['cogs']
product_21 = Label(text=f"{data[2]['cogs']}", bg="white", highlightthickness=0)
product_21.grid(column=1, row=4, sticky="E")
product_31v = data[3]['cogs']
product_31 = Label(text=f"{data[3]['cogs']}", bg="white", highlightthickness=0)
product_31.grid(column=1, row=5, sticky="E")
product_41v = data[4]['cogs']
product_41 = Label(text=f"{data[4]['cogs']}", bg="white", highlightthickness=0)
product_41.grid(column=1, row=6, sticky="E")
product_51v = data[5]['cogs']
product_51 = Label(text=f"{data[5]['cogs']}", bg="white", highlightthickness=0)
product_51.grid(column=1, row=7, sticky="E")
product_61v = data[6]['cogs']
product_61 = Label(text=f"{data[6]['cogs']}", bg="white", highlightthickness=0)
product_61.grid(column=1, row=8, sticky="E")
product_71v = data[7]['cogs']
product_71 = Label(text=f"{data[7]['cogs']}", bg="white", highlightthickness=0)
product_71.grid(column=1, row=9, sticky="E")
product_81v = data[8]['cogs']
product_81 = Label(text=f"{data[8]['cogs']}", bg="white", highlightthickness=0)
product_81.grid(column=1, row=10, sticky="E")
product_91v = data[9]['cogs']
product_91 = Label(text=f"{data[9]['cogs']}", bg="white", highlightthickness=0)
product_91.grid(column=1, row=11, sticky="E")
product_101v = data[10]['cogs']
product_101 = Label(text=f"{data[10]['cogs']}", bg="white", highlightthickness=0)
product_101.grid(column=1, row=12, sticky="E")
product_111v = data[11]['cogs']
product_111 = Label(text=f"{data[11]['cogs']}", bg="white", highlightthickness=0)
product_111.grid(column=1, row=13, sticky="E")
product_121v = data[12]['cogs']
product_121 = Label(text=f"{data[12]['cogs']}", bg="white", highlightthickness=0)
product_121.grid(column=1, row=14, sticky="E")

# Price Imports
product_02v = float(data[0]['wholesale_price'])
product_02 = Label(text=f"{data[0]['wholesale_price']}", bg="white", highlightthickness=0)
product_02.grid(column=2, row=2, sticky="E")
product_12v = float(data[1]['wholesale_price'])
product_12 = Label(text=f"{data[1]['wholesale_price']}", bg="white", highlightthickness=0)
product_12.grid(column=2, row=3, sticky="E")
product_22v = float(data[2]['wholesale_price'])
product_22 = Label(text=f"{data[2]['wholesale_price']}", bg="white", highlightthickness=0)
product_22.grid(column=2, row=4, sticky="E")
product_32v = float(data[3]['wholesale_price'])
product_32 = Label(text=f"{data[3]['wholesale_price']}", bg="white", highlightthickness=0)
product_32.grid(column=2, row=5, sticky="E")
product_42v = float(data[4]['wholesale_price'])
product_42 = Label(text=f"{data[4]['wholesale_price']}", bg="white", highlightthickness=0)
product_42.grid(column=2, row=6, sticky="E")
product_52v = float(data[5]['wholesale_price'])
product_52 = Label(text=f"{data[5]['wholesale_price']}", bg="white", highlightthickness=0)
product_52.grid(column=2, row=7, sticky="E")
product_62v = float(data[6]['wholesale_price'])
product_62 = Label(text=f"{data[6]['wholesale_price']}", bg="white", highlightthickness=0)
product_62.grid(column=2, row=8, sticky="E")
product_72v = float(data[7]['wholesale_price'])
product_72 = Label(text=f"{data[7]['wholesale_price']}", bg="white", highlightthickness=0)
product_72.grid(column=2, row=9, sticky="E")
product_82v = float(data[8]['wholesale_price'])
product_82 = Label(text=f"{data[8]['wholesale_price']}", bg="white", highlightthickness=0)
product_82.grid(column=2, row=10, sticky="E")
product_92v = float(data[9]['wholesale_price'])
product_92 = Label(text=f"{data[9]['wholesale_price']}", bg="white", highlightthickness=0)
product_92.grid(column=2, row=11, sticky="E")
product_102v = float(data[10]['wholesale_price'])
product_102 = Label(text=f"{data[10]['wholesale_price']}", bg="white", highlightthickness=0)
product_102.grid(column=2, row=12, sticky="E")
product_112v = float(data[11]['wholesale_price'])
product_112 = Label(text=f"{data[11]['wholesale_price']}", bg="white", highlightthickness=0)
product_112.grid(column=2, row=13, sticky="E")
product_122v = float(data[12]['wholesale_price'])
product_122 = Label(text=f"{data[12]['wholesale_price']}", bg="white", highlightthickness=0)
product_122.grid(column=2, row=14, sticky="E")

# KIV/Unit
product_03v = data[0]['kiv_per_unit']
product_03 = Label(window, text=data[0]['kiv_per_unit'], bg="white", highlightthickness=0)
product_03.grid(column=3, row=2, sticky="E")
product_13v = data[1]['kiv_per_unit']
product_13 = Label(text=f"{data[1]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_13.grid(column=3, row=3, sticky="E")
product_23v = data[2]['kiv_per_unit']
product_23 = Label(text=f"{data[2]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_23.grid(column=3, row=4, sticky="E")
product_33v = data[3]['kiv_per_unit']
product_33 = Label(text=f"{data[3]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_33.grid(column=3, row=5, sticky="E")
product_43v = data[4]['kiv_per_unit']
product_43 = Label(text=f"{data[4]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_43.grid(column=3, row=6, sticky="E")
product_53v = data[5]['kiv_per_unit']
product_53 = Label(text=f"{data[5]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_53.grid(column=3, row=7, sticky="E")
product_63v = data[6]['kiv_per_unit']
product_63 = Label(text=f"{data[6]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_63.grid(column=3, row=8, sticky="E")
product_73v = data[7]['kiv_per_unit']
product_73 = Label(text=f"{data[7]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_73.grid(column=3, row=9, sticky="E")
product_83v = data[8]['kiv_per_unit']
product_83 = Label(text=f"{data[8]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_83.grid(column=3, row=10, sticky="E")
product_93v = data[9]['kiv_per_unit']
product_93 = Label(text=f"{data[9]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_93.grid(column=3, row=11, sticky="E")
product_103v = data[10]['kiv_per_unit']
product_103 = Label(text=f"{data[10]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_103.grid(column=3, row=12, sticky="E")
product_113v = data[11]['kiv_per_unit']
product_113 = Label(text=f"{data[11]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_113.grid(column=3, row=13, sticky="E")
product_123v = data[12]['kiv_per_unit']
product_123 = Label(text=f"{data[12]['kiv_per_unit']}", bg="white", highlightthickness=0)
product_123.grid(column=3, row=14, sticky="E")

# Amount Desired
product_06 = Entry(bg="white", highlightthickness=0)
product_06.bind("<Return>", evaluate_0)
product_06.grid(column=6, row=2, sticky="E")
product_16 = Entry(bg="white", highlightthickness=0)
product_16.bind("<Return>", evaluate_1)
product_16.grid(column=6, row=3, sticky="E")
product_26 = Entry(bg="white", highlightthickness=0)
product_26.bind("<Return>", evaluate_2)
product_26.grid(column=6, row=4, sticky="E")
product_36 = Entry(bg="white", highlightthickness=0)
product_36.bind("<Return>", evaluate_3)
product_36.grid(column=6, row=5, sticky="E")
product_46 = Entry(bg="white", highlightthickness=0)
product_46.bind("<Return>", evaluate_4)
product_46.grid(column=6, row=6, sticky="E")
product_56 = Entry(bg="white", highlightthickness=0)
product_56.bind("<Return>", evaluate_5)
product_56.grid(column=6, row=7, sticky="E")
product_66 = Entry(bg="white", highlightthickness=0)
product_66.bind("<Return>", evaluate_6)
product_66.grid(column=6, row=8, sticky="E")
product_76 = Entry(bg="white", highlightthickness=0)
product_76.bind("<Return>", evaluate_7)
product_76.grid(column=6, row=9, sticky="E")
product_86 = Entry(bg="white", highlightthickness=0)
product_86.bind("<Return>", evaluate_8)
product_86.grid(column=6, row=10, sticky="E")
product_96 = Entry(bg="white", highlightthickness=0)
product_96.bind("<Return>", evaluate_9)
product_96.grid(column=6, row=11, sticky="E")
product_106 = Entry(bg="white", highlightthickness=0)
product_106.bind("<Return>", evaluate_10)
product_106.grid(column=6, row=12, sticky="E")
product_116 = Entry(bg="white", highlightthickness=0)
product_116.bind("<Return>", evaluate_11)
product_116.grid(column=6, row=13, sticky="E")
product_126 = Entry(bg="white", highlightthickness=0)
product_126.bind("<Return>", evaluate_12)
product_126.grid(column=6, row=14, sticky="E")

# KIV Consumed
product_07 = Label(bg="white", highlightthickness=0)
product_07.grid(column=7, row=2, sticky="E")
product_17 = Label(bg="white", highlightthickness=0)
product_17.grid(column=7, row=3, sticky="E")
product_27 = Label(bg="white", highlightthickness=0)
product_27.grid(column=7, row=4, sticky="E")
product_37 = Label(bg="white", highlightthickness=0)
product_37.grid(column=7, row=5, sticky="E")
product_47 = Label(bg="white", highlightthickness=0)
product_47.grid(column=7, row=6, sticky="E")
product_57 = Label(bg="white", highlightthickness=0)
product_57.grid(column=7, row=7, sticky="E")
product_67 = Label(bg="white", highlightthickness=0)
product_67.grid(column=7, row=8, sticky="E")
product_77 = Label(bg="white", highlightthickness=0)
product_77.grid(column=7, row=9, sticky="E")
product_87 = Label(bg="white", highlightthickness=0)
product_87.grid(column=7, row=10, sticky="E")
product_97 = Label(bg="white", highlightthickness=0)
product_97.grid(column=7, row=11, sticky="E")
product_107 = Label(bg="white", highlightthickness=0)
product_107.grid(column=7, row=12, sticky="E")
product_117 = Label(bg="white", highlightthickness=0)
product_117.grid(column=7, row=13, sticky="E")
product_127 = Label(bg="white", highlightthickness=0)
product_127.grid(column=7, row=14, sticky="E")

# Total Sales
product_08 = Label(bg="white", highlightthickness=0)
product_08.grid(column=8, row=2, sticky="E")
product_18 = Label(bg="white", highlightthickness=0)
product_18.grid(column=8, row=3, sticky="E")
product_28 = Label(bg="white", highlightthickness=0)
product_28.grid(column=8, row=4, sticky="E")
product_38 = Label(bg="white", highlightthickness=0)
product_38.grid(column=8, row=5, sticky="E")
product_48 = Label(bg="white", highlightthickness=0)
product_48.grid(column=8, row=6, sticky="E")
product_58 = Label(bg="white", highlightthickness=0)
product_58.grid(column=8, row=7, sticky="E")
product_68 = Label(bg="white", highlightthickness=0)
product_68.grid(column=8, row=8, sticky="E")
product_78 = Label(bg="white", highlightthickness=0)
product_78.grid(column=8, row=9, sticky="E")
product_88 = Label(bg="white", highlightthickness=0)
product_88.grid(column=8, row=10, sticky="E")
product_98 = Label(bg="white", highlightthickness=0)
product_98.grid(column=8, row=11, sticky="E")
product_108 = Label(bg="white", highlightthickness=0)
product_108.grid(column=8, row=12, sticky="E")
product_118 = Label(bg="white", highlightthickness=0)
product_118.grid(column=8, row=13, sticky="E")
product_128 = Label(bg="white", highlightthickness=0)
product_128.grid(column=8, row=14, sticky="E")

# COGs on AD
product_09 = Label(bg="white", highlightthickness=0)
product_09.grid(column=9, row=2, sticky="E")
product_19 = Label(bg="white", highlightthickness=0)
product_19.grid(column=9, row=3, sticky="E")
product_29 = Label(bg="white", highlightthickness=0)
product_29.grid(column=9, row=4, sticky="E")
product_39 = Label(bg="white", highlightthickness=0)
product_39.grid(column=9, row=5, sticky="E")
product_49 = Label(bg="white", highlightthickness=0)
product_49.grid(column=9, row=6, sticky="E")
product_59 = Label(bg="white", highlightthickness=0)
product_59.grid(column=9, row=7, sticky="E")
product_69 = Label(bg="white", highlightthickness=0)
product_69.grid(column=9, row=8, sticky="E")
product_79 = Label(bg="white", highlightthickness=0)
product_79.grid(column=9, row=9, sticky="E")
product_89 = Label(bg="white", highlightthickness=0)
product_89.grid(column=9, row=10, sticky="E")
product_99 = Label(bg="white", highlightthickness=0)
product_99.grid(column=9, row=11, sticky="E")
product_109 = Label(bg="white", highlightthickness=0)
product_109.grid(column=9, row=12, sticky="E")
product_119 = Label(bg="white", highlightthickness=0)
product_119.grid(column=9, row=13, sticky="E")
product_129 = Label(bg="white", highlightthickness=0)
product_129.grid(column=9, row=14, sticky="E")

# $/KIV/Unit
product_010 = Label(bg="white", highlightthickness=0)
product_010.grid(column=10, row=2, sticky="E")
product_110 = Label(bg="white", highlightthickness=0)
product_110.grid(column=10, row=3, sticky="E")
product_210 = Label(bg="white", highlightthickness=0)
product_210.grid(column=10, row=4, sticky="E")
product_310 = Label(bg="white", highlightthickness=0)
product_310.grid(column=10, row=5, sticky="E")
product_410 = Label(bg="white", highlightthickness=0)
product_410.grid(column=10, row=6, sticky="E")
product_510 = Label(bg="white", highlightthickness=0)
product_510.grid(column=10, row=7, sticky="E")
product_610 = Label(bg="white", highlightthickness=0)
product_610.grid(column=10, row=8, sticky="E")
product_710 = Label(bg="white", highlightthickness=0)
product_710.grid(column=10, row=9, sticky="E")
product_810 = Label(bg="white", highlightthickness=0)
product_810.grid(column=10, row=10, sticky="E")
product_910 = Label(bg="white", highlightthickness=0)
product_910.grid(column=10, row=11, sticky="E")
product_1010 = Label(bg="white", highlightthickness=0)
product_1010.grid(column=10, row=12, sticky="E")
product_1110 = Label(bg="white", highlightthickness=0)
product_1110.grid(column=10, row=13, sticky="E")
product_1210 = Label(bg="white", highlightthickness=0)
product_1210.grid(column=10, row=14, sticky="E")

window.mainloop()
