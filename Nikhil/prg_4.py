try:
    f = open('/opt/tmp/myfile.txt')
except EnvironmentError:
    print('Failed to open file')
except IOError:
    print('File not found')

