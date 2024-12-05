## Question 1: How many seconds are there in 42 minutes 42 seconds?

## To solve this, it's too simple, we just need to multiply 42 with 60 and add 42

number_of_seconds = 42 * 60 + 42
print("There is", number_of_seconds, "seconds in 42 minutes 42 seconds.")


## Question 2 : How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

## To solve this, we have 1 mile = 1.61kilometers, and the question is how much ? miles = 10kilometers
## we just need to devide 10 by 1.61 

miles_in_10_km = 10 / 1.61 
print("There is ",round(miles_in_10_km,2)," in 10 kilometers.")


## Question 3 : If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? 
##               What is your average speed in miles per hour?

## We already have the distance in miles 
## To get the Average pace we need to devide the total time by the distance 

## The average pace 

average_pace = number_of_seconds / miles_in_10_km 

## To know how much minutes and seconds, we just have to devide the average pace by 60 to get the minutes, 
## and get the rest of the Euclidean division of average pace by 60 to get seconds.

minutes = int(average_pace / 60)
seconds = average_pace % 60

print("The average pace is ",minutes," minutes and ",round(seconds,2)," seconds per mile.")

## To calculate the average speed in miles per hour, we need to convert time in hours 

hours = 42/60 + 42/360

## The average speed is calculated by deviding the distance by time 

average_speed = miles_in_10_km / hours 

print("The average speed in miles per hour is",average_speed)


#### Completed ####
