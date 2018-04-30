import numpy as np
import pandas
from ortools.linear_solver import pywraplp

for i in range(1,100):
    num_data = (2**i)
    batch_size = 1024
    batch = np.zeros(batch_size,dtype= np.float_)
    with open('bucket\\outputLinfinity{}.csv'.format(i), 'w') :
        pass
    for j in range(4096):
        initVal = 0
        y = 0
        solver = pywraplp.Solver('LinearReg',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
        t = solver.NumVar(-solver.infinity(), solver.infinity(), 't')
        beta = solver.NumVar(-solver.infinity(), solver.infinity(), 'beta')

        while (y<num_data):
            betaF = np.random.beta(1,num_data-y) # This is a float from 0 to 1
            x = (1-initVal)*betaF+initVal
            constraint_pos = solver.Constraint(y,solver.infinity())
            constraint_pos.SetCoefficient(beta,x)
            constraint_pos.SetCoefficient(t,1)
            constraint_neg = solver.Constraint(-1*y,solver.infinity())
            constraint_neg.SetCoefficient(beta,-1*x)
            constraint_neg.SetCoefficient(t,1)
            y+=1
            initVal = x
        objective = solver.Objective()
        objective.SetCoefficient(t,1)
        objective.SetMinimization()

        solver.Solve()
        np.put(batch,[j%batch_size],[t.solution_value()])    
        if (j%batch_size==batch_size-1):
            pandas.DataFrame(batch).to_csv("bucket\\outputLinfinity{}.csv".format(i), mode='a', header=False, index=False)
        
            

"""
#https://rosettacode.org/wiki/External_sort
import io

def sort_large_file(n: int, source: open, sink: open, file_opener = open)->None:

    '''
        approach:
            break the source into files of size n
            sort each of these files
            merge these onto the sink
    '''

    # store sorted chunks into files of size n
    mergers = []
    while True:
        text = list(source.read(n))
        if not len(text):
            break;
        text.sort()
        merge_me = file_opener()
        merge_me.write(''.join(text))
        mergers.append(merge_me)
        merge_me.seek(0)

    # merge onto sink
    stack_tops = [f.read(1) for f in mergers]
    while stack_tops:
        c = min(stack_tops)
        sink.write(c)
        i = stack_tops.index(c)
        t = mergers[i].read(1)
        if t:
            stack_tops[i] = t
        else:
            del stack_tops[i]
            mergers[i].close()
            del mergers[i]  # __del__ method of file_opener should delete the file

def main():
    '''
        test case
        sort 6,7,8,9,2,5,3,4,1 with several memory sizes
    '''

    # load test case into a file like object
    input_file_too_large_for_memory = io.StringIO('678925341')

    # generate the expected output
    t = list(input_file_too_large_for_memory.read())
    t.sort()
    expect = ''.join(t)
    print('expect', expect)

    # attempt to sort with several memory sizes
    for memory_size in range(1,12):
        input_file_too_large_for_memory.seek(0)
        output_file_too_large_for_memory = io.StringIO()
        sort_large_file(memory_size, input_file_too_large_for_memory, output_file_too_large_for_memory, io.StringIO)
        output_file_too_large_for_memory.seek(0)
        assert(output_file_too_large_for_memory.read() == expect)
        print('memory size {} passed'.format(memory_size))

if __name__ == '__main__':
   example = main
   example()



"""
