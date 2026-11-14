def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطأ: لا يمكن القسمة على صفر!"
    return x / y

print("أهلاً بك في الآلة الحاسبة!")
print("1. جمع")
print("2. طرح")
print("3. ضرب")
print("4. قسمة")

# أخذ اختيار العملية من المستخدم
choice = input("اختر رقم العملية (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    # أخذ الأرقام من المستخدم باستخدام float لقبول الأعداد العشرية
    num1 = float(input("أدخل الرقم الأول: "))
    num2 = float(input("أدخل الرقم الثاني: "))

    if choice == '1':
        print("النتيجة:", add(num1, num2))
    elif choice == '2':
        print("النتيجة:", subtract(num1, num2))
    elif choice == '3':
        print("النتيجة:", multiply(num1, num2))
    elif choice == '4':
        print("النتيجة:", divide(num1, num2))
else:
    print("اختيار غير صحيح، الرجاء إدخال رقم من 1 إلى 4.")
