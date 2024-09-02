def count_vowel(text):
    vowels = "aeiouAEIOU"  
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
            
    return count

print (count_vowel("hello"))
print (count_vowel("salyviah"))
