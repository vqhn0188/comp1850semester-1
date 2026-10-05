# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}
print(fruit)
# What do you think will be printed here? - tomato

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items? - becuase the union of the two sets returns all unique items in the sets (5)

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add('banana')
print(fruit)
# Remove an item from vegetables
print(vegetables.discard('potato'))
# Find and display symmetric difference of the two sets
print(fruit.symmetric_difference(vegetables))