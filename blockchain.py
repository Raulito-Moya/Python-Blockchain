#Initializing out blockchain list
blockchain = [] # -1 for get the last value in thelist

def get_last_blockchain_value():
      """Returns the ast value of the current blockchain"""
      if len(blockchain) < 1:
           return None
      return blockchain[-1]

def add_transaction(transaction_amount,last_transaction=[1]):
  """Append a new value as well as the last blockchain value to the blockchain
   
   Arguments:
     :transaction_amount: The amoun that should be added
     :last_transaction: The last blockchain transaction (default[1])

  
  """
  if last_transaction == None:
        last_transaction = [1]
  blockchain.append([last_transaction, transaction_amount])
  #print(blockchain)

def get_transaction_value():
    """Returns the input of the user ( a new trasnaction amount) as a float."""
    user_input = float(input("Your transaction amount please"))
    return user_input

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
       #output the blockchain lits to console
      for block in blockchain:
       print('Outputting in Block')
       print(block)    





while True:
      print("PLease choose")
      print("1: Add a new transaction value")
      print('2: Output the blockchain blocks')
      print('q: Quit')
      user_choice =  get_user_choice()
      if user_choice == '1':
          tx_amount = get_transaction_value()
          add_transaction(tx_amount, get_last_blockchain_value())
      elif user_choice == '2':
           print_blockchain_elements()  
      elif user_choice == 'q':
            break
      else:
          print('Input was invalida, please pick a value from the list')

   

print('Done!')