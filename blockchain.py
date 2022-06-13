#Initializing out blockchain list
from pickle import TRUE

MINING_REWARD = 10

genesis_block = {
    'previous_hash': '', 
    'index': 0, 
    'transactions':[]
}
blockchain = [genesis_block] # -1 for get the last value in thelist
open_transactions = []
owner = 'Max'
participants = {'Max'}

def hash_block(block):
    print('hash_block:',block)
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender =[[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]  # O|
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
          if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
          if len(tx) > 0:
           amount_received += tx[0]
    return amount_received - amount_sent

def get_last_blockchain_value():
      """Returns the ast value of the current blockchain"""
      if len(blockchain) < 1:
           return None
      return blockchain[-1]

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']
   


def add_transaction(recipient,sender=owner, amount=1.0):
  """Append a new value as well as the last blockchain value to the blockchain
   
   Arguments:
     :sender:  The sender of the coins
     :recipient: The recipient of the coins
     :amount: the amount of coins with the transacrion (default= 1.0)

  
  """
  transaction = {
      'sender':sender,
      'recipient':recipient,
      'amount':amount
      }
  if verify_transaction(transaction):
      print('Transaction verified!!!')
      open_transactions.append(transaction)
      participants.add(sender)
      participants.add(recipient)
      return True
  return False
      #print(blockchain)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender':'MINING',
        'recipient':owner,
        'amount':MINING_REWARD
    }
    copied_transaction = open_transactions
    open_transactions.append(reward_transaction)

    block = {
    'previous_hash': hashed_block, 
    'index': len(blockchain), 
    'transactions':open_transactions 
    }
    blockchain.append(block)
    return True


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
    """Verify the current blockchain and return True if it's valid """
   
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1 ]):
            print('Block!!!!',hash_block(blockchain[index - 1 ]))
          
            return False
    
    return True

waiting_for_input = True

while True:
      print("PLease choose")
      print("1: Add a new transaction value")
      print("2: Mine a new block")
      print('3: Output the blockchain blocks')
      print('4: Output Participants')
      print('h:Manipulate the chain')
      print('q: Quit')
      user_choice =  get_user_choice()
      if user_choice == '1':
          tx_data = get_transaction_value()
          recipient, amount= tx_data
          #add the transaction amount to the blockchain
          if add_transaction(recipient, amount=amount):
           print(open_transactions)
          else:
              print('Transaction failed!')

      elif user_choice == '2':
          if mine_block():
              open_transactions = []    
      elif user_choice == '3':
           print_blockchain_elements()  
      elif user_choice == '4':
           print(participants)
      elif user_choice == 'h':
          if len(blockchain) >= 1:
             blockchain[0] = {
                 'previous_hash': '', 
                 'index': 0, 
                 'transactions':[{'sender':'Chris', 'recipient':'Max', 'amount':100.0}]}
      elif user_choice == 'q':
          wating_for_input = False
          break
      else:
           print('Input was invalid, please pick a value from the list')
      if not verify_chain():
         print_blockchain_elements()
         print('Invalid blockchain')
         break
      print(get_balance('Max'))
    
else: 
     print('User left!')  

print('Done!')