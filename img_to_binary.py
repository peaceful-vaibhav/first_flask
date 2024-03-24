# This function takes the input file, uploaded by the user
# and then converts the file to Binary Large Object (BLOB)

def to_binary(filename):
    blob_img = filename.read()
    return blob_img