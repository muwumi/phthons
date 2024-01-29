def allArgs(data1, data2, *data3, data4='나는 기본 매개변수 1', data5 = "나는 두번째임"):
    print(data1, data2, sep=" , ")
    print(data3)
    print(data4, data5, sep = " / ", end = "\n\n===>")
    return data1, data2, data4, data5

#allArgs(10, 20)
#allArgs(10, 20, 30, 40, 50)
allArgs(10, 50, data4="머시깽이")
allArgs(data5="짱짱구구후", data4="데4임임", data2=2222, data1=11111 )
