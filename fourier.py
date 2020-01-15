import math
import matplotlib.pyplot as plt


class fourier:
    def __init__(self, interval = [-1,1], precision = 10000, decimals = 5, mode = "point by point"):
        self.data_y = []
        self.data_x = []
        self.serie_sin = []
        self.serie_cos = []
        self.mode = mode
        self.precision = precision
        self.interval = interval
        self.decimals = decimals

    
    def set_decimals(self, decimals):
        self.decimals = decimals

    def set_interval(self, interval):
        self.interval = interval

    def set_data(self, data):
        self.data_y = data[1]
        self.data_x = data[0]

    def set_precision(self, precision):
        self.precision = precision
    
    def set_mode(self, mode):
        if mode == "point by point" or mode == "function":
            self.mode = mode
    
    def set_function(self,fct):
        self.fct = fct
    
    def function(self,x):
        if self.mode == "function":
            return fct(x)

        
        if self.mode == "point by point":
            x_min = max(self.data_x)
            approx_x_index = 0
            for temp_x_index in range(len(self.data_x)):
                if abs(x-self.data_x[temp_x_index]) < x_min and x >= self.data_x[temp_x_index]:
                    x_min = abs(x-self.data_x[temp_x_index])
                    approx_x_index = temp_x_index
            if self.data_x[approx_x_index] == x:
                return self.data_y[approx_x_index]

            
            return (((self.data_y[approx_x_index+1]-self.data_y[approx_x_index])*(x-self.data_x[approx_x_index]))/(self.data_x[approx_x_index+1]-self.data_x[approx_x_index])+self.data_y[approx_x_index])
            

            
            return approx_x
    
    def average_value(self,type = "null",n = 1):
        sum_integral = 0
        sub_interval_size = (self.interval[1])/self.precision
        progress = min(self.interval)
        
        if type == "null":
            while progress < max(self.interval):
                sum_integral += self.function(progress)*sub_interval_size
                progress += sub_interval_size
        
        if type == "cos":
            while progress < max(self.interval):
                sum_integral += self.function(progress)*sub_interval_size*math.cos((n*math.pi*progress)/self.interval[1])
                progress += sub_interval_size
        if type == "sin":
            while progress < max(self.interval):
                sum_integral += self.function(progress)*sub_interval_size*math.sin((n*math.pi*progress)/self.interval[1])
                progress += sub_interval_size
        
        
        return round(sum_integral/(self.interval[1]),self.decimals)
        
    
    def calculate_serie(self, n):

        self.a0 = self.average_value()/(2)
        self.an = [self.average_value("cos",i+1) for i in range(n)]
        self.bn = [self.average_value("sin",i+1) for i in range(n)]
        
        print(self.a0)
        print("------")
        print(self.an)
        print("-----")
        print(self.bn)

    def calculate_function(self):
        interval = self.interval
        precision = self.precision
        x_axe = []
        y_axe = []
        print(interval[0])
        
        
        for i in range(int((interval[1]-interval[0])*precision)):
            x_axe += [(i)/precision+interval[0]]
            temp_y = 0
            for n in range(len(self.an)):
                temp_y += self.an[n]*math.cos((math.pi*(n+1)*x_axe[-1])/self.interval[1]) + self.bn[n]*math.sin((math.pi*(n+1)*x_axe[-1])/self.interval[1])
            y_axe += [temp_y]
        
        self.x_axe = x_axe
        self.y_axe = y_axe

    def plot(self, ref_curve = False):
        interval = self.interval
        y_axe2 = []
        
        for i in self.y_axe:
            y_axe2 += [i+self.a0]

        
        if ref_curve:
            y_axe3 = [self.function(i) for i in self.x_axe]
            plt.plot(self.x_axe,y_axe3)

        plt.plot(self.x_axe,y_axe2)

        
        plt.show()
    

# f = fourier()
# f.set_interval([-1,1])
# f.set_mode("point by point")
# f.set_data([[-1,-0.8,-0.5,-0.3,0.2,1],[1,2,4,-4,2,0]])
# f.calculate_serie(50)
# f.calculate_function()
# f.plot(True)


fct = lambda x: x**2

f2 = fourier()
f2.set_function(fct)
f2.set_interval([-1,1])
f2.set_mode("function")
f2.calculate_serie(1)
f2.calculate_function()
f2.plot(True)
