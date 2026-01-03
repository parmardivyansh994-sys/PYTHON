'''
wap to calculate GST tax amount from given bill
'''

bill_amount = 0
gst_rate = 0

bill_amount = input("enter value of bill_amount")
gst_rate = input("enter value of gst_rate")

bill_amount = float(bill_amount)
gst_rate = float(gst_rate)

GST =(bill_amount*gst_rate) /100
print("GST amount is..",GST)
