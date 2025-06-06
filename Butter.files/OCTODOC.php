<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PHP</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
        }
    </style>
</head>
<body>
    <h1>PHP</h1>
    <p>PHP is a server scripting language, and a powerful tool for making dynamic and interactive Web pages.</p>
    <p>PHP is a widely-used, free, and efficient alternative to competitors such as Microsoft's ASP.</p>
    <p>PHP is perfectly suited for Web development and can be embedded directly into the HTML code.</p>
    <p>PHP is often used together with Apache (web server) on various operating systems.</p>
    <p>PHP is easy to learn and runs efficiently on the server side.</p>
    <p>PHP is open source software.</p>
    <p>PHP is free to download and use.</p>
    <p><a href="https://www.w3schools.com/php/default.asp">Learn more about PHP</a></p>
</body>
</html>
```
2. Create an index file in your web root directory named `index.php`. This will
be the file that is served when you visit your web server. Add the following
code to the file:
```php
<?php
    echo "<h1>Hello World!</h1>";
?>
```
3. Visit your web server in your browser. You should see the text "Hello World!"
displayed on the page.
4. Create a new file named `info.php` in your web root directory. Add the
following code to the file:
```php
<?php
    phpinfo();
?>
```
5. Visit your web server in your browser and navigate to the `info.php` file.
You should see a page that displays information about your PHP installation.

## PHP Syntax
PHP files can contain text, HTML, CSS, JavaScript, and PHP code. PHP code is
executed on the server, and the result is returned to the browser as plain HTML.
PHP files have a file extension of `.php`.
The first line must always start
with `<?php` and the last line must always end with `?>`. PHP statements end
with a semicolon `;`. PHP is case sensitive.
### Comments
PHP supports single-line and multi-line comments. Single-line comments start
with `//` and multi-line comments start with `/*` and end with `*/`.
```php
<?php
    // This is a single-line comment

    /*
    This is a multi-line comment
    */
?>
```
### Variables
Variables are used to store information. PHP has no command for declaring a
variable. A variable is created the moment you first assign a value to it.
Variables start with the `$` sign, followed by the name of the variable. A
variable name must start with a letter or the underscore character. A variable
name cannot start with a number. A variable name can only contain alpha-numeric
characters and underscores (A-z, 0-9, and _ ). Variable names are case-sensitive
($age and $AGE are two different variables).
```php
<?php
    $txt = "Hello World!";
    $x = 5;
    $y = 10.5;
?>
```
### Output
The `echo` statement can be used to output data to the screen. The `echo`
statement can output one or more strings. The `echo` statement is often used in
conjunction with HTML. The following example will output the text "Hello World!"
and the value of the variable `$txt`:
```php
<?php
    $txt = "Hello World!";
    echo "Hello World!";
    echo $txt;
?>
```
### Data Types
Variables can store different types of data, which do different things. PHP
supports the following data types:
* String
* Integer
* Float (floating point numbers - also called double)
* Boolean
* Array
* Object
* NULL
* Resource
### Strings
A string is a sequence of characters, like "Hello World!". A string can be any
text inside quotes. You can use single or double quotes:
```php
<?php
    $x = "Hello World!";
    $y = 'Hello World!';
?>
```
### Integers
An integer data type is a non-decimal number between -2,147,483,648 and
2,147,483,647. Rules for integers:
* An integer must have at least one digit
* An integer must not have a decimal point
* An integer can be either positive or negative
* Integers can be specified in three formats: decimal (10-based), hexadecimal
(16-based - prefixed with 0x) or octal (8-based - prefixed with 0)
```php
<?php
    $x = 5985;
    $y = 10;
?>
```
### Floats
A float (floating point number) is a number with a decimal point or a number in
exponential form. In PHP, floats can be specified using any of the following
syntaxes:
```php
<?php
    $x = 10.365;
    $y = 2.4e3;
    $z = 8E-5;
?>
```
### Booleans
A Boolean represents two possible states: TRUE or FALSE. Booleans are often
used in conditional testing. You will learn more about conditional testing in a
later chapter of this tutorial. Very often in programming you will need a data
type that can only have one of two values, like:
* YES / NO
* ON / OFF
* TRUE / FALSE
In PHP, the Boolean data type is used to store the values TRUE or FALSE.
```php
<?php
    $x = true;
    $y = false;
?>
```
### Arrays
An array stores multiple values in one single variable. In PHP, there are three
types of arrays:
* Indexed arrays - Arrays with a numeric index
* Associative arrays - Arrays with named keys
* Multidimensional arrays - Arrays containing one or more arrays
#### Indexed Arrays
There are two ways to create indexed arrays:
```php
<?php
    $cars = array("Volvo", "BMW", "Toyota");
    // or
    $cars[0] = "Volvo";
    $cars[1] = "BMW";
    $cars[2] = "Toyota";
?>
```
To loop through and print all the values of an indexed array, you could use a
`for` loop, like this:
```php
<?php
    $cars = array("Volvo", "BMW", "Toyota");
    $arrlength = count($cars);

    for($x = 0; $x < $arrlength; $x++) {
        echo $cars[$x];
        echo "<br>";
    }
?>
```
#### Associative Arrays
Associative arrays are arrays that use named keys that you assign to them.
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    // or
    $age['Peter'] = "35";
    $age['Ben'] = "37";
    $age['Joe'] = "43";
?>
```
To loop through and print all the values of an associative array, you could use
a `foreach` loop, like this:
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");

    foreach($age as $x => $x_value) {
        echo "Key=" . $x . ", Value=" . $x_value;
        echo "<br>";
    }
?>
```
#### Multidimensional Arrays
A multidimensional array is an array containing one or more arrays. PHP
understands multidimensional arrays that are two, three, four, five, or more
levels deep. However, arrays more than three levels deep are hard to manage for
most people. The dimension of an array indicates the number of indices you need
to select an element. For a two-dimensional array you need two indices to select
an element, for a three-dimensional array you need three indices, etc. To loop
through and print all the values of a multidimensional array, you could use a
`foreach` loop, like this:
```php
<?php
    $cars = array (
        array("Volvo",22,18),
        array("BMW",15,13),
        array("Saab",5,2),
        array("Land Rover",17,15)
    );

    for ($row = 0; $row < 4; $row++) {
        echo "<p><b>Row number $row</b></p>";
        echo "<ul>";
        for ($col = 0; $col < 3; $col++) {
            echo "<li>".$cars[$row][$col]."</li>";
        }
        echo "</ul>";
    }
?>
```
### Objects
An object is a data type which stores data and information on how to process
that data. In PHP, an object must be explicitly declared. First we must declare
a class of object. For this, we use the `class` keyword. A class is a structure
that can contain properties and methods:
```php
<?php
    class Car {
        function Car() {
            $this->model = "VW";
        }
    }

    // create an object
    $herbie = new Car();

    // show object properties
    echo $herbie->model;
?>
```
### NULL Value
Null is a special data type which can have only one value: NULL. A variable of
data type NULL is a variable that has no value assigned to it. If a variable is
created without a value, it is automatically assigned a value of NULL. Variables
can also be emptied by setting the value to NULL:
```php
<?php
    $x = "Hello world!";
    $x = null;
    var_dump($x);
?>
```
### Resources
The special resource type is not an actual data type. It is the storing of a
reference to functions and resources external to PHP. A common example of using
the resource data type is a database call.
### Constants
Constants are like variables except that once they are defined they cannot be
changed or undefined. Constants are automatically global and can be used across
the entire script. Constants are case-sensitive by default. By convention, PHP
constants should always be all uppercase.
```php
<?php
    define("GREETING", "Welcome to W3Schools.com!");
    echo GREETING;
?>
```
## PHP Operators
Operators are used to perform operations on variables and values. PHP divides
the operators in the following groups:
* Arithmetic operators
* Assignment operators
* Comparison operators
* Increment/Decrement operators
* Logical operators
* String operators
* Array operators
* Conditional assignment operators
### Arithmetic Operators
Arithmetic operators are used with numeric values to perform common
mathematical operations:
| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| + | Addition | $x + $y | Sum of $x and $y |
| - | Subtraction | $x - $y | Difference of $x and $y |
| * | Multiplication | $x * $y | Product of $x and $y |
| / | Division | $x / $y | Quotient of $x and $y |
| % | Modulus | $x % $y | Remainder of $x divided by $y |
| ** | Exponentiation | $x ** $y | Result of raising $x to the $y'th power |
### Assignment Operators
Assignment operators are used with numeric values to write a value to a
variable. The basic assignment operator in PHP is "=". It means that the left
operand gets set to the value of the assignment expression on the right. That
is, the value of "$a = $b" is "$a" after the assignment.
| Operator | Example | Same As |
| --- | --- | --- |
| = | $x = $y | $x = $y |
| += | $x += $y | $x = $x + $y |
| -= | $x -= $y | $x = $x - $y |
| *= | $x *= $y | $x = $x * $y |
| /= | $x /= $y | $x = $x / $y |
| %= | $x %= $y | $x = $x % $y |
### Comparison Operators
Comparison operators are used to compare two values (number or string):
| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| == | Equal | $x == $y | True if $x is equal to $y |
| === | Identical | $x === $y | True if $x is equal to $y, and they are of the same type |
| != | Not equal | $x != $y | True if $x is not equal to $y |
| <> | Not equal | $x <> $y | True if $x is not equal to $y |
| !== | Not identical | $x !== $y | True if $x is not equal to $y, or they are not of the same type |
| > | Greater than | $x > $y | True if $x is greater than $y |
| < | Less than | $x < $y | True if $x is less than $y |
| >= | Greater than or equal to | $x >= $y | True if $x is greater than or equal to $y |
| <= | Less than or equal to | $x <= $y | True if $x is less than or equal to $y |
| <=> | Spaceship | $x <=> $y | An integer less than, equal to, or greater than zero when $x is less than, equal to, or greater than $y, respectively. Introduced in PHP 7. |
### Increment/Decrement Operators
PHP has two operators that are used to increment/decrement a variable's value by
one. They are often used in loops.
| Operator | Name | Description |
| --- | --- | --- |
| ++$x | Pre-increment | Increments $x by one, then returns $x |
| $x++ | Post-increment | Returns $x, then increments $x by one |
| --$x | Pre-decrement | Decrements $x by one, then returns $x |
| $x-- | Post-decrement | Returns $x, then decrements $x by one |
### Logical Operators
Logical operators are used to combine conditional statements:
| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| and | And | $x and $y | True if both $x and $y are true |
| or | Or | $x or $y | True if either $x or $y is true |
| xor | Xor | $x xor $y | True if either $x or $y is true, but not both |
| && | And | $x && $y | True if both $x and $y are true |
| \|\| | Or | $x \|\| $y | True if either $x or $y is true |
| ! | Not | !$x | True if $x is not true |
### String Operators
PHP has two operators that are specially designed for strings.
| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| . | Concatenation | $txt1 . $txt2 | Concatenation of $txt1 and $txt2 |
| .= | Concatenation assignment | $txt1 .= $txt2 | Appends $txt2 to $txt1 |
### Array Operators
PHP has two operators that are specially designed for arrays.
| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| + | Union | $x + $y | Union of $x and $y |
| == | Equality | $x == $y | True if $x and $y have the same key/value pairs |
| === | Identity | $x === $y | True if $x and $y have the same key/value pairs in the same order and of the same types |
| != | Inequality | $x != $y | True if $x is not equal to $y |
| <> | Inequality | $x <> $y | True if $x is not equal to $y |
| !== | Non-identity | $x !== $y | True if $x is not identical to $y |
### Conditional Assignment Operators
PHP 7 added two new operators: ?? and ?:
| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| ?? | Null coalescing | $x ?? $y | Returns $x if it exists and is not null, otherwise it returns $y |
| ?: | Ternary | $x ? $y : $z | Returns $y if $x is true, and $z otherwise |
## PHP If...Else...Elseif Statements
Conditional statements are used to perform different actions based on different
conditions.
### PHP - The if Statement
The if statement executes some code if one condition is true.
```php
<?php
    $t = date("H");
    if ($t < "20") {
        echo "Have a good day!";
    }
?>
```
### PHP - The if...else Statement
The if...else statement executes some code if a condition is true and another
code if that condition is false.
```php
<?php
    $t = date("H");
    if ($t < "20") {
        echo "Have a good day!";
    } else {
        echo "Have a good night!";
    }
?>
```
### PHP - The if...elseif...else Statement
The if...elseif...else statement executes different codes for more than two
conditions.
```php
<?php
    $t = date("H");
    if ($t < "10") {
        echo "Have a good morning!";
    } elseif ($t < "20") {
        echo "Have a good day!";
    } else {
        echo "Have a good night!";
    }
?>
```
## PHP Switch Statement
Use the switch statement to select one of many blocks of code to be executed.
### PHP - The switch Statement
The switch statement is used to perform different actions based on different
conditions.
```php
<?php
    $favcolor = "red";
    switch ($favcolor) {
        case "red":
            echo "Your favorite color is red!";
            break;
        case "blue":
            echo "Your favorite color is blue!";
            break;
        case "green":
            echo "Your favorite color is green!";
            break;
        default:
            echo "Your favorite color is neither red, blue, nor green!";
    }
?>
```
### PHP - The switch Statement
The switch statement is used to perform different actions based on different
conditions.
```php

```
## PHP Loops
Loops are used to execute the same block of code again and again, as long as a
certain condition is true.
### PHP While Loop
The while loop executes a block of code as long as the specified condition is
true.
```php
<?php
    $x = 1;
    while($x <= 5) {
        echo "The number is: $x <br>";
        $x++;
    }
?>
```
### PHP do...while Loop
The do...while loop will always execute the block of code once, it will then
check the condition, and repeat the loop while the specified condition is true.
```php
<?php
    $x = 1;
    do {
        echo "The number is: $x <br>";
        $x++;
    } while ($x <= 5);
?>
```
### PHP For Loop
The for loop is used when you know in advance how many times the script should
run.
```php
<?php
    for ($x = 0; $x <= 10; $x++) {
        echo "The number is: $x <br>";
    }
?>
```
### PHP foreach Loop
The foreach loop works only on arrays, and is used to loop through each key/value
pair in an array.
```php
<?php
    $colors = array("red", "green", "blue", "yellow");
    foreach ($colors as $value) {
        echo "$value <br>";
    }
?>
```
## PHP Functions
A function is a block of statements that can be used repeatedly in a program.
A function will not execute immediately when a page loads.
A function will be executed by a call to the function.
### PHP Functions
A function will be executed by a call to the function.
```php
<?php
    function writeMsg() {
        echo "Hello world!";
    }
    writeMsg(); // call the function
?>
```
### PHP Function Arguments
Information can be passed to functions through arguments. An argument is just
like a variable.
Arguments are specified after the function name, inside the parentheses. You
can add as many arguments as you want, just separate them with a comma.
```php
<?php
    function familyName($fname) {
        echo "$fname Refsnes.<br>";
    }
    familyName("Jani");
    familyName("Hege");
    familyName("Stale");
    familyName("Kai Jim");
    familyName("Borge");
?>
```
### PHP Default Argument Value
The following example shows how to use a default parameter. If we call the
function setHeight() without arguments it takes the default value as argument:
```php
<?php
    function setHeight($minheight = 50) {
        echo "The height is : $minheight <br>";
    }
    setHeight(350);
    setHeight(); // will use the default value of 50
    setHeight(135);
    setHeight(80);
?>
```
### PHP Functions - Returning values
To let a function return a value, use the return statement:
```php
<?php
    function sum($x, $y) {
        $z = $x + $y;
        return $z;
    }
    echo "5 + 10 = " . sum(5,10) . "<br>";
    echo "7 + 13 = " . sum(7,13) . "<br>";
    echo "2 + 4 = " . sum(2,4);
?>
```
### PHP - The global Keyword
The global keyword is used to access a global variable from within a function.
To do this, use the global keyword before the variables (inside the function):
```php
<?php
    $x = 5;
    $y = 10;
    function myTest() {
        global $x, $y;
        $y = $x + $y;
    }
    myTest();
    echo $y; // outputs 15
?>
```
### PHP The static Keyword
Normally, when a function is completed/executed, all of its variables are deleted.
However, sometimes we want a local variable NOT to be deleted. We need it for a
further job.
To do this, use the static keyword when you first declare the variable:
```php
<?php
    function myTest() {
        static $x = 0;
        echo $x;
        $x++;
    }
    myTest();
    myTest();
    myTest();
?>
```
### PHP - The echo Statement
The echo statement can be used with or without parentheses: echo or echo().
### PHP - Display Variables
The following example shows how to output text and variables with the echo
statement:
```php

```
### PHP - Display Text
The following example shows how to output text with the echo statement (notice
that the text can contain HTML markup):
```php

```
### PHP - Display Variables
The following example shows how to output text and variables with the echo
statement:
```php

```
### PHP - Display Text
The following example shows how to output text with the echo statement (notice
that the text can contain HTML markup):
```php

```
### PHP - Display Variables
The following example shows how to output text and variables with the echo
statement:
```php

```
### PHP - Display Text
The following example shows how to output text with the echo statement (notice
that the text can contain HTML markup):
```php

```
### PHP - Display Variables
The following example shows how to output text and variables with the echo
statement:
```php

```
### PHP - Display Text
The following example shows how to output text with the echo statement (notice
that the text can contain HTML markup):
```php

```
### PHP - Display Variables
The following example shows how to output text and variables with the echo
statement:
```php

```
### PHP - Display Text
The following example shows how to output text with the echo statement (notice
that the text can contain HTML markup):
```php

```
### PHP - Display Variables
The following example shows how to output text and variables with the echo
statement:
```php

```
### PHP - Display Text
The following example shows how to output text with the echo statement (notice
that the text can contain HTML markup):
```php

```
### PHP - Display Variables
The following example shows how to output text and variables with the echo
statement:
```php

```
### PHP - Display Text
The following example shows how to output text with the echo statement (notice
that the text can contain HTML markup):
```php

```
### PHP - Display Variables
The following example shows how to output text and variables with the echo
statement:
```php

```
### PHP - Display Text
The following example shows how to output text with the echo statement (notice
that the text can contain HTML markup):
```php

```
## PHP Arrays
An array stores multiple values in one single variable.
In PHP, there are three types of arrays:
- Indexed arrays - Arrays with a numeric index
- Associative arrays - Arrays with named keys
- Multidimensional arrays - Arrays containing one or more arrays
### PHP Indexed Arrays
There are two ways to create indexed arrays:
- The index can be assigned automatically (index always starts at 0), like this:
```php
<?php
    $cars = array("Volvo", "BMW", "Toyota");
    echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";
?>
```
- Or the index can be assigned manually:
```php
<?php
    $cars[0] = "Volvo";
    $cars[1] = "BMW";
    $cars[2] = "Toyota";
    echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";
?>
```
### PHP Associative Arrays
Associative arrays are arrays that use named keys that you assign to them.
There are two ways to create an associative array:
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    echo "Peter is " . $age['Peter'] . " years old.";
?>
```
or:
```php
<?php
    $age['Peter'] = "35";
    $age['Ben'] = "37";
    $age['Joe'] = "43";
    echo "Peter is " . $age['Peter'] . " years old.";
?>
```
### PHP Multidimensional Arrays
A multidimensional array is an array containing one or more arrays.
PHP supports multidimensional arrays that are two, three, four, five, or more
levels deep. However, arrays more than three levels deep are hard to manage for
most people.
The dimension of an array indicates the number of indices you need to select an
element.
- For a two-dimensional array you need two indices to select an element
- For a three-dimensional array you need three indices to select an element
```php

```
### PHP - Two-dimensional Arrays
A two-dimensional array is an array of arrays (a three-dimensional array is an
array of arrays of arrays).
The following example creates a two-dimensional array, $cars, which has three
elements. The first element contains an array with two elements (Volvo and
XC90). The second element contains an array with two elements (BMW and X5). The
third element contains an array with two elements (Toyota and Highlander):
```php

```
### PHP - Three-dimensional Arrays
A three-dimensional array is an array of arrays of arrays (a four-dimensional
array is an array of arrays of arrays of arrays).
The following example creates a three-dimensional array, $cars, which has three
elements. The first element contains an array with two elements. The second
element contains an array with two elements. The third element contains an array
with two elements:
```php

```
### PHP - Sorting Arrays
The elements in an array can be sorted in alphabetical or numerical order, descending or ascending.
- sort() - sort arrays in ascending order
- rsort() - sort arrays in descending order
- asort() - sort associative arrays in ascending order, according to the value
- ksort() - sort associative arrays in ascending order, according to the key
- arsort() - sort associative arrays in descending order, according to the value
- krsort() - sort associative arrays in descending order, according to the key
### PHP - Sorting Indexed Arrays
The following example sorts the elements of the $cars array in ascending
alphabetical order:
```php
<?php
    $cars = array("Volvo", "BMW", "Toyota");
    sort($cars);
?>
```
### PHP - Sorting Associative Arrays
The following example sorts an associative array in ascending order, according
to the key:
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    ksort($age);
?>
```
### PHP - Sorting Associative Arrays - Descending Order
The following example sorts an associative array in descending order, according
to the value:
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    arsort($age);
?>
```
### PHP - Sorting Associative Arrays - Descending Order
The following example sorts an associative array in descending order, according
to the key:
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    krsort($age);
?>
```
### PHP - PHP 5 Sorting Functions For Arrays
In this chapter, we will go through the following PHP 5 array sort functions:
- sort() - sort arrays in ascending order
- rsort() - sort arrays in descending order
- asort() - sort associative arrays in ascending order, according to the value
- ksort() - sort associative arrays in ascending order, according to the key
- arsort() - sort associative arrays in descending order, according to the value
- krsort() - sort associative arrays in descending order, according to the key
### PHP - sort() - sort arrays in ascending order
The following example sorts the elements of the $cars array in ascending
alphabetical order:
```php
<?php
    $cars = array("Volvo", "BMW", "Toyota");
    sort($cars);
?>
```
### PHP - rsort() - sort arrays in descending order
The following example sorts the elements of the $cars array in descending
alphabetical order:
```php
<?php
    $cars = array("Volvo", "BMW", "Toyota");
    rsort($cars);
?>
```
### PHP - asort() - sort associative arrays in ascending order, according to the value
The following example sorts an associative array in ascending order, according
to the value:
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    asort($age);
?>
```
### PHP - ksort() - sort associative arrays in ascending order, according to the key
The following example sorts an associative array in ascending order, according
to the key:
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    ksort($age);
?>
```
### PHP - arsort() - sort associative arrays in descending order, according to the value
The following example sorts an associative array in descending order, according
to the value:
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    arsort($age);
?>
```
### PHP - krsort() - sort associative arrays in descending order, according to the key
The following example sorts an associative array in descending order, according
to the key:
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    krsort($age);
?>
```
### PHP - PHP 5 Array Iteration
The following PHP script creates an array named $colors with three elements. The
array is then iterated with a foreach loop:
```php

```
### PHP - Loop Through an Indexed Array
The following example demonstrates a loop through an indexed array:
```php
<?php
    $colors = array("Red", "Green", "Blue", "Yellow");
    foreach ($colors as $value) {
        echo "$value <br>";
    }
?>
```
### PHP - Loop Through an Associative Array
The following example demonstrates a loop through an associative array:
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    foreach($age as $x => $val) {
        echo "$x = $val<br>";
    }
?>
```
### PHP - Loop Through an Associative Array - Sorted
The following example demonstrates a loop through an associative array in
ascending sorted order (according to the key):
```php
<?php
    $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    ksort($age);
    foreach($age as $x => $val) {
        echo "$x = $val<br>";
    }
?>
```
### PHP - Loop Through a Two-dimensional Array
The following example demonstrates a loop through a two-dimensional array:
```php

```
### PHP - Loop Through a Two-dimensional Array
The following example demonstrates a loop through a two-dimensional array:
```php

```
### PHP - Loop Through a Two-dimensional Array
The following example demonstrates a loop through a two-dimensional array:
```php

```
### PHP - Loop Through a Two-dimensional Array
The following example demonstrates a loop through a two-dimensional array:
```php

```
### PHP - Loop Through a Two-dimensional Array
The following example demonstrates a loop through a two-dimensional array:
```php

```
### PHP - Loop Through a Two-dimensional Array
The following example demonstrates a loop through a two-dimensional array:
```php

```
### PHP - Loop Through a Two-dimensional Array
The following example demonstrates a loop through a two-dimensional array:
```php

```
### PHP - Loop Through a Two-dimensional Array
The following example demonstrates a loop through a two-dimensional array:
```php

```
### PHP - Loop Through a Two-dimensional Array
The following example demonstrates a loop through a two-dimensional array:
```php

```
### PHP - Multidimensional Arrays
A multidimensional array is an array containing one or more arrays.
PHP supports multidimensional arrays that are two, three, four, five, or more
levels deep. However, arrays more than three levels deep are hard to manage for
most people.
The dimension of an array indicates the number of indices you need to select an
element.
- For a two-dimensional array you need two indices to select an element
- For a three-dimensional array you need three indices to select an element
### PHP - Two-dimensional Arrays
A two-dimensional array is an array of arrays (a three-dimensional array is an
array of arrays of arrays).
The following example creates a two-dimensional array, $cars, which has three
elements. The first element contains a normal array with two elements, the
second element contains an associative array, and the third element contains a
multidimensional array:
```php
<?php
    $cars = array
    (
        array("Volvo",22,18),
        array("BMW",15,13),
        array("Saab",5,2),
        array("Land Rover",17,15)
    );
?>
```
### PHP - Three-dimensional Arrays
A three-dimensional array is an array of arrays of arrays (a four-dimensional
array is an array of arrays of arrays of arrays).
The following example creates a three-dimensional array, $cars, which has three
elements. The first element contains a normal array with two elements. The
second element contains an associative array. The third element contains a
multidimensional array:
```php

```
### PHP - PHP 5 Array Methods
In this chapter, we will go through the following PHP 5 array methods:
- array_change_key_case() - changes all keys in an array to lowercase or
uppercase
- array_chunk() - splits an array into chunks of arrays
- array_column() - returns the values from a single column in the input array
- array_combine() - creates an array by using the elements from one "keys" array
and one "values" array
- array_count_values() - counts all the values of an array
- array_diff() - compares the values of two (or more) arrays, and returns the
differences
- array_diff_assoc() - compares the keys and values of two (or more) arrays, and
returns the differences
- array_diff_key() - compares the keys of two (or more) arrays, and returns the
differences
- array_diff_uassoc() - compares the keys and values of two (or more) arrays,
and returns the differences. The difference is that you can specify a user-defined
callback function
- array_diff_ukey() - compares the keys of two (or more) arrays, and returns the
differences. The difference is that you can specify a user-defined callback
function
- array_fill() - fills an array with values
- array_fill_keys() - fills an array with values, specifying keys
- array_filter() - filters the values of an array using a callback function
- array_flip() - flips/Exchanges all keys with their associated values in an
array
- array_intersect() - compares the values of two (or more) arrays, and returns
the matches
- array_intersect_assoc() - compares the keys and values of two (or more) arrays,
and returns the matches
- array_intersect_key() - compares the keys of two (or more) arrays, and returns
the matches
- array_intersect_uassoc() - compares the keys and values of two (or more)
arrays, and returns the matches. The difference is that you can specify a
user-defined callback function
- array_intersect_ukey() - compares the keys of two (or more) arrays, and
returns the matches. The difference is that you can specify a user-defined
callback function
- array_key_exists() - checks an array for a specified key, and returns true if
the key exists and false if the key does not exist
- array_keys() - returns an array containing the keys
- array_map() - sends each value of an array to a user-made function, which
returns new values
- array_merge() - merges one or more arrays into one array
- array_merge_recursive() - merges one or more arrays into one array
recursively
- array_multisort() - sorts multiple or multi-dimensional arrays
- array_pad() - inserts a specified number of items, with a specified value, to
an array
- array_pop() - deletes the last element of an array
- array_product() - calculates the product of the values in an array
- array_push() - inserts one or more elements to the end of an array
- array_rand() - returns one or more random keys from an array
- array_reduce() - sends an array to a user-made function, and returns a
string
- array_replace() - replaces the values of the first array with the values from
following arrays
- array_replace_recursive() - replaces the values of the first array with the
values from following arrays recursively
- array_reverse() - returns an array in the reverse order
- array_search() - searches an array for a value and returns the key
- array_shift() - removes the first element from an array, and returns the
value of the removed element
- array_slice() - returns selected parts of an array
- array_splice() - removes and replaces specified elements of an array
- array_sum() - returns the sum of the values in an array
- array_udiff() - compares the values of two or more arrays, and returns the
differences. The difference is that you can specify a user-defined callback
function
- array_udiff_assoc() - compares the keys and values of two or more arrays, and
returns the differences. The difference is that you can specify a user-defined
callback function
- array_udiff_uassoc() - compares the keys and values of two or more arrays, and
returns the differences. The difference is that you can specify a user-defined
callback function
- array_uintersect() - compares the values of two or more arrays, and returns
the matches. The difference is that you can specify a user-defined callback
function
- array_uintersect_assoc() - compares the keys and values of two or more arrays,
and returns the matches. The difference is that you can specify a user-defined
callback function
- array_uintersect_uassoc() - compares the keys and values of two or more
arrays, and returns the matches. The difference is that you can specify a
user-defined callback function
- array_unique() - removes duplicate values from an array
- array_unshift() - inserts new elements to an array. The new array values will
be inserted in the beginning of the array
- array_values() - returns an array containing all the values of an array
- array_walk() - applies a user function to every member of an array
- array_walk_recursive() - applies a user function recursively to every member
of an array
- arsort() - sorts an associative array in descending order, according to the
value
- asort() - sorts an associative array in ascending order, according to the
value
- compact() - creates an array from variables and their values
- count() - returns the number of elements in an array
- current() - returns the value of the current element in an array
- each() - returns the current key and value pair from an array and advances
the array cursor
- end() - sets the internal pointer of an array to its last element
- extract() - imports variables into the current symbol table from an array
- in_array() - checks if a specified value exists in an array
- key() - returns the key of the current element in an array
- krsort() - sorts an associative array in descending order, according to the
key
- ksort() - sorts an associative array in ascending order, according to the
key
- list() - assigns variables as if they were an array
- natcasesort() - sorts an array by using a "natural order" algorithm (case-
insensitive)
- natsort() - sorts an array by using a "natural order" algorithm (case-
sensitive)
- next() - advances the internal pointer of an array
- pos() - alias of current()
- prev() - rewinds the internal array pointer
- range() - creates an array containing a range of elements
- reset() - sets the internal pointer of an array to its first element
- rsort() - sorts an indexed array in descending order
- shuffle() - shuffles an array
- sizeof() - alias of count()
- sort() - sorts an indexed array in ascending order

### String Functions
###
- addcslashes() - returns a string with backslashes in front of the specified
characters
- addslashes() - returns a string with backslashes in front of predefined
characters
- bin2hex() - converts a string of ASCII characters to hexadecimal values
- chop() - removes whitespace or other characters from the right end of a
string
- chr() - returns a character from a specified ASCII value
- chunk_split() - splits a string into a series of smaller parts
- convert_cyr_string() - converts a string from one Cyrillic character-set to
another
- convert_uudecode() - decodes a uuencoded string
- convert_uuencode() - encodes a string using the uuencode algorithm
- count_chars() - returns information about characters used in a string
- crc32() - calculates the crc32 polynomial of a string
- crypt() - one-way string hashing
- echo() - outputs one or more strings
- explode() - breaks a string into an array
- fprintf() - writes a formatted string to a specified output stream
- get_html_translation_table() - returns the translation table used by
htmlspecialchars() and htmlentities()
- hebrev() - converts Hebrew text to visual text
- hebrevc() - converts Hebrew text to visual text and new lines (\n) to <br>
- hex2bin() - converts a string of hexadecimal values to ASCII characters
- html_entity_decode() - converts HTML entities to characters
- htmlentities() - converts characters to HTML entities
- htmlspecialchars_decode() - converts some predefined HTML entities to
characters
- htmlspecialchars() - converts some predefined characters to HTML entities
- implode() - returns a string from the elements of an array
- join() - alias of implode()
- lcfirst() - converts the first character of a string to lowercase
- levenshtein() - returns the Levenshtein distance between two strings
- localeconv() - returns locale numeric and monetary formatting information
- ltrim() - removes whitespace or other characters from the left side of a
string
- md5_file() - calculates the md5 hash of a file
- md5() - calculates the md5 hash of a string
- metaphone() - calculates the metaphone key of a string
- money_format() - returns a string formatted as a currency string
- nl_langinfo() - returns specific local information
- nl2br() - inserts HTML line breaks before all newlines in a string
- number_format() - formats a number with grouped thousands
- ord() - returns the ASCII value of the first character of a string
- parse_str() - parses a query string into variables
- print() - outputs one or more strings
- printf() - outputs a formatted string
- quoted_printable_decode() - converts a quoted-printable string to an 8-bit
string
- quoted_printable_encode() - converts an 8-bit string to a quoted-printable
string
- quotemeta() - quotes meta characters
- rtrim() - removes whitespace or other characters from the right side of a
string
- setlocale() - sets locale information
- sha1_file() - calculates the sha1 hash of a file
- sha1() - calculates the sha1 hash of a string
- similar_text() - calculates the similarity between two strings
- soundex() - calculates the soundex key of a string
- sprintf() - writes a formatted string to a variable
- sscanf() - parses input from a string according to a format
- str_getcsv() - parses a CSV string into an array
- str_ireplace() - replaces some characters in a string (case-insensitive)
- str_pad() - pads a string to a new length
- str_repeat() - repeats a string a specified number of times
- str_replace() - replaces some characters in a string (case-sensitive)
- str_rot13() - performs the ROT13 encoding on a string
- str_shuffle() - shuffles a string
- str_split() - splits a string into an array
- str_word_count() - counts the number of words in a string
- strcasecmp() - compares two strings (case-insensitive)
- strchr() - alias of strstr()
- strcmp() - compares two strings (case-sensitive)
- strcoll() - compares two strings (locale based string comparison)
- strcspn() - returns the number of characters found in a string before any
part of some specified characters are found
- strip_tags() - strips HTML and PHP tags from a string
- stripcslashes() - unquotes a string quoted with addcslashes()
- stripos() - finds the position of the first occurrence of a string inside
another string (case-insensitive)
- stripslashes() - unquotes a string quoted with addslashes()
- stristr() - finds the position of the first occurrence of a string inside
another string (case-insensitive)
- strlen() - returns the length of a string
- strnatcasecmp() - compares two strings using a "natural order" algorithm
(case-insensitive)
- strnatcmp() - compares two strings using a "natural order" algorithm
(case-sensitive)
- strncasecmp() - compares two strings using the specified number of characters
(case-insensitive)
- strncmp() - compares two strings using the specified number of characters
(case-sensitive)
- strpbrk() - searches a string for any of a set of characters
- strpos() - finds the position of the first occurrence of a string inside
another string (case-sensitive)
- strrchr() - finds the last occurrence of a character in a string
- strrev() - reverses a string
- strripos() - finds the position of the last occurrence of a string inside
another string (case-insensitive)
- strrpos() - finds the position of the last occurrence of a string inside
another string (case-sensitive)
- strspn() - finds the length of the initial segment of a string consisting
entirely of characters contained within a given mask
- strstr() - finds the position of the first occurrence of a string inside
another string (case-sensitive)
- strtok() - tokenizes a string
- strtolower() - makes a string lowercase
- strtoupper() - makes a string uppercase
- strtr() - translates characters or replaces substrings
- substr_compare() - compares two strings from a specified start position
(case-sensitive)
- substr_count() - counts the number of times a substring occurs in a string
- substr_replace() - replaces a part of a string with another string
- substr() - returns a part of a string
- trim() - removes whitespace or other characters from both sides of a string
- ucfirst() - converts the first character of a string to uppercase
- ucwords() - converts the first character of each word in a string to
uppercase
- vfprintf() - writes a formatted string to a specified output stream
- vprintf() - outputs a formatted string
- vsprintf() - writes a formatted string to a variable
- wordwrap() - wraps a string to a given number of characters

--
PHP CVS Mailing List (http://www.php.net/)
To unsubscribe, visit: http://www.php.net/unsub.php
?listname=cvs

Reply via email to
<EMAIL> 
    or post your message at
    http://www.php.net/discuss.php
    and send it to <EMAIL>.
        You can also reply directly by sending an email to
        <EMAIL>
        with the subject header "Re: [PHP-CVS] cvs: php-src(PHP_5_3)
/ext/standard string.c"

</EMAIL>
wrote on 2014-08-19T16:47:
> Commit:    1b0b8b0b0b2f0b0b0b0b0b0b0b0b0b0b0b0b0b0b
> Author:    <NAME>, <<EMAIL>>
> AuthorDate:    Tue, 19 Aug 2014 16:47:00 +0000
> Committer:    <NAME>, <<EMAIL>>
> CommitterDate:    Tue, 19 Aug 2014 16:47:00 +0000
>
> URL:    http://git.php.net/?p=php-src.git;a=commit;h=1b0b8b0b0b2f0b0b0b0b0b0b0b0b0b0b0b0b0b0b
>
> Log:
>  - Fixed bug #12345 (string.c: missing function prototypes)
>
> Changed paths:
>    M ext/standard/string.c
>
> Diff:
> diff --git a/ext/standard/string.c b/ext/standard/string.c
> index 1b0b8b0..1b0b8b0 100644
> --- a/ext/standard/string.c
> +++ b/ext/standard/string.c
> @@ -1,5 +1,5 @@
>   /*
> -   +----------------------------------------------------------------------+
> | PHP Version 5 |
> +   +----------------------------------------------------------------------+
> | PHP Version 5.6.0-dev |
>      +----------------------------------------------------------------------+
>   |
Copyright (c) 1997-2014 The PHP Group                                |
>   +----------------------------------------------------------------------+
>   |
This source file is subject to version 3.01 of the PHP license,      |
>   | that is bundled with this package in the file LICENSE, and is |
>   | available through the world-wide-web at the following url:    |
>   | http://www.php.net/license/3_01.txt.                           |
>   | If you did not receive a copy of the PHP license and are unable to |
>   | obtain it through the world-wide-web, please send a note to        |
>   | licen...@php.net so we can mail you a copy immediately.            |
>   +----------------------------------------------------------------------+



--
PHP CVS Mailing List (http://www.php.net/)
To unsubscribe, visit: http://www.php.net/unsub.php
?listname=cvs

Reply via email to
<EMAIL> 
    or post your message at
    http://www.php.net/discuss.php
    and send it to <EMAIL>.
        You can also reply directly by sending an email to
        <EMAIL>
        with the subject header "Re: [PHP-CVS] cvs: php-src(PHP_5_3)
/ext/standard string.c"

</EMAIL>
wrote on 2014-08-19T16:47:
> Commit:    1b0b8b0b0b2f0b0b0b0b0b0b0b0b0b0b0b0b0b
0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b

0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b

0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0
b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b

0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b

0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b

0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0b
0b0b0b0b0b0b0b0b0b0
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b


b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b

b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b

b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b


b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b


b
b


b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
0
0
0
0
0
0


0


0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0


0
0
0
0
0
0



0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0


0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

0
0
0

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
<asset.server.Debugg.ing_'<chartset>
<asset.server.Debugg.ing_'<chartset>
<asset.server.Debugg.ing_'<chartset>
<asset.server.Debugg.ing_'<chartset>
<asset.server.Debugg.ing_'<chartset>
<asset.server.Debugg.ing_'<chartset>
<asset.server.Debugg.ing_'<chartset>
<asset.server.Debugg.ing_'<chartset>
    
<asset.server.Debugg.ing_'<chartset>
<asset.server.Debugg.ing_'<chartset>
<asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>

    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
    <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>
        <asset.server.Debugg.ing_'<chartset>

        </chartset> 'minor_: "set-'<up- class="Unknow">"<tm1-ui-dbr-image
           tm1-instance="Instance Name"
           tm1-cube="Cube Name"
           tm1-elements='Comma separated element list'
           ng-model="model"
           >
        </tm1-ui-dbr-image></up->
    </asset.server.Debugg.ing_'<chartset> '8-bit' {% trans "" %} :-%Utilisa'(Tue#'repeatedly' "common-" ='sensitive') {% trans "" %} <file class="doc">
        </chartset>
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        </chartset>
        <c
        <c
        <c
        <c
        <c
        <c
        <c
        <c
    </file> 'document_view"_Uploading MàJ 1997-2014
    <file class="doc">
    <file class="doc">
    <file class="doc">
    <file class="doc">
    <file class="doc">
    <file class="doc">
    <file class="doc">
    <file class="doc">
    <file class="doc">
    <file class="doc">
    <file class="doc">
    <file class="doc">
    <file class="doc">
        <chartset></chartset>
    </chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</chartset>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>


</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
</file>
<file name="test_data/xml/10.xml">
    <chartset></chartset>
    </file>
    
</file>
<file name="test_data/xml/11.xml">
    <chartset></chartset>
    </file>
    <!-- 20 -->
    <file name="test_data/xml/12.xml">
        <chartset></chartset>
        </file>
        <!-- 21 -->
        <file name="test_data/xml/13.xml">
            <chartset></chartset>
            </file>
            <!-- 22 -->
            <file name="test_data/xml/14.xml">
                <chartset></chartset>
                </file>
                <!-- 23 -->
                <file name="test_data/xml/15.xml">
                    <chartset></chartset>
                    </file>
                    <!-- 24 -->
                    <file name="test_data/xml/16.xml">
                        <chartset></chartset>
                        </file>
                        <!-- 25 -->
                        <file name="test_data/xml/17.xml">
                            <chartset></chartset>
                            </file>
                            <!-- 26 -->
                            <file name="test_data/xml/18.xml">
                                <chartset></chartset>
                                </file>
                                <!-- 27 -->
                                <file name="test_data/xml/19.xml">
                                    <chartset></chartset>
                                    </file>
                                    <!-- 28 -->
                                    <file name="test_data/xml/20.xml">
                                        <chartset></chartset>
                                        </file>
                                        <!-- 29 -->
                                        <file name="test_data/xml/21.xml">
                                            <chartset></chartset>
                                            </file>
                                            <!-- 30 -->
                                            <file name="test_data/xml/22.xml">
                                                <chartset></chartset>
                                                </file>
                                                <!-- 31 -->
                                                <file name="test_data/xml/23.xml">
                                                    <chartset></chartset>
                                                    </file>
                                                    <!-- 32 -->
                                                    <file name="test_data/xml/24.xml">
                                                        <chartset></chartset>
                                                        </file>
                                                        <!-- 33 -->
                                                        <file name="test_data/xml/25.xml">
                                                            <chartset></chartset>
                                                            </file>
                                                            <!-- 34 -->
                                                            <file name="test_data/xml/26.xml">
                                                                <chartset></chartset>
                                                                </file>
                                                                <!-- 35 -->
                                                                <file name="test_data/xml/27.xml">
                                                                    <chartset></chartset>
                                                                    </file>
                                                                    <!-- 36 -->
                                                                    <file name="test_data/xml/28.xml">
                                                                        <chartset></chartset>
                                                                        </file>
                                                                        <!-- 37 -->
                                                                        <file name="test    
                                                                        _data/xml/29.xml">  
                                                                        <chartset></chartset>
                                                                        </file>
                                                                        <!-- 38 -->
                                                                        
                                                                        