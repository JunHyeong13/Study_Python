# H,M = map(int,input().split()); 

# if H > 0 :
#     if M-45 < 0 :
#         print(H-1, end = " ")
#         print(60+(M-45))
#     else:
#         print(H, end = " ")
#         print(M-45)
        
# if H == 0:
#     if M-45 < 0:
#         print(24+(H+1), end = " ")
#         print(60+(M-45))
#     else:
#         print(H, end = " ")
#         print(M-45)

    
H,M = map(int,input().split())
#n시 45분 이상
if M-45>=0:
    print(str(H)+' '+str(M-45))
#n시 44분 이하
else:
    #0시 -> 23시
    if H==0:
        print('23 ' + str(15+M))
    #n시
    else:
        print(str(H-1)+' '+str(15+M))

    
# if M-45 <= 0:   
#     print(60+(M-45))
# else:
#     print(M-45)

   

    
# 원래 시간보다 45분 일찍 설정