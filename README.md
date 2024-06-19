# Java-Python

This is a small running example of the Py4J example with run instructions.

## Java

First we need to compile the java binary. We are doing this with maven here.
We only did need to add py4j to the dependencies of the pom.xml.
Afterwards, we run the jar which runs a Py4J GatewayServer serving the AdditionApplication and a java context.
For this, we had to add the following mvn plugin:

```xml
<plugin>
    <artifactId>maven-assembly-plugin</artifactId>
    <configuration>
    <archive>
        <manifest>
        <mainClass>de.fh_aachen.App</mainClass>
        </manifest>
    </archive>
    <descriptorRefs>
        <descriptorRef>jar-with-dependencies</descriptorRef>
    </descriptorRefs>
    </configuration>
</plugin>
```

```bash
cd py4j_demo
mvn clean compile assembly:single
java -jar target/py4j_demo-1.0-SNAPSHOT-jar-with-dependencies.jar
```

## Python

When having the java server running in one terminal, we need to install py4j in a python environment and run the java_accessor.py file:

```bash
pip install py4j
python java_accessor.py
```

You should take a look [at the commented version](java_accessor.py).