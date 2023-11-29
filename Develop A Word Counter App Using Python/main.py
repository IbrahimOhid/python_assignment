file = open('Text.txt', 'r');
read_word = file.read();
search_word = ["Python", "C", "OOP", "Hello", "Java"];

a = read_word.count(search_word[0]);
b = read_word.count(search_word[1]);
c = read_word.count(search_word[2]);
d = read_word.count(search_word[3]);
e = read_word.count(search_word[4]);

print("Python -> {}".format(a));
print("C -> {}".format(b));
print("OOP -> {}".format(c));
print("Hello -> {}".format(d));
print("Java -> {}".format(e));