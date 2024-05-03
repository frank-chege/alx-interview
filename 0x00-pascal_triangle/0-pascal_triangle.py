def pascal_triangle(n):
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
                #when an index out of bounds is accessed
                print('error!')
                break
                
            finally:
                list.append(1)
                triangle.append(list)#add list to the triangle
                continue
        return triangle