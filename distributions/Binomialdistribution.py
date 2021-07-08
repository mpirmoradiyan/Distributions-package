import math
import seaborn as sns
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution. It inherits from Generaldistribution.Distribution class.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """
    
    #       A binomial distribution is defined by two variables: 
    #          p: the probability of getting a positive outcome
    #          n: the number of trials   
    #       
    #       For example, flipping a fair coin 25 times ==> p = 0.5 and n = 25
    #       The mean and standard deviation can the be calculated with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))
            
    def __init__(self,prob=0.1, size=20):
        self.n=size
        self.p = prob
        Distribution.__init__(self) 
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
            
    def calculate_mean(self):
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """        
        return self.p * self.n        

    
    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        
        return math.sqrt(self.n * self.p * (1-self.p))      
    
    # A method to update the parameters according to a dataset.
    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        self.n = len(self.data)
        self.p = sum(self.data)/len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return (self.p,self.n)    
    
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot and seaborn libraries.
        
        Args:
            None
            
        Returns:
            None
        """
        sns.countplot(x=self.data)
        plt.title('Bar Chart of the data')
        plt.xlabel('Outcome')        
        plt.ylabel('Count')
        plt.show() 
    
    
    def pdf(self,k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        comb = math.factorial(self.n)/(math.factorial(k) * math.factorial(self.n - k))
        return comb * self.p**k * (1-self.p)**(self.n - k)
    
    def plot_pdf(self):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x = list(range(self.n+1))
        y = [self.pdf(i) for i in range(self.n+1)]
        sns.barplot(x=x,y=y)        
        plt.title('Distribution of Outcomes')
        plt.xlabel('Outcome')
        plt.ylabel('Probability')
        plt.show()
        return [x,y]    
        
                
    # A method to output the sum of two binomial distributions, assuming both distributions have the same p value.
    def __add__(self,other):        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise        
        
        return Binomial(size=self.n+other.n, prob=self.p)
                        
    
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)        
