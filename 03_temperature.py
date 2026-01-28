temperature=int(input("enter temp"))

print(f"The current temperature is {temperature}°C.")

if temperature > 30:
    
    print("It's quite hot! Turning on the air conditioning.")

elif 20 <= temperature <= 30:
    
    print("The weather is pleasant. Let's just open a window.")

else:
  
    print("It's a bit chilly. Better grab a sweater.")

print("End of decision process.")



#output
enter temp55
The current temperature is 55°C.
It's quite hot! Turning on the air conditioning.
End of decision process.
