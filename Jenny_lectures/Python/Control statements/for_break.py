greetings = ["Hello", "Aloha", "Bonjour"]
names = ["Brian", "Silva", "Benzema"]

for greeting in greetings:
    for name in names:
        print(greeting, name)

        if greeting == "Aloha" and name == "Silva":
            break  # Exits the inner loop --> nearest loop
    print("EXITED INNER LOOP")
    
print("EXITED OUTER LOOP!!")