import os 
path = './所有SH' #存取位置
dirs = os.listdir(path) #將路徑中的資料存入一個陣列中 （資料0、 資料1）
dirs_count = len(dirs) #這個資料夾中有多少個文件
for i in range(0,dirs_count,1):
    print(i+1,".",dirs[i])
print("q . 退出")

while(1): #輸入的循環，錯誤就再輸入，輸入q就結束程式
    T = input("請輸入你要執行的項目")
    if T == "q" or T == "Q" :
        exit()
    else:
        if T.isdigit():
            if int(T) < dirs_count+1:
                T = int(T)-1
                break
    print("\nERROR:\n請檢查你輸入的項目是否正確:\n")

print("開始執行所指定的腳本：",dirs[T],"\n")
os.chdir(path)
os.system("./%s" %(dirs[T]))
print("\n執行結束")



