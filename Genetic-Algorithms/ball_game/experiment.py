
def get_sum_of_all_weights(space):
        return sum( sum_of_2d_array(layer) for layer in space ) 
    
def sum_of_2d_array(matrix):
    return sum( sum(row) for row in matrix ) 

space = [[[x + 100 * y + 10000 * z for x in range(3)]
            for y in range(3) 
    ] for z in range(3)
]

for grid in space:
    for row in grid:
        print(row) 
    print() 

print('\n')
print(get_sum_of_all_weights(space))