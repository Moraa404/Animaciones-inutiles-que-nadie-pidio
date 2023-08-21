import random
import time

def load_wordlist(file_path):
    with open(file_path, "r") as file:
        wordlist = file.read().splitlines()
    return wordlist

def generate_animation(wordlist):
    wordlist_length = len(wordlist)
    
    for keys_tested, passphrase in enumerate(wordlist, start=1):
        master_key = ' '.join(['{:02X}'.format(random.randint(0, 255)) for _ in range(32)])
        transient_key_lines = [
            ' '.join(['{:02X}'.format(random.randint(0, 255)) for _ in range(16)]) for _ in range(3)
        ]
        transient_key = '\n'.join(transient_key_lines)
        
        progress_percentage = (keys_tested / wordlist_length) * 100
        
        yield keys_tested, passphrase, master_key, transient_key, progress_percentage

if __name__ == "__main__":
    wordlist_path = input("Enter the path to the wordlist file: ")
    print(" ")
    wordlist = load_wordlist(wordlist_path)
    
    anim_generator = generate_animation(wordlist)
    
    try:
        print("[+]", end="")
        while True:
            keys_tested, passphrase, master_key, transient_key, percentage = next(anim_generator)
            print(f"\r          {keys_tested}/{len(wordlist)} keys tested ({percentage:.2f}%)", end="")
            print(f"\n  Current passphrase: {passphrase}")
            print(f"\n  Master Key     : {master_key}")
            print(f"\n  Transient Key  : {transient_key}\n")
            time.sleep(0.1)
            print("\033[F"*9, end="")  # Move cursor up
    except StopIteration:
        pass
