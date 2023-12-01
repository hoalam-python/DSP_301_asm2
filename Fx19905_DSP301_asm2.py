import pandas as pd 
import numpy as np
import re \

while True:
    while True: 
        filename = input("Enter a file name: ")
        filepath1 =  "/Users/hoalam/this mac/Data Sciency/GT_KHDL/data_file_asm2/" + filename + ".txt"
        #LOAD FILE, LOAD KHÔNG ĐƯỢC THÌ YÊU CẦU NHẬP LẠI: 
        try:
            df1 = pd.read_csv(filepath1, sep = " " , header = None, index_col = None,engine = 'python')
            #df = pd.read_csv(filepath1, sep = "," , header = None, index_col = None,engine = 'python',on_bad_lines = "warn")
            print("\n**** MỞ THÀNH CÔNG FILE: " + filename + "\n")
            break
        except:
            print("Lỗi nhập file, nhập lại (ví dụ class1): ")

        #BẮT ĐẦU PHÂN TÍCH ĐẾM SỐ CÂU LỖI: 
    print("**** Phân tích ****")
    list_N12345678 = []
    list_ABCD = []
    # tạo hai list rỗng, cho i chạy theo chiều dài tệp, nếu tách được 26 thành phần nghĩa là có đủ Mã HS và điền đủ 25 câu trả lời
    for i in range(0,len(df1),1):
        if len(str(df1.loc[i,0]).split(",")) == 26: 
            b = str(df1.loc[i,0])
            c = re.findall("N+[0-9]{8}",b)    #Đủ thành phần thì kiểm tra cấu trúc của mã học sinh
            if len(c) > 0:
                continue
            else:
                list_N12345678.append(i) 
        else:                                 # Nếu không đủ thành phần thì list thêm vào thứ tự của hs không điền đủ. 
            list_ABCD.append(i)
            b = str(df1.loc[i,0])
            c = re.findall("N+[0-9]{8}",b)
            if len(c) > 0:
                continue
            else:
                list_N12345678.append(i)    
    list_error = list(set(list_N12345678 + list_ABCD))     # dòng không hợp lệ sẽ được đếm một lần. 

    # DỰA VÀO SỐ CÂU LỖI ĐỂ BÁO CÁO: 
    if len(list_error) == 0:                               
        print("Không tìm thấy lỗi\n")
        print("**** Báo cáo ****")
        print("Tổng số dòng hợp lệ là: " , len(df1))
        print("Tổng số dòng không hợp lệ là: 0")
    else: 
        print("Dòng không hợp lệ, điền thiếu/ thừa giá trị:  ") 
        for a in list_ABCD:
            print(df1.loc[a,0])
        print("Dòng không hợp lệ, không nhập đúng cấu trúc N#:") 
        for a in list_N12345678:
            print(df1.loc[a,0])
        print("\n**** Báo cáo ****")
        print("Tổng số dòng hợp lệ là: ",len(df1) - len(list_error))
        print("Tổng số dòng không hợp lệ là: ",len(list_error))

    #PHẦN KIỂM TRA ĐÁP ÁN: z[]
    #sử dụng chức năng skiprows để tạo một data frame mới chỉ bao gồm các câu hợp lệ. 
    df2 = pd.read_csv(filepath1, sep = "," , header = None,index_col=None,engine = 'python', skiprows = list_error,)
    #print("dataframe của lớp",filename,"\n", df2) 
    answer_key = "Name,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    list_answer_key = answer_key.split(",")
    #print(list_answer_key)
    # thay tất cả câu trống bằng giá trị 0, 
    df3 = df2.fillna(0)
    #print("thay NaN thành 0\n\n", df3)
    # khớp vị trí ô với list đáp án để so sánh và chấm điểm theo quy định
    for n in range(0,len(df3),1):
        try:
            for m in range(1,len(list_answer_key),1):
                if df3.loc[n,m] == list_answer_key[m]:
                    df3.loc[n,m] = 4
                elif df3.loc[n,m] == 0:
                    df3.loc[n,m] = 0
                elif df3.loc[n,m] != 0 and df3.loc[n,m] != list_answer_key[m]:
                    df3.loc[n,m] = -1  
                else: print("lỗi")
        except: 
            print("location error") 
    print("\n****Chấm điểm ****")     
    # tạo một cột tổng điểm trong data frame bằng tổng các cột còn lại
    df3["Tổng điểm"] = df3[25]+df3[24]+df3[23]+df3[22]+df3[21]+df3[20]+df3[19]+df3[18]+df3[17]+df3[16]+df3[15]+df3[14]+df3[13]+df3[12]+df3[11]+df3[10]+df3[9]+df3[8]+df3[7]+df3[6]+df3[5]+df3[4]+df3[3]+df3[2]+df3[1]
    #print(df3)      
    print("Số lượng học sinh có điểm tổng kết >80 của lớp",filename,"là:",len(df3[df3["Tổng điểm"] > 80]))   
    print("Điểm trung bình lớp là:",df3["Tổng điểm"].mean())
    print("Điểm cao nhất lớp là:",df3["Tổng điểm"].max())
    print("Điểm thấp lớp là:",df3["Tổng điểm"].min())
    print("Miền giá trị của điểm là:",df3["Tổng điểm"].max() - df3["Tổng điểm"].min())
    df3_sort = pd.DataFrame(df3.sort_values("Tổng điểm"))
    #print(df3_sort)
    print("Trung vị là: ",df3_sort["Tổng điểm"].median())
    #df4 là data frame thống kê số NA theo câu hỏi, khi chưa thêm cột tổng điểm và chưa thay NA bằng 0, đếm giá trị NA
    # print(df4) 
    df4 = pd.DataFrame(df2.isna().sum())
    NA_max = df2.isna().sum().max()
    #print("Đếm số lượng học sinh bỏ qua theo câu:\n", df4.transpose(),"\n\n")
    print("Câu bị bỏ qua nhiều nhất là: ",(pd.DataFrame(df4[df4[0] == NA_max])).index.values,"bị bỏ qua ",NA_max,"lần và chiếm tỉ lệ: ",round((NA_max*100)/len(df3),1),"%")
    #df5 là data frame thống kê số câu sai theo câu hỏi
    df5 = pd.DataFrame(df3.isin([-1]).sum(axis=0))
    Wrong_answer_max = df3.isin([-1]).sum(axis=0).max()
    #print(df5)
    print("Câu hỏi bị sai nhiều nhất là: ",(pd.DataFrame(df5[df5[0] == Wrong_answer_max])).index.values,"bị sai ",Wrong_answer_max,"lần và chiếm tỉ lệ: ",round((Wrong_answer_max*100)/len(df3),1),"%")
    
    fullpath = "/Users/hoalam/this mac/Data Sciency/GT_KHDL/data_file_asm2/Output/"+ filename + "_grade.txt"
    f = open(fullpath,"w")
    row = ""
    for h in range (0,len(df3),1): 
        row = str(df3.loc[h,0]) + "," + str(df3.loc[h,"Tổng điểm"])
        f.write(row + "\n")
        #print(row)
    f.close()

    kiemtra_lopkhac = int(input("\n********\nKiểm tra lớp khác (0,1)",))
    if kiemtra_lopkhac != 1: 
        print("end")
        break
    if kiemtra_lopkhac == "":
        print("end")
        break
        
    


    
    


    
