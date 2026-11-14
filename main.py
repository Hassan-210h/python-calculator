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

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        return "خطأ: لا يمكن القسمة على صفر!"
    return x % y

def square_root(x):
    if x < 0:
        return "خطأ: لا يمكن أخذ الجذر التربيعي لعدد سالب!"
    return x ** 0.5


def show_menu():
    print("\nأهلاً بك في الآلة الحاسبة!")
    print("1. جمع")
    print("2. طرح")
    print("3. ضرب")
    print("4. قسمة")
    print("5. أس")
    print("6. باقي القسمة")
    print("7. الجذر التربيعي")
    print("8. عرض السجل")
    print("0. خروج")


def main():
    history = []

    while True:
        show_menu()
        choice = input("اختر رقم العملية (1-8 أو 0 للخروج): ").strip()

        if choice == '0':
            print("شكرًا لاستخدامك الآلة الحاسبة!")
            break

        if choice == '8':
            if not history:
                print("السجل فارغ.")
            else:
                print("\n--- سجل العمليات ---")
                for i, item in enumerate(history, 1):
                    print(f"{i}. {item}")
            continue

        if choice not in ('1', '2', '3', '4', '5', '6', '7'):
            print("اختيار غير صحيح، الرجاء إدخال رقم من 1 إلى 8 أو 0 للخروج.")
            continue

        try:
            if choice == '7':
                # الجذر التربيعي يحتاج رقمًا واحدًا فقط
                num1 = float(input("أدخل الرقم: "))
                result = square_root(num1)
                print("النتيجة:", result)
                history.append(f"√({num1}) = {result}")
            else:
                # أخذ الأرقام من المستخدم باستخدام float لقبول الأعداد العشرية
                num1 = float(input("أدخل الرقم الأول: "))
                num2 = float(input("أدخل الرقم الثاني: "))

                if choice == '1':
                    result = add(num1, num2)
                    history.append(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    history.append(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    history.append(f"{num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    history.append(f"{num1} / {num2} = {result}")
                elif choice == '5':
                    result = power(num1, num2)
                    history.append(f"{num1} ** {num2} = {result}")
                elif choice == '6':
                    result = modulo(num1, num2)
                    history.append(f"{num1} % {num2} = {result}")

                print("النتيجة:", result)
        except ValueError:
            print("خطأ: الرجاء إدخال أرقام صحيحة.")


if __name__ == "__main__":
    main()
