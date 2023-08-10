import random
import string

def storage_cal():
    # Formula (<# of media items> * <average storage requirements per media item in mb>) + (<# of media items> * 5mb)
    #  5mb is estimated overhead of storing derivatives (small JPEG, TilePic pan-and-zoom version, etc.) 
    # return the number of media items over 20GB of disk space

    media_items = 2000
    average_storage = 5 # in mb
    storage = (media_items * average_storage) + (media_items * 5)
    # return storage in GB
    return storage / 1000

print(storage_cal())

def generate_password(length):
    # generate a password with length characters, it must include special characters, numbers, and letters
    # return the password
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

print(generate_password(20))