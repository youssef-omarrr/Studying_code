## Courses
- [Every single feature of C# in 10 minutes](https://youtu.be/J0FhV3dM80o?si=_m8m3bGXtia2B4TW)

## Notes

**`var` keyword**: Type inference - let the compiler figure out the type from the right-hand side.

```c#
var name = "Alice"; // Compiler knows name is string
var count = 5;      // Compiler knows count is int
```

**Custom datatypes**:

- **`record`**: Immutable data carrier. Ideal for DTOs/data transfer objects. Fields are init-only.

```c#
record Person(string Name, int Age);
// Usage: var p = new Person("Alice", 30);
// p.Name = "Bob"; // Error - immutable
```

- **`struct`**: Value type stored on stack. Best for small, frequently used types (avoids heap overhead).

```c#
struct Point
{
    public int X;
    public int Y;
}
```

- **`class`**: Reference type stored on heap. Supports inheritance, polymorphism, and complex behavior.

```c#
public class MyClass
{
    public void DoWork() => Console.WriteLine("Working");
}
```

**Properties**: Class members that expose fields with controlled access.

```c#
public class Person
{
    // Auto-implemented property (read-write)
    public string Name { get; set; }

    // Property with restricted setter
    public int Age { get; private set; }

    // Read-only computed property
    public string Identifier => Guid.NewGuid().ToString();
}
```

**Instance creation**: Use `new` keyword + constructor.

```c#
var p = new Person("Alice", 30);

// Deconstruct into multiple variables
var (name, age) = p; // name = "Alice", age = 30
```

**Switch expressions**: Concise alternative to switch statements.

```c#
string GetLabel(int value) => value switch
{
    1 => "one",
    2 => "two",
    > 10 => "large number",
    _ => "unknown"
};
```

**Collections** (`System.Collections.Generic`):

- `List<T>`: Resizable array
- `Dictionary<TKey, TValue>`: Key-value map
- `.Select()`: LINQ method equivalent to `map`

**Generic typing**: Use `<T>` to write type-agnostic code.

```c#
public void PrintItems(List<int> items) { ... }
public T GetFirst(T[] array) => array[0];