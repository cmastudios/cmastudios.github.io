---
id: 155
title: Code Scope
date: 2018-02-04T16:07:38+00:00
author: Connor Monahan
layout: page
guid: https://connormonahan.net/?page_id=155
status: hidden
---
A common nuance of programming is that of code scope. Scope refers to the variables that can be accessed from a particular section of code. Scope can also be local or global. In Java, new levels of scope are delimited by `{ ... }` blocks.

From wikipedia:

> In [computer programming](https://en.wikipedia.org/wiki/Computer_programming "Computer programming"), the **scope** of a [variable](https://en.wikipedia.org/wiki/Variable_(programming) "Variable (programming)"){.mw-redirect} is the region of a [computer program](https://en.wikipedia.org/wiki/Computer_program "Computer program") where the binding is valid: where the variable name can be used to refer to the entity. Such a region is referred to as a **<span id="scope_block">scope block</span>**. In other parts of the program the name may refer to a different entity (it may have a different binding), or to nothing at all (it may be unbound).

Variables are declared like below. They cannot be **declared** twice within the same scope.

|Code sample|Type|
|-----------|----|
|`int x;` |Declaration|
|`int x = 24;`|Declaration and Assignment|
|`x = 24;`|Assignment|

In Java, imagine you have a class that looks like the following:

```java
public class BankAccount {
    String owner;
    double balance_c, balance_s;
}
```

Then imagine it has a method like this:

```java
public void deposit(double amount) {
    balance_c = balance_c + amount;
}
```



The variable **balance** has **global scope** and it can be accessed by the method deposit because it is declared outside of it.

Imagine if the method looked like this:

```java
public void deposit(double amount) {
    if (amount > 0) {
        String destination = ask("Savings or checking?");
    }
    if (destination == "savings") {
        balance_s = balance_s + amount;
    } else if (destination == "checking") {
        balance_c = balance_c + amount;
    }
}
```



Would this method compile? It would not. The variable **destination** has **local scope**, however it will not be accessible by the if statements below because its declaration `(String destination)` is within the scope of `if (amount > 0) { ... }`. How would this be fixed?

```java
public void deposit(double amount) {
    String destination;
    if (amount > 0) {
        destination = ask("Savings or checking?");
    }
    if (destination == "savings") {
        balance_s = balance_s + amount;
    } else if (destination == "checking") {
        balance_c = balance_c + amount;
    }
}
```



Move the declaration part up a level.
