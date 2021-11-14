#For example, if %s is encountered when formatting a unicode object in Python 2, it will attempt to use #__unicode__ first.
#Consider the following code, running in Python 2.7:

class MyObject:
    def __str__(self):
        return 'My Awesome Object!'

class Which:
    def __str__(self):
        return 'string'

    def __unicode__(self):
        return u'unicode'

if __name__ == '__main__':
    print('The %s was used.' % Which())
    x=u'The %s was used.' % Which()
