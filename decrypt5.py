import random
import time

print(f" ")
def generate_hex_decimal_animation():
    hex_number = random.randint(0, 0xFFFFFFFF)
    hex_string = format(hex_number, 'X')
    decimal_number = int(hex_string, 16)
    
    hash_length = decimal_number % 30 + 1
    animation = ['_' for _ in range(hash_length)]
    
    used_indices = set()
    
    for i in range(hash_length):
        available_indices = [idx for idx in range(hash_length) if idx not in used_indices]
        
        if not available_indices:
            break
        
        random_index = random.choice(available_indices)
        animation[random_index] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        used_indices.add(random_index)
        
        progress = i + 1
        percentage = (progress * 100) // hash_length
        yield ''.join(animation), progress, hash_length, percentage

if __name__ == "__main__":
    anim_generator = generate_hex_decimal_animation()
    
    print("[+]", end="")
    
    try:
        for animation_step, progress, total_length, percentage in anim_generator:
            print(f"\r[+] Retrieved: {animation_step} {progress}/{total_length} ({percentage}%)", end="")
            time.sleep(random.uniform(0.1, 0.9))
    except StopIteration:
        pass
    
    print("\n[+]Cracking complete!")
