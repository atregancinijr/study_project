if __name__=='__main__':
#list comprehension
    vals = [1, 2, 3, 4, 5]
    print([ii**2 for ii in vals])
#We can define a 'generator expression'
    print('generator: ')
    print(ii**2 for ii in vals)
    print(list(ii**2 for ii in vals))
#dictionary comprehension:
    print({ii:ii**2 for ii in vals})
