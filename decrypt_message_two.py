encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
temp = list(encrypted_message)
decrypted_message = encrypted_message
start = 1
end = len(encrypted_message) - 2
while start < end:
    temp[start], temp[end] = temp[end], temp[start]
    start+=2
    end-=2
decrypted_message = ''.join(temp)
print(decrypted_message)


