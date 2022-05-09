#读取CFGMAT中的每一行
#将HEAD中的前8行写入新文件POSCAR中（新文件夹用CFGMAT中第一列的数字命名）
#读取CFGMAT的第三列数值x1,将SPOSCAR中的第x1+8行写入新文件POSCAR
#读取CFGMAT的第四列数值x2，将SPOSCAR中的第x2+8行写入新文件POSCAR
#.........
#对于SPOSCAR中第九行到最后一行，刚刚没有用到的行，按顺序写入新文件POSCAR
#将新文件POSCAR拷入第一列命名的文件夹
import shutil
import os
#-----------------------------------------------------------


f0=open(r'HEAD','r')
f1=open(r'CFGMAT','r')
f2=open(r'SPOSCAR','r')
#pos=open(r'POSCAR','a+')
path0 = os.getcwd()
source_path=path0+'/POSCAR'
l0=f0.readlines()
l1=f1.readlines()
l2=f2.readlines()
lattice_constant=f0.readlines

#for i in range(0,5):
for i in range(0,len(l1)+2):     #读入CFGMAT第i行
    print ('第'+str(i)+'个结构')
    ii=i-1
    print(l1[ii])
    pos=open('POSCAR','w')
    final_path=path0+'/'+f"{ii}"
    ll1=l1[ii]
    x1=int(ll1.split()[2])         #读取第i行的数值，确定我们需要的掺杂原子号
    x2=int(ll1.split()[3])
    x3=int(ll1.split()[4])
    x4=int(ll1.split()[5])
    
##########         写入前8行        ##############################
    pos.write(str(x1)+str(x2)+str(x3)+str(x4)+'Pb atom'+"\n")
    for x in range(1,8):
        tmp_line=l0[x]
        #pos.write(f"222222222222{x}\n")
        #pos.write(f"222222222222{x}\n") #pos.write("333333333 %d \n" %x)同等替换
        pos.write(tmp_line)
    
##########        写入掺杂的原子 9-12行原子       ##############################


    pos_x1=l2[int(x1)+8]          #根据原子序号，找到对应的坐标
    pos_x2=l2[int(x2)+8]
    pos_x3=l2[int(x3)+8]
    pos_x4=l2[int(x4)+8]
    pb_list=[x1,x2,x3,x4]   #把原子序号写入列表，防止之后重复读取
    #写入掺杂原子的坐标
    pos.write(pos_x1+pos_x2+pos_x3+pos_x4)
    
#################      写入13-88行原子   #############################
    for j in range(8,len(l2)):
        k=j-7
        if k in pb_list:
            k=k
        else:
            tmp2=l2[j]
            pos.write(tmp2)
        
    pos.closed


###############        将POSCAR复制到对应文件夹里        ##################
    if not os.path.exists(final_path):
            os.mkdir(final_path) # if there is no such dir, please use this
    print ('初始路径为'+source_path)
    print ('最终路径为'+final_path)
    shutil.copy(source_path,final_path)
#    os.remove(source_path)




f1.closed
f2.closed








