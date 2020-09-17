try:
    num = int(input("masukan angka"))
    num / 0
except ZeroDivisionError:
    print("err")
finally:
    print("end")
