'''creates the pascal triangle
'''

#!/usr/bin/python3 
def pascal_triangle(n):
    '''creates the pascal triangle
    '''
    #list of lists
    triangle = [[1]]
    counter = 0
    #case where n <=0
    if n <= 0:
        return []
    else:
        #keep track of rows
        for x in range(1, n):
            list = [1] #initialise list with 1
            try:
                for index in range(1, x):
                    #calculate the pascal value
                    num = triangle[x-1][index-1] + triangle[x-1][index]
                    list.append(num)
            except:
                break

            finally:
                list.append(1)
                triangle.append(list)#add list to the triangle
                continue
        return triangle
    
def main():
    print(pascal_triangle(12))

if __name__ == '__main__':
    main()