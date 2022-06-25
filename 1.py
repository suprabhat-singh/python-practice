# #programing language is not good to store data , to store data permanently for the future purpose in our poject,Files are
# # very common permanent storage area to store data permanently
# # types of file 1 text file -usually we can use text files to store character eg abc.txt, abc.csv, abc.xls
# # Binary file-usually we can store binary data like image , video, audio..etc
# open(filename, mode), mode- r-(read), w-(write), a-(append), r+(read and write), w+(write and read), a+ -(append and read)
# # read--default mode is read mode, open the existing file for read operation, the file pointer is positioned at the begining of file
# # if the specified file does not exist then we will get file not found error
# # write(w)--open existing file for write operation, if file already contain data it will override,if file does not exist then python will create
# # # a new file
# # a--append mode open file for append operation,if file already contains data then it will add at the end of the text, if the file doesnot exist then
# #then python will create a new file
# # r+ -- read and write data into the file ,previous data will not be deleted,the file pointer positioned at the begining of the file.
# # w+ -- to write and read data from the file it will override the existing data
# #a+--to append and read the data from the file, it will override the existing data
# # x--to open a file in aexclusive creterion for write operation ,if file already exist then it will get error (file already exist)
# # after completeting yhe operation on file highly recommended to close the file syntax- filename.close()
# #name--file name, mode--'r' 'w' 'a' , closed--if file closed then it returns True, readable()--returns true if file is readable,
# # writable()-- returns true if file is writeable

# f = open('suprabhat.txt', 'w')
# print(f)
# print('the mode of file is', f.mode)
# print('the file is readable', f.readable)
# print('the file is writable', f.writable)
# f.close()
# print('the file is closed', f.closed)

f = open('suprabhat.txt', 'r')
print(f)
print('the mode of file', f.mode)
print('the file is readable', f.readable)
print('the file is writable', f.writable)
print('the file is closed', f.closed)



























