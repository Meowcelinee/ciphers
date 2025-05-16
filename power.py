# - - - - - - - - - - - - - - - - 
#                               |
#   the "power cipher"          |
#                               |
#   developed between 4/23      |
#   and 12:15pm on 4/24         |
#                               |
#   sets "key" as length of     |
#   longest word in message     |
#                               |
#   converts each letter to its |
#   corresponding number, and   |
#   raises each number to the   |
#   key-th power.               |
#                               |
# - - - - - - - - - - - - - - - -

alphabet = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# finds length of longest word in a word list, ignoring special characters
# used to get key for encrypting/decrypting
def find_longest(li): # li: string
    len_list = []
    for word in li.split(' '):
        for char in word:
            if char not in alphabet: word = word.replace(char, '')
        len_list.append(len(word))

    len_list.sort(reverse=True)

    return len_list[0]

# encrypt message using the length of the longest word in the message as a key
def encrypt(msg): # msg: string
    key = find_longest(msg)
    words = []
    for word in msg.split(' '):
        num_word = []
        for letter in list(word):
            if letter in alphabet:
                index = alphabet.index(letter)
                exp = str(pow(index, key))
                num_word.append(exp)
            else:
                num_word.append(letter)
        
        words.append(num_word)

    # destructure lists to make output prettier
    words = [' '.join(word) for word in words]
    words = ' '.join(words)

    print(f'\nYour encrypted message is:\n{words}')
    print(f'\nYour key is:\n{key}')

# decrypt message using the length of the longest word in the message as a key
def decrypt(msg, key): # msg: string, key: int
    words = msg.split(' ')
    new_msg = ''
    
    for word in words:
        try:
            word = int(word)
            word = round(pow(word, 1 / key))

            new_msg += alphabet[word].upper()
        except:
            # if the character isn't an index of the alphabet, add the raw character to the string
            new_msg += word
    
    print(f'\nYour decrypted message is:\n{new_msg}')

def main():
    method = input('Encrypt or decrypt? ').lower()
    try:
        if method == 'encrypt':
            msg = input('Enter your message: ')
            encrypt(msg)
        
        if method == 'decrypt':
            msg = input('Enter your message: ')
            key = int(input('Enter the decryption key: '))
            decrypt(msg, key)
        
        if not method in ['encrypt', 'decrypt']:
            print('Method must be either "encrypt" or "decrypt".')
            exit(1)

    except Exception as e:
        print(e)
        exit(1)

try:
    main()
except KeyboardInterrupt:
    print(f'\nExiting.')
    exit(0)
