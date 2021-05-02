#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')

# A basic code for matrix input from user 
  
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
ip=np.array(matrix)

#Getting mask_choice of user
mask_ip=int(input('Enter 1 if point is to be detected and 2 if line is to be detected:'))
if mask_ip==1:
    mask=np.array([[1,1,1],[1,-8,1],[1,1,1]])
elif mask_ip==2:
    line=int(input('Enter 1, 2, 3 or 4 for Horizontal, vertical, +45 diagonal or -45 diagonal line detection respectively:'))
    if line==1:
        mask=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
    elif line==2:
        mask=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
    elif line==3:
        mask=np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
    elif line==4:
        mask=np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
    else:
        print('Invalid mask')
else:
    print('Invalid entry')
        
#adding border padding to input matrix
def padding(ip,R,C):
    n1=np.vstack((ip,ip[R-1]))
    n2=np.vstack((ip[0],n1))
    f=[]
    for i in range(0,R+2):
        n_i=np.pad(n2[i], (1,1), 'constant', constant_values=(n2[i,0],n2[i,C-1]))
        f.append(n_i)
    padded=np.array(f)
    return(padded)

#masking each pixel of input matrix
def masking(R,padded,mask):
    px=[]
    for i in range(0,R):
        for j in range(0,R):
            mat=padded[i:i+3,j:j+3]
            y_i=0
            for m in range (0,3):
                for n in range(0,3):
                    y_i=y_i+(mat[m,n]*mask[m,n])
                    #print(y_i)
            px.append(y_i)
    return(px)
p = padding(ip,R,C)
px = masking(R,p,mask)

#printing input and output matrix 
ip_tr=np.array(px).reshape(R,R)              
print('Input matrix:\n',ip,"\n","Output after applying mask:\n",ip_tr)

#setting threshold
thr=int(input("Set your threshhold for detection:"))

if mask_ip==1:
    #detecting point
    pt=[]
    for i in range(R):
        for j in range(C):
            if abs(ip_tr[i,j])>thr:
                pt.append(ip[i,j])
                x=i
                y=j
    if len(pt)>0:
        print("Points detected : " ,pt,"( ",len(pt)," points )")
    else:
        print("Point not detected")
    plt.figure()
    plt.imshow(ip, cmap=plt.cm.gray)
    plt.title('Input image')
    plt.show()
    plt.figure()
    plt.imshow(ip_tr, cmap=plt.cm.gray)
    plt.title('Output image')
    plt.show()
elif mask_ip==2:
    #detecting line
    loc=[]
    pt=[]
    c=0
    for i in range(R):
        for j in range(C):
            if abs(ip_tr[i,j])>thr:
                x,y=i,j
                loc.extend([x,y])
                pt.append(ip[i,j])
                c=c+1

    k=np.array(loc).reshape(c,2)
    #print(k)
    global case
    if len(pt)>R-1:
        for b in range(1,len(k)):
            if k[b-1,0]==k[b,0]:
                case='row'
            elif k[b-1,1]==k[b,1]:
                case='col'
            elif k[b,0]==k[b,1]:
                case='45'
            elif (k[b,0]+k[b,1])==(R-1):
                case='-45'
            else:
                case='0'
        if case=='row':
            print('Horizontal line is detected in row number:',k[0,0]+1,'which is:',pt)
        elif case=='col':
            print('Vertical line is detected in column number:',k[0,1]+1,'which is:',pt)
        elif case=='45':
            print('+45 line is detected which is:',pt)
        elif case=='-45':
            print('-45 line is detected which is:',pt)
        else:
            print(":(")
    else:
        print("No line detected")

    plt.figure()
    plt.imshow(ip, cmap=plt.cm.gray)
    plt.title('Input image')
    plt.show()
    plt.figure()
    plt.imshow(ip_tr, cmap=plt.cm.gray)
    plt.title('Output image')
    plt.show()
else:
    print('')

