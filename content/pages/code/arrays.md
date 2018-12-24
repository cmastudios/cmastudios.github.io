title: Arrays in Java
date: 2018-02-08T00:19:57+00:00
author: Connor Monahan
status: hidden

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
	"HTML-CSS": { styles: {
		".MathJax .mo, .MathJax .mi": {color: "black ! important"}}
	},
	tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']],processEscapes: true}
});
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/MathJax.js?config=TeX-AMS_HTML">
</script>

# Simple lists with arrays

Simply put, an array is a very basic list. Lists have a wide variety of applications in programming.

What are examples of useful lists?

  * Shopping list
  * Nearby Chinese restaurants
  * Students in a class

Let&#8217;s take a look at the last example. A list of students in a class may look like this in English: Jeffrey, Paul, Sydney, William, and Kyle. In Java, that list would be stored as an array like this:

|`i`		|0	|1	|2	|3	|4	|
|---------------|-------|-------|-------|-------|-------|
|`students[i]`	|Jeffrey|Paul	|Sydney	|William|Kyle	|


Every element in the array has a unique index starting from zero. There are five students in this array, so in Java, `students.length` would be equal to 5.

for-loops are a very useful programming structure for manipulating arrays. To see why this is so, imagine needing to print the names of each student. Maybe you&#8217;re trying to print a class roster or something. That could be done as follows, but this is inconvenient for many reasons:

```java
System.out.println(students[0]);
System.out.println(students[1]);
System.out.println(students[2]);
System.out.println(students[3]);
System.out.println(students[4]);
```

Say Sally switched into this class. Or say Paul dropped the class. This code would then be invalid and require modification. And this code violates the DRY (don&#8217;t repeat yourself) principle, as it is executing the same thing five times. The code could easily be converted to using a for loop, as follows:

```java
for (int i = 0; i < students.length; i++) {
	System.out.println(students[i]);
}
```

This is equivalent to rewriting the mathematical statement $x_1 + x_2 + x_3 + x_4 + x_5$ as $\sum_{i=1}^{5} x_i$

Don&#8217;t forget that this data structure can be applied to any sort of sequence of data, and the indices of each element can be useful (such as to define a student id).

# Tables or matrices as two-dimensional arrays

Other objects, such as tables and matrices, can also be represented in Java. What are some types of data that these might represent?

  * Logs from a car containing speed, braking, and engine temperature
  * Multiplication table
  * A digital image!

Let&#8217;s take a look at the first example. Such a table may look like this:

|i \ j |0 |1 |2|
|-------------|--|--|-|
|0|24.0|9.8|40.2|
|1|88.0|0.0|62.1|


Note that the implementation of tables as arrays in java requires that all columns be of the same data type. The convention is that when storing as a 2d array, the rows are the first dimension and the columns are the second.

```java
{% raw %}
double data[][] = new double[2][3] {{24.0, 9.8, 40.2}, {88.0, 0.0, 62.1}};
int rows = data.length;
int columns = data[0].length;
{% endraw %}
```

In this example, I use `data.length` to access the number of rows, and I use `data[0].length` to access the number of columns. This second operation works because as you can see the first element of data is itself an array of length 3.

To then print out this table, it&#8217;s necessary to use nested for-loops:

```java
System.out.println("Row\tSpeed\tBraking\tTemp");
// for all rows
for (int row = 0; row < rows; row++) {
    System.out.print(row + "\t");
    // for all columns
    for (int column = 0; column < columns; column++) {
        System.out.print(data[row][column] + "\t");
    }
    System.out.println("");
}
```

The code above iterates through the data by rows at the outer level and columns at the inner level. What if instead we wanted to say find the average of the speed, braking, and temperature? We can choose to iterate by columns and then rows if we choose to, as follows. All that is necessary is to swap the for-loops.

```java
for (int column = 0; column < columns; column++) {
    double total = 0;
    for (int row = 0; row < rows; row++) {
        total += data[row][column];
    }
    double average = total / rows;
    System.out.println("Average of column " + column + ": " + average);
}
```

&nbsp;
