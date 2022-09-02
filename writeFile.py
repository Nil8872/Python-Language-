# fp = open("writing.txt", "w")
# fp.write("Hello, How are you? \n This this file is created automatically, hmm okk")

# fp = open("writing.txt", "a")
# fp.write("\nThis is content is append into this file by using append mode")
# fp.close

# f = open("writing.txt", "r")
# for item in f:
#     print(item)

# fw = open("writing.txt", "w")
# fw.write("All content of file writing.txt is replace with this content because we open this file in writing mode")

frw = open("Nilesh.txt", "r+")
frw.write("this file is open for read and write\n")
frw.close()
fa = open("Nilesh.txt", "a")
fa.write("In this file here new text is added\n")
fa.close()
fr = open("Nilesh.txt", "r")

for i in fr:
    print(i)