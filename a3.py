import numpy as np
import matplotlib.pyplot as plt


class Shape:
    
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        Shape.__init__(self)
        self.A=np.round_(A, decimals = 2)
        
        self.old_A=np.copy(self.A)
        self.x_new=None
        self.y_new=None
 
    def store_coord(self):
        self.old_A=np.copy(self.A)
    
    def translate(self, dx, dy=None):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        
        if dy==None:
            dy=dx
        Shape.translate(self,dx,dy)
        T=self.T_t
       
        A=self.A
        A=A.T
        
        new_A=np.dot(T,A)
        
        self.x_new=new_A[0]
        
        self.y_new=new_A[1]
        self.A=new_A
        self.A=self.A.T
        self.A=np.round_(self.A,decimals=2)
        self.x_new=np.round_(self.x_new,decimals=2)
        self.y_new=np.round_(self.y_new,decimals=2)
        return(self.x_new,self.y_new)
    
        
        
    def scale(self, sx, sy=None):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        
        if sy==None:
            sy=sx
        
         
        
        A=self.A
        A=A.T
        
        x=A[0]
        y=A[1]
        
        X=np.mean(x)
        Y=np.mean(y)
        
        self.translate(-X,-Y)
        new_A=np.array([self.x_new,self.y_new])
        
        Shape.scale(self,sx,sy)
        A[0]=self.x_new
        A[1]=self.y_new
        
        new_A=np.dot(self.T_s,A)
        
        
        self.A=new_A
        self.A=self.A.T
        
        self.translate(X,Y)
        
        
        self.A=np.round_(self.A,decimals=2)
        self.x_new=np.round_(self.x_new,decimals=2)
        self.y_new=np.round_(self.y_new,decimals=2)
        return(self.x_new,self.y_new)
   
    
    def rotate(self, deg, rx =0,ry=0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        
        
        deg=-1*deg
        self.translate(-rx,-ry)
    
        Shape.rotate(self,deg)
        
        self.A=np.dot(self.A,self.T_r)
        
        self.translate(rx,ry)
        A=self.A
        A=A.T
        A=np.round(A,2)
        self.x_new=A[0]
        self.y_new=A[1]
        
        self.A=np.round_(self.A,decimals=2)
        self.A=np.round(self.A,2)
        self.x_new=np.round_(self.x_new,decimals=2)
        self.y_new=np.round_(self.y_new,decimals=2)
        
        return(self.x_new,self.y_new)

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
       
        '''
        A=self.A
        A=A.T
        x_coord=list(A[0])
        x_coord.append(x_coord[0])
        x1_min=abs(min(x_coord))
        x1_max=abs(max(x_coord))
        x1=max(x1_min,x1_max)
        x_coord=np.array(x_coord)
        y_coord=list(A[1])
        y_coord.append(y_coord[0])
        y1_min=abs(min(y_coord))
        y1_max=abs(max(y_coord))
        y1=max(y1_min,y1_max)
        y_coord=np.array(y_coord)
        
        y1=np.amax(abs(y_coord))
        K=self.old_A
        K=K.T
        K=np.round(K,decimals=2)
        x_coord_old=list(K[0])
        x_coord_old.append(x_coord_old[0])
        x2_min=abs(min(x_coord_old))
        x2_max=abs(max(x_coord_old))
        x2=max(x2_min,x2_max)
        x_coord_old=np.array(x_coord_old)
        y_coord_old=list(K[1])
        y_coord_old.append(y_coord_old[0])
        y2_min=abs(min(y_coord_old))
        y2_max=abs(max(y_coord_old))
        y2=max(y2_min,y2_max)
        y_coord_old=np.array(y_coord_old)
        
        x1=max(abs(x1),abs(x2))
        y1=max(abs(y1),abs(y2))    
        plt.plot(x_coord_old,y_coord_old,'g',linestyle="dashed")
        plt.plot(x_coord,y_coord,'g')
        Shape.plot(self,x1,y1)
        self.store_coord()
        
        
        


class Circle(Shape):
   
    
    def __init__(self, x=0, y=0, radius=5):
        Shape.__init__(self)
        self.A=np.array((x,y,1),dtype= object)
        self.A=self.A.astype(float)
        self.radius=radius
        self.x=x
        self.y=y
        
        
    def store_coord(self):
        self.old_A=np.copy(self.A)
        self.x_old= self.old_A[0]
        self.y_old=self.old_A[1]
        k=[]
        k.append((self.radius))
        self.radius_old=k[0]
        
        
        

    
    def translate(self, dx, dy=None):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        
        if dy==None:
            dy=dx
        Shape.translate(self,dx,dy)
        T=self.T_t
        T=T.T   
        self.A=np.dot(self.A,T)
        self.A=np.round(self.A,2)
        self.x=self.A[0]
        self.y=self.A[1]
        
        
        return(self.x,self.y,self.radius)
 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        self.radius=self.radius*sx
        
        return(self.x,self.y,self.radius)
 
    
   
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        self.translate(-rx,-ry)
        Shape.rotate(self,deg)
        
        T=self.T_r
        T=T.T
        self.A=np.dot(self.A,T)
        
        self.translate(rx,ry)
        
        self.A=np.round(self.A,2)
        self.x=self.A[0]
        self.y=self.A[1]
        
        return(self.x,self.y,self.radius)
        
        
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        x=self.x_old
        y=self.y_old
        x1=self.A[0]
        y1=self.A[1]
        
        radius=self.radius_old
        circle_old=plt.Circle((x,y),radius,fill=False,linestyle="dashed")
        circle_new=plt.Circle((x1,y1),self.radius,fill=False)
        x1=max(abs(x1+self.radius),abs(x+radius),abs(x-radius),abs(x1-self.radius))
        y1=max(abs(y+radius),abs(y-radius),abs(y1+self.radius),abs(y1-self.radius))
        plt.gca().add_patch(circle_new)
        plt.gca().add_patch(circle_old)
        Shape.plot(self,x1,y1)
        self.store_coord()
        

if __name__ == "__main__":
   
    np.set_printoptions(precision=2)
    verbose = int(input("Verbose? 1 to plot, 0 otherwise: "))
    T=int(input("Enter no of test cases: "))
    while T<1:
        print("invalid no of test cases ")
        T=int(input("Enter no of test cases: "))
    for i in range(T):
        S=int(input("Enter type of shape (polygon/circle): "))
        if S==1:
            k=list(input("Enter a b and r of circle(space separated) ").split())
            a=float(k[0])
            b=float(k[1])
            r=float(k[2])
            c1=Circle(a,b,r)
            c1.store_coord()
        elif S==0:
            n=int(input("Enter no of sides of the polygon "))
            list1=[]
            for j in range(n):
                print("enter","(x",j+1,",y",j+1,") ")
                k=input().split()
                k=list(map(float,k))
                coord=[]
                coord.append(k[0])
                coord.append(k[1])
                coord.append(1)
                list1.append(coord)
            A=np.array(list1)
            p1=Polygon(A)
            p1.store_coord()
            k1=[]
           
            for i in list1:
              k1.append(i[0])
            for i in list1:
             k1.append(i[1])
        Q=int(input('Enter the no of queries: ')) 
        while(Q>20):
            print("invalid no of querries ")
        
        if S==0:
            print("""Enter Query:
1) R theta (rx) (ry)
2) S sx (sy)
3) T dx (dy)
4) P""")    
        
        elif S==1:
            print("""Enter Query:
1) R theta (rx)(ry)
2) S sr
3) T dx (dy)
4) P""")
        
    
        
     #just print results
        if S==0: #for polygon
          for i in range(Q):
                q=input().split()
                
                for i in k1:
                    print(i,end=" ")
                
                chr=q[0]
                if chr.lower()=="r":
                    deg=float(q[1])
                    while not(-360 <= deg <= 360):
                        print("Invalid degree, input new degree ")
                        deg=float(input())
                    if len(q)==2:
                        l=[]
                        
                        out=(p1.rotate(deg))
                        
                        
                        for i in out[0]:
                            print(i,end=" ")
                            l.append(i)
                        for i in out[1]:
                            print(i,end=" ")
                            l.append(i)
                        k1=l
                        print("\n")
                        if verbose==1:
                            p1.plot()
                    elif len(q)==3:
                        
                        rx=float(q[2])
                        l=[]
                        out=(p1.rotate(deg,rx))
                        for i in out[0]:
                            print(i,end=" ")
                            l.append(i)
                        for i in out[1]:
                            print(i,end=" ")
                            l.append(i)
                        k1=l
                        print("\n")
                        if verbose==1:
                            p1.plot()
                    elif len(q)==4:
                        
                        rx=float(q[2])
                        ry=float(q[3])
                        l=[]
                        out=(p1.rotate(deg,rx,ry))
                        for i in out[0]:
                            print(i,end=" ")
                            l.append(i)
                        for i in out[1]:
                            print(i,end=" ")
                            l.append(i)
                        k1=l
                        print("\n")
                        if verbose==1:
                            p1.plot()
                        
                elif chr.lower()=="t":
                    if len(q)==2:
                        dx=float(q[1])
                        out=p1.translate(dx)
                        l=[]
                        for i in out[0]:
                            print(i,end=" ")
                            l.append(i)
                        for i in out[1]:
                            print(i,end=" ")
                            l.append(i)
                        k1=l
                        print("\n")
                        if verbose==1:
                            p1.plot()
                    elif len(q)==3:
                        dx=float(q[1])
                        dy=float(q[2])
                        l=[]
                        out=p1.translate(dx,dy)
                        for i in out[0]:
                            print(i,end=" ")
                            l.append(i)
                        for i in out[1]:
                            print(i,end=" ")
                            l.append(i)
                        k1=l
                        print("\n")
                        if verbose==1:
                            p1.plot()
                        
                elif chr.lower()=="s":
                    if len(q)==2:
                        sx=float(q[1])
                        out=p1.scale(sx)
                        l=[]
                        for i in out[0]:
                            print(i,end=" ")
                            l.append(i)
                        for i in out[1]:
                            print(i,end=" ")
                            l.append(i)
                        k1=l
                        if verbose==1:
                            p1.plot()
                    elif len(q)==3:
                        sx=float(q[1])
                        sy=float(q[2])
                        l=[]
                        out=p1.scale(sx,sy)
                        for i in out[0]:
                            print(i,end=" ")
                            l.append(i)
                        for i in out[1]:
                            print(i,end=" ")
                            l.append(i)
                        k1=l
                        print("\n")
                            
                        if verbose==1:
                            p1.plot()
                elif chr.lower()=="p":
                    p1.plot()
                else:
                    print("Invalid querry")
                
         
        elif S==1:                      # for circle
          for i in range(Q):
                q=input().split()
                print(k[0],k[1],k[2])
                
                
                chr=q[0]
                if chr.lower()=="r":
                    deg=float(q[1])
                    while not(-360 <= deg <= 360):
                        print("Invalid degree, input new degree ")
                        deg=float(input())
                    
                    if len(q)==2:
                        l=[]
                        deg=float(q[1])
                        out=(c1.rotate(deg))
                        print(out[0],out[1],out[2])
                        k[0]=out[0]
                        k[1]=out[1]
                        k[2]=out[2]
                        print("\n")
                        if verbose==1:
                            c1.plot()
                    elif len(q)==3:
                        deg=float(q[1])
                        rx=float(q[2])
                        out=(c1.rotate(deg,rx))
                        print(out[0],out[1],out[2])
                        k[0]=out[0]
                        k[1]=out[1]
                        k[2]=out[2]
                        print("\n")
                        if verbose==1:
                            c1.plot()
                    elif len(q)==4:
                        deg=float(q[1])
                        rx=float(q[2])
                        ry=float(q[3])
                        
                        out=(c1.rotate(deg,rx,ry))
                        print(out[0],out[1],out[2])
                        k[0]=out[0]
                        k[1]=out[1]
                        k[2]=out[2]
                        print("\n")
                        if verbose==1:
                            c1.plot()
                        
                elif chr.lower()=="t":
                    if len(q)==2:
                        dx=float(q[1])
                        out=c1.translate(dx)
                        print(out[0],out[1],out[2])
                        k[0]=out[0]
                        k[1]=out[1]
                        k[2]=out[2]
                        
                        print("\n")
                        if verbose==1:
                            c1.plot()
                    elif len(q)==3:
                        dx=float(q[1])
                        dy=float(q[2])
                        
                        out=c1.translate(dx,dy)
                        print(out[0],out[1],out[2])
                        k[0]=out[0]
                        k[1]=out[1]
                        k[2]=out[2]
                        print("\n")
                        if verbose==1:
                            c1.plot()
                        
                elif chr.lower()=="s":
                    
                        sx=float(q[1])
                        out=c1.scale(sx)
                        print(out[0],out[1],out[2])
                        k[0]=out[0]
                        k[1]=out[1]
                        k[2]=out[2]
                        if verbose==1:
                            c1.plot()
                    
                elif chr.lower()=="p":
                    c1.plot()
                else:
                    print("Invalid querry")
                    
          print("The end")
          
                
                
                    
                    
                    
                        
                    
                
        
                
                
            
            
            
    
    
    
   
    
