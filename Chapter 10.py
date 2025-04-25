# Chapter 10 - Error handling
try:
    # risky operation
except Exception as e:
    print("Error:", e)
finally:
    GPIO.cleanup()
