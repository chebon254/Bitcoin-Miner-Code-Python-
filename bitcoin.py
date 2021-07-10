from hashlib import sha256



MAX_NONCE = 10000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros

    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)

        if new_hash.startswith(prefix_str):
            print("Whooray! Successfully mined bitcoins with nonce value: {nonce}")
            return new_hash

    raise BaseException("Ooops could not mine any bitcoin after tryingtimes{MAX_NONCE}")


if __name__=='__main__':
    transactions = '''
    chebon->kibet->30,
    meone->kt->50
    '''

    difficulty = 20;

    import time
    start = time.time()
    print("Start mining")
    new_hash = mine(5, transactions, '', difficulty)
    total_time =  str((time.time() - start))



    print(new_hash)