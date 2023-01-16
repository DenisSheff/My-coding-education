

my_text = input("Write your text here, using space: ")
my_list = [i for i in my_text.split() if 'abc' not in i]
print(f'New text: {" ".join(my_list)}')

# Use sample from the song ABC by The Jackson 5
# abc, It's easy as 1 2 3, as simple as Do re mi, abc, 1 2 3 Baby you and me girl