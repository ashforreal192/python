username = "chaiAurCode"

def func():
    username = "chai" # But if I comment this out, the global username would be printed, not chai.
    print(username)

print(username)
func()