print("Enter Marks Obtained in 4 Subjects: ")
bangla = int(input());
English = int(input());
Math = int(input());
Science = int(input());

total_mark = bangla + English + Math + Science;
avg = total_mark / 4;

if  avg >= 91 and avg <= 100:
    print("A+")
elif  avg >= 81 and avg < 90:
    print("A")
elif  avg >= 71 and avg < 80:
    print("B")
elif avg >= 61 and avg  < 70:
    print("C")
elif avg >= 41 and avg  < 60:
    print("D")
elif  avg >= 0 and avg < 41:
    print("D")
else:
    print("Invalid Input!")
