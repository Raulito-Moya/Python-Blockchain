#Initializing out blockchain list
blockchain = [] # -1 for get the last value in thelist
open_transaction = []
owner = 'Max'



def get_last_blockchain_value():
      """Returns the ast value of the current blockchain"""
      if len(blockchain) < 1:
           return None
      return blockchain[-1]

def add_transaction(recipient,sender=owner, amount=1.0):
  """Append a new value as well as the last blockchain value to the blockchain
   
   Arguments:
     :sender:  The sender of the coins
     :recipient: The recipient of the coins
     :amount: the amount of coins with the transacrion (default= 1.0)

  
  """
  transaction = {'sender':sender,'recipient':recipient,'amount':amount}
  open_transaction.append(transaction)
 
  #print(blockchain)


def mine_block():
    pass

def get_transaction_value():
    """Returns the input of the user ( a new trasnaction amount) as a float."""
    recipient = input('enter the recipient of the transaction')
    tx_amount = float(input("Your transaction amount please"))
    return (recipient, tx_amount)

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
       #output the blockchain lits to console
      for block in blockchain:
       print('Outputting in Block')
       print(block) 
      else:
          print('-' * 20)    

def verify_chain():
   # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
         if block_index == 0:
            continue
         elif blockchain[block_index] [0] == blockchain[block_index - 1]:
            is_valid = True
         else:
             is_valid = False
           # break
   # for block in blockchain:
    #    if block_index == 0:
    #        block_index += 1
    #        continue
    #    elif block[0] == blockchain[block_index - 1]:
     #       is_valid = True
     #   else: 
     #       is_valid = False
    #        break
    #    block_index += 1
    return is_valid

waiting_forinput = True

while True:
      print("PLease choose")
      print("1: Add a new transaction value")
      print('2: Output the blockchain blocks')
      print('h:Manipulate the chain')
      print('q: Quit')
      user_choice =  get_user_choice()
      if user_choice == '1':
          tx_data = get_transaction_value()
          recipient, amount= tx_data
          #add the transaction amount to the blockchain
          add_transaction(recipient, amount=amount)
          print(open_transaction)
      elif user_choice == '2':
           print_blockchain_elements()  

      elif user_choice == 'h':
          if len(blockchain) >= 1:
             blockchain[0] = [2]
      elif user_choice == 'q':
          wating_for_input = False
          break
      else:
          print('Input was invalid, please pick a value from the list')
      if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain')
        break
else: 
     print('User left!')  

print('Done!')