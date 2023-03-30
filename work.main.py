def even_list(int_list):
    even_int_list=[]
    j=0
    
    i=0
    while i<len(int_list):
        if int_list[i]%2==0:
            even_int_list[j]=int_list[j]
            j=j+1
    
    return even_int_list

int_list = [1,2,3,4,5,6,7,8,9,10]
a=even_list(int_list)

def sum_of_squares_of_even(even_int_list):
    sum=0
    for i in even_int_list:
        sum+=even_int_list[i]*even_int_list[i]

    return sum

def main():
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)