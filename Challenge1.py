print("1. Encodez le message")
print("2. Décodez le message")
print("3.Quittez")
alphabet="abcdefghijklmnopqrstuvwxyz "
def code(nombre:int,message:str)->str:
    message_coder=""
    for el in range (len(message)):
        #print(message[el])
        position=alphabet.find(message[el])
       # print(position)
        
        #print("la nouvelle position est" ,nouvelle_position)
        #print(alphabet[nouvelle_position])
        
    print ("le message codé de", message, "est" ,message_coder)
    if position >26:
            nouvelle_position=position-27
            nouvelle_position=position+nombre
            message_coder+=alphabet[nouvelle_position]
    return message_coder 

def decode(nombre:int,message:str)->str:
    message_decoder=""
    for el in range (len(message)):
        print(message[el])
        position=alphabet.find(message[el])
        print(position)
        nouvelle_position=position-nombre
        print("la nouvelle position est" ,nouvelle_position)
        print(alphabet[nouvelle_position])
        message_decoder+=alphabet[nouvelle_position]
        print ("le message décodé de", message, "est" ,message_decoder)
        if position <0:
            nouvelle_position=position+27
            nouvelle_position=position+nombre
    return message_decoder 


code(2,"bonjouz")
decode(2,"awe ovugjohsslunl")

