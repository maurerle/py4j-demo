from py4j.java_collections import MapConverter
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()                   # connect to the JVM

# here we are instantiationg Java classes ourselves
random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
number1 = random.nextInt(10)              # call the Random.nextInt method
number2 = random.nextInt(10)
print(number1, number2)

# the entry_point is the app given in `new GatewayServer(app);`
addition_app = gateway.entry_point               # get the AdditionApplication instance
value = addition_app.addition(number1, number2) # call the addition method
print(value)

# we can also create a new instance of an object ourselves
myAddition = gateway.jvm.de.fh_aachen.AdditionApplication()   # create a new AdditionApplication

# and call the function there, leading to the same result surely
myValue = myAddition.addition(number1, number2)
print(f"MyAddtionService {myValue}")

# the say hello does not print in our python terminal but on the java output
addition_app.sayHello()

# sending a plain dict does not work
my_dict = {"hello": 4, "goodbye": "ciao"}
try:
    addition_app.printDict(my_dict)
except Exception as e:
    print("Error was:", e)

# we first need to convert it
java_dict = MapConverter().convert(my_dict, gateway._gateway_client)
# then it works
output = addition_app.printDict(java_dict)
print(f"Dict is represented as {output}")


# Alternatively we can directly create a Java HashMap:
m = gateway.jvm.java.util.HashMap()
m["a"] = 0
m.put("b",1)
print(m)

# We can print that one too from Java:
print(addition_app.printDict(m))