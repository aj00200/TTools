import os
def file_or_dir(path):
    '''
    file_or_dir(path)
        Tell wether the object located at path is a file or a folder:
        Return Values:
            0 - Object is a folder
            1 - Object is a file
            2 - Unknown
    '''
    try:
        os.listdir(path)
        return 0
    except Exception,e:
        if e.strerror=='Not a directory':
            try:
                open(path,'r')
                return 1
            except Exception,e:
                return 2
        else:
            return 2

